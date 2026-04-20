#!/usr/bin/env python3
"""
fix_dangling_refs.py — Path A Guard C: nightly dangling-reference auto-fixer.

Scans js/data.js for article title references in the five article-reference
blocks (BREAKING_NEWS, FEATURED_ARTICLES, GEO_ITEMS, COMPANY_NEWS,
CATEGORY_CONTENT) and verifies each title has a valid article target.

A title is "dangling" if:
  - It is not in ARTICLE_SLUGS (js/article-slugs.js), AND
  - The slugify(title) doesn't produce a file that exists on disk

For each dangling title:
  1. Fuzzy-match against known titles. Confidence signals:
       - Jaccard token ratio >= 0.70
       - SequenceMatcher ratio >= 0.80
       - Levenshtein distance <= 3 (for short titles)
     → If confident match found, auto-correct the title to canonical form.
  2. No confident match → remove the enclosing object from the array.

IMPORTANT: This script ONLY modifies title strings within the five named
blocks. It never touches title keys that happen to appear in commodity
label arrays, route tables, or other non-article data.

Runs during nightly-audit.yml so a misfire can't blow up mid-day.

Exit codes:
  0 — Changes made (caller should re-run rebuild_slug_map + validate)
  1 — No dangling references found (no-op, clean exit)
  2 — Error (data.js unparseable, syntax broken after edit, etc.)

Safety:
  - Targets only the five article-reference blocks, never arbitrary titles
  - Writes to data.js.new.js, syntax-validates via `node -c`, then renames
  - Backup preserved in /tmp/ for rollback
  - All changes logged to data/logs/dangling-fixer.log
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_JS_PATH = ROOT / "js" / "data.js"
ARTICLE_SLUGS_JS = ROOT / "js" / "article-slugs.js"
ARTICLES_DIR = ROOT / "articles"
LOG_PATH = ROOT / "data" / "logs" / "dangling-fixer.log"
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

# ONLY these blocks contain article references.
ARTICLE_REF_BLOCKS = [
    "BREAKING_NEWS",
    "FEATURED_ARTICLES",
    "GEO_ITEMS",
    "COMPANY_NEWS",
    "CATEGORY_CONTENT",
]

# Fuzzy-match thresholds
TOKEN_RATIO_THRESHOLD = 0.70
SEQUENCE_RATIO_THRESHOLD = 0.80
MAX_LEVENSHTEIN = 3


# ─── Utilities ────────────────────────────────────────────────────
def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat()
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")
    print(msg)


def load_article_slugs() -> dict[str, str]:
    if not ARTICLE_SLUGS_JS.exists():
        return {}
    content = ARTICLE_SLUGS_JS.read_text()
    mapping: dict[str, str] = {}
    for m in re.finditer(r'^\s*"((?:[^"\\]|\\.)*)"\s*:\s*"([^"]+)",?\s*$',
                         content, re.MULTILINE):
        title = m.group(1).replace('\\"', '"').replace('\\\\', '\\')
        slug = m.group(2)
        mapping[title] = slug
    return mapping


def python_slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s[:80]


def decode_js_string(s: str) -> str:
    if "\\u" in s:
        try:
            return s.encode("latin-1", "ignore").decode("unicode_escape")
        except (UnicodeDecodeError, UnicodeEncodeError):
            return s
    return s


# ─── Block boundaries ─────────────────────────────────────────────
def find_block_span(content: str, block_name: str) -> tuple[int, int] | None:
    """Find (start, end) character offsets of a named const block."""
    decl_pat = re.compile(
        rf"const\s+{re.escape(block_name)}\s*=\s*([\[\{{])"
    )
    m = decl_pat.search(content)
    if not m:
        return None
    open_pos = m.end(1) - 1
    opener = m.group(1)
    closer = "]" if opener == "[" else "}"

    depth = 0
    i = open_pos
    in_string = False
    string_char = None
    escape = False
    while i < len(content):
        c = content[i]
        if escape:
            escape = False
        elif in_string:
            if c == "\\":
                escape = True
            elif c == string_char:
                in_string = False
        else:
            if c == '"' or c == "'":
                in_string = True
                string_char = c
            elif c == opener:
                depth += 1
            elif c == closer:
                depth -= 1
                if depth == 0:
                    return (m.start(), i + 1)
        i += 1
    return None


def get_block_spans(content: str) -> dict[str, tuple[int, int]]:
    spans = {}
    for name in ARTICLE_REF_BLOCKS:
        span = find_block_span(content, name)
        if span:
            spans[name] = span
    return spans


# ─── Title discovery (scoped to article-ref blocks) ───────────────
TITLE_RE = re.compile(r'title\s*:\s*"((?:[^"\\]|\\.)*)"')


def find_titles_in_block(content: str, span: tuple[int, int]) -> list[tuple[int, int, str]]:
    start, end = span
    results = []
    for m in TITLE_RE.finditer(content, start, end):
        title_start = m.start(1)
        title_end = m.end(1)
        raw = m.group(1)
        decoded = decode_js_string(raw.replace('\\"', '"').replace('\\\\', '\\'))
        results.append((title_start, title_end, decoded))
    return results


def find_dangling_titles(
    content: str,
    slug_map: dict[str, str],
) -> list[tuple[int, int, str, str]]:
    dangling = []
    block_spans = get_block_spans(content)
    for block_name, span in block_spans.items():
        for start, end, title in find_titles_in_block(content, span):
            if title in slug_map:
                continue
            slug = python_slugify(title)
            if (ARTICLES_DIR / f"{slug}.html").exists():
                continue
            dangling.append((start, end, title, block_name))
    return dangling


# ─── Fuzzy matching ───────────────────────────────────────────────
def tokens(s: str) -> set[str]:
    return set(re.sub(r"[^a-z0-9\s]", " ", s.lower()).split())


def token_ratio(a: str, b: str) -> float:
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def sequence_ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def levenshtein(a: str, b: str) -> int:
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        curr = [i + 1]
        for j, cb in enumerate(b):
            cost = 0 if ca == cb else 1
            curr.append(min(curr[-1] + 1, prev[j + 1] + 1, prev[j] + cost))
        prev = curr
    return prev[-1]


def best_match(title: str, candidates: list[str]) -> tuple[str | None, float, str]:
    if not candidates or not title.strip():
        return None, 0.0, "no_candidates"

    best = None
    best_score = 0.0
    best_reason = "no_match"

    for cand in candidates:
        tr = token_ratio(title, cand)
        if tr >= TOKEN_RATIO_THRESHOLD and tr > best_score:
            best, best_score, best_reason = cand, tr, f"token_ratio={tr:.2f}"

        sr = sequence_ratio(title, cand)
        if sr >= SEQUENCE_RATIO_THRESHOLD and sr > best_score:
            best, best_score, best_reason = cand, sr, f"sequence_ratio={sr:.2f}"

        if len(title) <= 40 and len(cand) <= 40:
            dist = levenshtein(title, cand)
            if dist <= MAX_LEVENSHTEIN:
                score = 1.0 - (dist / max(len(title), len(cand), 1))
                if score > best_score:
                    best, best_score, best_reason = cand, score, f"levenshtein={dist}"

    if best and best_score >= TOKEN_RATIO_THRESHOLD:
        return best, best_score, best_reason
    return None, 0.0, "no_confident_match"


# ─── Modifications ────────────────────────────────────────────────
def replace_title(content: str, start: int, end: int, new_title: str) -> str:
    escaped = new_title.replace("\\", "\\\\").replace('"', '\\"')
    return content[:start] + escaped + content[end:]


def remove_enclosing_object(content: str, title_start: int) -> tuple[str, bool]:
    """Walk back to find enclosing { ... } and remove it from its array."""
    depth = 0
    obj_start = None
    for i in range(title_start, -1, -1):
        c = content[i]
        if c == "}":
            depth += 1
        elif c == "{":
            if depth == 0:
                obj_start = i
                break
            depth -= 1
    if obj_start is None:
        return content, False

    depth = 0
    obj_end = None
    for i in range(obj_start, len(content)):
        c = content[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                obj_end = i + 1
                break
    if obj_end is None:
        return content, False

    before = content[:obj_start]
    after = content[obj_end:]

    trailing_comma = re.search(r',\s*$', before)
    leading_comma = re.match(r'\s*,', after)
    if trailing_comma:
        before = before[:trailing_comma.start()]
    elif leading_comma:
        after = after[leading_comma.end():]

    return before + after, True


# ─── Main ─────────────────────────────────────────────────────────
def main() -> int:
    if not DATA_JS_PATH.exists():
        log("[fix_dangling_refs] ERR: data.js not found")
        return 2

    slug_map = load_article_slugs()
    if not slug_map:
        log("[fix_dangling_refs] ERR: article-slugs.js empty or unparseable")
        return 2

    log(f"[fix_dangling_refs] Loaded {len(slug_map)} known articles")
    content = DATA_JS_PATH.read_text()
    original_content = content

    dangling = find_dangling_titles(content, slug_map)
    if not dangling:
        log("[fix_dangling_refs] No dangling references in article blocks — clean exit")
        return 1

    log(f"[fix_dangling_refs] Found {len(dangling)} dangling title(s) in article-ref blocks")
    canonical_titles = list(slug_map.keys())

    corrected = 0
    removed = 0
    unresolved = 0

    # Work back-to-front so offsets don't shift as we modify
    dangling_sorted = sorted(dangling, key=lambda d: d[0], reverse=True)

    for start, end, title, block_name in dangling_sorted:
        match, score, reason = best_match(title, canonical_titles)
        if match:
            log(f"  CORRECT [{block_name}]: '{title[:50]}' → '{match[:50]}' ({reason})")
            content = replace_title(content, start, end, match)
            corrected += 1
        else:
            log(f"  REMOVE [{block_name}]: '{title[:50]}' (no confident match)")
            new_content, ok = remove_enclosing_object(content, start)
            if ok:
                content = new_content
                removed += 1
            else:
                log(f"    ! Could not safely remove — leaving in place")
                unresolved += 1

    if content == original_content:
        log("[fix_dangling_refs] No modifications applied")
        return 1

    # Backup
    backup = Path("/tmp") / f"data.js.backup.{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    try:
        shutil.copy(DATA_JS_PATH, backup)
        log(f"[fix_dangling_refs] Backup: {backup}")
    except Exception as e:
        log(f"[fix_dangling_refs] Backup failed (non-fatal): {e}")

    # Atomic write + validate
    tmp = DATA_JS_PATH.with_suffix(".new.js")
    tmp.write_text(content, encoding="utf-8")

    result = subprocess.run(["node", "-c", str(tmp)], capture_output=True, text=True)
    if result.returncode != 0:
        log(f"[fix_dangling_refs] SYNTAX ERROR in rewritten data.js:")
        log(result.stderr.strip()[:300])
        log("[fix_dangling_refs] Reverting — data.js untouched")
        tmp.unlink(missing_ok=True)
        return 2

    tmp.replace(DATA_JS_PATH)
    log(f"[fix_dangling_refs] ✓ {corrected} corrected, {removed} removed, {unresolved} unresolved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
