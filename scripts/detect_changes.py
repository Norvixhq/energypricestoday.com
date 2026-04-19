#!/usr/bin/env python3
"""
detect_changes.py — Change detection layer.

Reads the current snapshot files in data/sources/, compares each one
against the previous-generation snapshot recorded in data/state/previous.json,
and writes a changeset to data/state/changes.json describing what moved
beyond the thresholds defined in data/config/thresholds.json.

Importantly: this script does NOT publish anything. It only produces
a structured description of what changed, which downstream renderers
and the orchestrator consume to decide whether work is needed.

Exit codes:
  0  = ran successfully (changes may or may not be present)
  2  = error (config missing, malformed state)
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CONFIG_DIR = DATA_DIR / "config"
SOURCES_DIR = DATA_DIR / "sources"
STATE_DIR = DATA_DIR / "state"

THRESHOLDS_PATH = CONFIG_DIR / "thresholds.json"
PREVIOUS_PATH = STATE_DIR / "previous.json"
CHANGES_PATH = STATE_DIR / "changes.json"


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_json_or(path: Path, default):
    if not path.exists():
        return default
    try:
        return load_json(path)
    except Exception:
        return default


def meaningful(old: float, new: float, thresholds: dict) -> bool:
    """Is the change beyond both abs and pct thresholds? Either qualifies."""
    if old is None or new is None:
        return new is not None  # going from None to a value counts as change
    abs_diff = abs(new - old)
    if old == 0:
        return abs_diff >= thresholds.get("abs", 0)
    pct_diff = abs((new - old) / old) * 100
    return abs_diff >= thresholds.get("abs", float("inf")) or \
           pct_diff >= thresholds.get("pct", float("inf"))


def load_api_backed_names() -> set[str]:
    """Names owned by live-data.js client-side. Detector ignores changes to these."""
    names = set()
    live_data = ROOT.parent / "js" / "live-data.js"
    # detect_changes.py lives in scripts/ so ROOT.parent is the repo root
    if not live_data.exists():
        # Fallback: try the actual layout
        live_data = Path(__file__).resolve().parent.parent / "js" / "live-data.js"
    if not live_data.exists():
        return names
    try:
        with open(live_data, encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return names
    import re as _re
    m = _re.search(r"var\s+CODE_MAP\s*=\s*\{([\s\S]*?)\};", content)
    if not m:
        return names
    for em in _re.finditer(r"'([^']+)'\s*:\s*'([A-Z0-9_]+)'", m.group(1)):
        names.add(em.group(1))
    return names


def detect_commodity_changes(new_snap: dict, old_snap: dict, thresholds: dict) -> list[dict]:
    """Return list of change entries for commodities we actually render."""
    changes = []
    new_prices = new_snap.get("prices", {})
    old_prices = old_snap.get("prices", {})
    per_item = thresholds.get("commodity_prices", {})
    default_th = per_item.get("_default", {"abs": 0.5, "pct": 0.75})

    # Skip API-backed commodities — live-data.js handles those client-side,
    # no reason to commit git diffs for values that change every 5 min
    api_backed = load_api_backed_names()

    for name, newp in new_prices.items():
        if name in api_backed:
            continue
        oldp = old_prices.get(name, {})
        old_val = oldp.get("price")
        new_val = newp.get("price")
        th = per_item.get(name, default_th)
        is_meaningful = meaningful(old_val, new_val, th)
        if is_meaningful:
            changes.append({
                "commodity": name,
                "old": old_val,
                "new": new_val,
                "diff": None if old_val is None else round(new_val - old_val, 4),
                "pct_diff": None if (not old_val) else round(((new_val - old_val) / old_val) * 100, 2),
                "threshold_used": th,
            })
    return changes


def detect_gas_changes(new_snap: dict, old_snap: dict, thresholds: dict) -> list[dict]:
    changes = []
    new_prices = new_snap.get("prices", {})
    old_prices = old_snap.get("prices", {})
    per_item = thresholds.get("gas_prices_national", {})
    default_th = {"abs": 0.003, "pct": 0.1}

    for grade in ("regular", "mid", "premium", "diesel"):
        old_val = old_prices.get(grade)
        new_val = new_prices.get(grade)
        if new_val is None:
            continue
        th = per_item.get(grade, default_th)
        if meaningful(old_val, new_val, th):
            changes.append({
                "grade": grade,
                "old": old_val,
                "new": new_val,
                "diff": None if old_val is None else round(new_val - old_val, 4),
            })
    return changes


def detect_source_status_flip(new_snap: dict, old_snap: dict) -> str | None:
    """Flag status transitions (fresh -> failed, failed -> fresh)."""
    old_status = (old_snap or {}).get("meta", {}).get("status")
    new_status = (new_snap or {}).get("meta", {}).get("status")
    if old_status != new_status and new_status:
        return f"{old_status or 'unknown'} -> {new_status}"
    return None


def main() -> int:
    if not THRESHOLDS_PATH.exists():
        print("ERROR: thresholds.json missing")
        return 2

    thresholds = load_json(THRESHOLDS_PATH)
    previous = load_json_or(PREVIOUS_PATH, {})

    # Load current snapshots
    commodity_snap = load_json_or(SOURCES_DIR / "commodity-prices.json", {})
    gas_snap       = load_json_or(SOURCES_DIR / "gas-prices-national.json", {})

    # Extract previous snapshots
    prev_commodity = previous.get("commodity-prices", {})
    prev_gas       = previous.get("gas-prices-national", {})

    changeset = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sources": {},
        "affected_pages": [],
    }

    # Commodity changes
    if commodity_snap.get("prices"):
        ch = detect_commodity_changes(commodity_snap, prev_commodity, thresholds)
        status_flip = detect_source_status_flip(commodity_snap, prev_commodity)
        changeset["sources"]["commodity_prices"] = {
            "changes": ch,
            "status_flip": status_flip,
            "current_status": commodity_snap.get("meta", {}).get("status"),
        }

    # Gas changes
    if gas_snap.get("prices"):
        ch = detect_gas_changes(gas_snap, prev_gas, thresholds)
        status_flip = detect_source_status_flip(gas_snap, prev_gas)
        changeset["sources"]["gas_prices_aaa"] = {
            "changes": ch,
            "status_flip": status_flip,
            "current_status": gas_snap.get("meta", {}).get("status"),
        }

    # Compute affected pages using the dependency map
    deps_path = CONFIG_DIR / "page-dependencies.json"
    if deps_path.exists():
        deps = load_json(deps_path)
        sources_with_changes = {
            s for s, info in changeset["sources"].items()
            if info.get("changes") or info.get("status_flip")
        }
        for page, page_info in deps.items():
            if page.startswith("_"):
                continue
            page_sources = set(page_info.get("depends_on", []))
            if page_sources & sources_with_changes:
                changeset["affected_pages"].append({
                    "page": page,
                    "label": page_info.get("label", page),
                    "triggered_by": list(page_sources & sources_with_changes),
                })

    # Write changeset
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    tmp = CHANGES_PATH.with_suffix(".new")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(changeset, f, indent=2)
    tmp.replace(CHANGES_PATH)

    # Snapshot current state as "previous" for next comparison
    new_previous = {
        "commodity-prices": commodity_snap,
        "gas-prices-national": gas_snap,
        "as_of": datetime.now(timezone.utc).isoformat(),
    }
    tmp2 = PREVIOUS_PATH.with_suffix(".new")
    with open(tmp2, "w", encoding="utf-8") as f:
        json.dump(new_previous, f, indent=2)
    tmp2.replace(PREVIOUS_PATH)

    # Report summary
    total_changes = sum(
        len(info.get("changes", []))
        for info in changeset["sources"].values()
    )
    affected = len(changeset["affected_pages"])
    print(f"[detect_changes] {total_changes} meaningful changes across "
          f"{len(changeset['sources'])} sources; {affected} page(s) affected")
    for src, info in changeset["sources"].items():
        if info.get("changes"):
            print(f"  • {src}: {len(info['changes'])} changes")
        if info.get("status_flip"):
            print(f"  • {src}: status {info['status_flip']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
