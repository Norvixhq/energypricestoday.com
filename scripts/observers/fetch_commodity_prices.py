#!/usr/bin/env python3
"""
fetch_commodity_prices.py — Observer for OilPriceAPI.

Fetches all commodity prices in a single call, snapshots them to
data/sources/commodity-prices.json, and logs success/failure. Does
NOT modify js/data.js — that's the renderer's job later.

Behavior on failure:
  1. Try primary endpoint
  2. If primary fails, keep the previous snapshot in place
  3. Append a log entry noting the failure and last-success time
  4. Exit 0 (don't break the workflow chain) unless a catastrophic
     error occurs (e.g. can't read config)

The snapshot's `meta.status` field flags freshness for downstream
consumers: "fresh" | "stale" | "failed".
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib import request, error as urlerror

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = ROOT / "data" / "config" / "sources.json"
OUTPUT_PATH = ROOT / "data" / "sources" / "commodity-prices.json"
LOG_PATH = ROOT / "data" / "logs" / "commodity-prices.log"

# Map OilPriceAPI codes -> display names we use in the site
CODE_MAP = {
    "WTI_USD":             "WTI Crude",
    "BRENT_CRUDE_USD":     "Brent Crude",
    "NATURAL_GAS_USD":     "Natural Gas",
    "GASOLINE_USD":        "Gasoline RBOB",
    "HEATING_OIL_USD":     "Heating Oil",
    "DIESEL_USD":          "Diesel ULSD",
    "JET_FUEL_USD":        "Jet Fuel",
    "NEWCASTLE_COAL_USD":  "Coal",
    "TAPIS_CRUDE_USD":     "Tapis Crude",
    "DUTCH_TTF_EUR":       "Dutch TTF Natural Gas",
    "JKM_LNG_USD":         "JKM LNG (Japan/Korea)",
}

# Display-name -> unit (for snapshot enrichment)
UNIT_MAP = {
    "WTI Crude":       "$/bbl",
    "Brent Crude":     "$/bbl",
    "Tapis Crude":     "$/bbl",
    "Natural Gas":     "$/MMBtu",
    "Gasoline RBOB":   "$/gal",
    "Heating Oil":     "$/gal",
    "Diesel ULSD":     "$/gal",
    "Jet Fuel":        "$/gal",
    "Coal":            "$/ton",
    "Dutch TTF Natural Gas": "EUR/MWh",
    "JKM LNG (Japan/Korea)": "$/MMBtu",
}


def log(message: str) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now(timezone.utc).isoformat()}] {message}\n")
    print(message)


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)["commodity_prices"]


def load_previous_snapshot() -> dict | None:
    if not OUTPUT_PATH.exists():
        return None
    try:
        with open(OUTPUT_PATH, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        log(f"WARN: could not read previous snapshot: {e}")
        return None


def fetch_from_api(config: dict) -> dict | None:
    """Hit the OilPriceAPI endpoint. Returns parsed JSON or None on failure."""
    primary = config["primary"]
    api_key = os.environ.get(primary["auth_env"]) or primary.get("api_key_fallback")
    if not api_key:
        log("ERROR: no API key available")
        return None

    req = request.Request(
        primary["endpoint"],
        headers={"Authorization": f"Token {api_key}"},
    )
    try:
        with request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except (urlerror.URLError, urlerror.HTTPError, TimeoutError) as e:
        log(f"WARN: primary fetch failed: {e}")
        return None
    except Exception as e:
        log(f"WARN: unexpected fetch error: {e}")
        return None


def normalize_api_response(raw: dict) -> dict:
    """
    Turn the raw OilPriceAPI response into our internal snapshot shape.
    Expected raw shape: {"status":"success","data":[{"code":"WTI_USD","price":...}, ...]}
    """
    prices = {}
    items = raw.get("data", []) if isinstance(raw, dict) else []
    for item in items:
        code = item.get("code")
        display = CODE_MAP.get(code)
        if not display:
            continue
        try:
            price = float(item.get("price", 0))
            change = float(item.get("change", 0) or 0)
            pct = float(item.get("pct_change", 0) or 0)
        except (TypeError, ValueError):
            continue
        prices[display] = {
            "price": round(price, 4),
            "change": round(change, 4),
            "pct": round(pct, 4),
            "unit": UNIT_MAP.get(display, ""),
            "source_code": code,
        }
    return prices


def write_snapshot(prices: dict, status: str, prev: dict | None) -> None:
    """Atomic write: .new then rename."""
    now = datetime.now(timezone.utc).isoformat()
    snapshot = {
        "meta": {
            "generated_at": now,
            "status": status,  # fresh | stale | failed
            "source": "oilpriceapi",
            "endpoint": "https://api.oilpriceapi.com/v1/prices/all",
        },
        "prices": prices,
    }
    # Preserve last successful fetch time across failed runs
    if status == "failed" and prev:
        snapshot["meta"]["last_success"] = prev.get("meta", {}).get("last_success") \
                                             or prev.get("meta", {}).get("generated_at")
        snapshot["meta"]["generated_at"] = prev.get("meta", {}).get("generated_at", now)
    else:
        snapshot["meta"]["last_success"] = now

    tmp = OUTPUT_PATH.with_suffix(".new")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2)
    tmp.replace(OUTPUT_PATH)


def main() -> int:
    config = load_config()
    prev = load_previous_snapshot()

    raw = fetch_from_api(config)
    if raw is None:
        # Primary failed. Keep previous snapshot data but flag as failed.
        if prev and prev.get("prices"):
            write_snapshot(prev["prices"], "failed", prev)
            log("Kept previous snapshot; marked status=failed")
            return 0
        else:
            log("ERROR: no previous snapshot to preserve and API failed")
            # Write an empty failed snapshot so downstream knows
            write_snapshot({}, "failed", None)
            return 0

    prices = normalize_api_response(raw)
    if not prices:
        log("WARN: API responded but no usable prices parsed")
        if prev and prev.get("prices"):
            write_snapshot(prev["prices"], "failed", prev)
            return 0
        write_snapshot({}, "failed", None)
        return 0

    write_snapshot(prices, "fresh", prev)
    log(f"OK: fetched {len(prices)} commodity prices")
    return 0


if __name__ == "__main__":
    sys.exit(main())
