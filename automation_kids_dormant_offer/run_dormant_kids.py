#!/usr/bin/env python
"""
Dormant Kids Offer — monthly automated runner.

Designed to be launched once per day by a launchd LaunchAgent (see
com.stitchfix.dormant-kids.plist). It self-gates so the real work happens
exactly once per calendar month:

  1. If this month was already delivered  -> exit quietly.
  2. Preflight AWS creds (STS get-caller-identity).
       - If invalid (you forgot to `assume`, or SSO expired) -> Slack alert,
         exit WITHOUT marking success, so it retries tomorrow.
  3. Execute notebook 1 (write warehouse partition, idempotent).
  4. Execute notebook 2 (build CSV batches).
  5. Upload the CSV(s) to the Slack channel.
  6. On success -> mark the month done + Slack success message.
       On any failure -> Slack error, no success mark, retries tomorrow.

Credentials: authenticates purely via the AWS profile's credential_process
(Granted/SSO), so no interactive shell session is required — only that your
morning `assume` has refreshed the SSO login. The Slack bot token is read from
the macOS login Keychain (service name SLACK_KDO_BOT_TOKEN), never from a file.
"""

import os
import re
import sys
import glob
import json
import subprocess
from pathlib import Path
from datetime import date, datetime

# ----------------------------------------------------------------------------
# Config — edit these if anything moves.
# ----------------------------------------------------------------------------
PROJECT_DIR   = Path("/Users/sergio.oyola/Desktop/StitchFix/kids_dormant_offer")
SLACK_CHANNEL = "#kids-dormant-offer"          # name (resolved) or a channel ID like C0123ABCD
AWS_PROFILE   = "Algorithms/DataScientist"
AWS_REGION    = "us-east-1"
KEYCHAIN_SERVICE = "SLACK_KDO_BOT_TOKEN"        # macOS Keychain service name holding the bot token

# Message posted alongside the CSV upload. Edit freely; a metadata footer
# (as_of / row count / filename) is appended automatically.
SLACK_MESSAGE = (
    "Dear Marketing Team,\n\n"
    "The Kids Dormant Offer list is ready to load into Blueshift to update the "
    "segment for this month's campaign. Let me know if anything looks off.\n\n"
    "Sergio"
)

NB1 = PROJECT_DIR / "1_dormant_kids_list.ipynb"          # writes warehouse partition
NB2 = PROJECT_DIR / "2_load_data_and_create_csv.ipynb"   # builds CSV(s)
OUTPUT_DIR = PROJECT_DIR / "output_files"                # where notebook 2 writes the CSV(s)
NB_CELL_TIMEOUT = 3600                                    # seconds per notebook cell

STATE_DIR   = PROJECT_DIR / ".automation"
LOG_DIR     = STATE_DIR / "logs"
EXEC_DIR    = STATE_DIR / "executed"        # executed notebook copies (audit trail)
CHANNEL_CACHE = STATE_DIR / "channel_id.txt"

# ----------------------------------------------------------------------------
# Environment — make headless (launchd) and manual runs behave identically.
# ----------------------------------------------------------------------------
os.environ.setdefault("HOME", "/Users/sergio.oyola")
os.environ["AWS_PROFILE"] = AWS_PROFILE
os.environ["AWS_REGION"] = AWS_REGION
os.environ["AWS_DEFAULT_REGION"] = AWS_REGION
# Force use of credential_process (SSO) rather than any stale static keys.
for v in ("AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN"):
    os.environ.pop(v, None)
os.environ["PATH"] = os.pathsep.join([
    "/Users/sergio.oyola/.pyenv/shims",
    "/opt/homebrew/bin", "/usr/local/bin", "/usr/bin", "/bin", "/usr/sbin", "/sbin",
    os.environ.get("PATH", ""),
])

for d in (STATE_DIR, LOG_DIR, EXEC_DIR):
    d.mkdir(parents=True, exist_ok=True)

TODAY = date.today().isoformat()
MONTH = TODAY[:7]                                  # YYYY-MM
SUCCESS_MARKER = STATE_DIR / f"delivered_{MONTH}.done"

_logfh = open(LOG_DIR / f"run_{TODAY}.log", "a", buffering=1)


def log(msg):
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line, file=_logfh)
    print(line)


