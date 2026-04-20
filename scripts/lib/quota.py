#!/usr/bin/env python3
"""
quota.py — Phase 5.3: API quota tracker.

Shared library that observers import to record API calls. Writes daily
counters to data/state/api-quotas.json, auto-resetting at UTC midnight.

Usage from an observer:
    from lib import quota
    quota.record("oilpriceapi", endpoint="prices/all", succeeded=True)

The counters file is read by scripts/write_health.py to surface quota
signals in the health endpoint. Limits are defined in QUOTA_LIMITS below
and enforced only in the "warn via reason code" sense — this library
NEVER blocks calls, just tracks them.

File format:
    {
      "date": "2026-04-20",
      "apis": {
        "oilpriceapi": {
          "calls_today": 47,
          "succeeded": 45,
          "failed": 2,
          "limit_per_day": 100,
          "pct_of_limit": 47,
          "endpoints": {"prices/all": 47},
          "last_call": "2026-04-20T01:23:45+00:00"
        },
        ...
      }
    }

Auto-reset: if the saved `date` differs from today (UTC), counters zero.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
QUOTAS_PATH = ROOT / "data" / "state" / "api-quotas.json"

# Per-day soft limits. These don't enforce — they only drive reason codes
# (API_QUOTA_HIGH at 80%, API_QUOTA_CRITICAL at 95%). Tune as needed.
# Use generous estimates; better to under-warn than over-warn.
QUOTA_LIMITS: dict[str, int] = {
    "oilpriceapi":   10000,  # OilPriceAPI free tier: ~10k/mo; daily soft cap
    "eia":           5000,   # EIA API: 5000/day is typical
    "anthropic":     1000,   # Article generation: conservative limit
    "google_news":   5000,   # RSS, no hard limit but log for visibility
    "gdelt":         500,    # GDELT is rate-limited, getting 429s frequently
    "rss2json":      200,    # Free tier 10k/day; we rarely call but log anyway
    "finnhub":       60,     # 60/min = unlimited daily; log for visibility
    "aaa":           500,    # AAA scrape; GitHub runners blocked so rarely hits
}


def _today_utc() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load() -> dict:
    """Load the quotas file. If the date rolled over, reset to empty."""
    if not QUOTAS_PATH.exists():
        return {"date": _today_utc(), "apis": {}}
    try:
        data = json.loads(QUOTAS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"date": _today_utc(), "apis": {}}
    # Auto-reset at UTC midnight
    if data.get("date") != _today_utc():
        return {"date": _today_utc(), "apis": {}}
    if "apis" not in data:
        data["apis"] = {}
    return data


def _save(data: dict) -> None:
    """Atomic write to QUOTAS_PATH."""
    QUOTAS_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = QUOTAS_PATH.with_suffix(".new.json")
    try:
        tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        os.replace(tmp, QUOTAS_PATH)
    except OSError:
        # Quota tracking must never break an observer. Swallow errors.
        pass


def record(api_name: str, endpoint: str = "", succeeded: bool = True) -> None:
    """Record one API call against the running daily counter.

    NEVER raises. NEVER blocks. If anything goes wrong, the call is silently
    dropped — quota tracking must not become a reliability liability for
    the observer that called it.
    """
    try:
        data = _load()
        apis = data.setdefault("apis", {})
        entry = apis.setdefault(api_name, {
            "calls_today": 0,
            "succeeded": 0,
            "failed": 0,
            "limit_per_day": QUOTA_LIMITS.get(api_name, 0),
            "pct_of_limit": 0,
            "endpoints": {},
            "last_call": "",
        })

        entry["calls_today"] = entry.get("calls_today", 0) + 1
        if succeeded:
            entry["succeeded"] = entry.get("succeeded", 0) + 1
        else:
            entry["failed"] = entry.get("failed", 0) + 1

        if endpoint:
            endpoints = entry.setdefault("endpoints", {})
            endpoints[endpoint] = endpoints.get(endpoint, 0) + 1

        # Recompute pct_of_limit based on current counter + limit
        limit = entry.get("limit_per_day") or QUOTA_LIMITS.get(api_name, 0)
        entry["limit_per_day"] = limit
        if limit > 0:
            entry["pct_of_limit"] = round(100 * entry["calls_today"] / limit, 1)
        else:
            entry["pct_of_limit"] = 0

        entry["last_call"] = _now_iso()
        _save(data)
    except Exception:
        # Absolutely never let quota tracking break an observer
        pass


def snapshot() -> dict:
    """Return the current quotas dict. Used by write_health.py."""
    return _load()
