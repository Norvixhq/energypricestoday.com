#!/usr/bin/env python3
"""
validate.py — Pre-publish guardrail. Runs all integrity checks.
If ANY check fails, exits non-zero and the commit/push is aborted.

Checks:
  1. JS syntax (node -c) on every .js file in js/
  2. Every title in BREAKING_NEWS, FEATURED_ARTICLES, GEO_ITEMS,
     COMPANY_NEWS, and CATEGORY_CONTENT has a matching article file
  3. Every href="articles/*.html" reference in any HTML resolves
  4. No literal \\uXXXX sequences in any HTML (encoding bug indicator)
  5. Sitemap <lastmod> is a valid date and not in the future
  6. Critical integrations are intact (FB Pixel, GA4, FB domain verify)
  7. Gas prices within sanity range ($2-$9)
  8. No empty content arrays in data.js

Exit codes:
  0 — All checks pass, safe to publish
  1 — One or more checks failed; DO NOT publish
"""

import os
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import data_js  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"
JS_DIR = ROOT / "js"

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def check_js_syntax() -> None:
    """node -c every .js file."""
    for f in sorted(JS_DIR.glob("*.js")):
        result = subprocess.run(
            ["node", "-c", str(f)], capture_output=True, text=True
        )
        if result.returncode != 0:
            err(f"JS syntax error in {f.name}: {result.stderr.strip()[:200]}")


def check_inline_scripts() -> None:
    """Extract inline <script> blocks from every HTML file and validate with node -c.
    Catches the class of bug where a hand-edited inline script has a syntax error
    that breaks the entire page (pages render "bare" with empty sections).

    Skips non-JavaScript script blocks (JSON-LD, template types, etc.)."""
    import tempfile
    for root, _, files in os.walk(ROOT):
        if "/.git" in root or "/__pycache__" in root:
            continue
        for f in files:
            if not f.endswith(".html"):
                continue
            path = Path(root) / f
            try:
                with open(path, encoding="utf-8") as fp:
                    content = fp.read()
            except Exception:
                continue
            # Match <script>...</script> but skip:
            #   - script with src="..." (external, not inline)
            #   - script with type="application/ld+json" or similar non-JS types
            #   - script with type="text/template" or similar
            # Accept: no type attribute, type="text/javascript", type="module"
            for match in re.finditer(
                r'<script\b([^>]*)>(.*?)</script>', content, re.DOTALL
            ):
                attrs = match.group(1)
                if "src=" in attrs:
                    continue
                # Extract type attr
                type_m = re.search(r'type\s*=\s*["\']([^"\']+)["\']', attrs)
                if type_m:
                    script_type = type_m.group(1).lower()
                    if script_type not in ("text/javascript", "module", "application/javascript"):
                        continue  # Skip JSON-LD, templates, etc.
                script = match.group(2).strip()
                if not script:
                    continue
                with tempfile.NamedTemporaryFile(
                    mode="w", suffix=".js", delete=False
                ) as tf:
                    tf.write(script)
                    tmp_path = tf.name
                try:
                    result = subprocess.run(
                        ["node", "-c", tmp_path],
                        capture_output=True,
                        text=True,
                        timeout=10,
                    )
                    if result.returncode != 0:
                        # Extract the meaningful error line (skip the generic
                        # "Node.js vXX.Y.Z" tail)
                        lines = [
                            ln for ln in result.stderr.strip().split("\n")
                            if ln.strip() and not ln.startswith("Node.js v")
                        ]
                        msg = lines[-1] if lines else "syntax error"
                        err(f"Inline JS error in {path.relative_to(ROOT)}: {msg[:200]}")
                finally:
                    os.unlink(tmp_path)


def check_visible_titles_have_articles() -> None:
    """Every visible content title needs a matching article file."""
    visible = data_js.extract_all_visible_titles()
    missing = []
    for title in visible:
        slug = data_js.slugify(title)
        if not (ARTICLES_DIR / f"{slug}.html").exists():
            missing.append(title[:70])
    if missing:
        err(f"{len(missing)} visible titles missing article files. First 3: "
            + "; ".join(missing[:3]))


