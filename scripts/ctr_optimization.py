#!/usr/bin/env python3
"""
ctr_optimization.py — Rewrite titles and meta descriptions on the
highest-traffic pages and articles for better SERP click-through.

Rules:
  - Title target: 50-60 chars (Google truncates at ~60)
  - Meta desc target: 140-158 chars (Google shows ~155)
  - Brand suffix: " | EnergyPricesToday" (19ch, shorter than current
    " — EnergyPricesToday.com" at 25ch) for articles
  - Pillar pages: drop the brand from title when it would push past 60ch
  - Keep OG title / OG description in sync with the canonical versions
  - Never use "Coverage of ..." auto-generated text
  - Every desc should include a specific fact, number, or current detail
"""

import re
import html as htmllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def update_title_and_meta(path: Path, new_title: str, new_desc: str,
                          og_title: str = None, og_desc: str = None) -> bool:
    """Update <title>, meta description, and OG equivalents."""
    if not path.exists():
        print(f"  SKIP (missing): {path}")
        return False

    with open(path, encoding="utf-8") as f:
        c = f.read()

    orig = c
    # Escape for HTML attribute context (meta content)
    desc_html = htmllib.escape(new_desc, quote=True)

    # Update <title>
    c = re.sub(
        r"<title>[^<]+</title>",
        f"<title>{new_title}</title>",
        c,
        count=1,
    )

    # Update <meta name="description">
    c = re.sub(
        r'<meta\s+name="description"\s+content="[^"]+"\s*/?>',
        f'<meta name="description" content="{desc_html}">',
        c,
        count=1,
    )

    # Update <meta property="og:title">
    if og_title is None:
        og_title = new_title
    if re.search(r'<meta\s+property="og:title"', c):
        c = re.sub(
            r'<meta\s+property="og:title"\s+content="[^"]+"\s*/?>',
            f'<meta property="og:title" content="{og_title}">',
            c,
            count=1,
        )

    # Update <meta property="og:description">
    if og_desc is None:
        og_desc = new_desc
    og_desc_html = htmllib.escape(og_desc, quote=True)
    if re.search(r'<meta\s+property="og:description"', c):
        c = re.sub(
            r'<meta\s+property="og:description"\s+content="[^"]+"\s*/?>',
            f'<meta property="og:description" content="{og_desc_html}">',
            c,
            count=1,
        )

    # Also update twitter:title and twitter:description if present
    if re.search(r'<meta\s+name="twitter:title"', c):
        c = re.sub(
            r'<meta\s+name="twitter:title"\s+content="[^"]+"\s*/?>',
            f'<meta name="twitter:title" content="{og_title}">',
            c,
            count=1,
        )
    if re.search(r'<meta\s+name="twitter:description"', c):
        c = re.sub(
            r'<meta\s+name="twitter:description"\s+content="[^"]+"\s*/?>',
            f'<meta name="twitter:description" content="{og_desc_html}">',
            c,
            count=1,
        )

    if c != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        return True
    return False


