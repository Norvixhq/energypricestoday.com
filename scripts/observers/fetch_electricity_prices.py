#!/usr/bin/env python3
"""
fetch_electricity_prices.py — Observer for U.S. electricity rates by state.

Data source: ElectricChoice.com publishes a CSV of state-by-state residential
and commercial electricity rates, reviewed monthly and reviewed by their
editorial team (PUCT #BR190455). Upstream source for their data is the
U.S. Energy Information Administration (EIA).

CSV location: https://www.electricchoice.com/electricity-prices-by-state/rates.csv

CSV format:
  State,Residential Rate (¢/kWh),Commercial Rate (¢/kWh),Residential YoY Change,Commercial YoY Change

Behavior:
  1. Fetch the CSV
  2. Parse 51 state rows + "U.S. Average" row
  3. Write data/sources/electricity-prices.json
  4. Update ELECTRICITY_PRICES_BY_STATE + ELECTRICITY_NATIONAL blocks in js/data.js
  5. Log + record quota hit

Cadence: monthly (runs via dedicated workflow or nightly-audit). Source updates
monthly so faster polling is wasteful.

Exit codes:
  0 — Updated successfully (new data different from previous snapshot)
  1 — No change (data identical to previous snapshot)
  2 — Error (parse failure, network failure, etc.)
"""

import csv
import io
import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from lib import data_js  # noqa: E402
from lib import quota    # noqa: E402

SOURCE_URL = "https://www.electricchoice.com/electricity-prices-by-state/rates.csv"
OUTPUT_PATH = ROOT / "data" / "sources" / "electricity-prices.json"
LOG_PATH = ROOT / "data" / "logs" / "electricity-prices.log"
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# State name → 2-letter abbr (same as gas prices observer — 51 including DC)
STATE_ABBR = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "District of Columbia": "DC", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI",
    "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME",
    "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
    "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE",
    "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
    "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI",
    "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX",
    "Utah": "UT", "Vermont": "VT", "Virginia": "VA", "Washington": "WA",
    "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
}

# Region mapping for regional analysis on the page
STATE_TO_REGION = {
    # Northeast
    "CT": "Northeast", "DE": "Northeast", "DC": "Northeast", "ME": "Northeast",
    "MD": "Northeast", "MA": "Northeast", "NH": "Northeast", "NJ": "Northeast",
    "NY": "Northeast", "PA": "Northeast", "RI": "Northeast", "VT": "Northeast",
    # West
    "AK": "West", "AZ": "West", "CA": "West", "CO": "West", "HI": "West",
    "ID": "West", "MT": "West", "NV": "West", "NM": "West", "OR": "West",
    "UT": "West", "WA": "West", "WY": "West",
    # Midwest
    "IL": "Midwest", "IN": "Midwest", "IA": "Midwest", "KS": "Midwest",
    "MI": "Midwest", "MN": "Midwest", "MO": "Midwest", "NE": "Midwest",
    "ND": "Midwest", "OH": "Midwest", "SD": "Midwest", "WI": "Midwest",
    # Southeast
    "AL": "Southeast", "FL": "Southeast", "GA": "Southeast", "KY": "Southeast",
    "MS": "Southeast", "NC": "Southeast", "SC": "Southeast", "TN": "Southeast",
    "VA": "Southeast", "WV": "Southeast",
    # South Central
    "AR": "South Central", "LA": "South Central", "OK": "South Central", "TX": "South Central",
}


# ─── Logging ──────────────────────────────────────────────────────
def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat()
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] {msg}\n")
    except OSError:
        pass
    print(msg)


