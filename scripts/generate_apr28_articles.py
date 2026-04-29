#!/usr/bin/env python3
"""
Generate 4 new article files covering April 27-28, 2026 developments.
Uses the same template as the April 26 generator.
"""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

STORIES = [
    {
        "slug": "iran-proposes-hormuz-reopening-if-us-lifts-naval-blockade",
        "title_variants": [
            "Iran Proposes Hormuz Reopening if U.S. Lifts Naval Blockade",
            "Iran Submits Formal Proposal: Reopen Hormuz, Postpone Nuclear Talks",
            "Tehran Offers Hormuz-for-Blockade Deal as Trump Weighs Response",
            "Iran's New Proposal: Hormuz for Blockade Lift, Nuclear Talks Deferred",
        ],
        "display_title": "Iran Proposes Hormuz Reopening if U.S. Lifts Naval Blockade",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "April 27, 2026",
        "read_time": "6 min",
        "meta_desc": "Iran submitted a formal proposal Monday April 27 to reopen the Strait of Hormuz if the U.S. lifts its naval blockade and ends military operations, while postponing nuclear talks for a later phase. Trump and his national security team discussed the offer; early indications suggest the proposal is unlikely to be accepted in its current form.",
        "paragraphs": [
            "Iran on Monday, April 27, 2026, submitted a formal proposal to the United States that would reopen the Strait of Hormuz if Washington lifts its naval blockade on Iranian ports and agrees to end military operations &mdash; while postponing direct negotiations on Tehran&rsquo;s nuclear program to a later phase. The proposal was first reported by Axios on Monday and confirmed by White House Press Secretary Karoline Leavitt the same afternoon, who said President Trump and his national security team had discussed the offer.",
            "Iranian Foreign Minister Abbas Araghchi presented the framework during weekend visits to Islamabad and Muscat, after the second round of direct U.S.-Iran talks collapsed when Araghchi left Pakistan on Sunday April 26 without meeting any U.S. officials. Trump cancelled the Witkoff-Kushner trip to Islamabad on Saturday. Pakistani Prime Minister Sharif and Iranian President Pezeshkian held a 50-minute phone call Saturday evening to keep the back-channel open.",
            "Under the proposal, Iran would reopen the Strait of Hormuz to commercial shipping if the United States ends its blockade on Iranian ports and concludes the active phase of the conflict. Critically, Tehran wants nuclear talks deferred &mdash; a sequencing that goes to the heart of Washington&rsquo;s objections. The Trump administration has publicly maintained that dismantling Iran&rsquo;s nuclear capabilities was the primary objective for initiating the conflict in the first place.",
            "Secretary of State Marco Rubio appeared to pour cold water on the proposal in a Fox News interview Monday, saying that Iran is &ldquo;serious about figuring out how they can buy themselves more time&rdquo; and that the U.S. &ldquo;can&rsquo;t let them get away with it.&rdquo; He added that Iran is &ldquo;worse off&rdquo; and &ldquo;weaker&rdquo; than it was at the start of the conflict. Rubio specifically dismissed the framing of Iran &ldquo;reopening&rdquo; the strait, noting that Hormuz is international waters and Iran has no legitimate authority to close or open it.",
            "Multiple media reports cited unnamed senior officials saying President Trump &ldquo;does not love&rdquo; the proposal because it omits provisions for Iran&rsquo;s nuclear program. CNN reported Trump is unlikely to accept the offer in its current form. U.S. intelligence assessments reportedly suggest that Iranian negotiators have not been authorized by the Supreme Leader or the IRGC to make meaningful concessions on the nuclear program, complicating any sequenced framework.",
            "European allies have begun pushing for a more comprehensive solution. German Chancellor Friedrich Merz has warned that Washington risks being outmaneuvered if it accepts an Iran-controlled framework for Hormuz transit, accusing Tehran of engaging in tactical delay while the U.S. lacks a clear exit strategy. The U.K. and France remain part of a coordinated effort to secure the strait.",
            "Oil markets reacted with continued volatility through Monday and Tuesday. WTI crude rallied sharply, touching $100/bbl, on hopes that any framework deal &mdash; even a partial one &mdash; could begin restoring tanker traffic. For continuous market reaction, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">oil price dashboard</a> and <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>.",
        ],
        "related": [
            ("Araghchi Leaves Pakistan Without Meeting U.S. Officials as Talks Collapse", "araghchi-leaves-pakistan-without-meeting-us-officials-as-talks-collapse"),
            ("Trump Cancels Witkoff-Kushner Pakistan Trip as Iran Talks Stall", "trump-cancels-witkoff-kushner-pakistan-trip-as-iran-talks-stall"),
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
        ],
    },
    {
        "slug": "wti-tops-100-brent-111-on-iran-hormuz-proposal-uncertainty",
        "title_variants": [
            "WTI Tops $100, Brent $111 on Iran Hormuz Proposal Uncertainty",
            "Crude Rallies 7th Straight Session as Markets Weigh Iran Offer",
            "WTI Settles at $99.93, Brent at $111.26 on Tuesday Surge",
            "Oil Prices Surge Nearly 4% as Trump Weighs Iran's Hormuz Deal",
            "Brent Crosses $111 Tuesday on Trump's Skepticism Over Iran Plan",
        ],
        "display_title": "WTI Tops $100, Brent $111 on Iran Hormuz Proposal Uncertainty",
        "category": "Oil Markets",
        "category_url": "../oil-prices.html",
        "date": "April 28, 2026",
        "read_time": "5 min",
        "meta_desc": "WTI crude futures jumped more than 3% Tuesday April 28 to settle above $99.93, with Brent above $111.26 as markets weighed Iran's new Hormuz proposal and Trump's skepticism. The 7th consecutive session of gains pushed both benchmarks to highs not seen since early April.",
        "paragraphs": [
            "U.S. crude oil futures rallied for a seventh consecutive session on Tuesday, April 28, 2026, with West Texas Intermediate jumping more than 3% to settle at $99.93 per barrel and Brent crude climbing nearly 3% to settle at $111.26. Brent traded as high as $111.57 intraday, the highest level since early March. The combined seven-session rally has lifted WTI by roughly $7 per barrel and Brent by more than $9.",
            "The price action reflects a complex mix of cross-currents: hopes that Iran&rsquo;s formal Hormuz reopening proposal could restore tanker traffic, set against signals from the Trump administration that the proposal is unlikely to be accepted in its current form because it postpones nuclear discussions. President Trump posted on Truth Social Tuesday morning that Iran had informed the U.S. it was in &ldquo;a State of Collapse&rdquo; and was eager to see the strait reopened, language widely read as reinforcing his negotiating leverage rather than indicating imminent agreement.",
            "Press Secretary Karoline Leavitt reiterated Tuesday afternoon that the President&rsquo;s &ldquo;red lines with respect to Iran have been made very, very clear,&rdquo; declining to characterize the proposal as actively under consideration. She noted that Trump and his national security team had discussed it on Monday and would communicate any decision directly. Sources familiar with internal deliberations told CNN that Trump was unlikely to accept the proposal as currently framed.",
            "From an oil markets standpoint, the conflict is now in its ninth week, and the persistent closure of the Strait of Hormuz &mdash; which in normal times moves roughly 20% of global seaborne oil &mdash; has fundamentally repriced the geopolitical risk premium. Analysts at Goldman Sachs, Morgan Stanley, and JPMorgan have all noted that the typical correlation between U.S. inventory data and crude prices has weakened materially since the conflict began.",
            "The International Energy Agency this week warned of an &ldquo;unprecedented supply shock&rdquo; alongside rising risks of a global demand slowdown driven by elevated energy prices. The IEA flagged spare capacity, OPEC+ pipeline routing, and emergency stockpile policy as the three principal demand-side cushions, with each near or at structural limits.",
            "Refined product markets followed crude higher. Gasoline RBOB futures jumped roughly 5% on the day, ULSD heating oil futures gained more than 4%, and jet fuel posted similar gains. AAA reported the U.S. retail gasoline national average rose to $4.144 per gallon Tuesday, the highest level in nearly four years. For continuous tracking of all energy benchmarks, see <a href=\"../markets.html\" style=\"color:var(--blue);text-decoration:none\">our markets dashboard</a> and <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">oil price dashboard</a>.",
        ],
        "related": [
            ("Iran Proposes Hormuz Reopening if U.S. Lifts Naval Blockade", "iran-proposes-hormuz-reopening-if-us-lifts-naval-blockade"),
            ("WTI Surges 13% on Week as Hormuz Stays Closed and Talks Stall", "wti-surges-13-percent-on-week-as-hormuz-stays-closed-and-talks-stall"),
            ("Trump Says Iran in 'State of Collapse' as Hormuz Standoff Drags Into Ninth Week", "trump-says-iran-in-state-of-collapse-as-hormuz-standoff-drags-into-ninth-week"),
        ],
    },
    {
        "slug": "trump-says-iran-in-state-of-collapse-as-hormuz-standoff-drags-into-ninth-week",
        "title_variants": [
            "Trump Says Iran in 'State of Collapse' as Hormuz Standoff Drags Into Ninth Week",
            "Trump: Iran 'Informed Us' It Is in State of Collapse",
            "President Posts on Iran's 'Collapse' as Hormuz Negotiations Continue",
        ],
        "display_title": "Trump Says Iran in 'State of Collapse' as Hormuz Standoff Drags Into Ninth Week",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "April 28, 2026",
        "read_time": "4 min",
        "meta_desc": "President Trump posted Tuesday April 28 that Iran had informed the U.S. it was in 'a State of Collapse' and wanted Hormuz reopened. The post came as the U.S. weighs Iran's Monday proposal to lift the blockade in exchange for reopening the strait.",
        "paragraphs": [
            "President Donald Trump posted on Truth Social Tuesday morning, April 28, 2026, that Iran had &ldquo;informed us&rdquo; it was in &ldquo;a State of Collapse&rdquo; and wanted the United States to &ldquo;Open the Hormuz Strait, as soon as possible.&rdquo; The post, which did not cite supporting evidence, came as the White House continues to weigh Iran&rsquo;s Monday proposal to reopen the strait if the U.S. lifts its naval blockade.",
            "&ldquo;They want us to &lsquo;Open the Hormuz Strait,&rsquo; as soon as possible, as they try to figure out their leadership situation,&rdquo; Trump wrote, framing the negotiating posture as one of overwhelming U.S. leverage. The post appeared to formalize what has been the President&rsquo;s consistent message since the start of the conflict: that the U.S. blockade is an effective economic strangulation tool and that Iran must come to terms on U.S. conditions, including nuclear program restraints.",
            "The Iranian government did not immediately respond to the &ldquo;State of Collapse&rdquo; framing. Iranian state media earlier in the day emphasized that the proposal submitted Monday was a serious diplomatic effort and accused Washington of negotiating in bad faith. Pro-government demonstrators rallied in Tehran on Monday in what state media described as a show of national resilience.",
            "White House Press Secretary Karoline Leavitt declined Tuesday afternoon to characterize the proposal as actively under consideration, saying instead that the President&rsquo;s &ldquo;red lines with respect to Iran have been made very, very clear, not just to the American public, but also to them as well.&rdquo; She added that Trump and his national security team had discussed the matter Monday morning and would announce any decision directly.",
            "The conflict has now extended into its ninth week, with the Strait of Hormuz effectively closed to commercial traffic since mid-March. Iran reportedly lost track of mines it laid in the strait, complicating any technical reopening even after a political deal is reached. Trump on April 22 ordered the U.S. Navy to &ldquo;shoot and kill&rdquo; Iranian small boats observed laying mines, formalizing rules of engagement that previously governed only defensive operations.",
            "Markets read the post as further reducing the probability of a near-term agreement. WTI crude rallied to $99.93 and Brent to $111.26 by Tuesday&rsquo;s close, both at multi-week highs. The U.S. retail gasoline national average rose to $4.144 per gallon, also a multi-year high. For continuous coverage, see the <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>, <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">oil price dashboard</a>, and <a href=\"../category/gas-prices.html\" style=\"color:var(--blue);text-decoration:none\">U.S. gas prices by state</a>.",
        ],
        "related": [
            ("Iran Proposes Hormuz Reopening if U.S. Lifts Naval Blockade", "iran-proposes-hormuz-reopening-if-us-lifts-naval-blockade"),
            ("Araghchi Leaves Pakistan Without Meeting U.S. Officials as Talks Collapse", "araghchi-leaves-pakistan-without-meeting-us-officials-as-talks-collapse"),
            ("Trump Orders Navy to 'Shoot and Kill' Iranian Mine-Laying Vessels in Strait", "trump-orders-navy-shoot-and-kill-iranian-mine-laying-vessels-in-strait"),
        ],
    },
    {
        "slug": "us-gas-average-hits-414-highest-in-nearly-four-years",
        "title_variants": [
            "U.S. Gas Average Hits $4.14, Highest in Nearly Four Years",
            "AAA: National Gas Price Climbs to $4.14 as Crude Tops $100",
            "Pump Prices Hit Multi-Year High as Hormuz Standoff Persists",
            "U.S. Retail Gasoline at $4.14, Up 11 Cents in a Week on Crude Surge",
        ],
        "display_title": "U.S. Gas Average Hits $4.14, Highest in Nearly Four Years",
        "category": "Gas Prices",
        "category_url": "../category/gas-prices.html",
        "date": "April 28, 2026",
        "read_time": "4 min",
        "meta_desc": "AAA reported Tuesday April 28 that the U.S. national average for regular gasoline rose to $4.144 per gallon, the highest level in nearly four years. Diesel reached $5.689. Crude oil's seven-session rally to $99.93 WTI is feeding through to retail prices.",
        "paragraphs": [
            "The U.S. national average for a gallon of regular gasoline rose to $4.144 on Tuesday, April 28, 2026, according to AAA &mdash; the highest level recorded since the summer of 2022. The new high reflects a roughly 11-cent increase over the past week, undoing the brief downward move recorded between April 16 and April 23 when crude oil prices had pulled back below $100.",
            "The renewed rally in crude markets &mdash; WTI settled at $99.93 and Brent at $111.26 Tuesday, both up roughly 4% on the session and at multi-week highs &mdash; is the primary driver. Crude oil costs typically account for roughly 51% of the retail gasoline price, with refining (~20%), distribution and marketing (~11%), and taxes (~18%) comprising the rest.",
            "California remains the most expensive state at roughly $5.95 per gallon, followed by Hawaii ($5.79) and Washington ($5.54). Oregon also exceeds $5.00. The least expensive state is Oklahoma at $3.36, followed by Kansas ($3.42) and North Dakota ($3.43). Diesel is now at a national average of $5.689 per gallon, near record levels not seen since the summer of 2022.",
            "AAA spokesperson Jana Tidwell noted in a statement Tuesday that the closure of the Strait of Hormuz and the duration of the conflict are the primary drivers, with seasonal demand from spring break travel adding to the upward pressure. She cautioned that further escalation or any disruption to global supplies could push averages even higher in coming weeks.",
            "Refined product wholesale markets confirm the move. Gasoline RBOB futures gained roughly 5% Tuesday, ULSD heating oil futures gained more than 4%, and jet fuel posted similar gains. Refiner crack spreads &mdash; the spread between crude and refined products &mdash; remain near multi-year highs, signaling that refineries are running aggressively to supply summer-blend demand even as crude costs climb.",
            "U.S. Energy Information Administration data for the week ending April 24 showed gasoline demand at 8.94 million barrels per day, up modestly from 8.81 million the previous week. Total domestic gasoline supply remains tight at 233.4 million barrels. For continuous state-level pricing, see our <a href=\"../category/gas-prices.html\" style=\"color:var(--blue);text-decoration:none\">U.S. gas prices dashboard</a>; for crude pricing, see the <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">oil price dashboard</a>.",
        ],
        "related": [
            ("WTI Tops $100, Brent $111 on Iran Hormuz Proposal Uncertainty", "wti-tops-100-brent-111-on-iran-hormuz-proposal-uncertainty"),
            ("Iran Proposes Hormuz Reopening if U.S. Lifts Naval Blockade", "iran-proposes-hormuz-reopening-if-us-lifts-naval-blockade"),
            ("Gas Prices Fall to $4.058, Seventh Consecutive Daily Decline", "gas-prices-fall-to-4058-seventh-consecutive-daily-decline"),
        ],
    },
]