# ================================================================
# PILLAR PAGES — CTR-optimized titles (50-60ch) + metas (140-158ch)
# ================================================================
PILLAR_REWRITES = {
    # HOMEPAGE — traffic: 232 views. Drop .com, keep core keywords.
    # Title: "Live Oil & Gas Prices, Energy Geopolitics — EnergyPricesToday"
    # Length: 61ch — close to limit, brand at end for recognition
    "index.html": {
        "title": "Live Oil & Gas Prices, Energy Geopolitics | EnergyPricesToday",
        "desc": "Live oil prices, U.S. gas prices by state, and real-time energy geopolitics. WTI, Brent, and AAA data updated continuously — free and fast.",
    },

    # GAS PRICES — traffic: 105 views. Lead with search intent.
    # Title drops "EnergyPricesToday" to fit under 60ch with "AAA"
    "category/gas-prices.html": {
        "title": "Gas Prices Today by State — U.S. National Average & AAA Data",
        "desc": "Today's gas prices for all 50 states plus D.C. National average, regular, mid-grade, premium, and diesel from AAA — updated daily.",
    },

    # OIL PRICES — traffic: 151 views. Keep the "150+ benchmarks" hook visible.
    "oil-prices.html": {
        "title": "Oil Prices Today — WTI, Brent & 150+ Global Crude Benchmarks",
        "desc": "Live oil prices today: WTI crude, Brent crude, and 150+ global benchmarks updated every 5 minutes. OPEC blends, regional crudes, refined products.",
    },

    # GEOPOLITICS — traffic: 103 views. Use concrete search terms.
    "category/geopolitics.html": {
        "title": "Energy Geopolitics Today — Hormuz, Iran, OPEC, Oil Risk",
        "desc": "Real-time energy geopolitics: Strait of Hormuz, Iran tensions, OPEC+ policy, sanctions, and conflicts moving oil markets. Risk dashboard updated live.",
    },

    # MARKETS
    "markets.html": {
        "title": "Energy Markets Dashboard — Live Oil, Gas, LNG & Refined Products",
        "desc": "Live energy markets dashboard: WTI, Brent, natural gas, gasoline, diesel, heating oil, and 150+ global benchmarks. Cross-asset pricing in one view.",
    },

    # RIG COUNT
    "rig-count.html": {
        "title": "U.S. Rig Count — Weekly Baker Hughes Drilling Data",
        "desc": "Weekly Baker Hughes U.S. rig count: oil rigs, gas rigs, basin breakdowns, trajectory analysis, and year-over-year drilling activity trends.",
    },

    # COMPANY NEWS
    "category/company-news.html": {
        "title": "Energy Company News — Exxon, Shell, Chevron, BP, Aramco",
        "desc": "Latest oil and gas company news: earnings, dividends, buybacks, mergers, capex, and LNG projects from ExxonMobil, Shell, Chevron, BP, and Aramco.",
    },

    # NATURAL GAS
    "category/natural-gas.html": {
        "title": "Natural Gas Prices Today — Henry Hub, LNG & Storage",
        "desc": "Natural gas market updates: Henry Hub prices, U.S. LNG exports, storage inventory, weather-driven demand, and regional gas dynamics.",
    },

    # RENEWABLE ENERGY
    "category/renewable-energy.html": {
        "title": "Renewable Energy News — Solar, Wind, Storage & Clean Power",
        "desc": "Renewable energy news and analysis: solar, wind, hydro, and storage growth, grid integration, policy drivers, and the energy transition.",
    },

    # NUCLEAR
    "category/nuclear.html": {
        "title": "Nuclear Energy News — Reactors, SMRs, Uranium & Policy",
        "desc": "Nuclear energy coverage: U.S. reactor fleet, Small Modular Reactors, baseload reliability, uranium fuel cycle, and the nuclear renaissance.",
    },
}


