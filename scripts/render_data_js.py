#!/usr/bin/env python3
"""
render_data_js.py — Phase 1 renderer.

Reads:
  - data/sources/commodity-prices.json
  - data/sources/gas-prices-national.json
  - data/overrides/prices.json
  - data/state/changes.json

Updates:
  - js/data.js COMMODITIES array prices (in-place, surgical)
    * ONLY for commodities NOT handled by live-data.js client-side
    * API-backed commodities (WTI, Brent, Natural Gas, Gasoline, Heating Oil,
      Diesel, Jet Fuel, Coal from Newcastle, Gold, etc.) are left untouched
      because live-data.js updates them every 5 minutes from OilPriceAPI.
      Writing to them server-side creates pollution and risks stale-cache
      flashes; the client handles them better.
    * Hardcoded commodities that ARE touched: Murban Crude, FULL_PRICES
      secondary blends, anything that live-data.js doesn't have a CODE_MAP
      entry for.
  - js/data.js US_GAS_NATIONAL object (in-place, surgical)
    * Gas prices are NOT updated by live-data.js — they're fully static
      today, so this is the renderer's responsibility.

Rules:
  1. Only rewrite if there are meaningful changes in data/state/changes.json
     OR --force flag is passed
  2. Active override entries always win over observer data
  3. Preserves every other field, line, and ordering in js/data.js
  4. Atomic write: .new file then rename
  5. Exits 0 on success with clear "changes applied" or "no-op" log

This is a PRECISE string-level rewriter — it does not reformat the file.
The goal is minimum diff to the existing data.js so git commits stay clean.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_JS = ROOT / "js" / "data.js"
LIVE_DATA_JS = ROOT / "js" / "live-data.js"
SOURCES_DIR = ROOT / "data" / "sources"
OVERRIDES_DIR = ROOT / "data" / "overrides"
STATE_DIR = ROOT / "data" / "state"


def load_api_backed_names() -> set[str]:
    """
    Parse live-data.js CODE_MAP to find every commodity display name that is
    refreshed client-side from OilPriceAPI. These names are OFF-LIMITS to
    the server-side renderer.
    """
    names = set()
    if not LIVE_DATA_JS.exists():
        return names
    with open(LIVE_DATA_JS, encoding="utf-8") as f:
        content = f.read()
    # Find var CODE_MAP = { ... };
    m = re.search(r"var\s+CODE_MAP\s*=\s*\{([\s\S]*?)\};", content)
    if not m:
        return names
    block = m.group(1)
    # Each entry: 'Display Name': 'API_CODE',
    for em in re.finditer(r"'([^']+)'\s*:\s*'([A-Z0-9_]+)'", block):
        names.add(em.group(1))
    return names


def load_json_or(path: Path, default=None):
    if not path.exists():
        return default
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def apply_overrides(prices: dict, override_file: dict, section: str) -> dict:
    """Replace prices with active overrides from the override file."""
    overrides = override_file.get(section, {}) if override_file else {}
    result = dict(prices)
    for name, entry in overrides.items():
        if name.startswith("_"):
            continue
        if not isinstance(entry, dict):
            continue
        if not entry.get("active"):
            continue
        if section == "commodity_prices":
            result[name] = {
                "price": entry.get("price"),
                "change": entry.get("change", 0),
                "pct": entry.get("pct", 0),
            }
        elif section == "gas_prices_national":
            # Whole object override
            result = {
                "regular": entry.get("regular"),
                "mid":     entry.get("mid"),
                "premium": entry.get("premium"),
                "diesel":  entry.get("diesel"),
                "_override": True,
                "_reason":   entry.get("reason"),
            }
    return result


def update_commodities_line(line: str, prices: dict, api_backed: set[str]) -> str:
    """
    Given a single line from the COMMODITIES array, replace its price/change/pct
    fields with values from `prices` if the commodity name appears in prices.
    Returns the updated line unchanged if no match.

    API-backed commodities (updated by live-data.js every 5 min) are skipped —
    we do not want to churn those values in git.
    """
    # Match the commodity name first: { name: "WTI Crude", ...
    name_m = re.search(r'name:\s*"([^"]+)"', line)
    if not name_m:
        return line
    name = name_m.group(1)
    if name in api_backed:
        return line  # live-data.js owns this commodity; leave it alone
    if name not in prices:
        return line

    newp = prices[name]
    if newp.get("price") is None:
        return line

    new_price = round(float(newp["price"]), 4)
    new_change = round(float(newp.get("change") or 0), 4)
    new_pct = round(float(newp.get("pct") or 0), 4)

    # Use formatting matching existing style (compact trailing zeros handled)
    def fmt(n: float) -> str:
        # Keep up to 4 decimals but strip trailing zeros like the source data
        if n == int(n):
            return str(int(n))
        s = f"{n:.4f}".rstrip("0").rstrip(".")
        return s

    line = re.sub(r'(price:\s*)[-\d.]+',  rf'\g<1>{fmt(new_price)}', line, count=1)
    line = re.sub(r'(change:\s*)[-\d.]+', rf'\g<1>{fmt(new_change)}', line, count=1)
    line = re.sub(r'(pct:\s*)[-\d.]+',    rf'\g<1>{fmt(new_pct)}', line, count=1)
    return line


def update_commodities_block(content: str, prices: dict, api_backed: set[str]) -> tuple[str, int]:
    """Walk each line of the COMMODITIES array and patch matching non-API-backed ones."""
    # Find the array boundaries
    m = re.search(r"(const COMMODITIES\s*=\s*\[\n)([\s\S]*?)(\n\];)", content)
    if not m:
        return content, 0

    prefix, body, suffix = m.group(1), m.group(2), m.group(3)
    lines = body.split("\n")
    updated_count = 0
    new_lines = []
    for line in lines:
        new_line = update_commodities_line(line, prices, api_backed)
        if new_line != line:
            updated_count += 1
        new_lines.append(new_line)
    new_body = "\n".join(new_lines)

    if new_body == body:
        return content, 0

    new_content = content[:m.start()] + prefix + new_body + suffix + content[m.end():]
    return new_content, updated_count


def update_full_prices_block(content: str, prices: dict, api_backed: set[str]) -> tuple[str, int]:
    """
    Walk the FULL_PRICES object. Same non-API-backed rule applies, but the
    FULL_PRICES entries are mostly secondary blends (OPEC Basket, Arab Light,
    Bonny Light, Louisiana Light, WTI Midland, Canadian blends, etc.) that
    are currently stale hardcoded values. Observer doesn't yet fetch these
    individually, so for now this is a pass-through — leaves them untouched.

    Future (Phase 2/3): extend observer CODE_MAP to fetch OPEC Basket and
    other secondary blends that OilPriceAPI provides, then this function
    will actually update them.
    """
    # Phase 1: no-op. Return unchanged.
    return content, 0


def update_gas_national_block(content: str, gas_prices: dict, source_label: str) -> tuple[str, bool]:
    """Replace the US_GAS_NATIONAL object with fresh values."""
    m = re.search(r"(const US_GAS_NATIONAL\s*=\s*\{)([\s\S]*?)(\};)", content)
    if not m:
        return content, False

    old_inner = m.group(2)

    # Build the new inner object
    def fmt(n):
        return f"{n:.3f}" if n is not None else "null"

    updated_date = datetime.now(timezone.utc).strftime("%B %d, %Y")
    new_inner = (
        f'\n  regular: {fmt(gas_prices.get("regular"))},\n'
        f'  mid: {fmt(gas_prices.get("mid"))},\n'
        f'  premium: {fmt(gas_prices.get("premium"))},\n'
        f'  diesel: {fmt(gas_prices.get("diesel"))},\n'
        f'  source: "{source_label}",\n'
        f'  updated: "As of {updated_date}"\n'
    )

    if new_inner.strip() == old_inner.strip():
        return content, False

    new_content = content[:m.start()] + m.group(1) + new_inner + m.group(3) + content[m.end():]
    return new_content, True


def write_data_js(content: str) -> None:
    tmp = DATA_JS.with_suffix(".new.js")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
    tmp.replace(DATA_JS)


def should_render(changes: dict, force: bool) -> tuple[bool, str]:
    """Return (should_render, reason)."""
    if force:
        return True, "forced"
    if not changes:
        return False, "no changeset"
    sources = changes.get("sources", {})
    total_changes = sum(len(s.get("changes", [])) for s in sources.values())
    status_flips = sum(1 for s in sources.values() if s.get("status_flip"))
    if total_changes == 0 and status_flips == 0:
        return False, "no meaningful changes"
    return True, f"{total_changes} price changes, {status_flips} status flips"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true",
                        help="Re-render even if no meaningful changes detected")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print planned changes without writing")
    args = parser.parse_args()

    # Load current state
    commodity_snap = load_json_or(SOURCES_DIR / "commodity-prices.json", {})
    gas_snap       = load_json_or(SOURCES_DIR / "gas-prices-national.json", {})
    overrides      = load_json_or(OVERRIDES_DIR / "prices.json", {})
    changes        = load_json_or(STATE_DIR / "changes.json", {})

    proceed, reason = should_render(changes, args.force)
    if not proceed:
        print(f"[render_data_js] no-op: {reason}")
        return 0

    print(f"[render_data_js] rendering: {reason}")

    # Apply overrides on top of observer data
    commodity_prices = apply_overrides(
        commodity_snap.get("prices", {}),
        overrides,
        "commodity_prices",
    )
    gas_prices = apply_overrides(
        gas_snap.get("prices", {}),
        overrides,
        "gas_prices_national",
    )

    # Determine which commodities live-data.js owns (we don't touch those)
    api_backed = load_api_backed_names()
    if api_backed:
        print(f"[render_data_js] live-data.js owns {len(api_backed)} commodities — skipping those")

    if not DATA_JS.exists():
        print("[render_data_js] ERROR: js/data.js not found")
        return 2

    with open(DATA_JS, encoding="utf-8") as f:
        content = f.read()
    original = content

    # Update COMMODITIES (only non-API-backed entries)
    if commodity_prices:
        content, n_updated = update_commodities_block(content, commodity_prices, api_backed)
        print(f"  COMMODITIES: {n_updated} non-API-backed entries updated")

    # Update US_GAS_NATIONAL
    if gas_prices and all(gas_prices.get(g) is not None for g in ("regular", "mid", "premium", "diesel")):
        source_label = gas_snap.get("meta", {}).get("source_label", "AAA Daily Fuel Gauge Report")
        if gas_prices.get("_override"):
            source_label = gas_prices.get("_reason") or "Manual override"
        content, gas_updated = update_gas_national_block(content, gas_prices, source_label)
        print(f"  US_GAS_NATIONAL: {'updated' if gas_updated else 'no change'}")

    if content == original:
        print("[render_data_js] computed changes equal existing values; writing skipped")
        return 0

    if args.dry_run:
        print("[render_data_js] --dry-run: would write js/data.js (not written)")
        return 0

    write_data_js(content)
    print("[render_data_js] ✓ js/data.js updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