def render_article(s):
    title_safe = s["display_title"].replace('&', '&amp;').replace("'", '&rsquo;')
    paragraphs = "\n          ".join(f"<p>{p}</p>" for p in s["paragraphs"])
    related_items = "\n            ".join(
        f'<li><a href="{slug}.html" style="color:var(--blue);text-decoration:none">{title}</a></li>'
        for title, slug in s["related"]
    )
    cat_label = s["category"]

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','957762016897581');fbq('track','PageView');</script><noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=957762016897581&ev=PageView&noscript=1"/></noscript>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{title_safe} | EnergyPricesToday</title>
  <meta name="description" content="{s['meta_desc']}">
  <link rel="canonical" href="https://www.energypricestoday.com/articles/{s['slug']}.html">
  <meta property="og:type" content="article"><meta property="og:title" content="{title_safe} | EnergyPricesToday">
  <meta property="og:description" content="{s['meta_desc']}">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap"></noscript>
  <link rel="stylesheet" href="../css/styles.css?v=13">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-FXGF8HZFWL"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-FXGF8HZFWL");</script>
  <link rel="icon" type="image/x-icon" href="../images/favicon.ico?v=2">
  <link rel="icon" type="image/svg+xml" href="../images/favicon.svg?v=2">
  <link rel="icon" type="image/png" sizes="16x16" href="../images/favicon-16x16.png?v=2">
  <link rel="icon" type="image/png" sizes="32x32" href="../images/favicon-32x32.png?v=2">
  <link rel="icon" type="image/png" sizes="48x48" href="../images/favicon-48x48.png?v=2">
  <link rel="apple-touch-icon" sizes="180x180" href="../images/apple-touch-icon.png?v=2">
  <link rel="shortcut icon" href="../images/favicon.ico?v=2">
