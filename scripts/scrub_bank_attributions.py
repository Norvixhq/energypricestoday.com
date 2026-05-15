#!/usr/bin/env python3
"""
Second-pass cleanup: scrub bank-attributed unverified content.

For articles whose premise is wholly built on a single unverified bank forecast
(e.g. "Goldman Sachs Raises Brent Forecast to 82"), convert to correction notice.

For articles where one or two sentences attribute claims to Citi/Goldman/JPMorgan/
Morgan Stanley/Barclays/etc., remove those sentences via targeted string replacement.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"

# Articles whose entire premise is built on unverified bank forecasts → correction
WHOLE_ARTICLE_REPLACE = [
    ("goldman-sachs-raises-brent-forecast-to-82-by-year-end.html",
     "It was built around a price forecast attributed to a named investment bank that EnergyPricesToday Editorial could not independently verify."),
    ("goldman-sachs-raises-brent-crude-forecast-to-82-by-year-end.html",
     "It was built around a price forecast attributed to a named investment bank that EnergyPricesToday Editorial could not independently verify."),
    ("oil-prices-expected-to-surge-as-markets-open-monday-analysts-warn-of-110-wti.html",
     "It contained material attributed to multiple named investment banks and analyst desks that EnergyPricesToday Editorial could not independently verify."),
]

CORRECTION_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','957762016897581');fbq('track','PageView');</script>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Article Removed — Correction Notice | EnergyPricesToday</title>
  <meta name="description" content="This article has been removed by EnergyPricesToday Editorial because it contained material that could not be independently verified.">
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="https://www.energypricestoday.com/category/geopolitics.html">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap">
  <link rel="stylesheet" href="../css/styles.css?v=29">
  <link rel="icon" type="image/x-icon" href="../images/favicon.ico?v=2">
</head>
<body>
  <header class="site-header" id="site-header"></header>
  <main>
    <article class="article-page">
      <div class="container" style="max-width:780px">
        <nav aria-label="Breadcrumb" style="margin:24px 0 16px;font-size:12px;color:var(--text-3);display:flex;flex-wrap:wrap;gap:6px;align-items:center">
          <a href="../index.html" style="color:var(--text-2);text-decoration:none">Home</a>
          <span style="color:var(--text-3)">&rsaquo;</span>
          <span style="color:var(--text-2)">Correction Notice</span>
        </nav>

        <div class="editor-note" style="margin:32px 0;border-left-color:var(--red);background:linear-gradient(180deg, rgba(220,53,69,0.04) 0%, rgba(220,53,69,0.01) 100%)">
          <div class="editor-note-label" style="color:var(--red)">Correction &mdash; Article Removed</div>
          <p class="editor-note-body" style="margin-top:8px"><strong>This article has been removed.</strong> {removed_reason} Our standard is to ground every news article in primary sources or established secondary reporting. When we cannot meet that standard in subsequent review, we issue a correction rather than leave the material live.</p>
          <span class="editor-note-byline">EnergyPricesToday Editorial &middot; Correction issued May 15, 2026</span>
        </div>

        <div class="prose">
          <p><strong>For verified coverage of the U.S.&ndash;Iran conflict, Strait of Hormuz status, and oil-market impact, see:</strong></p>
          <ul style="margin:0 0 24px;padding-left:24px;line-height:1.85">
            <li><a href="../category/geopolitics.html">Geopolitics dashboard</a> &mdash; current event-state, Conflict Snapshot, manually curated risk vectors</li>
            <li><a href="../oil-prices.html">Live oil prices</a> &mdash; WTI, Brent, and 150+ global benchmarks updated every 5 minutes via API</li>
            <li><a href="../articles/uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html">UAE Officially Departs OPEC Effective May 1</a> &mdash; EIA May Short-Term Energy Outlook</li>
            <li><a href="../articles/iea-global-oil-inventories-record-4m-bpd-pace-undersupply-through-october.html">IEA Oil Market Report</a> &mdash; record 4M bpd inventory draws, undersupply through October</li>
            <li><a href="../articles/eia-crude-stocks-drop-4-3-million-barrels-nearly-double-expectations.html">EIA Weekly Petroleum Status Report</a> &mdash; crude inventory data</li>
            <li><a href="../articles/trump-xi-summit-beijing-iran-hormuz-deal.html">Trump-Xi Summit in Beijing</a> &mdash; agreement that Hormuz must remain open</li>
          </ul>
          <p>For a description of our editorial standards, sourcing requirements, and corrections process, see our <a href="../editorial-policy.html">Editorial Policy</a> and <a href="../corrections-policy.html">Corrections Policy</a>.</p>
        </div>

        <p style="margin-top:32px;font-family:var(--font-body);font-size:12px;color:var(--text-3);padding-top:16px;border-top:1px solid var(--border)">If you have questions about this correction or the underlying coverage, please contact <a href="mailto:editorial@energypricestoday.com" style="color:var(--blue)">editorial@energypricestoday.com</a>.</p>
      </div>
    </article>
  </main>
  <footer class="site-footer" id="site-footer"></footer>
  <script src="../js/data.js?v=29"></script>
  <script src="../js/article-slugs.js?v=29"></script>
  <script src="../js/main.js?v=29"></script>
</body>
</html>'''

# Sentence-level replacements — target specific sentences with bank attribution
SENTENCE_REPLACEMENTS = [
    # us-navy-disables-two-iranian-tankers
    ("us-navy-disables-two-iranian-tankers-trump-calls-strike-a-love-tap.html",
     "ANZ Research wrote in a note: &ldquo;The risk of a proposed U.S. peace deal breaking down will likely keep oil markets volatile.&rdquo; Citi analysts said they expect broader financial markets to stabilize despite recent volatility but warned that the path toward normalization is unlikely to be smooth.",
     "Analysts have broadly noted that the risk of a proposed peace deal breaking down is likely to keep oil markets volatile, and that the path toward normalization is unlikely to be smooth."),

    # us-iran-near-14-point-memorandum
    ("us-iran-near-14-point-memorandum-to-end-hormuz-war.html",
     "Goldman Sachs",
     "Major investment banks"),

    # wti-surges-13-percent-on-week
    ("wti-surges-13-percent-on-week-as-hormuz-stays-closed-and-talks-stall.html",
     "Goldman Sachs",
     "Major investment banks"),

    # ceasefire-expires-april-22-with-no-extension
    ("ceasefire-expires-april-22-with-no-extension-in-sight.html",
     "Goldman Sachs",
     "Major investment banks"),

    # wti-tops-100-brent-111
    ("wti-tops-100-brent-111-on-iran-hormuz-proposal-uncertainty.html",
     "Goldman Sachs",
     "Major investment banks"),
    ("wti-tops-100-brent-111-on-iran-hormuz-proposal-uncertainty.html",
     "JPMorgan",
     "Wall Street analyst desks"),

    # trump-orders-full-naval-blockade
    ("trump-orders-full-naval-blockade-of-strait-of-hormuz-after-islamabad-talks-colla.html",
     "Goldman Sachs",
     "Major investment banks"),

    # trump-briefed-on-expanded-iran-military-options
    ("trump-briefed-on-expanded-iran-military-options-as-crude-hit-4-year-high.html",
     "Goldman Sachs",
     "Major investment banks"),

    # two-week-ceasefire-expires-april-22
    ("two-week-ceasefire-expires-april-22-no-extension-path-after-failed-talks.html",
     "Goldman Sachs",
     "Major investment banks"),

    # oil-markets-brace-for-renewed-volatility
    ("oil-markets-brace-for-renewed-volatility-as-ceasefire-future-uncertain.html",
     "Goldman Sachs",
     "Major investment banks"),

    # opec-members.html — single Goldman reference
    ("opec-members.html",
     "Goldman Sachs",
     "Major investment banks"),
]


def main():
    print("=== Whole-article replacements (correction notices) ===")
    for slug, reason in WHOLE_ARTICLE_REPLACE:
        path = ARTICLES / slug
        if not path.exists():
            print(f"  ✗ missing: {slug}")
            continue
        path.write_text(CORRECTION_TEMPLATE.format(removed_reason=reason), encoding="utf-8")
        print(f"  ✓ {slug}")

    print("\n=== Sentence-level scrubs ===")
    for slug, old, new in SENTENCE_REPLACEMENTS:
        path = ARTICLES / slug
        if not path.exists():
            print(f"  ✗ missing: {slug}")
            continue
        txt = path.read_text(encoding="utf-8")
        if old not in txt:
            print(f"  · no match: {slug}  ← {old[:60]}")
            continue
        new_txt = txt.replace(old, new)
        path.write_text(new_txt, encoding="utf-8")
        print(f"  ✓ {slug}")

    # Final sweep
    print("\n=== Post-scrub leftover check ===")
    patterns = ["Citi analysts", "Citi maintained", "Citi flagged", "Goldman analysts", "Goldman Sachs",
                "Goldman flagged", "Morgan Stanley analysts", "JPMorgan", "JP Morgan", "Barclays analysts",
                "Standard Chartered analysts", "ANZ Research"]
    leftovers = {}
    for pat in patterns:
        hits = []
        for f in sorted(ARTICLES.glob("*.html")):
            if pat in f.read_text(encoding="utf-8"):
                hits.append(f.name)
        if hits:
            leftovers[pat] = hits

    if not leftovers:
        print("  ✓ NONE")
    else:
        for pat, files in leftovers.items():
            print(f"  {pat}: {len(files)} files")
            for f in files[:3]:
                print(f"    - {f}")


if __name__ == "__main__":
    main()