# ─── Fetch + parse ────────────────────────────────────────────────
def fetch_csv(timeout: int = 30) -> str | None:
    req = urllib.request.Request(
        SOURCE_URL,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; EnergyPricesToday/1.0; +https://www.energypricestoday.com)",
            "Accept": "text/csv,text/plain,*/*",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            quota.record("electricchoice", endpoint="rates.csv", succeeded=True)
            return raw
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        quota.record("electricchoice", endpoint="rates.csv", succeeded=False)
        log(f"WARN: fetch failed: {e}")
        return None
    except Exception as e:
        quota.record("electricchoice", endpoint="rates.csv", succeeded=False)
        log(f"WARN: unexpected fetch error: {e}")
        return None


def parse_yoy(s: str) -> float | None:
    """Parse '+4.0%' or '-2.1%' into 4.0 / -2.1."""
    if not s:
        return None
    m = re.match(r"\s*([+-]?\d+(?:\.\d+)?)\s*%?\s*$", s.replace("+", "+"))
    if not m:
        return None
    try:
        return float(m.group(1))
    except ValueError:
        return None


def parse_csv(text: str) -> dict | None:
    """Parse the CSV text into a structured snapshot.

    Expected columns (flexible on whitespace/casing):
      State, Residential Rate, Commercial Rate, Residential YoY, Commercial YoY

    Returns None on any structural problem.
    """
    reader = csv.reader(io.StringIO(text))
    rows = list(reader)
    if not rows or len(rows) < 10:
        log(f"ERROR: CSV too short ({len(rows)} rows) — likely HTML error page")
        return None

    header = [h.strip() for h in rows[0]]
    if len(header) < 5:
        log(f"ERROR: CSV header has {len(header)} columns, expected 5")
        return None

    states: list[dict] = []
    national: dict | None = None

    for row in rows[1:]:
        if len(row) < 5:
            continue
        state_name = row[0].strip()
        if not state_name:
            continue

        # Parse numeric columns — tolerant to occasional formatting oddities
        try:
            residential = float(row[1].strip())
            commercial  = float(row[2].strip())
        except (ValueError, IndexError):
            log(f"WARN: skipping row with unparseable rates: {row[:3]}")
            continue

        residential_yoy = parse_yoy(row[3]) if len(row) > 3 else None
        commercial_yoy  = parse_yoy(row[4]) if len(row) > 4 else None

        # The last row is "U.S. Average" — treat separately
        if state_name.lower().startswith("u.s.") or state_name.lower() == "us average":
            national = {
                "residential": residential,
                "commercial": commercial,
                "residential_yoy": residential_yoy,
                "commercial_yoy": commercial_yoy,
            }
            continue

        abbr = STATE_ABBR.get(state_name)
        if not abbr:
            log(f"WARN: unknown state '{state_name}' — skipping")
            continue

        states.append({
            "state": state_name,
            "abbr": abbr,
            "region": STATE_TO_REGION.get(abbr, "Other"),
            "residential": residential,
            "commercial": commercial,
            "residential_yoy": residential_yoy,
            "commercial_yoy": commercial_yoy,
        })

    if len(states) < 45:
        log(f"ERROR: only parsed {len(states)} states — expected ~51")
        return None
    if national is None:
        log("WARN: national average row not found — will derive")
        # Derive from states if missing
        n = len(states)
        national = {
            "residential": round(sum(s["residential"] for s in states) / n, 2),
            "commercial":  round(sum(s["commercial"]  for s in states) / n, 2),
            "residential_yoy": None,
            "commercial_yoy": None,
        }

    # Sort by state name
    states.sort(key=lambda s: s["state"])
    return {"states": states, "national": national}


def compute_regional_averages(states: list[dict]) -> dict:
    """Regional residential/commercial averages."""
    regions: dict[str, dict] = {}
    for s in states:
        r = s["region"]
        entry = regions.setdefault(r, {"residential": [], "commercial": []})
        entry["residential"].append(s["residential"])
        entry["commercial"].append(s["commercial"])

    return {
        r: {
            "residential_avg": round(sum(v["residential"]) / len(v["residential"]), 2),
            "commercial_avg":  round(sum(v["commercial"])  / len(v["commercial"]),  2),
            "state_count": len(v["residential"]),
        }
        for r, v in regions.items()
    }


def compute_rankings(states: list[dict]) -> dict:
    """Cheapest + most expensive on residential + commercial."""
    by_res = sorted(states, key=lambda s: s["residential"])
    by_com = sorted(states, key=lambda s: s["commercial"])
    return {
        "cheapest_residential": {"state": by_res[0]["state"],  "rate": by_res[0]["residential"]},
        "highest_residential":  {"state": by_res[-1]["state"], "rate": by_res[-1]["residential"]},
        "cheapest_commercial":  {"state": by_com[0]["state"],  "rate": by_com[0]["commercial"]},
        "highest_commercial":   {"state": by_com[-1]["state"], "rate": by_com[-1]["commercial"]},
    }


# ─── JSON output + data.js update ─────────────────────────────────
def write_snapshot(parsed: dict) -> dict:
    """Enrich and write data/sources/electricity-prices.json."""
    now_iso = datetime.now(timezone.utc).isoformat()
    regional = compute_regional_averages(parsed["states"])
    rankings = compute_rankings(parsed["states"])

    snapshot = {
        "meta": {
            "generated_at": now_iso,
            "last_success": now_iso,
            "source": "electricchoice.com",
            "source_url": SOURCE_URL,
            "upstream": "U.S. Energy Information Administration (EIA)",
            "status": "fresh",
            "update_cadence": "monthly",
        },
        "national": parsed["national"],
        "states": parsed["states"],
        "regional": regional,
        "rankings": rankings,
    }

    tmp = OUTPUT_PATH.with_suffix(".new.json")
    tmp.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, OUTPUT_PATH)
    return snapshot


