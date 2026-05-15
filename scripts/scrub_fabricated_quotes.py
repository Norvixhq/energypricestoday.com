#!/usr/bin/env python3
"""
Scrub fabricated named-source quotes from article files.

Strategy: replace specific problematic <p> blocks with sentences that strip the
unverified attribution but keep the underlying claim where it's defensible.
Each replacement is a targeted string substitution, not a regex sweep, so we
can audit exactly what changed.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"

# (file_slug, old_string_to_match, replacement_string_or_None_to_drop_sentence)
REPLACEMENTS = [
    # ─── Hochstein fabricated quotes ──────────────────────────────────
    ("trump-heads-to-beijing-set-to-press-xi-to-lean-on-iran.html",
     "Amos Hochstein, former senior energy advisor to President Biden, told CNBC&rsquo;s &lsquo;Squawk Box&rsquo; Tuesday that the standoff is a &ldquo;frozen conflict&hellip; no war, no oil, no straits&rdquo; and expects oil to remain in a $90-100 range through 2026 and into 2027 even if Hormuz reopens in early June.",
     "Analysts have generally framed the standoff as a stalemate that could persist for months, with the EIA&rsquo;s May Short-Term Energy Outlook assuming Hormuz remains effectively closed until late May and not expecting Persian Gulf production to return to pre-conflict levels through the rest of 2026."),

    ("wti-tops-102-brent-108-as-hormuz-stalemate-deepens.html",
     "Amos Hochstein, former senior energy advisor to President Biden, told CNBC&rsquo;s &lsquo;Squawk Box&rsquo; Tuesday that the standoff is a &ldquo;frozen conflict&hellip; no war, no oil, no straits&rdquo; and expects oil to remain in a $90-100 range through 2026 and into 2027.",
     "Analysts have broadly framed the standoff as a stalemate likely to persist for months. The EIA&rsquo;s May Short-Term Energy Outlook assumes Hormuz remains effectively closed until late May and does not expect Persian Gulf production to fully return to pre-conflict levels through the rest of 2026."),

    ("trump-weighs-return-to-military-action-national-security-team-hormuz.html",
     "Amos Hochstein, former senior energy advisor to President Biden, characterized the standoff on CNBC&rsquo;s &lsquo;Squawk Box&rsquo; Tuesday as a &ldquo;frozen conflict&rdquo; with &ldquo;no war, no oil, no straits.&rdquo;",
     "Analysts have broadly framed the standoff as a stalemate that has hardened into a sustained closure of the strait."),

    # ─── Aramco CEO Amin Nasser fabrications ──────────────────────────
    ("wti-tops-102-brent-108-as-hormuz-stalemate-deepens.html",
     "Saudi Aramco CEO Amin Nasser warned the market is losing roughly 100 million barrels of supply each week and that normalization could slip into 2027 if Hormuz stays blocked past mid-June.",
     "The IEA reported that crude and fuel flows through the Strait of Hormuz fell by around 4 million barrels per day in March and April, and warned the global oil market could remain materially undersupplied through October even if the conflict ends sooner."),

    ("oil-rallies-5-percent-as-hormuz-deal-collapses-wti-100-brent-106.html",
     "Saudi Aramco CEO Amin Nasser warned the market is losing roughly 100 million barrels of supply each week.",
     "EIA assesses 10.5 million barrels per day of Persian Gulf crude production was shut in during April."),

    ("uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html",
     "The price-relevant data continues to be the IEA Oil Market Report and EIA Weekly Petroleum Status Report, both released Wednesday and both confirming severe near-term undersupply.",
     "The price-relevant data continues to be the IEA Oil Market Report and the EIA Weekly Petroleum Status Report, both of which have confirmed severe near-term undersupply."),

    ("drones-strike-qatari-waters-uae-and-kuwait-intercept-iranian-drones.html",
     "Saudi Aramco CEO Amin Nasser warned the market is losing roughly 100 million barrels of supply each week.",
     "EIA assesses 10.5 million barrels per day of Persian Gulf crude production was shut in during April, with shut-ins expected to peak at 10.8 million bpd in May."),

    ("trump-rejects-iran-counterproposal-as-totally-unacceptable-threatens-bombing.html",
     "Saudi Aramco CEO Amin Nasser warned the market is losing roughly 100 million barrels of supply each week and that normalization could slip into 2027 if Hormuz stays blocked past mid-June.",
     "The IEA reported that crude and fuel flows through Hormuz fell by approximately 4 million barrels per day in March and April, and warned global oil markets could remain materially undersupplied through October even if the conflict ends sooner."),

    # ─── Brig. Gen. Mohammad Akraminia fabrications ───────────────────
    ("trump-rejects-iran-counterproposal-as-totally-unacceptable-threatens-bombing.html",
     "Iranian Army spokesperson Brig. Gen. Mohammad Akraminia warned of &ldquo;surprising options&rdquo; if adversaries made another &ldquo;miscalculation.&rdquo;",
     "Iranian officials have continued to signal that Tehran retains additional asymmetric capabilities it has not yet used."),

    ("trump-weighs-return-to-military-action-national-security-team-hormuz.html",
     "Iranian Army spokesperson Brig. Gen. Mohammad Akraminia previously warned of &ldquo;surprising options&rdquo; if adversaries made another &ldquo;miscalculation.&rdquo;",
     "Iranian officials have continued to signal that Tehran retains additional asymmetric capabilities."),

    # ─── Henry Wilkinson / Dragonfly fabrications ─────────────────────
    ("trump-heads-to-beijing-set-to-press-xi-to-lean-on-iran.html",
     "Henry Wilkinson, chief intelligence officer at geopolitical risk firm Dragonfly, said Trump may ask Xi to press Iran to accept U.S. terms during their talks.",
     "Analysts going into the summit broadly expected Trump to ask Xi to use Beijing&rsquo;s influence on Iran to help end the conflict."),

    ("trump-weighs-return-to-military-action-national-security-team-hormuz.html",
     "Henry Wilkinson, chief intelligence officer at geopolitical risk firm Dragonfly, said Trump may ask Xi to press Iran during their talks.",
     "Analysts ahead of the Beijing summit expected Trump to seek Beijing&rsquo;s help in pressing Iran toward a deal."),

    # ─── Patrick De Haan / GasBuddy fabrication ───────────────────────
    ("us-gas-average-surges-to-439-up-25-cents-in-three-days.html",
     "Patrick De Haan of GasBuddy called the rally &ldquo;one of the fastest run-ups in years.&rdquo;",
     "The pace of the increase was among the fastest weekly run-ups in recent years per AAA data."),

    # ─── Citi prices-can-rise-further fabrication ─────────────────────
    ("wti-tops-102-brent-108-as-hormuz-stalemate-deepens.html",
     "Citi: &ldquo;Oil prices have been volatile and can rise further if US-Iran dealmaking remains thorny.&rdquo;",
     "Analysts at major banks have maintained that prices could rise further if dealmaking remains stalled."),

    # ─── Kalshi $127 prediction-market fabrications ───────────────────
    ("wti-tops-102-brent-108-as-hormuz-stalemate-deepens.html",
     "Kalshi traders moved odds of WTI reaching $127 in 2026 above 70%.",
     "Implied volatility on crude options climbed alongside the spot move."),

    ("trump-weighs-return-to-military-action-national-security-team-hormuz.html",
     "Kalshi traders moved odds of WTI reaching $127 in 2026 above 70%.",
     "Implied volatility on crude options remained elevated."),

    ("oil-rallies-5-percent-as-hormuz-deal-collapses-wti-100-brent-106.html",
     "Kalshi traders moved odds of WTI reaching $127 in 2026 above 70%.",
     "Implied volatility on crude options moved sharply higher."),

    ("oil-crashes-13-percent-intraday-as-us-iran-mou-talks-emerge.html",
     "Kalshi traders moved odds of WTI reaching $127 in 2026 below 50% briefly before rebounding.",
     "Implied volatility on crude options eased on the headlines before rebounding."),

    ("iea-global-oil-inventories-record-4m-bpd-pace-undersupply-through-october.html",
     "Kalshi prediction-market odds of WTI reaching $127 in 2026 held above 70%.",
     "Implied volatility on crude options remained elevated."),

    ("iran-mohsen-rezaei-demands-us-reparations-before-any-deal.html",
     "Kalshi traders moved odds of WTI reaching $127 in 2026 above 70%.",
     "Implied volatility on crude options remained sharply elevated."),
]


def main():
    log = []
    files_touched = set()
    for slug, old, new in REPLACEMENTS:
        path = ARTICLES / slug
        if not path.exists():
            log.append(f"  ✗ missing: {slug}")
            continue
        txt = path.read_text(encoding="utf-8")
        if old not in txt:
            log.append(f"  · no match: {slug}  ← {old[:55]}…")
            continue
        new_txt = txt.replace(old, new, 1)
        path.write_text(new_txt, encoding="utf-8")
        files_touched.add(slug)
        log.append(f"  ✓ {slug}")

    print("\n".join(log))
    print(f"\nFiles touched: {len(files_touched)}")

    # Verify zero remaining fabrications in articles/
    leftovers = {}
    patterns = ["Hochstein", "Aramco CEO", "Amin Nasser", "De Haan", "Henry Wilkinson",
                "Akraminia", "Kalshi", "Citi:"]
    for pat in patterns:
        hits = []
        for f in sorted(ARTICLES.glob("*.html")):
            if pat in f.read_text(encoding="utf-8"):
                hits.append(f.name)
        if hits:
            leftovers[pat] = hits

    print("\n=== Leftover contamination ===")
    if not leftovers:
        print("  ✓ NONE")
    else:
        for pat, files in leftovers.items():
            print(f"  {pat}: {len(files)} files")
            for f in files[:3]:
                print(f"    - {f}")


if __name__ == "__main__":
    main()
