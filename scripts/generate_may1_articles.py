#!/usr/bin/env python3
"""
Generate 5 new article files covering April 30 - May 1, 2026 developments.
Uses EnergyPricesToday Editorial byline + NewsMediaOrganization schema author.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

STORIES = [
    {
        "slug": "iran-sends-updated-peace-proposal-through-pakistan-trump-not-satisfied",
        "title_variants": [
            "Iran Sends Updated Peace Proposal Through Pakistan; Trump 'Not Satisfied'",
            "Iran Submits Updated Proposal via Pakistan as Trump Rejects Offer",
            "Pakistani Mediators Deliver New Iran Proposal to Washington; Trump Unsatisfied",
            "Iran's Updated Peace Proposal Reaches U.S.; Trump Says No Deal",
            "Tehran's New Offer Lands at White House; Trump 'Not Satisfied'",
        ],
        "display_title": "Iran Sends Updated Peace Proposal Through Pakistan; Trump 'Not Satisfied'",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 1, 2026",
        "iso_date": "2026-05-01T08:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "6 min",
        "meta_desc": "Pakistani officials confirmed Friday May 1 that Iranian mediators delivered an updated peace proposal to the U.S. through Islamabad. President Trump told reporters he was unsatisfied with the offer; oil prices retraced from Thursday's 4-year highs.",
        "keywords": "Iran peace proposal, Trump Iran deal, Pakistan mediation, Hormuz negotiations, Iran sanctions, U.S.-Iran conflict, Mojtaba Khamenei",
        "paragraphs": [
            "Pakistani officials confirmed Friday, May 1, 2026, that they had received an updated peace proposal from Iran and delivered it to the United States. The development marked the first concrete diplomatic movement since direct U.S.-Iran talks collapsed the prior weekend in Islamabad. President Donald Trump confirmed receipt of the proposal during remarks to reporters at the White House but said he was not satisfied with its terms.",
            "&ldquo;Iran wants to make a deal,&rdquo; Trump told reporters, &ldquo;but I&rsquo;m not satisfied with it. They have no military left.&rdquo; The President did not detail his specific objections to the proposal, but the framing echoed his previous insistence that any agreement must include verifiable constraints on Iran&rsquo;s nuclear program &mdash; a point the prior April 27 proposal had attempted to defer to a later phase.",
            "Markets responded immediately to the news that diplomacy was technically alive but moving slowly. WTI crude futures fell roughly 3% Friday to settle at $101.94 per barrel after touching a four-year intraday high of $111 on Thursday. Brent crude fell 2% to settle at $108.17, having reached $114.10 intraday Thursday on reports that President Trump was being briefed on expanded military options against Iran.",
            "The April 30 Thursday spike was tied to a Reuters and Axios report that CENTCOM commander Adm. Brad Cooper had presented Trump with options for &ldquo;a short and intense wave of strikes&rdquo; against Iranian targets &mdash; a meaningful escalation in stated U.S. posture, even if no decision had been taken. Friday&rsquo;s pullback reflected hopes that the Iranian counter-proposal could provide a diplomatic off-ramp.",
            "Trump faces a 60-day deadline under the War Powers Resolution related to military action in the Iran conflict. Under the 1973 law, a president must withdraw troops within 60 days of notifying Congress of their deployment unless lawmakers authorize the action. Congress has not done so. The administration has argued that the April 10 ceasefire, which has officially held, &ldquo;terminated&rdquo; hostilities under the resolution &mdash; an interpretation that legal scholars and several members of Congress have pushed back on.",
            "Iran&rsquo;s public posture has hardened in recent days. Supreme Leader Mojtaba Khamenei this week pledged not to relinquish the country&rsquo;s nuclear or missile capabilities and indicated Tehran would retain control over the Strait of Hormuz. The hardline framing complicates any path to a deal that satisfies Washington&rsquo;s stated objectives.",
            "The conflict is now in its tenth week. The Strait of Hormuz remains essentially closed to commercial traffic. The IEA has called the disruption an &ldquo;unprecedented supply shock&rdquo;; final pre-blockade Persian Gulf cargoes have now reached destinations, and analysts warn several countries face acute oil shortages in the coming weeks. U.S. crude exports surged to record levels last week as global buyers turned to American producers. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a> and <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices</a>.",
        ],
        "related": [
            ("Trump Briefed on Expanded Iran Military Options as Crude Hit 4-Year High", "trump-briefed-on-expanded-iran-military-options-as-crude-hit-4-year-high"),
            ("Mojtaba Khamenei Vows to Retain Nuclear and Missile Capabilities", "mojtaba-khamenei-vows-to-retain-nuclear-and-missile-capabilities"),
            ("Iran Proposes Hormuz Reopening if U.S. Lifts Naval Blockade", "iran-proposes-hormuz-reopening-if-us-lifts-naval-blockade"),
        ],
    },
    {
        "slug": "trump-briefed-on-expanded-iran-military-options-as-crude-hit-4-year-high",
        "title_variants": [
            "Trump Briefed on Expanded Iran Military Options as Crude Hit 4-Year High",
            "CENTCOM Briefs Trump on Iran Strike Options; WTI Hits $111, Brent $114",
            "Adm. Cooper Presents Iran Strike Options to Trump as Oil Spikes",
            "Crude Oil Spikes to 4-Year Highs on Reports Trump Briefed on Iran Strikes",
        ],
        "display_title": "Trump Briefed on Expanded Iran Military Options as Crude Hit 4-Year High",
        "category": "Oil Markets",
        "category_url": "../oil-prices.html",
        "date": "April 30, 2026",
        "iso_date": "2026-04-30T08:00:00-04:00",
        "section": "Oil Markets",
        "read_time": "5 min",
        "meta_desc": "Reports Thursday April 30 that CENTCOM Adm. Brad Cooper briefed President Trump on expanded military options against Iran sent WTI crude to a 4-year intraday high of $111 and Brent to $114 — the highest level since June 2022 — before profit-taking trimmed gains.",
        "keywords": "WTI crude oil price, Brent crude, CENTCOM, Adm. Brad Cooper, Iran military options, oil prices spike, energy markets, Hormuz blockade",
        "paragraphs": [
            "U.S. crude oil futures jumped to a four-year intraday high on Thursday, April 30, 2026, after reports that U.S. Central Command chief Admiral Brad Cooper presented President Trump with expanded military options against Iran &mdash; including a planned &ldquo;short and intense wave of strikes&rdquo; reportedly under review.",
            "WTI futures touched $111.05 per barrel intraday before turning lower, settling at $105.09 per barrel as profit-taking and uncertainty over actual policy direction tempered the move. Brent crude reached $114.10 intraday before settling at $110.40 &mdash; both benchmarks at their highest intraday levels since June 2022. The spike unwound partially during Friday trading after Iran sent an updated peace proposal through Pakistani mediators.",
            "The Axios report described the Cooper briefing as a meaningful shift in stated U.S. posture rather than an immediate decision to act. Sources told the outlet the briefing covered a range of options, with the &ldquo;short and intense wave of strikes&rdquo; framework explicitly intended to compress the action into a tight window that could be argued to fall outside extended-engagement provisions of the War Powers Resolution.",
            "Markets read the briefing as confirmation that diplomatic patience in Washington is wearing thin. The April 10 ceasefire has held formally, but the underlying conflict has continued to intensify economically as the U.S. naval blockade persists, Iran retains effective control over the Strait of Hormuz, and final pre-blockade Persian Gulf cargoes reach their destinations.",
            "&ldquo;The market is now pricing a meaningful tail risk of expanded U.S. action,&rdquo; one Goldman Sachs trader told clients in a note circulated Thursday afternoon. &ldquo;The asymmetry has shifted: the floor is no longer the diplomatic-resolution scenario, it&rsquo;s the active-conflict scenario.&rdquo; Goldman now sees Brent averaging above $100 per barrel for full-year 2026, with the EIA forecasting a Q2 peak near $115 per barrel.",
            "Refined product markets followed crude higher Thursday before pulling back Friday. Gasoline RBOB futures gained on the day; ULSD heating oil and jet fuel posted similar gains. AAA reported the U.S. retail gasoline national average reached $4.392 per gallon Friday May 1 &mdash; up roughly 25 cents in three days and the highest level since July 2022.",
            "For continuing coverage, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices</a>, <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>, and <a href=\"../markets.html\" style=\"color:var(--blue);text-decoration:none\">full markets view</a>.",
        ],
        "related": [
            ("Iran Sends Updated Peace Proposal Through Pakistan; Trump 'Not Satisfied'", "iran-sends-updated-peace-proposal-through-pakistan-trump-not-satisfied"),
            ("Mojtaba Khamenei Vows to Retain Nuclear and Missile Capabilities", "mojtaba-khamenei-vows-to-retain-nuclear-and-missile-capabilities"),
            ("WTI Tops $100, Brent $111 on Iran Hormuz Proposal Uncertainty", "wti-tops-100-brent-111-on-iran-hormuz-proposal-uncertainty"),
        ],
    },
    {
        "slug": "mojtaba-khamenei-vows-to-retain-nuclear-and-missile-capabilities",
        "title_variants": [
            "Mojtaba Khamenei Vows to Retain Nuclear and Missile Capabilities",
            "Iran's Mojtaba Khamenei Vows to Retain Nuclear and Missile Capabilities",
            "Tehran's Khamenei Pledges No Concessions on Nuclear Program or Missiles",
            "Iran Supreme Leader Mojtaba Khamenei Rejects Nuclear Concessions",
        ],
        "display_title": "Mojtaba Khamenei Vows to Retain Nuclear and Missile Capabilities",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "April 30, 2026",
        "iso_date": "2026-04-30T10:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "4 min",
        "meta_desc": "Iran's Supreme Leader Mojtaba Khamenei pledged this week not to relinquish the country's nuclear or missile capabilities and indicated Tehran would retain control over the Strait of Hormuz, complicating prospects for a comprehensive U.S.-Iran deal.",
        "keywords": "Mojtaba Khamenei, Iran Supreme Leader, Iran nuclear program, Iran missiles, Tehran, Strait of Hormuz, U.S.-Iran negotiations",
        "paragraphs": [
            "Iran&rsquo;s Supreme Leader Mojtaba Khamenei this week pledged that Tehran would not relinquish its nuclear or missile capabilities, dampening prospects for a comprehensive deal even as Pakistani mediators worked to deliver an updated Iranian peace proposal to Washington. Khamenei indicated that Tehran would also retain control over the Strait of Hormuz &mdash; the chokepoint at the center of the current conflict.",
            "The remarks delivered through Iranian state media carried particular weight given the ongoing succession dynamics inside Tehran. Mojtaba Khamenei&rsquo;s consolidation of decision-making authority has shifted Iran&rsquo;s negotiating posture toward more hardline framings than during the early phase of the conflict, when civilian Foreign Minister Abbas Araghchi was the primary public voice.",
            "&ldquo;The Islamic Republic will not surrender what it has built over decades to outside pressure,&rdquo; Khamenei said in remarks framed as a response to U.S. demands for verifiable constraints on the nuclear program. &ldquo;The Strait of Hormuz is part of the homeland and will be defended as such.&rdquo;",
            "U.S. officials have consistently maintained that any deal must include enforceable limits on Iran&rsquo;s nuclear program. The April 27 proposal that Tehran submitted via Pakistan attempted to defer that question to a later phase &mdash; a sequencing the Trump administration has called unacceptable. Friday&rsquo;s updated proposal reportedly addresses some U.S. concerns, but Trump&rsquo;s public response (&ldquo;I&rsquo;m not satisfied with it&rdquo;) suggested the gap remains wide.",
            "European foreign ministries continue to push for a more comprehensive framework. German Chancellor Merz, French President Macron, and U.K. Prime Minister Starmer convened a Paris coalition earlier this month focused on Hormuz security and shipping. The European position has been that any deal must address both the strait and the nuclear program in parallel, not sequentially.",
            "Markets read Khamenei&rsquo;s remarks as a near-term ceiling on diplomatic optimism. WTI fell from a 4-year intraday high of $111 on Thursday to settle at $101.94 on Friday after the updated Iranian proposal arrived, but analysts noted the conflict remains structurally far from resolution. For more, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a> and <a href=\"../articles/iran.html\" style=\"color:var(--blue);text-decoration:none\">Iran topic hub</a>.",
        ],
        "related": [
            ("Iran Sends Updated Peace Proposal Through Pakistan; Trump 'Not Satisfied'", "iran-sends-updated-peace-proposal-through-pakistan-trump-not-satisfied"),
            ("Trump Briefed on Expanded Iran Military Options as Crude Hit 4-Year High", "trump-briefed-on-expanded-iran-military-options-as-crude-hit-4-year-high"),
            ("Iran Nuclear Program Remains Central Sticking Point in U.S. Negotiations", "iran-nuclear-program-remains-central-sticking-point-in-us-negotiations"),
        ],
    },
    {
        "slug": "exxonmobil-q1-2026-profit-falls-to-5-year-low-but-beats-estimates",
        "title_variants": [
            "ExxonMobil Q1 Profit Falls to 5-Year Low at $4.2B Despite Beating Estimates",
            "Exxon Reports Q1 Net of $4.2B; Adj EPS $1.16 Beats $1.01 Estimate",
            "ExxonMobil Q1 2026 Profit Hits 5-Year Low; Permian on Track for 1.8M boe/d",
            "ExxonMobil Q1 Earnings Beat: Guyana Sets Production Record",
        ],
        "display_title": "ExxonMobil Q1 Profit Falls to 5-Year Low at $4.2B Despite Beating Estimates",
        "category": "Company News",
        "category_url": "../category/company-news.html",
        "date": "May 1, 2026",
        "iso_date": "2026-05-01T07:00:00-04:00",
        "section": "Company News",
        "read_time": "5 min",
        "meta_desc": "ExxonMobil reported Q1 2026 net income of $4.2 billion — its lowest in five years — but beat Wall Street estimates with $1.16 adjusted EPS and $85.14 billion in revenue. Production hit 4.6 million bpd; Guyana set a quarterly record above 900,000 gross bpd.",
        "keywords": "ExxonMobil earnings, XOM Q1 2026, Exxon revenue, Permian Basin, Guyana oil production, Darren Woods, oil major earnings",
        "paragraphs": [
            "ExxonMobil reported first-quarter 2026 results on Friday, May 1, that beat Wall Street expectations even as net income fell to its lowest level in five years. The company reported Q1 net income of $4.2 billion, or $1.00 per diluted share, compared with $7.7 billion or $1.76 per share in the year-earlier period. On an adjusted basis excluding identified items, EPS was $1.16, beating the LSEG consensus estimate of $1.01.",
            "Revenue reached $85.14 billion, beating consensus estimates of $79.78 billion and growing 2.4% year-over-year despite operational disruptions in the Middle East. The earnings beat reflected stronger-than-expected refining margins, record production in Guyana, and disciplined cost management offsetting headwinds from Middle East trading-timing effects and the ongoing conflict.",
            "Total oil-equivalent production reached 4.6 million barrels per day in the quarter. Guyana production set a new quarterly record at more than 900,000 gross barrels per day from the Stabroek block. Production in the Permian Basin also increased; ExxonMobil reaffirmed it remains on track to reach 1.8 million oil-equivalent barrels per day in full-year 2026 Permian output, with growth focused on value over volume.",
            "&ldquo;Events in the Middle East tested that strength,&rdquo; CEO Darren Woods said in a statement, referring to the integrated portfolio strategy executed since 2018. &ldquo;Our underlying business delivered results that reflect the benefits of years of strategic investment.&rdquo; Excluding identified items and derivative-timing effects, ExxonMobil&rsquo;s underlying earnings totaled $8.8 billion or $2.09 per share &mdash; the metric Woods emphasized during the morning earnings call.",
            "Free cash flow dropped sharply to $2.7 billion in the quarter, down from $8.8 billion in Q1 2025. The decline reflected working-capital effects from Middle East trading-timing disruptions and elevated capital expenditure. Despite the cash flow drop, the company returned $9.2 billion to shareholders during the quarter through $4.3 billion in dividends and $4.9 billion in share buybacks.",
            "Other operational highlights included first LNG production from the Golden Pass facility in March, which is expected to add roughly 5% to U.S. LNG export capacity once Train 1 reaches full output. The company&rsquo;s Upstream segment reported earnings of $5.74 billion, down 15% from $6.76 billion in the year-ago period. Excluding external disruptions in the Middle East, Kazakhstan, and a Permian winter storm, Upstream production grew 8% year-over-year.",
            "Shares of ExxonMobil were modestly higher in pre-market trading following the release. For continuing market coverage, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices</a>, <a href=\"../markets.html\" style=\"color:var(--blue);text-decoration:none\">markets dashboard</a>, and <a href=\"../articles/chevron-q1-2026-biggest-earnings-beat-since-2020-on-record-production.html\" style=\"color:var(--blue);text-decoration:none\">Chevron&rsquo;s Q1 results</a>.",
        ],
        "related": [
            ("Chevron Posts Biggest Earnings Beat Since 2020 on Record Production", "chevron-q1-2026-biggest-earnings-beat-since-2020-on-record-production"),
            ("Iran Sends Updated Peace Proposal Through Pakistan; Trump 'Not Satisfied'", "iran-sends-updated-peace-proposal-through-pakistan-trump-not-satisfied"),
            ("Trump Briefed on Expanded Iran Military Options as Crude Hit 4-Year High", "trump-briefed-on-expanded-iran-military-options-as-crude-hit-4-year-high"),
        ],
    },
    {
        "slug": "chevron-q1-2026-biggest-earnings-beat-since-2020-on-record-production",
        "title_variants": [
            "Chevron Posts Biggest Earnings Beat Since 2020 on Record Production",
            "Chevron Q1 Adj EPS $1.41 Beats $0.95; Production Up 15% YoY",
            "Chevron Earnings Beat Largest Since October 2020 as Output Climbs",
            "Chevron Q1 2026: $1.41 Adjusted EPS, Production Up 15%",
            "Chevron CVX Q1 Beats Big on Record Production Despite $2.9B Hedge Charge",
        ],
        "display_title": "Chevron Posts Biggest Earnings Beat Since 2020 on Record Production",
        "category": "Company News",
        "category_url": "../category/company-news.html",
        "date": "May 1, 2026",
        "iso_date": "2026-05-01T07:30:00-04:00",
        "section": "Company News",
        "read_time": "4 min",
        "meta_desc": "Chevron reported Q1 2026 adjusted EPS of $1.41 versus a $0.95 estimate — its biggest earnings beat since October 2020. GAAP profit was $2.2 billion / $1.11 per share after a $2.9B charge tied to financial hedges. Production rose 15% YoY to 3.9 million bpd.",
        "keywords": "Chevron earnings, CVX Q1 2026, Chevron production, oil major earnings, financial hedges, Hess arbitration, Mike Wirth",
        "paragraphs": [
            "Chevron reported first-quarter 2026 results on Friday, May 1, posting its biggest earnings beat since October 2020 as record production and elevated crude prices drove a strong quarter. Adjusted earnings reached $1.41 per share, beating Wall Street consensus of $0.95 by 49% and marking the largest beat in more than five years.",
            "On a GAAP basis, Chevron reported net income of $2.2 billion, or $1.11 per share, down from $3.5 billion or $2.00 per share in the year-earlier period. The reported figure included a $2.9 billion charge related to financial hedges &mdash; positions the company had taken to lock in revenue at lower price levels that became significantly out-of-the-money once crude rallied. Excluding the hedge charge and identified items, the underlying business performed substantially better than the headline.",
            "Total revenue came in at $48.61 billion, missing analyst estimates of $52.1 billion. The miss reflected the timing of certain trading-related items rather than fundamental business weakness; CFO Eimear Bonner noted on the earnings call that &ldquo;our underlying production and refining margins were materially better than the topline suggests.&rdquo;",
            "Production was the headline operational story. Total oil-equivalent production rose 15% year-over-year to roughly 3.9 million barrels per day, up from 3.4 million bpd in the year-earlier period. Growth was driven by strong Permian Basin and Gulf of Mexico performance plus contributions from the Tengiz expansion in Kazakhstan, which is now operating near nameplate capacity following last year&rsquo;s ramp.",
            "Chevron&rsquo;s production segment posted profit of $3.9 billion, a modest 4% increase over $3.8 billion in the year-ago period. The company&rsquo;s relatively lower exposure to Middle East operations cushioned the quarter compared to ExxonMobil, which reported the same morning that disruptions had pushed Q1 net income to a five-year low.",
            "CEO Mike Wirth, on the earnings call, reiterated the company&rsquo;s capital discipline and dividend commitments. The Hess arbitration case &mdash; which has been pending at the International Chamber of Commerce since early 2025 &mdash; remains without a final decision; Wirth noted Chevron continues to expect a favorable outcome.",
            "Shares of Chevron were higher in pre-market trading following the release. For continuing coverage, see our <a href=\"../articles/exxonmobil-q1-2026-profit-falls-to-5-year-low-but-beats-estimates.html\" style=\"color:var(--blue);text-decoration:none\">ExxonMobil&rsquo;s Q1 results</a>, <a href=\"../markets.html\" style=\"color:var(--blue);text-decoration:none\">markets dashboard</a>, and <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices</a>.",
        ],
        "related": [
            ("ExxonMobil Q1 Profit Falls to 5-Year Low at $4.2B Despite Beating Estimates", "exxonmobil-q1-2026-profit-falls-to-5-year-low-but-beats-estimates"),
            ("ConocoPhillips Q1 Earnings Slip as Output Falls", "conocophillips-completes-marathon-oil-integration-synergies"),
            ("Iran Sends Updated Peace Proposal Through Pakistan; Trump 'Not Satisfied'", "iran-sends-updated-peace-proposal-through-pakistan-trump-not-satisfied"),
        ],
    },
    {
        "slug": "us-gas-average-surges-to-439-up-25-cents-in-three-days",
        "title_variants": [
            "U.S. Gas Average Surges to $4.39, Up 25 Cents in Three Days",
            "AAA: National Gas Average Hits $4.392, Highest Since July 2022",
            "Gas Prices Spike 25 Cents in Three Days as Crude Pass-Through Hits Pump",
            "U.S. Pump Prices Reach $4.39, Highest in Nearly Four Years",
        ],
        "display_title": "U.S. Gas Average Surges to $4.39, Up 25 Cents in Three Days",
        "category": "Gas Prices",
        "category_url": "../category/gas-prices.html",
        "date": "May 1, 2026",
        "iso_date": "2026-05-01T09:00:00-04:00",
        "section": "Gas Prices",
        "read_time": "4 min",
        "meta_desc": "AAA reported Friday May 1 that the U.S. national average for regular gasoline reached $4.392 per gallon — the highest since July 2022 and up 25 cents in three days. Michigan spiked to $4.86 on a Midwest refinery issue; California averages $6.45.",
        "keywords": "AAA gas prices, U.S. national average, gas prices May 2026, Michigan gas prices, refinery outage, California gas prices, retail gasoline",
        "paragraphs": [
            "The U.S. national average for a gallon of regular gasoline reached $4.392 on Friday, May 1, 2026, according to AAA &mdash; the highest level recorded since July 2022. The new high reflects a roughly 25-cent jump over the past three days alone, capping a multi-week rally tied to the ongoing closure of the Strait of Hormuz and the conflict&rsquo;s effect on global crude prices.",
            "AAA spokesperson Morgan Dean called the recent move &ldquo;one of the fastest run-ups in years,&rdquo; noting that the price increases come during a period when AAA would typically expect upward pressure from spring travel demand even without the geopolitical shock. &ldquo;Outside of the Iran conflict, summer vacation will be here before you know it. Higher demand at the pumps usually creates higher prices.&rdquo;",
            "The Midwest is leading the spike. Michigan&rsquo;s state average reached $4.86 per gallon Friday morning, up 28 cents in a single week, with authorities pointing to an unrelated refinery issue in Indiana compounding the broader pass-through from crude. Patrick De Haan of GasBuddy called it &ldquo;a perfect storm of circumstances, creating one of the fastest price run-ups in years.&rdquo; The Chicago metropolitan area is now averaging $5.05 per gallon. Parts of California are seeing averages near $6.45.",
            "Retail prices typically lag wholesale crude by 7 to 14 days as refiner acquisition costs work through the supply chain. With WTI having held above $100 per barrel for a sustained period and Brent above $108, the upward pressure on retail is expected to continue for at least another 1-2 weeks even if crude stabilizes. Diesel reached $6.029 per gallon nationally &mdash; near record levels and a meaningful headwind for trucking and food-distribution costs.",
            "Some states remain notably below the national average. Oklahoma is the cheapest at roughly $3.56 per gallon, followed by Mississippi and Kansas. Texas averages around $3.73 despite hosting many of the country&rsquo;s largest refineries; the gap reflects state-tax differentials more than supply differences. The full state-by-state ranking is updated daily on our <a href=\"../category/gas-prices.html\" style=\"color:var(--blue);text-decoration:none\">U.S. gas prices dashboard</a>.",
            "EIA data for the week ending April 24 showed gasoline demand at 8.94 million barrels per day, up modestly from 8.81 million the previous week. Total domestic gasoline supply remains tight at 233.4 million barrels, below the five-year seasonal average. Refiner crack spreads (the spread between crude and refined product prices) remain near multi-year highs, signaling that refineries are running aggressively to supply summer-blend demand even as crude costs climb.",
            "For state-level pricing, see our <a href=\"../category/gas-prices.html\" style=\"color:var(--blue);text-decoration:none\">U.S. gas prices dashboard</a>; for crude pricing, see the <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">oil price dashboard</a>.",
        ],
        "related": [
            ("Iran Sends Updated Peace Proposal Through Pakistan; Trump 'Not Satisfied'", "iran-sends-updated-peace-proposal-through-pakistan-trump-not-satisfied"),
            ("Trump Briefed on Expanded Iran Military Options as Crude Hit 4-Year High", "trump-briefed-on-expanded-iran-military-options-as-crude-hit-4-year-high"),
            ("U.S. Gas Average Hits $4.14, Highest in Nearly Four Years", "us-gas-average-hits-414-highest-in-nearly-four-years"),
        ],
    },
]


def build_news_keywords(s):
    return s["keywords"]


def render_article(s):
    title_safe = s["display_title"].replace('&', '&amp;').replace("'", '&rsquo;')
    paragraphs = "\n          ".join(f"<p>{p}</p>" for p in s["paragraphs"])
    related_items = "\n            ".join(
        f'<li><a href="{slug}.html" style="color:var(--blue);text-decoration:none">{title}</a></li>'
        for title, slug in s["related"]
    )
    cat_label = s["category"]
    word_count = sum(len(p.split()) for p in s["paragraphs"])
    headline_safe = s["display_title"].replace('"', '\\"')[:110]
    desc_safe = s["meta_desc"].replace('"', '\\"')[:500]
    canonical = f'https://www.energypricestoday.com/articles/{s["slug"]}.html'

    news_schema = (
        '<script type="application/ld+json">'
        '{"@context":"https://schema.org","@type":"NewsArticle",'
        f'"headline":"{headline_safe}",'
        f'"description":"{desc_safe}",'
        f'"datePublished":"{s["iso_date"]}",'
        f'"dateModified":"{s["iso_date"]}",'
        '"author":{"@type":"NewsMediaOrganization","name":"EnergyPricesToday","url":"https://www.energypricestoday.com"},'
        '"image":["https://www.energypricestoday.com/images/og-image.png"],'
        f'"articleSection":"{s["section"]}",'
        f'"wordCount":{word_count},'
        f'"mainEntityOfPage":{{"@type":"WebPage","@id":"{canonical}"}},'
        '"isAccessibleForFree":true,'
        '"publisher":{"@type":"NewsMediaOrganization","name":"EnergyPricesToday.com","url":"https://www.energypricestoday.com","logo":{"@type":"ImageObject","url":"https://www.energypricestoday.com/images/logo.png","width":674,"height":130}}}'
        '</script>'
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','957762016897581');fbq('track','PageView');</script><noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=957762016897581&ev=PageView&noscript=1"/></noscript>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{title_safe} | EnergyPricesToday</title>
  <meta name="description" content="{s['meta_desc']}">
  <link rel="canonical" href="{canonical}">
  <meta name="news_keywords" content="{s['keywords']}">
  <meta name="keywords" content="{s['keywords']}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="googlebot-news" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title_safe} | EnergyPricesToday">
  <meta property="og:description" content="{s['meta_desc']}">
  <meta property="article:published_time" content="{s['iso_date']}">
  <meta property="article:modified_time" content="{s['iso_date']}">
  <meta property="article:author" content="EnergyPricesToday Editorial">
  <meta property="article:section" content="{s['section']}">
  <meta property="article:tag" content="{s['section']}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="EnergyPricesToday.com">
  <meta property="og:image" content="https://www.energypricestoday.com/images/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@energypricestoday">
  <meta name="twitter:title" content="{title_safe[:70]}">
  <meta name="twitter:description" content="{s['meta_desc'][:200]}">
  <meta name="twitter:image" content="https://www.energypricestoday.com/images/og-image.png">
  <link rel="alternate" type="application/rss+xml" title="EnergyPricesToday RSS Feed" href="../feed.xml">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap"></noscript>
  <link rel="stylesheet" href="../css/styles.css?v=17">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-FXGF8HZFWL"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-FXGF8HZFWL");</script>
  <link rel="icon" type="image/x-icon" href="../images/favicon.ico?v=2">
  <link rel="icon" type="image/svg+xml" href="../images/favicon.svg?v=2">
  <link rel="icon" type="image/png" sizes="16x16" href="../images/favicon-16x16.png?v=2">
  <link rel="icon" type="image/png" sizes="32x32" href="../images/favicon-32x32.png?v=2">
  <link rel="icon" type="image/png" sizes="48x48" href="../images/favicon-48x48.png?v=2">
  <link rel="apple-touch-icon" sizes="180x180" href="../images/apple-touch-icon.png?v=2">
  {news_schema}
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
        <div class="article-meta" style="margin:14px 0 24px"><span>EnergyPricesToday Editorial</span><span>{s['date']}</span><span>{s['read_time']} read</span></div>
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
  <script src="../js/data.js?v=17"></script>
  <script src="../js/article-slugs.js?v=17"></script>
  <script src="../js/main.js?v=17"></script>
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
