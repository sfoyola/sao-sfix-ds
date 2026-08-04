#!/usr/bin/env python
"""
Dormant Kids Offer — watchdog.

Companion to run_dormant_kids.py, registered as its own independent
LaunchAgent (com.stitchfix.dormant-kids-watchdog.plist) so a launchd
registration glitch that wedges the main job doesn't also silence this
check.

Fires a couple hours after the main job's noon schedule and looks for
today's run_<date>.log. If it's missing, the main job's calendar trigger
never actually fired (this is what happened silently for ~a month
starting 2026-07-06 — `launchctl print` showed a stale EX_CONFIG exit
and the unified log showed "service inactive" instead of a real
invocation). When that's detected, the watchdog:

  1. unloads + reloads the main LaunchAgent (clears the stuck launchd
     state), and
  2. invokes run_dormant_kids.py directly so today's delivery isn't lost.

The re-invoked script posts its own Slack success/failure/creds-alert
messages as usual; this watchdog only posts a message when it had to
step in, so the channel stays quiet on normal days.
"""

import os
import subprocess
import sys
from pathlib import Path
from datetime import date, datetime

PROJECT_DIR = Path("/Users/sergio.oyola/Desktop/StitchFix/sao-sfix-ds/automation_kids_dormant_offer")
MAIN_SCRIPT = PROJECT_DIR / "run_dormant_kids.py"
MAIN_PLIST = Path.home() / "Library/LaunchAgents/com.stitchfix.dormant-kids.plist"
SLACK_CHANNEL = "C0BBY6XA09X"                  # #kids-dormant-offer
KEYCHAIN_SERVICE = "SLACK_KDO_BOT_TOKEN"        # same bot token as the main script
NB_TIMEOUT = 3900                               # generous: two notebook cells + upload

STATE_DIR = PROJECT_DIR / ".automation"
LOG_DIR = STATE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

TODAY = date.today().isoformat()
MAIN_LOG = LOG_DIR / f"run_{TODAY}.log"          # written by run_dormant_kids.py as its first action

_logfh = open(LOG_DIR / f"watchdog_{TODAY}.log", "a", buffering=1)


def log(msg):
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line, file=_logfh)
    print(line)


def slack_alert(text):
    """Best-effort chat message; never raises.

    Deliberately a standalone copy of the main script's Slack helper
    rather than an import of run_dormant_kids.py — keeps this watchdog's
    own alerting path fully independent of the module it's babysitting.
    """
    try:
        import requests
        token = subprocess.run(
            ["security", "find-generic-password", "-a", os.environ.get("USER", ""),
             "-s", KEYCHAIN_SERVICE, "-w"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        if not token:
            log("WARN: Slack token not found in Keychain; skipping alert.")
            return
        r = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers={"Authorization": f"Bearer {token}",
                     "Content-Type": "application/json; charset=utf-8"},
            json={"channel": SLACK_CHANNEL, "text": text}, timeout=60,
        ).json()
        if not r.get("ok"):
            log(f"WARN: chat.postMessage not ok: {r.get('error')}")
    except Exception as e:
        log(f"WARN: could not send Slack alert: {e}")


def main():
    log(f"=== watchdog check  today={TODAY} ===")

    if MAIN_LOG.exists():
        log("Main job already logged activity today — nothing to do.")
        return 0

    log("No run log for today — main job's scheduled trigger appears not to "
        "have fired (stuck LaunchAgent). Self-repairing.")

    slack_alert(
        f":gear: *Dormant Kids Offer watchdog* — today's ({TODAY}) scheduled run "
        "never started (the LaunchAgent looks stuck). Reloading it and "
        "triggering the job directly now."
    )

    try:
        subprocess.run(["launchctl", "unload", str(MAIN_PLIST)],
                        capture_output=True, text=True)
        subprocess.run(["launchctl", "load", str(MAIN_PLIST)],
                        capture_output=True, text=True, check=True)
        log("Reloaded main LaunchAgent.")
    except subprocess.CalledProcessError as e:
        log(f"WARN: could not reload main LaunchAgent: {e.stderr.strip()}")

    log(f"Invoking {MAIN_SCRIPT.name} directly ...")
    res = subprocess.run([sys.executable, str(MAIN_SCRIPT)],
                         capture_output=True, text=True, cwd=str(PROJECT_DIR),
                         timeout=NB_TIMEOUT)
    log(f"Direct invocation exit code: {res.returncode}")
    if res.stdout.strip():
        log(f"  stdout tail: {res.stdout.strip()[-500:]}")

    if res.returncode != 0:
        tail = (res.stderr or res.stdout)[-1500:]
        log(f"FAILURE: direct invocation failed:\n{tail}")
        slack_alert(
            f":x: *Dormant Kids Offer watchdog* — reloaded the agent but the "
            f"direct retry for {TODAY} still failed. Manual attention needed.\n"
            f"```{tail[:500]}```\nLogs: `{LOG_DIR}/watchdog_{TODAY}.log`"
        )
        return 1

    log("Watchdog-triggered run completed (see run_<date>.log for its own result).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
