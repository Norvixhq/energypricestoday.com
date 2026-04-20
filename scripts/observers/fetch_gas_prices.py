#!/usr/bin/env python3
"""
fetch_gas_prices.py — Observer for AAA + EIA national gas prices.

Strategy:
  1. Try AAA scrape (blocked from GitHub runners but works locally)
  2. Fall back to EIA weekly API if AAA fails
  3. If both fail, keep the previous snapshot with status=failed

Writes data/sources/gas-prices-national.json with fields:
  regular, mid, premium, diesel, source, updated

EIA API is free with registration: https://www.eia.gov/opendata/
Series used: PET.EMM_EPMR_PTE_NUS_DPG.W (regular gasoline weekly U.S. avg)
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib import request, error as urlerror

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from lib import quota  # noqa: E402
OUTPUT_PATH = ROOT / "data" / "sources" / "gas-prices-national.json"
LOG_PATH = ROOT / "data" / "logs" / "gas-prices-national.log"

EIA_API_KEY = os.environ.get("EIA_API_KEY", "")
EIA_SERIES = {
    "regular": "EMM_EPMR_PTE_NUS_DPG",
    "mid":     "EMM_EPMM_PTE_NUS_DPG",
    "premium": "EMM_EPMP_PTE_NUS_DPG",
    "diesel":  "EMD_EPD2D_PTE_NUS_DPG",
}


def log(msg: str) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now(timezone.utc).isoformat()}] {msg}\n")
    print(msg)


def load_previous() -> dict | None:
    if not OUTPUT_PATH.exists():
        return None
    try:
        with open(OUTPUT_PATH, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def try_aaa() -> dict | None:
    """
    Attempt AAA fetch. Uses a browser-like User-Agent but GitHub Actions
    IPs are usually blocked (403). Returns None on any failure.
    """
    try:
        req = request.Request(
            "https://gasprices.aaa.com/",
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
            },
        )
        with request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
            quota.record("aaa", endpoint="gasprices", succeeded=True)
    except Exception as e:
        quota.record("aaa", endpoint="gasprices", succeeded=False)
        log(f"AAA fetch failed (expected on GitHub runners): {e}")
        return None

    # Look for the 4 price fields in AAA's page
    # AAA markup varies; try a few common patterns
    prices = {}
    # Pattern: <td>Regular</td><td>$4.058</td>
    for grade, label in [("regular", "Regular"), ("mid", "Mid-Grade"),
                         ("premium", "Premium"), ("diesel", "Diesel")]:
        m = re.search(
            rf">{label}</[^>]*>\s*<[^>]*>\s*\$?([\d.]+)",
            html, re.IGNORECASE,
        )
        if m:
            try:
                prices[grade] = float(m.group(1))
            except ValueError:
                pass

    if len(prices) < 4:
        log(f"AAA page returned but parsed {len(prices)}/4 grades")
        return None

    return {
        "regular": prices["regular"],
        "mid":     prices["mid"],
        "premium": prices["premium"],
        "diesel":  prices["diesel"],
        "source":  "AAA Daily Fuel Gauge Report",
        "updated": datetime.now(timezone.utc).strftime("%B %d, %Y"),
    }


def try_eia() -> dict | None:
    """EIA weekly gasoline + diesel averages. Requires EIA_API_KEY."""
    if not EIA_API_KEY:
        log("EIA fallback skipped: no EIA_API_KEY set")
        return None

    prices = {}
    for grade, series_id in EIA_SERIES.items():
        url = (
            f"https://api.eia.gov/v2/petroleum/pri/gnd/data/"
            f"?frequency=weekly&data[0]=value&facets[series][]={series_id}"
            f"&sort[0][column]=period&sort[0][direction]=desc"
            f"&offset=0&length=1&api_key={EIA_API_KEY}"
        )
        try:
            with request.urlopen(url, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            series_data = data.get("response", {}).get("data", [])
            if series_data:
                prices[grade] = round(float(series_data[0]["value"]), 4)
            quota.record("eia", endpoint=f"gasoline/{grade}", succeeded=True)
        except Exception as e:
            quota.record("eia", endpoint=f"gasoline/{grade}", succeeded=False)
            log(f"EIA {grade} fetch failed: {e}")

    if len(prices) < 4:
        log(f"EIA returned {len(prices)}/4 grades")
        return None

    return {
        "regular": prices["regular"],
        "mid":     prices["mid"],
        "premium": prices["premium"],
        "diesel":  prices["diesel"],
        "source":  "EIA Weekly Retail Gasoline Prices",
        "updated": datetime.now(timezone.utc).strftime("%B %d, %Y"),
    }


def write_snapshot(data: dict | None, status: str, prev: dict | None) -> None:
    now = datetime.now(timezone.utc).isoformat()
    snapshot = {"meta": {"generated_at": now, "status": status}}

    if data:
        snapshot["prices"] = {
            "regular": data["regular"],
            "mid":     data["mid"],
            "premium": data["premium"],
            "diesel":  data["diesel"],
        }
        snapshot["meta"]["source_label"] = data["source"]
        snapshot["meta"]["source_date"] = data["updated"]
        snapshot["meta"]["last_success"] = now
    elif prev and prev.get("prices"):
        snapshot["prices"] = prev["prices"]
        snapshot["meta"]["source_label"] = prev.get("meta", {}).get("source_label", "Unknown")
        snapshot["meta"]["last_success"] = prev.get("meta", {}).get("last_success")
        snapshot["meta"]["generated_at"] = prev.get("meta", {}).get("generated_at", now)
    else:
        snapshot["prices"] = {}

    tmp = OUTPUT_PATH.with_suffix(".new")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2)
    tmp.replace(OUTPUT_PATH)


def main() -> int:
    prev = load_previous()

    data = try_aaa()
    if data:
        write_snapshot(data, "fresh", prev)
        log(f"OK: AAA regular=${data['regular']:.3f} diesel=${data['diesel']:.3f}")
        return 0

    data = try_eia()
    if data:
        write_snapshot(data, "fresh", prev)
        log(f"OK: EIA regular=${data['regular']:.3f} diesel=${data['diesel']:.3f}")
        return 0

    # Both failed. Keep previous snapshot if available.
    if prev and prev.get("prices"):
        write_snapshot(None, "failed", prev)
        log("Both AAA and EIA failed; kept previous snapshot")
        return 0

    log("ERROR: no data available and no previous snapshot to preserve")
    write_snapshot(None, "failed", None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