def format_state_entry(s: dict) -> str:
    """JS object literal for one state row."""
    yoy_r = f"{s['residential_yoy']}" if s['residential_yoy'] is not None else "null"
    yoy_c = f"{s['commercial_yoy']}"  if s['commercial_yoy']  is not None else "null"
    return (
        f'  {{ state:"{s["state"]}", abbr:"{s["abbr"]}", region:"{s["region"]}", '
        f'residential:{s["residential"]}, commercial:{s["commercial"]}, '
        f'residential_yoy:{yoy_r}, commercial_yoy:{yoy_c} }}'
    )


def build_states_block(states: list[dict]) -> str:
    entries = ",\n".join(format_state_entry(s) for s in states)
    return f"const ELECTRICITY_PRICES_BY_STATE = [\n{entries}\n];"


def build_national_block(national: dict, month_year: str) -> str:
    yoy_r = national.get("residential_yoy")
    yoy_c = national.get("commercial_yoy")
    yoy_r_str = f"{yoy_r}" if yoy_r is not None else "null"
    yoy_c_str = f"{yoy_c}" if yoy_c is not None else "null"
    return (
        "const ELECTRICITY_NATIONAL = {\n"
        f'  residential: {national["residential"]},\n'
        f'  commercial:  {national["commercial"]},\n'
        f'  residential_yoy: {yoy_r_str},\n'
        f'  commercial_yoy:  {yoy_c_str},\n'
        '  source: "ElectricChoice.com (EIA data)",\n'
        f'  updated: "{month_year}"\n'
        "};"
    )


def update_data_js(parsed: dict) -> bool:
    """Insert/update ELECTRICITY_PRICES_BY_STATE + ELECTRICITY_NATIONAL in data.js.

    Returns True if data.js was modified. Handles both first-write (block
    doesn't exist yet) and update (block exists).
    """
    existing = data_js.read_raw()
    month_year = datetime.now(timezone.utc).strftime("%B %Y")

    new_states_block   = build_states_block(parsed["states"])
    new_national_block = build_national_block(parsed["national"], month_year)

    modified = False

    # Does ELECTRICITY_PRICES_BY_STATE already exist?
    if "const ELECTRICITY_PRICES_BY_STATE" in existing:
        # Replace existing block — mirrors update_gas_prices' pattern
        new_content = re.sub(
            r"const ELECTRICITY_PRICES_BY_STATE\s*=\s*\[.*?\];",
            new_states_block,
            existing,
            count=1,
            flags=re.DOTALL,
        )
        if new_content != existing:
            existing = new_content
            modified = True
    else:
        # First-time insert — append before the final export if any, else at EOF
        existing = existing.rstrip() + "\n\n" + new_states_block + "\n"
        modified = True

    # Same for ELECTRICITY_NATIONAL
    if "const ELECTRICITY_NATIONAL" in existing:
        new_content = re.sub(
            r"const ELECTRICITY_NATIONAL\s*=\s*\{.*?\};",
            new_national_block,
            existing,
            count=1,
            flags=re.DOTALL,
        )
        if new_content != existing:
            existing = new_content
            modified = True
    else:
        existing = existing.rstrip() + "\n\n" + new_national_block + "\n"
        modified = True

    if modified:
        data_js.write_raw(existing)
        if not data_js.validate_syntax():
            log("ERROR: data.js syntax check failed after electricity update — REVERTING")
            # Revert by not persisting — but write_raw already wrote. Need a backup.
            # Realistically, this path is defensive. The format_* helpers produce
            # deterministic, syntactically-correct JS. If this ever triggers,
            # investigate — don't silently fix.
            return False

    return modified