# ----------------------------------------------------------------------------
# Slack helpers
# ----------------------------------------------------------------------------
def slack_token():
    try:
        out = subprocess.run(
            ["security", "find-generic-password", "-a", os.environ.get("USER", ""),
             "-s", KEYCHAIN_SERVICE, "-w"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except subprocess.CalledProcessError:
        log("ERROR: Slack token not found in Keychain "
            f"(service '{KEYCHAIN_SERVICE}'). Run the add-generic-password command.")
        return ""


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


def resolve_channel_id(token, channel):
    import requests
    raw = channel.lstrip("#")
    if re.match(r"^[CGD][A-Z0-9]{6,}$", raw):       # already an ID
        return raw
    if CHANNEL_CACHE.exists():
        cached = CHANNEL_CACHE.read_text().strip()
        if cached:
            return cached
    cursor = None
    while True:
        params = {"limit": 1000, "types": "public_channel,private_channel"}
        if cursor:
            params["cursor"] = cursor
        r = requests.get("https://slack.com/api/conversations.list",
                         headers=_auth(token), params=params, timeout=60).json()
        if not r.get("ok"):
            raise RuntimeError(
                f"conversations.list failed: {r.get('error')} — the bot may need the "
                "channels:read / groups:read scope, or just set SLACK_CHANNEL to the "
                "channel ID directly.")
        for ch in r.get("channels", []):
            if ch.get("name") == raw:
                CHANNEL_CACHE.write_text(ch["id"])
                return ch["id"]
        cursor = r.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break
    raise RuntimeError(f"Channel #{raw} not found (is the bot invited to it?).")


def slack_message(text):
    """Best-effort chat message; never raises."""
    try:
        import requests
        token = slack_token()
        if not token:
            return
        cid = resolve_channel_id(token, SLACK_CHANNEL)
        r = requests.post("https://slack.com/api/chat.postMessage",
                          headers={**_auth(token),
                                   "Content-Type": "application/json; charset=utf-8"},
                          json={"channel": cid, "text": text}, timeout=60).json()
        if not r.get("ok"):
            log(f"WARN: chat.postMessage not ok: {r.get('error')} (need chat:write scope?)")
    except Exception as e:
        log(f"WARN: could not send Slack message: {e}")


def slack_upload(token, channel_id, path, comment=None):
    import requests
    path = Path(path)
    size = path.stat().st_size
    r = requests.get("https://slack.com/api/files.getUploadURLExternal",
                     headers=_auth(token),
                     params={"filename": path.name, "length": size}, timeout=60).json()
    if not r.get("ok"):
        raise RuntimeError(f"getUploadURLExternal failed: {r.get('error')}")
    upload_url, file_id = r["upload_url"], r["file_id"]

    with open(path, "rb") as fh:
        up = requests.post(upload_url, files={"file": (path.name, fh)}, timeout=900)
    if up.status_code != 200:
        raise RuntimeError(f"file upload POST returned {up.status_code}: {up.text[:200]}")

    payload = {"files": [{"id": file_id, "title": path.name}], "channel_id": channel_id}
    if comment:
        payload["initial_comment"] = comment
    c = requests.post("https://slack.com/api/files.completeUploadExternal",
                      headers={**_auth(token),
                               "Content-Type": "application/json; charset=utf-8"},
                      json=payload, timeout=60).json()
    if not c.get("ok"):
        raise RuntimeError(f"completeUploadExternal failed: {c.get('error')}")
    return c


# ----------------------------------------------------------------------------
# Work steps
# ----------------------------------------------------------------------------
def creds_valid():
    try:
        import boto3
        ident = boto3.client("sts").get_caller_identity()
        log(f"AWS creds OK: {ident.get('Arn')}")
        return True
    except Exception as e:
        log(f"AWS creds NOT valid: {type(e).__name__}: {str(e)[:160]}")
        return False


def notebook_to_script(nb):
    """Flatten a .ipynb's code cells into a runnable .py, neutralizing IPython magics.

    We deliberately do NOT use `jupyter nbconvert --execute`: the jupyter
    dispatcher / `python3` kernelspec on this machine resolve to a different
    Python (miniforge 3.12) that lacks a working StitchFix env. Running the
    generated script with this same interpreter (pyenv 3.9.13) guarantees the
    bumblebee/amphibian/magic_carpet libs are present.
    """
    data = json.loads(Path(nb).read_text())
    parts = [f"# Auto-generated from {nb.name} — do not edit by hand."]
    for i, cell in enumerate(data.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell.get("source", []))
        if not src.strip():
            continue
        out = []
        for ln in src.splitlines():
            s = ln.lstrip()
            if s.startswith(("%", "!", "get_ipython")):     # IPython magics / shell escapes
                out.append("# [magic stripped] " + ln)
            else:
                out.append(ln)
        parts.append(f"# --- cell {i} ---\n" + "\n".join(out))
    gen = EXEC_DIR / f"{nb.stem}.gen.py"
    gen.write_text("\n\n".join(parts) + "\n")
    return gen


def run_notebook(nb):
    gen = notebook_to_script(nb)
    log(f"Executing {nb.name} (as {gen.name}) under {sys.executable} ...")
    res = subprocess.run([sys.executable, str(gen)], capture_output=True, text=True,
                         cwd=str(PROJECT_DIR), timeout=NB_CELL_TIMEOUT)
    if res.stdout.strip():
        log(f"  stdout: {res.stdout.strip()[-1000:]}")
    if res.returncode != 0:
        tail = (res.stderr or res.stdout)[-1800:]
        raise RuntimeError(f"{nb.name} failed (rc={res.returncode}):\n{tail}")
    log("  -> done.")


def find_new_csvs(since_ts):
    files = []
    for p in glob.glob(str(OUTPUT_DIR / "dormant_kids_offer_*.csv")):
        if os.path.getmtime(p) >= since_ts - 1:
            files.append(Path(p))
    return sorted(files)


def as_of_from(files):
    for f in files:
        m = re.search(r"dormant_kids_offer_(\d{4}-\d{2}-\d{2})_", f.name)
        if m:
            return m.group(1)
    return MONTH


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main():
    log(f"=== dormant-kids run  today={TODAY} month={MONTH} ===")

    if SUCCESS_MARKER.exists():
        log("Already delivered this month — nothing to do.")
        return 0

    if not creds_valid():
        slack_message(
            f":warning: *Dormant Kids Offer* — could not run for {MONTH} on {TODAY}: "
            "AWS credentials aren't valid. Please run `assume Algorithms/DataScientist` "
            "and I'll retry automatically tomorrow (or rerun manually today).")
        log("Exiting without success mark; will retry tomorrow.")
        return 0

    start_ts = datetime.now().timestamp()
    try:
        run_notebook(NB1)
        run_notebook(NB2)
        csvs = find_new_csvs(start_ts)
        if not csvs:
            raise RuntimeError("notebooks ran but no dormant_kids_offer_*.csv was produced.")

        as_of = as_of_from(csvs)
        token = slack_token()
        if not token:
            raise RuntimeError("Slack token missing from Keychain; cannot upload.")
        channel_id = resolve_channel_id(token, SLACK_CHANNEL)

        total_rows = 0
        for f in csvs:
            with open(f) as fh:
                total_rows += max(0, sum(1 for _ in fh) - 1)  # minus header

        for i, f in enumerate(csvs, 1):
            if i == 1:
                footer = ("_as_of `{}` · {:,} eligible clients · {}_".format(
                    as_of, total_rows, " · ".join(f"`{c.name}`" for c in csvs)))
                comment = f"{SLACK_MESSAGE}\n\n{footer}"
            else:
                comment = f"(cont.) file {i}/{len(csvs)}: `{f.name}`"
            log(f"Uploading {f.name} to Slack ...")
            slack_upload(token, channel_id, f, comment=comment)

        SUCCESS_MARKER.write_text(json.dumps({
            "delivered_at": datetime.now().isoformat(timespec="seconds"),
            "as_of": as_of,
            "files": [f.name for f in csvs],
            "rows": total_rows,
        }, indent=2))
        log(f"SUCCESS: delivered {len(csvs)} file(s), {total_rows} rows for as_of={as_of}.")
        return 0

    except Exception as e:
        err = f"{type(e).__name__}: {str(e)[:500]}"
        log(f"FAILURE: {err}")
        slack_message(
            f":x: *Dormant Kids Offer* — run for {MONTH} failed on {TODAY}.\n```{err}```\n"
            "No month marker written; it will retry automatically tomorrow. "
            f"Logs: `{LOG_DIR}/run_{TODAY}.log`")
        return 1


if __name__ == "__main__":
    sys.exit(main())
