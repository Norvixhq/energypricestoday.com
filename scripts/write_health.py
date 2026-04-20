#!/usr/bin/env python3
"""
write_health.py — Phase 5.1/5.2: Health endpoint + freshness drift detector.

Runs at the end of every autopilot cycle. Reads the current state of each
data source and pipeline step, applies deterministic threshold-based
freshness rules, and writes data/health.json — a machine-readable snapshot
that anyone (human eyeball or external monitor) can consume.

Output layout (structured, matches Phase 5 design):
  {
    "status": "healthy" | "degraded" | "failing",
    "generated_at": ISO timestamp,
    "checks": {
      "commodity_prices": { status, age_minutes, threshold_minutes, ... },
      "gas_prices":       { ... },
      "headlines":        { ... },
      "clusters":         { ... },
      "events":           { ... },
      "autopilot":        { last_success, minutes_since, ... },
      "news_update":      { ... },
      "nightly_audit":    { ... }
    },
    "quotas":        { <filled by lib/quota.py, optional> },
    "recent_activity": {
      "last_successful_autopilot":     ISO | null,
      "last_successful_news_update":   ISO | null,
      "last_successful_nightly_audit": ISO | null,
      "meaningful_changes_last_24h":   int,
      "articles_created_last_24h":     int
    },
    "reason_codes": [
      "HEADLINES_STALE",
      "AUTOPILOT_DELAYED",
      ...
    ]
  }

Reason codes (machine-readable, stable):
  HEADLINES_STALE       headlines observer output older than threshold
  EVENTS_STALE          events.json older than threshold
  COMMODITY_STALE       commodity prices older than threshold
  GAS_STALE             gas prices older than threshold
  AUTOPILOT_DELAYED     more than 45 min since last successful run
  AUTOPILOT_FAILING     more than 2 hours since last successful run
  NEWS_UPDATE_DELAYED   more than 8 hours since last successful news run
  NIGHTLY_AUDIT_MISSING more than 48 hours since last nightly audit
  OBSERVER_FAILED       any observer reported failed status
  API_QUOTA_HIGH        any API quota above 80% of limit
  API_QUOTA_CRITICAL    any API quota above 95% of limit

Overall status derivation (deterministic, threshold-based, no scoring):
  - Any CRITICAL-level code  -> "failing"
  - Any non-critical code    -> "degraded"
  - Zero codes               -> "healthy"

Exit codes:
  0 — health file written successfully (regardless of health status)
  1 — could not write health file
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SOURCES_DIR = DATA_DIR / "sources"
CLUSTERS_DIR = DATA_DIR / "clusters"
STATE_DIR = DATA_DIR / "state"
LOGS_DIR = DATA_DIR / "logs"
HEALTH_PATH = DATA_DIR / "health.json"
QUOTAS_PATH = STATE_DIR / "api-quotas.json"
ARTICLES_DIR = ROOT / "articles"

# ─── Thresholds (in minutes) ──────────────────────────────────────
# Deterministic rules. Deliberately simple — no weighted scoring.
THRESHOLDS = {
    "commodity_prices_minutes":   60,    # expected: every 15 min; stale if >60
    "gas_prices_minutes":         1440,  # daily refresh; stale if >24h
    "headlines_minutes":          60,    # every 15 min; stale if >60
    "clusters_minutes":           60,    # every 15 min; stale if >60
    "events_minutes":             60,    # every 15 min; stale if >60
    "autopilot_delayed_minutes":  45,    # >45 min since success: concerning
    "autopilot_failing_minutes":  120,   # >2h since success: failing
    "news_update_delayed_minutes": 480,  # >8h since success (runs every 4h)
    "nightly_audit_missing_minutes": 2880,  # >48h since success
    "quota_high_pct":             80,    # 80% of daily limit
    "quota_critical_pct":         95,    # 95% of daily limit
}

# Codes that escalate "degraded" to "failing"
CRITICAL_CODES = {
    "AUTOPILOT_FAILING",
    "API_QUOTA_CRITICAL",
}


# ─── Helpers ──────────────────────────────────────────────────────
def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_now() -> str:
    return now_utc().isoformat()


def parse_iso(s: str) -> datetime | None:
    if not s:
        return None
    try:
        # Accept both 'Z' and '+00:00' suffix
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None


def minutes_since(dt: datetime | None) -> int | None:
    """Return minutes between now and dt, or None if dt is None."""
    if dt is None:
        return None
    return int((now_utc() - dt).total_seconds() / 60)


def read_json_safe(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def file_mtime(path: Path) -> datetime | None:
    """File modification time (falls back to None if missing)."""
    if not path.exists():
        return None
    ts = path.stat().st_mtime
    return datetime.fromtimestamp(ts, tz=timezone.utc)


# ─── Check builders ───────────────────────────────────────────────
def check_commodity_prices() -> dict:
    """Freshness of data/sources/commodity-prices.json."""
    path = SOURCES_DIR / "commodity-prices.json"
    data = read_json_safe(path)
    last_success_str = None
    status_flag = None
    if data and isinstance(data, dict):
        meta = data.get("meta", {})
        last_success_str = meta.get("last_success") or meta.get("generated_at")
        status_flag = meta.get("status")
    last_success = parse_iso(last_success_str) if last_success_str else file_mtime(path)
    age = minutes_since(last_success)
    threshold = THRESHOLDS["commodity_prices_minutes"]
    stale = age is None or age > threshold
    observer_failed = status_flag == "failed"
    return {
        "status": "stale" if stale else ("failed" if observer_failed else "fresh"),
        "last_success": last_success.isoformat() if last_success else None,
        "age_minutes": age,
        "threshold_minutes": threshold,
        "observer_reported_status": status_flag,
    }


def check_gas_prices() -> dict:
    path = SOURCES_DIR / "gas-prices-national.json"
    data = read_json_safe(path)
    last_success_str = None
    status_flag = None
    if data and isinstance(data, dict):
        meta = data.get("meta", {})
        last_success_str = meta.get("last_success") or meta.get("generated_at")
        status_flag = meta.get("status")
    last_success = parse_iso(last_success_str) if last_success_str else file_mtime(path)
    age = minutes_since(last_success)
    threshold = THRESHOLDS["gas_prices_minutes"]
    stale = age is None or age > threshold
    observer_failed = status_flag == "failed"
    return {
        "status": "stale" if stale else ("failed" if observer_failed else "fresh"),
        "last_success": last_success.isoformat() if last_success else None,
        "age_minutes": age,
        "threshold_minutes": threshold,
        "observer_reported_status": status_flag,
    }


def check_headlines() -> dict:
    """Freshness of data/sources/headlines-index.json (aggregate topic index)."""
    path = SOURCES_DIR / "headlines-index.json"
    data = read_json_safe(path)
    last_success_str = None
    total_stories = 0
    failed_topics: list[str] = []
    if data and isinstance(data, dict):
        last_success_str = data.get("generated_at")
        total_stories = data.get("total_stories", 0)
        failed_topics = data.get("failed_topics") or []
    last_success = parse_iso(last_success_str) if last_success_str else file_mtime(path)
    age = minutes_since(last_success)
    threshold = THRESHOLDS["headlines_minutes"]
    stale = age is None or age > threshold
    return {
        "status": "stale" if stale else "fresh",
        "last_success": last_success.isoformat() if last_success else None,
        "age_minutes": age,
        "threshold_minutes": threshold,
        "total_stories": total_stories,
        "failed_topics": failed_topics,
    }


def check_clusters() -> dict:
    path = CLUSTERS_DIR / "top-stories.json"
    data = read_json_safe(path)
    last_success_str = None
    cluster_count = 0
    if data and isinstance(data, dict):
        last_success_str = data.get("generated_at")
        cluster_count = len(data.get("top_overall", []))
    last_success = parse_iso(last_success_str) if last_success_str else file_mtime(path)
    age = minutes_since(last_success)
    threshold = THRESHOLDS["clusters_minutes"]
    stale = age is None or age > threshold
    return {
        "status": "stale" if stale else "fresh",
        "last_success": last_success.isoformat() if last_success else None,
        "age_minutes": age,
        "threshold_minutes": threshold,
        "top_cluster_count": cluster_count,
    }


def check_events() -> dict:
    path = STATE_DIR / "events.json"
    data = read_json_safe(path)
    last_success_str = None
    event_count = 0
    if data and isinstance(data, dict):
        last_success_str = data.get("generated_at")
        event_count = len(data.get("events", {}))
    last_success = parse_iso(last_success_str) if last_success_str else file_mtime(path)
    age = minutes_since(last_success)
    threshold = THRESHOLDS["events_minutes"]
    stale = age is None or age > threshold
    return {
        "status": "stale" if stale else "fresh",
        "last_success": last_success.isoformat() if last_success else None,
        "age_minutes": age,
        "threshold_minutes": threshold,
        "event_count": event_count,
    }


# ─── Workflow-run freshness ───────────────────────────────────────
# We derive these from the logs since we can't hit the Actions API here.
# The autopilot.log gets appended on every run; nightly-audit leaves its
# own traces in commit history but we use the logs we have.
AUTOPILOT_START_RE = re.compile(
    r"^\[([\d\-T:\.+]+)\] autopilot: (?:render complete|no-op)"
)


def check_autopilot_runs() -> dict:
    """Parse data/logs/autopilot.log for last successful run."""
    log_path = LOGS_DIR / "autopilot.log"
    last_success: datetime | None = None
    if log_path.exists():
        try:
            for line in log_path.read_text(encoding="utf-8").splitlines():
                m = AUTOPILOT_START_RE.match(line)
                if m:
                    parsed = parse_iso(m.group(1))
                    if parsed and (last_success is None or parsed > last_success):
                        last_success = parsed
        except OSError:
            pass
    age = minutes_since(last_success)
    delayed_threshold = THRESHOLDS["autopilot_delayed_minutes"]
    failing_threshold = THRESHOLDS["autopilot_failing_minutes"]
    if age is None:
        status = "unknown"
    elif age > failing_threshold:
        status = "failing"
    elif age > delayed_threshold:
        status = "delayed"
    else:
        status = "ok"
    return {
        "status": status,
        "last_success": last_success.isoformat() if last_success else None,
        "minutes_since": age,
        "delayed_threshold_minutes": delayed_threshold,
        "failing_threshold_minutes": failing_threshold,
    }


def check_news_update() -> dict:
    """Article generation runs every 4 hours. Derive from articles/ mtimes."""
    if not ARTICLES_DIR.exists():
        return {"status": "unknown", "last_success": None, "minutes_since": None}
    try:
        files = list(ARTICLES_DIR.glob("*.html"))
        if not files:
            return {"status": "unknown", "last_success": None, "minutes_since": None}
        latest_mtime = max(f.stat().st_mtime for f in files)
        last_success = datetime.fromtimestamp(latest_mtime, tz=timezone.utc)
        age = minutes_since(last_success)
        threshold = THRESHOLDS["news_update_delayed_minutes"]
        status = "delayed" if age is not None and age > threshold else "ok"
        return {
            "status": status,
            "last_success": last_success.isoformat(),
            "minutes_since": age,
            "threshold_minutes": threshold,
            "total_articles": len(files),
        }
    except OSError:
        return {"status": "unknown", "last_success": None, "minutes_since": None}


def check_nightly_audit() -> dict:
    """Derive from the existence of a daily commit in the repo.

    Heuristic: look at data/health.json's previous generated_at if it's the
    cumulative marker, or fall back to the dangling-fixer log (written by
    nightly only). Simpler heuristic: use repo's .git HEAD mtime as upper
    bound, but that's noisy. Use dangling-fixer.log as primary signal.
    """
    log_path = LOGS_DIR / "dangling-fixer.log"
    last_success: datetime | None = None
    if log_path.exists():
        # Read the latest timestamp from the log
        try:
            content = log_path.read_text(encoding="utf-8")
            timestamps = re.findall(r"^\[([\d\-T:\.+]+)\]", content, re.MULTILINE)
            if timestamps:
                parsed = parse_iso(timestamps[-1])
                if parsed:
                    last_success = parsed
        except OSError:
            pass
    age = minutes_since(last_success)
    threshold = THRESHOLDS["nightly_audit_missing_minutes"]
    if age is None:
        status = "unknown"
    elif age > threshold:
        status = "missing"
    else:
        status = "ok"
    return {
        "status": status,
        "last_success": last_success.isoformat() if last_success else None,
        "minutes_since": age,
        "threshold_minutes": threshold,
    }


# ─── Activity counters ────────────────────────────────────────────
def count_meaningful_changes_last_24h() -> int:
    """Scan autopilot.log for '[plan] N changes' lines in last 24h."""
    log_path = LOGS_DIR / "autopilot.log"
    if not log_path.exists():
        return 0
    cutoff = now_utc()
    count = 0
    try:
        for line in log_path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\[([\d\-T:\.+]+)\].*\[plan\]\s+(\d+)\s+changes", line)
            if not m:
                continue
            ts = parse_iso(m.group(1))
            if ts and (cutoff - ts).total_seconds() <= 86400:
                count += int(m.group(2))
    except OSError:
        return 0
    return count


def count_articles_created_last_24h() -> int:
    """Count article files with mtime in last 24h."""
    if not ARTICLES_DIR.exists():
        return 0
    cutoff = now_utc().timestamp() - 86400
    count = 0
    try:
        for f in ARTICLES_DIR.glob("*.html"):
            if f.stat().st_mtime >= cutoff:
                count += 1
    except OSError:
        return 0
    return count


# ─── Reason code derivation ───────────────────────────────────────
def derive_reason_codes(checks: dict, quotas: dict) -> list[str]:
    codes: list[str] = []

    # Data staleness
    if checks["commodity_prices"]["status"] == "stale":
        codes.append("COMMODITY_STALE")
    if checks["gas_prices"]["status"] == "stale":
        codes.append("GAS_STALE")
    if checks["headlines"]["status"] == "stale":
        codes.append("HEADLINES_STALE")
    if checks["events"]["status"] == "stale":
        codes.append("EVENTS_STALE")

    # Observer self-reports
    for check_key in ("commodity_prices", "gas_prices"):
        if checks[check_key]["status"] == "failed":
            codes.append("OBSERVER_FAILED")
            break  # one instance is enough

    # Workflow-run freshness
    autopilot_status = checks["autopilot"]["status"]
    if autopilot_status == "failing":
        codes.append("AUTOPILOT_FAILING")
    elif autopilot_status == "delayed":
        codes.append("AUTOPILOT_DELAYED")

    if checks["news_update"]["status"] == "delayed":
        codes.append("NEWS_UPDATE_DELAYED")

    if checks["nightly_audit"]["status"] == "missing":
        codes.append("NIGHTLY_AUDIT_MISSING")

    # Quota signals (populated by lib/quota.py if present)
    for api_name, quota_data in (quotas or {}).items():
        if not isinstance(quota_data, dict):
            continue
        pct = quota_data.get("pct_of_limit")
        if pct is None:
            continue
        if pct >= THRESHOLDS["quota_critical_pct"]:
            codes.append("API_QUOTA_CRITICAL")
            break
        elif pct >= THRESHOLDS["quota_high_pct"]:
            if "API_QUOTA_HIGH" not in codes:
                codes.append("API_QUOTA_HIGH")

    return codes


def derive_overall_status(codes: list[str]) -> str:
    if any(code in CRITICAL_CODES for code in codes):
        return "failing"
    if codes:
        return "degraded"
    return "healthy"


# ─── Main ────────────────────────────────────────────────────────
def main() -> int:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    checks = {
        "commodity_prices": check_commodity_prices(),
        "gas_prices":       check_gas_prices(),
        "headlines":        check_headlines(),
        "clusters":         check_clusters(),
        "events":           check_events(),
        "autopilot":        check_autopilot_runs(),
        "news_update":      check_news_update(),
        "nightly_audit":    check_nightly_audit(),
    }

    quotas = read_json_safe(QUOTAS_PATH) or {}

    recent_activity = {
        "last_successful_autopilot":     checks["autopilot"]["last_success"],
        "last_successful_news_update":   checks["news_update"]["last_success"],
        "last_successful_nightly_audit": checks["nightly_audit"]["last_success"],
        "meaningful_changes_last_24h":   count_meaningful_changes_last_24h(),
        "articles_created_last_24h":     count_articles_created_last_24h(),
    }

    reason_codes = derive_reason_codes(checks, quotas)
    status = derive_overall_status(reason_codes)

    health = {
        "status":          status,
        "generated_at":    iso_now(),
        "checks":          checks,
        "quotas":          quotas,
        "recent_activity": recent_activity,
        "reason_codes":    reason_codes,
        "thresholds":      THRESHOLDS,
    }

    # Atomic write
    tmp = HEALTH_PATH.with_suffix(".new.json")
    try:
        tmp.write_text(json.dumps(health, indent=2, ensure_ascii=False), encoding="utf-8")
        os.replace(tmp, HEALTH_PATH)
    except OSError as e:
        print(f"[write_health] FAILED to write {HEALTH_PATH}: {e}")
        return 1

    # Compact stdout summary — shows up in autopilot log
    if reason_codes:
        codes_str = ", ".join(reason_codes)
        print(f"[write_health] status={status} codes=[{codes_str}]")
    else:
        print(f"[write_health] status={status} — all checks pass")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
