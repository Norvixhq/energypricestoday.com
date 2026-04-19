#!/usr/bin/env python3
"""
update_gas_prices.py — Scrape AAA daily fuel gauge report and update
the GAS_PRICES_BY_STATE and US_GAS_NATIONAL blocks in data.js.

AAA data source: https://gasprices.aaa.com/state-gas-price-averages/
Update frequency: AAA refreshes daily around 7am ET. Running 3x/day
(10am/2pm/7pm CT) ensures we catch the daily update with redundancy.

Exit codes:
  0 — Updated successfully
  1 — No change needed (data identical)
  2 — Error (parse failure, network failure, etc.)
"""

import re
import sys
import urllib.request
import urllib.error
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import data_js  # noqa: E402

AAA_NATIONAL_URL = "https://gasprices.aaa.com/"
AAA_STATE_URL = "https://gasprices.aaa.com/state-gas-price-averages/"

# Map state name → 2-letter abbr (51 including DC)
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


def fetch(url: str, timeout: int = 20) -> str:
    req = urllib.request.Request(
        url,
        headers={
            # Mimic a real browser — AAA's WAF can 403 simple bot UAs
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/131.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "identity",  # avoid gzip — we want plain text
            "Referer": "https://gasprices.aaa.com/",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_national(html: str) -> dict:
    """Extract Current Avg. row: Regular, Mid-Grade, Premium, Diesel."""
    # Find the Current Avg table row
    # Pattern: | Current Avg. | $4.058 | $4.569 | $4.936 | $5.570 | $3.228 |
    # Or HTML table equivalent
    m = re.search(
        r"Current\s*Avg\.?\s*</?t[dh][^>]*>\s*\|?\s*"  # label + optional cell close
        r"\$?([\d.]+)\s*</?t[dh][^>]*>\s*\|?\s*"        # regular
        r"\$?([\d.]+)\s*</?t[dh][^>]*>\s*\|?\s*"        # mid
        r"\$?([\d.]+)\s*</?t[dh][^>]*>\s*\|?\s*"        # premium
        r"\$?([\d.]+)",                                 # diesel
        html,
    )
    if not m:
        # Fallback: markdown-ish pipe table (as AAA sometimes renders)
        m = re.search(
            r"Current Avg\.\s*\|\s*\$?([\d.]+)\s*\|\s*\$?([\d.]+)\s*\|"
            r"\s*\$?([\d.]+)\s*\|\s*\$?([\d.]+)",
            html,
        )
    if not m:
        raise ValueError("Could not parse national averages from AAA page")

    return {
        "regular": float(m.group(1)),
        "mid": float(m.group(2)),
        "premium": float(m.group(3)),
        "diesel": float(m.group(4)),
    }


def parse_states(html: str) -> list[dict]:
    """Extract per-state table rows.

    AAA renders as either HTML table rows or (if we get markdown output)
    pipe-delimited rows. We support both.
    """
    rows = []
    seen = set()

    # Pattern for pipe-delimited: | State | $X.XXX | $X.XXX | $X.XXX | $X.XXX |
    for m in re.finditer(
        r"\|\s*(?:\[)?([A-Z][A-Za-z ]+?)(?:\])?(?:\([^)]+\))?\s*\|\s*"
        r"\$?([\d.]+)\s*\|\s*\$?([\d.]+)\s*\|\s*\$?([\d.]+)\s*\|\s*\$?([\d.]+)",
        html,
    ):
        state = m.group(1).strip()
        if state in STATE_ABBR and state not in seen:
            seen.add(state)
            rows.append({
                "state": state,
                "abbr": STATE_ABBR[state],
                "regular": float(m.group(2)),
                "mid": float(m.group(3)),
                "premium": float(m.group(4)),
                "diesel": float(m.group(5)),
            })

    # Fallback: HTML table rows
    if len(rows) < 40:
        rows = []
        seen = set()
        # <tr>...<a href="?state=XX">State</a>...</td><td>$X.XXX</td>...
        for m in re.finditer(
            r'state=[A-Z]{2}[^>]*>([A-Za-z ]+?)</a>\s*</t[dh]>\s*'
            r'<t[dh][^>]*>\s*\$?([\d.]+)\s*</t[dh]>\s*'
            r'<t[dh][^>]*>\s*\$?([\d.]+)\s*</t[dh]>\s*'
            r'<t[dh][^>]*>\s*\$?([\d.]+)\s*</t[dh]>\s*'
            r'<t[dh][^>]*>\s*\$?([\d.]+)',
            html,
        ):
            state = m.group(1).strip()
            if state in STATE_ABBR and state not in seen:
                seen.add(state)
                rows.append({
                    "state": state,
                    "abbr": STATE_ABBR[state],
                    "regular": float(m.group(2)),
                    "mid": float(m.group(3)),
                    "premium": float(m.group(4)),
                    "diesel": float(m.group(5)),
                })

    if len(rows) < 45:
        raise ValueError(
            f"Parsed only {len(rows)} states — expected 51. Page structure may have changed."
        )

    # Sort alphabetically for consistent diffs
    rows.sort(key=lambda r: r["state"])
    return rows


def sanity_check(national: dict, states: list[dict]) -> list[str]:
    """Verify data is within sane ranges. Returns list of error messages."""
    errors = []
    # National should be $2-$8
    for grade, price in national.items():
        if not (2.0 <= price <= 8.0):
            errors.append(f"National {grade} = ${price} out of range (2-8)")
    # Each state should be $2-$9 (California outlier)
    for row in states:
        for grade in ["regular", "mid", "premium", "diesel"]:
            price = row[grade]
            if not (2.0 <= price <= 9.0):
                errors.append(f"{row['state']} {grade} = ${price} out of range")
    # State count
    if len(states) < 45:
        errors.append(f"Only {len(states)} states parsed")
    return errors


def serialize_states(states: list[dict]) -> str:
    """Serialize states as JS array matching existing data.js format."""
    entries = ",\n  ".join(
        f'{{ state:"{r["state"]}", abbr:"{r["abbr"]}", '
        f'regular:{r["regular"]:.3f}, mid:{r["mid"]:.3f}, '
        f'premium:{r["premium"]:.3f}, diesel:{r["diesel"]:.3f} }}'
        for r in states
    )
    return f"const GAS_PRICES_BY_STATE = [\n  {entries}\n];"


def serialize_national(n: dict) -> str:
    """Serialize national averages as JS object."""
    today = date.today().strftime("%B %-d, %Y")
    return (
        "const US_GAS_NATIONAL = {\n"
        f"  regular: {n['regular']:.3f},\n"
        f"  mid: {n['mid']:.3f},\n"
        f"  premium: {n['premium']:.3f},\n"
        f"  diesel: {n['diesel']:.3f},\n"
        '  source: "AAA Daily Fuel Gauge Report",\n'
        f'  updated: "As of {today}"\n'
        "};"
    )


def main() -> int:
    print(f"[update_gas_prices] Fetching AAA national averages...")
    try:
        html_national = fetch(AAA_NATIONAL_URL)
        national = parse_national(html_national)
        print(f"  National: Reg ${national['regular']}  Diesel ${national['diesel']}")
    except (urllib.error.URLError, ValueError, TimeoutError) as e:
        print(f"[update_gas_prices] FAIL fetching/parsing national: {e}")
        return 2

    print(f"[update_gas_prices] Fetching per-state data...")
    try:
        html_states = fetch(AAA_STATE_URL)
        states = parse_states(html_states)
        print(f"  Parsed {len(states)} states")
    except (urllib.error.URLError, ValueError, TimeoutError) as e:
        print(f"[update_gas_prices] FAIL fetching/parsing states: {e}")
        return 2

    errors = sanity_check(national, states)
    if errors:
        print("[update_gas_prices] SANITY CHECK FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 2

    # Check if anything actually changed
    existing = data_js.read_raw()
    new_national_js = serialize_national(national)
    new_states_js = serialize_states(states)

    # Current national block (strip updated date line for comparison)
    current_nat = re.search(
        r"const US_GAS_NATIONAL = \{.*?\};", existing, re.DOTALL
    )
    current_states = re.search(
        r"const GAS_PRICES_BY_STATE = \[.*?\];", existing, re.DOTALL
    )

    def strip_date(js: str) -> str:
        return re.sub(r'updated:\s*"[^"]*"', "", js)

    changed = False
    if current_nat is None or strip_date(current_nat.group(0)) != strip_date(new_national_js):
        changed = True
    if current_states is None or current_states.group(0) != new_states_js:
        changed = True

    if not changed:
        print("[update_gas_prices] No change — data identical.")
        return 1

    print("[update_gas_prices] Applying updates...")
    ok1 = data_js.replace_block("US_GAS_NATIONAL", new_national_js)
    ok2 = data_js.replace_block("GAS_PRICES_BY_STATE", new_states_js)
    if not (ok1 and ok2):
        print("[update_gas_prices] Block replacement failed")
        return 2

    print(f"[update_gas_prices] ✓ Updated — national ${national['regular']}, {len(states)} states")
    return 0


if __name__ == "__main__":
    sys.exit(main())