</head>
<body>
  <header class="site-header" id="site-header"></header>
  <main>
    <article class="article-page">
      <div class="container" style="max-width:780px">
        <nav aria-label="Breadcrumb" style="margin:24px 0 16px;font-size:12px;color:var(--text-3);display:flex;flex-wrap:wrap;gap:6px;align-items:center">
          <a href="../index.html" style="color:var(--text-2);text-decoration:none">Home</a>
          <span style="color:var(--text-3)">&rsaquo;</span>
          <a href="{s['category_url']}" style="color:var(--text-2);text-decoration:none">{cat_label}</a>
          <span style="color:var(--text-3)">&rsaquo;</span>
          <span style="color:var(--text-2)">Article</span>
        </nav>
        <h1>{title_safe}</h1>
        <div class="article-meta" style="margin:14px 0 24px"><span>Staff</span><span>{s['date']}</span><span>{s['read_time']} read</span></div>
        <div class="article-body">
          {paragraphs}
        </div>

        <div style="margin-top:40px;padding:24px;background:var(--surface-2);border-radius:10px;border-left:3px solid var(--blue)">
          <h3 style="margin:0 0 12px 0;font-size:14px;text-transform:uppercase;letter-spacing:0.06em;color:var(--text-2)">Related Coverage</h3>
          <ul style="margin:0;padding-left:20px;line-height:1.8">
            {related_items}
          </ul>
        </div>

        <div style="margin-top:32px;padding-top:20px;border-top:1px solid var(--border);display:flex;gap:12px;flex-wrap:wrap">
          <a href="../oil-prices.html" class="btn-secondary">Oil Prices</a>
          <a href="../category/gas-prices.html" class="btn-secondary">Gas Prices</a>
          <a href="../electricity-prices.html" class="btn-secondary">Electricity</a>
          <a href="../category/geopolitics.html" class="btn-secondary">Geopolitics</a>
          <a href="../markets.html" class="btn-secondary">Markets</a>
        </div>
      </div>
    </article>
  </main>
  <footer class="site-footer" id="site-footer"></footer>
  <script src="../js/data.js?v=13"></script>
  <script src="../js/article-slugs.js?v=13"></script>
  <script src="../js/main.js?v=13"></script>
</body>
</html>
'''


def main():
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    created = 0
    for s in STORIES:
        path = ARTICLES_DIR / f"{s['slug']}.html"
        if path.exists():
            print(f"SKIP (exists): {s['slug']}.html")
            continue
        path.write_text(render_article(s), encoding='utf-8')
        print(f"CREATED: {s['slug']}.html")
        created += 1
    print(f"\nTotal created: {created} of {len(STORIES)}")


if __name__ == "__main__":
    main()
