#!/usr/bin/env python3
"""
autopilot.py — Phase 1 orchestrator.

Single entry point for the autopilot loop. Runs:

  1. Observers  — fetch fresh data from external APIs
  2. Detect     — compare snapshots, produce changeset
  3. Render     — update js/data.js if changes are meaningful
  4. Validate   — run pre-publish checks
  5. Log        — write a summary to data/logs/autopilot.log

Does NOT commit/push. Commit is done by the caller (workflow or manual)
so the human has final control over what goes live.

Flags:
  --force       Run renderers even without meaningful changes
  --dry-run     Produce the full plan without writing js/data.js
  --observers-only   Run just the observers (useful for testing)
  --verbose     Print full subprocess output

Exit codes:
  0 = success (may be no-op)
  1 = non-critical issue (validator failed, observer unreachable)
  2 = critical error (config missing, crash)
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
LOG_PATH = ROOT / "data" / "logs" / "autopilot.log"


def log(msg: str, also_print: bool = True) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")
    if also_print:
        print(msg)


def run_script(path: Path, args: list[str] = None, verbose: bool = False) -> tuple[int, str]:
    """Run a Python script, return (exit_code, combined_output)."""
    cmd = [sys.executable, str(path)] + (args or [])
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=180,
        )
        output = (result.stdout or "") + (result.stderr or "")
        if verbose:
            print(output)
        return result.returncode, output
    except subprocess.TimeoutExpired:
        return 2, f"TIMEOUT running {path.name}"
    except Exception as e:
        return 2, f"EXCEPTION running {path.name}: {e}"


def run_observers(verbose: bool) -> dict:
    """Run every observer script. Return per-observer status dict."""
    observers = [
        ("commodity_prices", SCRIPTS / "observers" / "fetch_commodity_prices.py"),
        ("gas_prices",       SCRIPTS / "observers" / "fetch_gas_prices.py"),
        ("headlines",        SCRIPTS / "observers" / "fetch_headlines.py"),
    ]
    results = {}
    for name, script in observers:
        if not script.exists():
            log(f"[observers] {name}: script missing ({script})")
            results[name] = {"ok": False, "reason": "missing"}
            continue
        code, output = run_script(script, verbose=verbose)
        ok = code == 0
        # First line of output is usually the observer's human summary
        summary = output.strip().split("\n")[-1] if output else ""
        log(f"[observers] {name}: {'OK' if ok else 'FAIL'} — {summary}")
        results[name] = {"ok": ok, "exit_code": code, "summary": summary}
    return results


def load_changeset() -> dict:
    p = ROOT / "data" / "state" / "changes.json"
    if not p.exists():
        return {}
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--observers-only", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    log("═" * 60)
    log("autopilot: start")

    # Step 1 — Observers
    obs_results = run_observers(verbose=args.verbose)
    if args.observers_only:
        log("autopilot: observers-only complete")
        return 0

    # Step 1b — Story clustering (Phase 2.2)
    # Reads data/sources/headlines-*.json, writes data/clusters/*.json.
    # Additive only — does not affect price-change detection or rendering.
    # Exit 1 = no-change is normal; exit 2 = hard fail.
    code, output = run_script(SCRIPTS / "cluster_stories.py", verbose=args.verbose)
    if code == 2:
        log(f"[cluster] FAILED exit=2: {output.strip()[-200:]}")
        # Don't block the rest of autopilot on clustering failure — it's non-critical
    else:
        last_line = output.strip().split("\n")[-1] if output.strip() else ""
        log(f"[cluster] {last_line}")

    # Step 1c — Event-state resolution (Phase 2.3)
    # Reads data/clusters/*.json, writes data/state/events.json — the single
    # source of truth all future state-dependent UI modules will read from.
    # Non-critical to price pipeline. Exit 2 = hard fail; 0/1 = ok.
    code, output = run_script(SCRIPTS / "resolve_event_state.py", verbose=args.verbose)
    if code == 2:
        log(f"[resolver] FAILED exit=2: {output.strip()[-200:]}")
        # Don't block autopilot — previous events.json remains valid
    else:
        last_line = output.strip().split("\n")[-1] if output.strip() else ""
        log(f"[resolver] {last_line}")

    # Step 2 — Change detection
    code, output = run_script(SCRIPTS / "detect_changes.py", verbose=args.verbose)
    if code != 0:
        log(f"[detect] FAILED exit={code}: {output.strip()[-200:]}")
        return 1
    log(f"[detect] {output.strip().split(chr(10))[-1]}")

    changeset = load_changeset()
    total_changes = sum(
        len(s.get("changes", []))
        for s in changeset.get("sources", {}).values()
    )
    affected = len(changeset.get("affected_pages", []))

    if total_changes == 0 and not args.force:
        log(f"autopilot: no-op — no meaningful changes (affected={affected})")
        # Even on no-op, write health snapshot so freshness timestamps update.
        # This is critical — it's the heartbeat monitoring relies on.
        _write_health(args.verbose)
        return 0

    log(f"[plan] {total_changes} changes, {affected} page(s) affected")

    # Step 3 — Render
    render_args = []
    if args.force:
        render_args.append("--force")
    if args.dry_run:
        render_args.append("--dry-run")
    code, output = run_script(SCRIPTS / "render_data_js.py", render_args, verbose=args.verbose)
    if code != 0:
        log(f"[render] FAILED exit={code}")
        log(output.strip()[-400:], also_print=args.verbose)
        _write_health(args.verbose)  # log failure for health endpoint
        return 1
    for line in output.strip().split("\n")[-5:]:
        if line.strip():
            log(f"[render] {line}")

    if args.dry_run:
        log("autopilot: dry-run complete")
        return 0

    # Step 4 — Validate
    code, output = run_script(SCRIPTS / "validate.py", verbose=args.verbose)
    if code != 0:
        log(f"[validate] FAILED exit={code}")
        log(output.strip()[-400:])
        log("autopilot: REFUSING to proceed — manual review required")
        _write_health(args.verbose)  # log failure for health endpoint
        return 1

    log("[validate] all checks pass")
    log("autopilot: render complete, ready to commit")

    # Step 5 — Write health snapshot (Phase 5.1).
    # Non-blocking: if this fails, autopilot still succeeded, we just lose
    # the health snapshot for this cycle.
    _write_health(args.verbose)

    log("═" * 60)
    return 0


def _write_health(verbose: bool) -> None:
    """Run write_health.py. Non-blocking — log failures and continue."""
    code, output = run_script(SCRIPTS / "write_health.py", verbose=verbose)
    last_line = output.strip().split("\n")[-1] if output.strip() else ""
    if code == 0:
        log(f"[health] {last_line}")
    else:
        log(f"[health] FAILED exit={code}: {last_line[:200]}")


if __name__ == "__main__":
    sys.exit(main())
