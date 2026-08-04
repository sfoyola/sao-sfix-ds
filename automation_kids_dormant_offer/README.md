# Dormant Kids Offer — monthly automation

Generates the monthly list of **dormant kids' accounts eligible for the FY26 segment
offer**, writes it to the warehouse, exports CSV(s), and posts them to Slack
(`#kids-dormant-offer`) — automatically, once per month.

> **Where it runs:** locally on a designated operator's Mac (not a server). Paths in
> `run_dormant_kids.py`, `com.stitchfix.dormant-kids.plist`, and notebook 2 are
> hardcoded to that machine's home directory and must be updated to set it up on a
> different host. References to "the operator" below mean whoever owns that machine.

## Pieces

| File | Purpose |
|------|---------|
| `1_dormant_kids_list.ipynb` | Writes the eligible client IDs to `incentive_allocation.fy26_dormant_kids_incentive` (idempotent per `as_of` partition). |
| `2_load_data_and_create_csv.ipynb` | Reads the partition back, writes `dormant_kids_offer_<as_of>_<n>.csv` (500k-row batches) into `output_files/`. |
| `run_dormant_kids.py` | Orchestrator: gates to once/month, preflights creds, runs both notebooks, uploads CSV(s) to Slack with the team message. |
| `com.stitchfix.dormant-kids.plist` | macOS LaunchAgent that runs the orchestrator daily at **12:00**. |
| `run_dormant_kids_watchdog.py` | Watchdog: checks that today's `run_<date>.log` exists; if the main job's trigger silently didn't fire, reloads its LaunchAgent and re-invokes it directly. |
| `com.stitchfix.dormant-kids-watchdog.plist` | Independent macOS LaunchAgent that runs the watchdog daily at **15:00** (3h buffer after the main job). |
| `output_files/` | Generated CSV(s) land here (git-ignored). |
| `.automation/` | State markers, logs, generated scripts, cached channel ID (git-ignored). |

## How it works

- **Auth:** the orchestrator authenticates purely through the AWS profile's
  `credential_process` (Granted/SSO). It needs **no shell session** — only that the
  operator has refreshed the SSO login by running `assume Algorithms/DataScientist`
  on the host machine that morning.
- **Scheduling:** launchd fires daily at 12:00 on the host machine. The script delivers
  **once per month** (a `.automation/delivered_YYYY-MM.done` marker stops further runs).
  If the machine is asleep/off at noon, launchd runs it on next wake; if an attempt
  fails (e.g. the morning `assume` was missed), the next day retries until it succeeds.
- **Notebook execution:** the orchestrator flattens each notebook's code cells into a
  `.py` and runs it with its own pyenv 3.9.13 interpreter (no jupyter/kernel), so the
  StitchFix libs are always available.
- **Slack message:** the note posted with the CSV lives in the `SLACK_MESSAGE` constant
  in `run_dormant_kids.py` — edit it there. A footer (as_of / row count / filename) is
  added automatically.
- **Failure notice:** if creds are invalid or the run errors, it posts a Slack alert
  and does **not** write the month marker, so it retries the following day.
- **Watchdog:** the retries above only help if the main job's launchd trigger
  actually fires. On 2026-08 it didn't — a boot-time launchd registration
  glitch left the job silently wedged (`EX_CONFIG`) for weeks with no log and
  no Slack alert, since the script never got invoked at all. A second,
  independently-registered LaunchAgent (`com.stitchfix.dormant-kids-watchdog.plist`,
  fires daily at 15:00) checks whether today's `run_<date>.log` exists; if not,
  it reloads the main LaunchAgent and re-invokes `run_dormant_kids.py` directly,
  posting a Slack notice only when it has to step in. It's a separate `Label`
  so the same registration glitch doesn't necessarily wedge both jobs at once —
  but both still depend on this one laptop being logged in and awake.

## One-time setup

1. **Store the Slack bot token in the Keychain** (run in a shell where
   `SLACK_KDO_BOT_TOKEN` is set, so the value is never typed out):
   ```bash
   security add-generic-password -a "$USER" -s SLACK_KDO_BOT_TOKEN -w "$SLACK_KDO_BOT_TOKEN" -U
   ```
   The bot needs scopes **`files:write`** (upload) and **`chat:write`** (status/alerts);
   resolving the channel by name also needs **`channels:read`** (or set `SLACK_CHANNEL`
   in `run_dormant_kids.py` to the channel ID directly to skip that).

2. **Install the LaunchAgent (main job + watchdog):**
   ```bash
   cp com.stitchfix.dormant-kids.plist ~/Library/LaunchAgents/
   cp com.stitchfix.dormant-kids-watchdog.plist ~/Library/LaunchAgents/
   for label in com.stitchfix.dormant-kids com.stitchfix.dormant-kids-watchdog; do
     launchctl unload ~/Library/LaunchAgents/$label.plist 2>/dev/null
     launchctl load   ~/Library/LaunchAgents/$label.plist
   done
   ```

## Test it

After `assume Algorithms/DataScientist`, force a real run:
```bash
rm -f .automation/delivered_$(date +%Y-%m).done   # clear the month marker so it runs
python run_dormant_kids.py
```
Watch `.automation/logs/run_<date>.log`. A successful run posts the CSV(s) to
`#kids-dormant-offer` and writes the month marker.

## Operations

- **Re-deliver this month:** delete `.automation/delivered_YYYY-MM.done` and run again
  (or wait for the next noon fire).
- **Logs:** `.automation/logs/` — per-day `run_<date>.log` / `watchdog_<date>.log`,
  plus `launchd.{out,err}.log` / `watchdog_launchd.{out,err}.log`.
- **Disable:** `launchctl unload ~/Library/LaunchAgents/com.stitchfix.dormant-kids.plist`
  (and `...-watchdog.plist` if you want the watchdog off too).
- **Change run time:** edit `StartCalendarInterval` in the relevant plist, then unload + load.
- **If the main job goes silently stuck again** (no `run_<date>.log` for today,
  `launchctl print gui/<uid>/com.stitchfix.dormant-kids` shows a stale
  `last exit code`): the watchdog should self-heal it by 15:00. To check by hand,
  `launchctl unload` then `load` the main plist — that alone cleared the 2026-08
  incident.

## Data handling

Output contains customer identifiers (`client_id`, `household_primary_client_id`).
CSVs and `.automation/` are git-ignored. Delivery is restricted to the controlled
Slack channel. Confirm any wider sharing with the data-governance owner.