def check_html_article_hrefs() -> None:
    """Every href="articles/xxx.html" or "../articles/xxx.html" must resolve."""
    broken = []
    for root, _, files in os.walk(ROOT):
        for f in files:
            if not f.endswith(".html"):
                continue
            path = Path(root) / f
            # Skip files in articles/ — they use their own internal link format
            try:
                with open(path, encoding="utf-8") as fp:
                    content = fp.read()
            except Exception:
                continue
            for m in re.finditer(
                r'href="(?:\.\./)?articles/([a-z0-9\-]+)\.html"', content
            ):
                slug = m.group(1)
                if not (ARTICLES_DIR / f"{slug}.html").exists():
                    broken.append(f"{path.name} → {slug}.html")
    if broken:
        err(f"{len(broken)} broken article links. First 3: "
            + "; ".join(broken[:3]))


def check_no_literal_unicode() -> None:
    """No \\uXXXX literals in HTML — means an escape wasn't decoded."""
    total = 0
    for root, _, files in os.walk(ROOT):
        for f in files:
            if not f.endswith(".html"):
                continue
            path = Path(root) / f
            try:
                with open(path, encoding="utf-8") as fp:
                    content = fp.read()
            except Exception:
                continue
            # Only flag in body content (not in scripts)
            # Remove <script> blocks first
            content_no_js = re.sub(
                r"<script[^>]*>.*?</script>", "", content, flags=re.DOTALL
            )
            matches = re.findall(r"\\u[0-9a-fA-F]{4}", content_no_js)
            total += len(matches)
    if total > 0:
        err(f"{total} literal \\uXXXX sequences in HTML body content")


def check_sitemap_dates() -> None:
    """Sitemap lastmod dates should be valid and not in the future."""
    sm = ROOT / "sitemap.xml"
    if not sm.exists():
        warn("sitemap.xml not found")
        return
    with open(sm, encoding="utf-8") as f:
        content = f.read()
    today = date.today()
    for m in re.finditer(r"<lastmod>([^<]+)</lastmod>", content):
        try:
            d = datetime.fromisoformat(m.group(1)).date()
        except ValueError:
            err(f"Invalid sitemap date: {m.group(1)}")
            continue
        if d > today:
            err(f"Sitemap date in future: {m.group(1)}")


def check_critical_integrations() -> None:
    """Homepage must have FB Pixel, GA4, FB domain verification."""
    home = ROOT / "index.html"
    if not home.exists():
        err("index.html not found")
        return
    with open(home, encoding="utf-8") as f:
        content = f.read()
    if "957762016897581" not in content:
        err("FB Pixel ID missing from homepage")
    if "G-FXGF8HZFWL" not in content:
        err("GA4 ID missing from homepage")
    if "iabb2balkajrsqzetut0ekrins5m6a" not in content:
        warn("FB domain verification meta missing")


def check_gas_sanity() -> None:
    """National gas average should be $2-$8."""
    content = data_js.read_raw()
    m = re.search(
        r"const US_GAS_NATIONAL\s*=\s*\{[^}]*regular:\s*([\d.]+)",
        content, re.DOTALL,
    )
    if not m:
        warn("Could not find US_GAS_NATIONAL.regular for sanity check")
        return
    val = float(m.group(1))
    if not (2.0 <= val <= 8.0):
        err(f"National gas price ${val} out of sane range (2-8)")


def check_empty_content_blocks() -> None:
    """No content array should be empty."""
    for block in ["BREAKING_NEWS", "FEATURED_ARTICLES", "GEO_ITEMS", "COMPANY_NEWS"]:
        titles = data_js.extract_titles_from_block(block)
        if not titles:
            err(f"Content block {block} is empty")


def main() -> int:
    print("[validate] Running pre-publish checks...")
    check_js_syntax()
    check_inline_scripts()
    check_visible_titles_have_articles()
    check_html_article_hrefs()
    check_no_literal_unicode()
    check_sitemap_dates()
    check_critical_integrations()
    check_gas_sanity()
    check_empty_content_blocks()

    if warnings:
        print(f"\n[validate] {len(warnings)} warning(s):")
        for w in warnings:
            print(f"  ⚠ {w}")

    if errors:
        print(f"\n[validate] ✗ FAILED — {len(errors)} error(s):")
        for e in errors:
            print(f"  ✗ {e}")
        return 1

    print("[validate] ✓ All checks pass — safe to publish")
    return 0


if __name__ == "__main__":
    sys.exit(main())