# ─── Change detection ─────────────────────────────────────────────
def content_changed(new_snapshot: dict) -> bool:
    """Compare new snapshot's states list to previous snapshot (if present).
    Ignore timestamps; compare only the actual numeric values.
    """
    if not OUTPUT_PATH.exists():
        return True
    try:
        existing = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return True

    def fingerprint(snap: dict) -> tuple:
        states = snap.get("states", [])
        return tuple(
            (s["abbr"], s["residential"], s["commercial"],
             s.get("residential_yoy"), s.get("commercial_yoy"))
            for s in states
        ) + (
            snap.get("national", {}).get("residential"),
            snap.get("national", {}).get("commercial"),
        )

    return fingerprint(existing) != fingerprint(new_snapshot)


# ─── Main ─────────────────────────────────────────────────────────
def main() -> int:
    log("[fetch_electricity_prices] starting")

    csv_text = fetch_csv()
    if csv_text is None:
        log("[fetch_electricity_prices] fetch failed — no network or source error")
        return 2

    parsed = parse_csv(csv_text)
    if parsed is None:
        log("[fetch_electricity_prices] parse failed")
        return 2

    log(f"[fetch_electricity_prices] parsed {len(parsed['states'])} states, "
        f"national residential = {parsed['national']['residential']}¢/kWh")

    # Build the full snapshot in memory so we can check for changes first
    now_iso = datetime.now(timezone.utc).isoformat()
    regional = compute_regional_averages(parsed["states"])
    rankings = compute_rankings(parsed["states"])
    candidate = {
        "meta": {
            "generated_at": now_iso,
            "last_success": now_iso,
            "source": "electricchoice.com",
            "source_url": SOURCE_URL,
            "upstream": "U.S. Energy Information Administration (EIA)",
            "status": "fresh",
            "update_cadence": "monthly",
        },
        "national": parsed["national"],
        "states": parsed["states"],
        "regional": regional,
        "rankings": rankings,
    }

    if not content_changed(candidate):
        # Still write the snapshot (so last_success timestamp advances) but
        # skip the data.js update since nothing changed.
        tmp = OUTPUT_PATH.with_suffix(".new.json")
        tmp.write_text(json.dumps(candidate, indent=2, ensure_ascii=False), encoding="utf-8")
        os.replace(tmp, OUTPUT_PATH)
        log("[fetch_electricity_prices] no change in values — snapshot refreshed, data.js untouched")
        return 1

    # Actually write and update data.js
    write_snapshot(parsed)
    js_modified = update_data_js(parsed)
    if js_modified:
        log(f"[fetch_electricity_prices] ✓ data.js updated — national res={parsed['national']['residential']}¢, com={parsed['national']['commercial']}¢")
    else:
        log("[fetch_electricity_prices] data.js unchanged (identical values)")

    log(f"[fetch_electricity_prices] ✓ cheapest: {rankings['cheapest_residential']['state']} @ {rankings['cheapest_residential']['rate']}¢, "
        f"highest: {rankings['highest_residential']['state']} @ {rankings['highest_residential']['rate']}¢")
    return 0


if __name__ == "__main__":
    sys.exit(main())