# ================================================================
# TOP ARTICLES — rewrite titles to fit 60ch and descriptions to be
# specific (not "Coverage of ...") and current. Descriptions use
# actual concrete details from each article.
# ================================================================
ARTICLE_REWRITES = {
    # ----- Hormuz/Iran cluster (highest priority) -----
    "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade": {
        "title": "Iran Re-Closes Strait of Hormuz | EnergyPricesToday",
        "desc": "One day after declaring the strait open, Iran has reimposed strict control. IRGC gunboats fire on Indian tankers. April 18 update on oil market impact.",
    },
    "trump-warns-he-may-not-extend-ceasefire-threatens-to-resume-bombing-iran": {
        "title": "Trump May Let Iran Ceasefire Expire | EnergyPricesToday",
        "desc": "Aboard Air Force One: Trump says he may not extend the U.S.-Iran ceasefire set to expire Tuesday April 21, threatening to resume bombing if Hormuz stays closed.",
    },
    "oil-prices-whipsaw-on-hormuz-reversal-wti-recovers-from-fridays-11-plunge": {
        "title": "Oil Whipsaws After Hormuz Reversal | EnergyPricesToday",
        "desc": "After crashing 11.45% Friday on the Hormuz reopening, WTI crude is rebounding as Iran re-closes the strait. Brent-WTI spread widens on renewed uncertainty.",
    },
    "israel-lebanon-10-day-ceasefire-takes-effect-hezbollah-holds-fire": {
        "title": "Israel-Lebanon 10-Day Ceasefire Takes Effect | EnergyPricesToday",
        "desc": "A 10-day Israel-Lebanon ceasefire is holding for now, with Hezbollah standing down. Trump issued his strongest demand yet that Israel honor the agreement.",
    },
    "french-un-peacekeeper-killed-in-lebanon-attack-macron-blames-hezbollah": {
        "title": "French UN Peacekeeper Killed in Lebanon | EnergyPricesToday",
        "desc": "A French UN peacekeeper was killed in a Lebanon attack. President Macron publicly blames Hezbollah, putting the 10-day Israel-Lebanon ceasefire at risk.",
    },
    "irgc-gunboats-fire-on-two-indian-flagged-merchant-ships-in-strait-of-hormuz": {
        "title": "IRGC Gunboats Fire on Indian Tankers | EnergyPricesToday",
        "desc": "Iran's IRGC opened fire on two Indian-flagged merchant ships in the Strait of Hormuz after the re-closure. India has summoned the Iranian ambassador.",
    },
    "21-hour-marathon-talks-end-without-deal-vance-departs-pakistan-blaming-iran": {
        "title": "U.S.-Iran Talks Collapse After 21 Hours | EnergyPricesToday",
        "desc": "Marathon Islamabad talks ended without agreement. VP Vance departed blaming Iran; Pakistan's FM Dar continues mediation with a second round planned.",
    },
    "container-ship-struck-by-unknown-projectile-off-oman-coast": {
        "title": "Container Ship Hit by Projectile Off Oman | EnergyPricesToday",
        "desc": "A container ship was hit by an unidentified projectile off Oman, raising maritime insurance costs and shipping fears after Hormuz's re-closure.",
    },
    "maersk-hapag-lloyd-suspend-hormuz-transits-again-after-iran-reversal": {
        "title": "Maersk, Hapag-Lloyd Pull Ships From Hormuz | EnergyPricesToday",
        "desc": "Container giants Maersk and Hapag-Lloyd have re-suspended Hormuz transits after Iran's reversal. Re-routing via the Cape adds 10-14 days to voyages.",
    },
    "india-summons-iranian-ambassador-over-attack-on-indian-merchant-ships": {
        "title": "India Summons Iran Envoy Over Tanker Fire | EnergyPricesToday",
        "desc": "India has formally summoned the Iranian ambassador after IRGC gunboats fired on two Indian-flagged merchant ships in the Strait of Hormuz on April 18.",
    },
    "abqaiq-facility-hit": {
        "title": "Saudi Aramco Abqaiq Facility Hit | EnergyPricesToday",
        "desc": "Satellite imagery confirms smoke rising from Saudi Aramco's Abqaiq processing plant — which handles 5% of global oil supply — after an Iranian drone strike.",
    },

    # ----- Price/data cluster -----
    "gas-prices-continue-slide-aaa-national-falls-to-4076": {
        "title": "Gas Prices Slide to $4.076 AAA National | EnergyPricesToday",
        "desc": "AAA national gas price average falls to $4.076 — a seventh consecutive daily decline as the earlier crude drop works through refiner margins to the pump.",
    },
    "eia-reports-second-consecutive-weekly-crude-draw-cushing-stocks-below-5-year-ave": {
        "title": "EIA Reports Second Weekly Crude Draw | EnergyPricesToday",
        "desc": "EIA reports a second consecutive weekly crude draw with Cushing stocks falling below the 5-year average. WTI up 3.72% to $94.62; Brent climbs in sympathy.",
    },
    "wti-futures-curve-flips-to-backwardation-through-december-2026": {
        "title": "WTI Futures Curve Flips to Backwardation | EnergyPricesToday",
        "desc": "The WTI futures curve is now in backwardation through December 2026 — prompt crude trading above deferred months. Signal of tight physical markets.",
    },
    "april-206k-bpd-increase-proceeds": {
        "title": "OPEC+ April 206K bpd Increase Proceeds | EnergyPricesToday",
        "desc": "OPEC+ is proceeding with April's 206,000 bpd production increase despite Hormuz turmoil. The group signals readiness to act further if disruption extends.",
    },
    "us-rig-count-falls-for-third-consecutive-week-baker-hughes-reports": {
        "title": "U.S. Rig Count Falls 3rd Straight Week | EnergyPricesToday",
        "desc": "Baker Hughes reports U.S. rig count declined for a third consecutive week. Permian activity still dominates despite the national downtrend in drilling.",
    },
    "gulf-coast-refinery-margins-improve-as-crack-spreads-widen": {
        "title": "Gulf Coast Refinery Margins Widen on Cracks | EnergyPricesToday",
        "desc": "Gulf Coast refiners see expanding margins as crack spreads widen. The gap between crude input cost and finished product output is boosting refiner profits.",
    },

    # ----- Company cluster -----
    "exxonmobil-announces-42b-expansion-of-permian-basin-operations": {
        "title": "Exxon Announces $4.2B Permian Expansion | EnergyPricesToday",
        "desc": "ExxonMobil unveils a $4.2 billion expansion of Permian operations, increasing Midland and Delaware basin capex and integrating Pioneer acquisition synergies.",
    },
    "california-gas-prices-hit-518-as-state-specific-regulations-add-costs": {
        "title": "California Gas Prices Hit $5.18 | EnergyPricesToday",
        "desc": "California gas prices climb to $5.18 — far above the national average — as CARB reformulated fuel rules, cap-and-trade, and gas taxes drive regional premiums.",
    },

    # ----- Chokepoints/explainers (high evergreen SEO value) -----
    "strait-of-hormuz-why-this-chokepoint-controls-global-oil-prices": {
        "title": "Why the Strait of Hormuz Controls Oil Prices | EnergyPricesToday",
        "desc": "The Strait of Hormuz is the world's most important oil chokepoint — ~20% of seaborne crude passes through. Why any closure immediately moves Brent and WTI.",
    },
    "strait-of-malacca": {
        "title": "Strait of Malacca — Why It Matters for Oil | EnergyPricesToday",
        "desc": "The Strait of Malacca is Asia's critical oil artery, moving roughly 16 million barrels per day. Why it's the second-most-important chokepoint after Hormuz.",
    },
}


def main():
    print("[ctr_optimization] Updating pillar pages...")
    pillar_count = 0
    for rel_path, meta in PILLAR_REWRITES.items():
        path = ROOT / rel_path
        t = meta["title"]
        d = meta["desc"]
        print(f"  {rel_path}")
        print(f"    title ({len(t)}ch): {t}")
        print(f"    desc ({len(d)}ch): {d}")
        if update_title_and_meta(path, t, d):
            pillar_count += 1
    print(f"  ✓ Updated {pillar_count} pillar pages")

    print(f"\n[ctr_optimization] Updating top articles...")
    article_count = 0
    for slug, meta in ARTICLE_REWRITES.items():
        path = ROOT / "articles" / f"{slug}.html"
        t = meta["title"]
        d = meta["desc"]
        if update_title_and_meta(path, t, d):
            article_count += 1
    print(f"  ✓ Updated {article_count} articles")


if __name__ == "__main__":
    main()
