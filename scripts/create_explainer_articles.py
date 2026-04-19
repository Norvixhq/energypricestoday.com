#!/usr/bin/env python3
"""
create_explainer_articles.py — Generate 5 high-intent explainer articles
and integrate them into the site's article system.

Each article:
  - 800-1,200 words of original evergreen content
  - Proper heading hierarchy (h1 + multiple h2s)
  - FAQ section with schema.org FAQPage structured data
  - Continue Reading + Related Coverage blocks (matches site template)
  - Article tags at bottom
  - Breadcrumb navigation (single nav, not duplicated)

Integration steps:
  - Write HTML files to articles/
  - Append entries to article-slugs.js via rebuild_slug_map.py
  - Add slugs to sitemap.xml
"""

import os
import html as htmllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

# ================================================================
# Article content — each is a dict with all metadata + body
# ================================================================

ARTICLES = [

    # ============== Article 1 ==============
    {
        "slug": "oil-price-per-barrel-today-wti-brent-explained",
        "title_tag": "Oil Price Per Barrel Today — WTI & Brent Explained | EnergyPricesToday",
        "h1": "What's the Oil Price Per Barrel Today? WTI & Brent Explained",
        "meta_desc": "What's the oil price per barrel today? A plain-English explainer on WTI, Brent, why there are two prices, and what moves crude oil per barrel.",
        "category_slug": "oil-prices",
        "category_label": "Oil Prices",
        "category_href": "../oil-prices.html",
        "schema_headline": "What Is the Oil Price Per Barrel Today? WTI and Brent Explained",
        "continue_reading_slug": "wti-vs-brent-difference-why-it-matters",
        "related_slugs": [
            "wti-vs-brent-difference-why-it-matters",
            "wti-futures-curve-flips-to-backwardation-through-december-2026",
            "eia-reports-second-consecutive-weekly-crude-draw-cushing-stocks-below-5-year-ave",
            "april-206k-bpd-increase-proceeds",
        ],
        "tags": [
            ("Oil Prices", "../oil-prices.html"),
            ("Markets", "../markets.html"),
            ("Geopolitics", "../category/geopolitics.html"),
        ],
        "body_html": """
        <p>If you're asking what the oil price per barrel is today, the honest answer is: it depends on which barrel. Crude oil trades continuously in global markets and the price changes every few seconds, but the two benchmarks most people mean are <strong>WTI</strong> (West Texas Intermediate, the U.S. benchmark) and <strong>Brent</strong> (the international benchmark, named after a North Sea oil field). For the live price right now, see our <a href="../oil-prices.html">oil prices dashboard</a>, which updates every five minutes.</p>

        <p>In the spring of 2026, WTI has been trading in a wide range — crashing 11% on news the <a href="strait-of-hormuz-why-this-chokepoint-controls-global-oil-prices.html">Strait of Hormuz</a> would reopen, then rebounding sharply when Iran <a href="hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade.html">reversed course and re-closed the strait</a>. Brent has traded a few dollars above WTI throughout. That gap — called the Brent-WTI spread — is itself a tradable instrument and a signal about shipping conditions.</p>

        <h2>What "Per Barrel" Actually Means</h2>
        <p>A barrel of oil is 42 U.S. gallons — roughly 159 liters. The figure is a legacy of the 1860s Pennsylvania oil fields, where producers shipped crude in 42-gallon wooden barrels originally used for whale oil and wine. The physical barrel is long gone, but the unit stuck. Every time a financial headline references "oil at $94 per barrel," that's 42 gallons of crude, priced in U.S. dollars, at a specific delivery location.</p>

        <p>The delivery location matters. WTI's price is set for crude delivered to <strong>Cushing, Oklahoma</strong>, a pipeline hub in the middle of the country. Brent's price references crude produced in the North Sea, typically delivered via tanker. Because moving oil around the world involves pipelines, tankers, storage, and insurance, the same grade of crude can trade at meaningfully different prices in different places on the same day.</p>

        <h2>Why There Are Two Main Prices</h2>
        <p>WTI and Brent exist because the global oil market is not one market — it's many regional markets loosely connected by shipping. WTI is light and sweet (low sulfur, easy to refine), ideal for making gasoline, and mostly stays in North America. Brent is the benchmark for about two-thirds of the world's crude trade, covering cargoes from Europe, Africa, and much of the Middle East. We've written a full explainer on the <a href="wti-vs-brent-difference-why-it-matters.html">differences between WTI and Brent</a> and why the spread matters.</p>

        <p>A third benchmark, <strong>Dubai/Oman</strong>, sets the price for sour crude exported to Asia. You'll see it quoted less often in consumer media, but it drives the oil price most Asian refiners actually pay.</p>

        <h2>What Moves the Oil Price Per Barrel</h2>
        <p>Five forces explain most daily price action:</p>

        <p><strong>Supply from OPEC+.</strong> The 23-nation producer group controls roughly 40% of world crude output. Small changes in their quota — even 206,000 barrels per day <a href="april-206k-bpd-increase-proceeds.html">as announced for April</a> — can shift prices by several dollars. We explain the group in detail in <a href="what-is-opec-plus-how-it-affects-oil-prices.html">What Is OPEC+</a>.</p>

        <p><strong>Demand from China, India, and the U.S.</strong> These three countries consume more than a third of world oil. A Chinese manufacturing slowdown or an American summer driving season can move the price per barrel by $5 or more over a few weeks.</p>

        <p><strong>Geopolitics.</strong> Roughly 20% of seaborne crude passes through the Strait of Hormuz. When that chokepoint is threatened — as it is right now — traders price in a "risk premium" of anywhere from $5 to $25 per barrel, depending on how serious the threat looks.</p>

        <p><strong>The U.S. dollar.</strong> Oil is priced in dollars worldwide. When the dollar strengthens, the same barrel costs more in other currencies, which tends to suppress demand and push the oil price down. Most of the time this is a minor factor, but during currency shocks it can move prices more than supply news.</p>

        <p><strong>U.S. inventory data.</strong> Every Wednesday morning the U.S. Energy Information Administration publishes crude stock levels. A <a href="eia-reports-second-consecutive-weekly-crude-draw-cushing-stocks-below-5-year-ave.html">larger-than-expected draw</a> usually sends prices higher; an unexpected build pushes them down. The market reacts within seconds.</p>

        <h2>Reading Today's Oil Price</h2>
        <p>A typical quote looks like this: <em>"WTI crude up $1.42, or 1.5%, to $94.62 per barrel."</em> That tells you three things — the benchmark (WTI), the absolute change since the prior close, and the percentage change. The price is for the <em>front-month</em> futures contract, meaning oil scheduled for delivery in the next calendar month. Different delivery months trade at different prices, which is why you'll sometimes see references to the "futures curve."</p>

        <p>When the front-month price is higher than later-month prices, the curve is in <em>backwardation</em>, which usually means physical supply is tight. When later months cost more than the front month, it's <em>contango</em>, which usually signals oversupply. The WTI curve has been <a href="wti-futures-curve-flips-to-backwardation-through-december-2026.html">in backwardation through December 2026</a> for much of this year.</p>

        <h2>Frequently Asked Questions</h2>

        <h3>Why is oil priced in barrels instead of gallons or liters?</h3>
        <p>Historical convention. The 42-gallon barrel became the U.S. standard during the 1870s Pennsylvania oil boom and was formalized by the U.S. Geological Survey in 1882. The industry never converted to metric, and the unit is now locked into every major futures contract.</p>

        <h3>Does the "oil price per barrel" include shipping?</h3>
        <p>No. The quoted benchmark price is at a specific delivery point — Cushing for WTI, the North Sea for Brent. A refinery on the U.S. Gulf Coast pays WTI plus pipeline tariffs. A refinery in India pays Brent or Dubai plus shipping, insurance, and port fees. The headline number is just a reference.</p>

        <h3>How often does the oil price per barrel change?</h3>
        <p>Continuously during trading hours. Electronic futures markets are open roughly 23 hours a day, five days a week. Prices update every second or two. Most consumer websites — including ours — poll the price feed every few minutes to keep displays current without overwhelming the data provider.</p>

        <h3>What's the highest price oil has ever reached?</h3>
        <p>Brent crude hit an intraday peak of $147.50 per barrel in July 2008, before the global financial crisis collapsed demand and sent prices below $40 within six months. On an inflation-adjusted basis, oil has briefly traded higher in the early 1980s and during parts of the 1970s oil embargoes.</p>
""",
    },

    # ============== Article 2 ==============
    {
        "slug": "wti-vs-brent-difference-why-it-matters",
        "title_tag": "WTI vs Brent: What's the Difference & Why It Matters | EnergyPricesToday",
        "h1": "WTI vs Brent: What's the Difference and Why It Matters",
        "meta_desc": "WTI vs Brent crude oil: what separates the two benchmarks, how the Brent-WTI spread is calculated, and why the difference matters for gasoline and markets.",
        "category_slug": "oil-prices",
        "category_label": "Oil Prices",
        "category_href": "../oil-prices.html",
        "schema_headline": "WTI vs Brent Crude Oil: Differences Between the Two Main Oil Benchmarks",
        "continue_reading_slug": "oil-price-per-barrel-today-wti-brent-explained",
        "related_slugs": [
            "oil-price-per-barrel-today-wti-brent-explained",
            "what-is-opec-plus-how-it-affects-oil-prices",
            "wti-futures-curve-flips-to-backwardation-through-december-2026",
            "oil-prices-whipsaw-on-hormuz-reversal-wti-recovers-from-fridays-11-plunge",
        ],
        "tags": [
            ("Oil Prices", "../oil-prices.html"),
            ("Markets", "../markets.html"),
            ("Company News", "../category/company-news.html"),
        ],
        "body_html": """
        <p>WTI and Brent are the two most widely quoted oil prices on earth. They track two different kinds of crude, produced in two different places, delivered under two different sets of contract terms — yet they move together most of the time. The gap between them, called the <strong>Brent-WTI spread</strong>, tells you something useful about global shipping, U.S. pipeline capacity, and where refiners are willing to pay up for physical barrels. For the live price of both right now, check our <a href="../oil-prices.html">oil prices dashboard</a>.</p>

        <h2>What Is WTI?</h2>
        <p>WTI stands for <strong>West Texas Intermediate</strong>. It's a light, sweet crude oil produced mostly in the Permian Basin of Texas and New Mexico, plus smaller volumes from Oklahoma, Wyoming, and North Dakota. "Light" refers to low density (it flows easily); "sweet" means low sulfur content — under 0.42% by weight — which makes it cheaper and easier to refine into gasoline and diesel.</p>

        <p>The WTI futures contract is traded on the New York Mercantile Exchange (CME Group) and settles at <strong>Cushing, Oklahoma</strong>. Cushing is the pipeline junction of North American oil — a small town with tank farms holding tens of millions of barrels of crude, connected by pipelines to the Gulf Coast, the Midwest, and Canada. When you see the WTI price quoted, it's the cost of delivering a barrel of WTI-grade crude to a Cushing tank.</p>

        <h2>What Is Brent?</h2>
        <p>Brent is named for the original North Sea oil field that fed the benchmark in the 1970s — though the actual Brent field itself has mostly depleted. Today the benchmark reflects a basket of North Sea crudes: Brent, Forties, Oseberg, Ekofisk, and Troll ("BFOET"). These grades are also light and sweet, though slightly heavier and more sulfurous than WTI on average.</p>

        <p>Brent futures trade on ICE (Intercontinental Exchange) in London. Critically, Brent is a <strong>waterborne</strong> benchmark — contracts settle via physical tanker cargoes loaded at specific North Sea terminals. That difference matters: Brent more accurately reflects the global seaborne oil trade, because it moves the same way most of the world's exported crude does.</p>

        <h2>How the Two Differ at a Glance</h2>
        <p>At refinery level, the chemistry is similar enough that either can be processed into gasoline, diesel, and jet fuel with comparable economics. The key differences are logistical. WTI is fundamentally a <strong>landlocked</strong> crude — the Cushing delivery hub is 500 miles from the Gulf Coast export terminals. Brent is inherently <strong>seaborne</strong>, loaded onto tankers the moment it leaves the platform. That single fact drives much of the price difference.</p>

        <p>Another distinction: roughly two-thirds of globally traded oil is priced off Brent, including nearly all African, European, and much Middle Eastern crude. WTI is the reference for U.S. and some Canadian grades, and for some Latin American crudes sold into the U.S. market. Asian refiners generally price off Dubai/Oman, a third benchmark not covered here.</p>

        <h2>Why the Brent-WTI Spread Matters</h2>
        <p>Historically, WTI traded slightly above Brent because WTI's lower sulfur content and ease of refining commanded a premium. After the U.S. shale boom of the 2010s, that flipped — suddenly there was too much WTI crude trapped inland without enough pipeline capacity to reach export terminals, and Brent traded at a premium that sometimes exceeded $20 per barrel.</p>

        <p>Today the spread usually sits in the $3-to-$7 range with Brent above WTI, but it widens sharply during shipping disruptions. When the <a href="hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade.html">Strait of Hormuz tensions escalate</a>, Brent typically spikes faster than WTI because Brent reflects the actual cost of moving oil by sea through contested waterways. WTI, delivered to a tank in Oklahoma, is insulated from maritime risk.</p>

        <p>Traders watch the spread for three reasons. First, it signals global shipping stress — a widening Brent premium usually means tanker freight rates are rising too. Second, it affects U.S. export economics. When the spread is wide enough, it becomes profitable for U.S. producers to ship crude from Houston to European or Asian refiners, which helps rebalance the market. Third, it's the basis for hundreds of billions of dollars of hedging positions held by refiners, airlines, and trading houses.</p>

        <h2>Why Consumers Should Care</h2>
        <p>Most U.S. drivers pay attention to WTI because American refiners buy WTI-referenced crude and the pump price follows with a two-to-three-week lag. But the U.S. Gulf Coast also imports and exports large volumes of oil priced off Brent, and West Coast refineries — especially California's — import significant volumes of Alaskan, Saudi, and Ecuadorian crude, most of which is priced off Brent or Dubai benchmarks.</p>

        <p>The practical rule: if WTI moves $5 per barrel, expect U.S. pump prices to move roughly 10-12 cents per gallon over the following two weeks. When Brent moves and WTI doesn't, California and East Coast gas prices react faster than the national average, while interior Midwest states stay flatter.</p>

        <h2>Frequently Asked Questions</h2>

        <h3>Is WTI or Brent the "real" oil price?</h3>
        <p>Neither. They're benchmarks, not a single price. Both are real prices for real barrels of crude — just in different places. Most news coverage defaults to whichever benchmark is most relevant to the audience: WTI for American readers, Brent for European and most international coverage.</p>

        <h3>Why does Brent usually trade higher than WTI?</h3>
        <p>Because Brent reflects what the global seaborne market will pay, and that market has had tighter supply balance for most of the past decade. Also, Brent's delivery terms (tanker loading in the North Sea) are closer to what international buyers actually need; WTI requires additional shipping from Cushing to coastal terminals before export.</p>

        <h3>Can the Brent-WTI spread go negative?</h3>
        <p>Yes, and historically WTI did trade above Brent for decades before 2011. It's rare now because U.S. shale production keeps WTI abundant at Cushing, but a major Gulf Coast export disruption or a sudden U.S. supply shock could flip it again.</p>

        <h3>Which benchmark moves first on news?</h3>
        <p>It depends on the news. U.S. inventory surprises from the EIA move WTI first. Middle East geopolitical events move Brent first. OPEC+ decisions usually move both almost simultaneously, with Brent reacting a fraction of a second earlier.</p>
""",
    },

    # ============== Article 3 ==============
    {
        "slug": "how-are-gas-prices-set-crude-oil-to-pump",
        "title_tag": "How Are Gas Prices Set? From Crude Oil to the Pump | EnergyPricesToday",
        "h1": "How Are Gas Prices Set? From Crude Oil to the Pump",
        "meta_desc": "How are gas prices set? The full path from crude oil to the pump: refining, distribution, taxes, and why prices vary by state and season. Plain-English explainer.",
        "category_slug": "gas-prices",
        "category_label": "Gas Prices",
        "category_href": "../category/gas-prices.html",
        "schema_headline": "How Are Gas Prices Set? The Full Chain From Crude Oil to the Pump",
        "continue_reading_slug": "california-gas-prices-hit-518-as-state-specific-regulations-add-costs",
        "related_slugs": [
            "california-gas-prices-hit-518-as-state-specific-regulations-add-costs",
            "gas-prices-continue-slide-aaa-national-falls-to-4076",
            "gulf-coast-refinery-margins-improve-as-crack-spreads-widen",
            "oil-price-per-barrel-today-wti-brent-explained",
        ],
        "tags": [
            ("Gas Prices", "../category/gas-prices.html"),
            ("Oil Prices", "../oil-prices.html"),
            ("Markets", "../markets.html"),
        ],
        "body_html": """
        <p>If you've ever wondered why the price on the pump changes from week to week, or why your cousin in Texas pays a dollar less per gallon than you do in California, the short answer is that gas prices are built from four stacked costs: <strong>crude oil, refining, distribution and marketing, and taxes</strong>. Each of these moves independently, and the mix is different in every state. Our <a href="../category/gas-prices.html">gas prices page</a> has today's AAA national average and the current breakdown by state.</p>

        <p>Here's how the chain actually works, in the order the cost builds up.</p>

        <h2>1. Crude Oil — Usually the Biggest Single Cost</h2>
        <p>On a typical day, the raw crude oil in a gallon of gasoline accounts for about <strong>50-60% of the pump price</strong>. When crude is cheap, it can drop as low as 40%; when crude spikes — as it did during the <a href="oil-prices-whipsaw-on-hormuz-reversal-wti-recovers-from-fridays-11-plunge.html">recent Hormuz volatility</a> — it can exceed 65%. A barrel of oil is 42 gallons, so if WTI crude is trading at $84 per barrel, the raw input cost is about $2.00 per gallon before anyone has done anything to it. See our companion piece on <a href="oil-price-per-barrel-today-wti-brent-explained.html">how oil prices are quoted per barrel</a>.</p>

        <p>This is why pump prices follow crude prices with a lag. Refiners buy crude on contracts that lock in delivery two to six weeks ahead. When WTI drops sharply, it takes roughly two to three weeks for the cheaper input to work through the refining system and show up at retail. The same lag operates in reverse when crude spikes.</p>

        <h2>2. Refining — The Step That Converts Oil Into Gasoline</h2>
        <p>Refineries take crude oil and fractionally distill it into gasoline, diesel, jet fuel, heating oil, and petrochemical feedstocks. The margin refineries earn — the difference between what they pay for crude and what they sell the finished product for — is called the <strong>crack spread</strong>. It usually accounts for 10-20% of the pump price.</p>

        <p>Crack spreads widen when refining capacity is tight, which happens in two main situations: planned maintenance seasons (spring and fall), and unplanned outages from storm damage, fires, or mechanical failures. Gulf Coast refineries in particular set the tone for U.S. gasoline pricing, and we track that closely in our coverage of <a href="gulf-coast-refinery-margins-improve-as-crack-spreads-widen.html">Gulf Coast refinery margins</a>.</p>

        <p>The other refining variable is <strong>fuel specification</strong>. The U.S. does not have a single national gasoline formula. California, the Northeast, and certain metropolitan areas require special reformulated gasoline (RFG) blends that burn cleaner but cost more to produce. California's CARB gasoline is the most expensive to refine in the country — one of the main reasons <a href="california-gas-prices-hit-518-as-state-specific-regulations-add-costs.html">California gas prices regularly exceed $5.00 per gallon</a>.</p>

        <h2>3. Distribution and Marketing</h2>
        <p>Once gasoline leaves the refinery, it has to get to your neighborhood. Pipelines carry it most of the way, then tanker trucks deliver it to stations. Terminal storage, pipeline tariffs, truck transport, station rent, credit card fees, and retail margin together account for roughly <strong>10-15%</strong> of the pump price.</p>

        <p>Retail margins are thinner than people assume. Gas stations typically make 5-15 cents per gallon on fuel — most of their profit comes from the convenience store attached to the pumps. That's why gas stations are almost always paired with a c-store now; pure fuel retailing is barely profitable on its own.</p>

        <h2>4. Taxes</h2>
        <p>Every gallon of gasoline sold in the U.S. pays the federal fuel tax of <strong>18.4 cents per gallon</strong>, which has been unchanged since 1993 and funds the Highway Trust Fund. On top of that, every state adds its own tax, ranging from around 15 cents in Alaska to more than 60 cents in California and Pennsylvania. Some states also add environmental fees, underground storage tank fees, and cap-and-trade program costs.</p>

        <p>State taxes are the single biggest driver of why the pump price you pay in Texas is different from the one your cousin pays in California. The crude oil cost is the same; the refining cost is similar; the distribution cost is close. But the tax stack can differ by 45 cents or more per gallon between states.</p>

        <h2>Why Prices Vary by State</h2>
        <p>Combining everything above, four factors explain virtually all state-to-state variation:</p>

        <p><strong>State tax levels</strong> (explains roughly half of interstate variation). California, Pennsylvania, Illinois, Washington, and a handful of Northeast states sit at the high end. Oklahoma, Mississippi, Texas, Louisiana, and several Mountain West states sit at the low end.</p>

        <p><strong>Proximity to refineries</strong> (about a quarter). Gulf Coast states with dense refining capacity — Texas, Louisiana, Alabama, Mississippi — enjoy the cheapest gasoline in the country. The West Coast, isolated from the Gulf Coast refining complex, pays a persistent premium.</p>

        <p><strong>Unique fuel specifications</strong> (California and a few metro areas). California's CARB gasoline adds roughly 30-50 cents per gallon over standard grade. New York City, Chicago, and several other urban areas have their own seasonal specifications.</p>

        <p><strong>Local competition and density</strong> (the remainder). Areas with many stations within a few miles have tighter margins; isolated highway stops can charge more.</p>

        <h2>Why Summer Gas Costs More Than Winter</h2>
        <p>Summer-grade gasoline has a lower Reid vapor pressure, meaning it evaporates less in heat — required by EPA rules from June 1 to September 15 in most of the country. Producing the summer blend adds roughly 10-15 cents per gallon. Combine that with the traditional summer driving-season demand spike, and the May-to-September period is typically 30-50 cents per gallon more expensive than December-February.</p>

        <h2>Frequently Asked Questions</h2>

        <h3>If oil prices drop, why don't pump prices drop the next day?</h3>
        <p>Because the gasoline at your local station was refined from crude that was purchased two to six weeks ago. The tank truck that delivered it might have loaded at a terminal priced the day before, but refiners can't reprice stock they've already committed to. Expect pump prices to respond to crude moves over a two-to-three-week window.</p>

        <h3>Are gas stations price-gouging when crude drops?</h3>
        <p>Rarely. The bigger issue is asymmetric response: retailers often raise prices quickly on crude spikes (to protect future margin) and lower them slowly on crude drops (to recover prior margin erosion). It feels like gouging but usually reflects rational risk-management on 5-to-15-cent retail margins.</p>

        <h3>Why is gas cheaper in Texas than in California?</h3>
        <p>Three reasons, in order: California's state taxes and environmental fees add 60+ cents versus Texas's roughly 20 cents; California requires a more expensive reformulated fuel blend; and California is geographically isolated from Gulf Coast refining capacity. The <a href="california-gas-prices-hit-518-as-state-specific-regulations-add-costs.html">California premium</a> is structural, not a temporary gouge.</p>

        <h3>Does the price of diesel track gasoline?</h3>
        <p>Not as closely as you'd think. Diesel is a middle distillate, which also produces heating oil and jet fuel. When winter heating demand spikes or when trucking activity surges, diesel can move independently of gasoline. Diesel currently trades at a notable premium to regular gasoline.</p>
""",
    },

    # ============== Article 4 ==============
    {
        "slug": "what-happens-if-strait-of-hormuz-closes",
        "title_tag": "What Happens If the Strait of Hormuz Closes? | EnergyPricesToday",
        "h1": "What Happens If the Strait of Hormuz Closes?",
        "meta_desc": "What happens if the Strait of Hormuz closes: hour-by-hour, week-by-week impact on oil prices, global shipping, gasoline, and the countries most exposed.",
        "category_slug": "geopolitics",
        "category_label": "Geopolitics",
        "category_href": "../category/geopolitics.html",
        "schema_headline": "What Happens If the Strait of Hormuz Closes? A Scenario Analysis",
        "continue_reading_slug": "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade",
        "related_slugs": [
            "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade",
            "strait-of-hormuz-why-this-chokepoint-controls-global-oil-prices",
            "strait-of-malacca",
            "what-is-opec-plus-how-it-affects-oil-prices",
            "irgc-gunboats-fire-on-two-indian-flagged-merchant-ships-in-strait-of-hormuz",
        ],
        "tags": [
            ("Geopolitics", "../category/geopolitics.html"),
            ("Oil Prices", "../oil-prices.html"),
            ("Gas Prices", "../category/gas-prices.html"),
        ],
        "body_html": """
        <p>The Strait of Hormuz carries roughly 20 million barrels of crude oil per day — about a fifth of the world's seaborne oil and nearly a third of all seaborne petroleum products. It's the single most important chokepoint in the global energy system. If it closes, even briefly, the consequences ripple through oil prices, gasoline costs, shipping, inflation, and eventually recession risk. Follow the real-time situation on our <a href="../category/geopolitics.html">geopolitics dashboard</a>.</p>

        <p>Here's what would actually happen, hour by hour and then week by week. This is a scenario analysis based on historical precedents, IEA and EIA modeling, and current commodity market structure — not a prediction.</p>

        <h2>Why the Strait Matters</h2>
        <p>The Strait of Hormuz is 21 miles wide at its narrowest point, between Iran and the Musandam Peninsula of Oman. Every tanker carrying Saudi Arabian, Kuwaiti, Iraqi, Emirati, Qatari, or Iranian oil to Asia, Europe, or the Americas must pass through it. There are alternative routes for some of that oil — notably Saudi Arabia's East-West pipeline to the Red Sea and the UAE's pipeline to Fujairah — but those alternatives can handle at most 6-7 million barrels per day, less than a third of normal Hormuz flow. We cover the geography and strategic significance in detail in our <a href="strait-of-hormuz-why-this-chokepoint-controls-global-oil-prices.html">Strait of Hormuz explainer</a>.</p>

        <h2>Hours 0-48: The Price Shock</h2>
        <p>An actual closure — confirmed by insurance underwriters suspending coverage for transits — would move oil prices by $20 to $40 per barrel within hours. Brent would move faster than WTI because Brent is the seaborne benchmark and Hormuz is fundamentally a shipping problem. The Brent-WTI spread would widen dramatically; we've seen smaller versions of this pattern during the <a href="oil-prices-whipsaw-on-hormuz-reversal-wti-recovers-from-fridays-11-plunge.html">recent Hormuz volatility</a>.</p>

        <p>Asian buyers — Japan, South Korea, China, India — would start drawing down strategic reserves within 24 hours. The International Energy Agency's coordinated release mechanism would activate, freeing up to 4 million barrels per day from member-country stockpiles for as long as the crisis lasted. The U.S. Strategic Petroleum Reserve holds roughly 370 million barrels, enough to compensate for a full Hormuz disruption for about 18 days if released at maximum rate.</p>

        <p>Equity markets would react within the same 48 hours. Airlines, cruise operators, trucking, chemicals, and consumer discretionary sectors would sell off. Oil producers not dependent on Gulf exports — ExxonMobil, Chevron, ConocoPhillips, Canadian producers, Norwegian Equinor — would rally. The U.S. dollar would strengthen on safe-haven flows.</p>

        <h2>Days 3-7: Reality Sets In</h2>
        <p>By the first week, the shape of the closure would matter more than the closure itself. There are three main scenarios, each with very different outcomes:</p>

        <p><strong>Harassment without actual closure.</strong> This is what has unfolded in real time in mid-2026: Iran declares the strait closed, IRGC gunboats <a href="irgc-gunboats-fire-on-two-indian-flagged-merchant-ships-in-strait-of-hormuz.html">fire on some commercial vessels</a>, insurance rates spike, a few major shippers suspend transits, but most flow continues under heightened risk premium. Oil stays $15-25 higher than pre-crisis levels. This scenario can persist for weeks or months.</p>

        <p><strong>Partial physical closure.</strong> If Iran were to mine the strait or sink a tanker in the shipping lane, flow could drop 50-70% while the U.S. Fifth Fleet and allied navies clear the waterway. Historical minesweeping operations (including U.S. operations in 1987-88 during the Iran-Iraq tanker war) took weeks. Oil would settle in the $130-160 range and gasoline would spike 80-150 cents per gallon in the U.S.</p>

        <p><strong>Full sustained closure.</strong> This has never actually happened in the modern era and is considered unlikely because it would devastate Iran's own economy — Iran exports its own oil through the strait. In a worst-case scenario, oil could briefly touch $200+ per barrel and the global economy would enter recession.</p>

        <h2>Who Gets Hurt Most</h2>
        <p>Asia bears the highest direct exposure. China imports roughly 4-5 million barrels per day from the Persian Gulf. India, Japan, and South Korea combine for another 6-7 million barrels per day. A prolonged Hormuz closure would force these economies into rapid rationing, government subsidies, or recession.</p>

        <p>Europe is indirectly exposed because Brent-priced crude from North Africa and the North Sea would trade up in sympathy, and because European refineries cannot fully replace Middle Eastern medium-sour grades with the lighter crudes they could realistically source.</p>

        <p>The United States, counterintuitively, is relatively insulated. Domestic shale production plus Canadian imports cover roughly 90% of U.S. refinery demand. Gulf Coast refineries that currently import Middle Eastern crude could substitute more Canadian, Guyanese, and Brazilian barrels. The main U.S. impact would come through the global oil price — WTI would still rise sharply because all oil markets are linked — not through physical shortages.</p>

        <h2>Can Oil Flow Around the Strait?</h2>
        <p>Partially. Saudi Arabia's East-West pipeline (the Petroline) can move about 5 million barrels per day from eastern Saudi fields to Yanbu on the Red Sea, bypassing Hormuz. The UAE has a 1.5 million bpd pipeline to Fujairah on the Gulf of Oman. Iraq has some pipeline capacity to Turkey, though that route has its own political complications. Combined, these alternatives could carry roughly 6-7 million barrels per day — less than a third of normal Hormuz throughput.</p>

        <p>There is no realistic substitute for the remaining 13-14 million barrels per day. Qatar's LNG exports have no pipeline alternative at all. This is why a sustained Hormuz closure is considered the single largest oil supply risk in the world.</p>

        <h2>Frequently Asked Questions</h2>

        <h3>Has the Strait of Hormuz ever actually closed?</h3>
        <p>No, not fully. During the 1980s Iran-Iraq "tanker war," both sides attacked more than 400 commercial vessels transiting the strait, but traffic continued under U.S. Navy escort. The current situation involves threats and harassment, but the strait has not been physically sealed.</p>

        <h3>How long would it take to clear mines from the strait?</h3>
        <p>Historical minesweeping operations have taken two to six weeks for similar-size waterways. The U.S. Navy's mine countermeasures forces, combined with allied assets, would need to sweep both the main eastbound and westbound shipping lanes before insurers would restore coverage for commercial transits.</p>

        <h3>What would happen to U.S. gasoline prices?</h3>
        <p>A sustained Hormuz closure would push U.S. average gas prices up 80-150 cents per gallon over four to eight weeks, with California and Northeast states reacting faster than the interior. U.S. production would fully cover domestic demand, but the national average pump price tracks global crude, not just domestic supply.</p>

        <h3>Would the U.S. military intervene?</h3>
        <p>The U.S. Fifth Fleet is permanently headquartered in Bahrain specifically to ensure freedom of navigation through Hormuz, and keeping the strait open is considered a U.S. vital interest. Historical precedent — from the Reagan-era tanker escort operations to recent convoy operations in the Red Sea — suggests any closure attempt would draw direct U.S. military response within days.</p>
""",
    },

    # ============== Article 5 ==============
    {
        "slug": "what-is-opec-plus-how-it-affects-oil-prices",
        "title_tag": "What Is OPEC+? How It Affects Oil Prices | EnergyPricesToday",
        "h1": "What Is OPEC+ and How Does It Affect Oil Prices?",
        "meta_desc": "What is OPEC+? Who's in it, how it sets production quotas, and why its decisions move global oil prices. Plain-English explainer with current context.",
        "category_slug": "geopolitics",
        "category_label": "Geopolitics",
        "category_href": "../category/geopolitics.html",
        "schema_headline": "What Is OPEC+ and How Does It Affect Global Oil Prices?",
        "continue_reading_slug": "april-206k-bpd-increase-proceeds",
        "related_slugs": [
            "april-206k-bpd-increase-proceeds",
            "oil-price-per-barrel-today-wti-brent-explained",
            "wti-vs-brent-difference-why-it-matters",
            "what-happens-if-strait-of-hormuz-closes",
            "wti-futures-curve-flips-to-backwardation-through-december-2026",
        ],
        "tags": [
            ("Geopolitics", "../category/geopolitics.html"),
            ("Oil Prices", "../oil-prices.html"),
            ("Markets", "../markets.html"),
        ],
        "body_html": """
        <p>OPEC+ is the 23-nation producer alliance that controls roughly 40% of global oil production and a much larger share of world oil exports. When it raises or cuts production quotas, oil prices move — usually within minutes. Understanding how the group works is essential for understanding why the <a href="../oil-prices.html">oil price</a> does what it does on any given day.</p>

        <h2>What Does OPEC+ Stand For?</h2>
        <p>The "+" part is the key. OPEC — the Organization of the Petroleum Exporting Countries — was founded in 1960 by five countries: Saudi Arabia, Iran, Iraq, Kuwait, and Venezuela. It has since expanded to 12 members. OPEC was powerful through the 1970s and 1980s but lost pricing influence as non-OPEC producers like Russia, Mexico, Norway, and later the U.S. shale industry grew.</p>

        <p>OPEC+ was formed in late 2016 when OPEC (led by Saudi Arabia) reached a production-coordination deal with <strong>10 non-OPEC producers</strong>, the most important of which is Russia. Other OPEC+ non-OPEC members include Mexico, Kazakhstan, Azerbaijan, Oman, Bahrain, Malaysia, Brunei, Sudan, and South Sudan. The combined group pumps somewhere between 37 and 42 million barrels per day, depending on quotas.</p>

        <h2>How OPEC+ Sets Policy</h2>
        <p>The group's policy body is the <strong>Joint Ministerial Monitoring Committee (JMMC)</strong>, which meets monthly, and the full ministerial meeting of all 23 countries, which meets twice a year and can be called for emergency sessions. Decisions require consensus, but in practice Saudi Arabia and Russia are the dominant voices. Saudi Arabia has the largest spare capacity — the ability to quickly raise or lower output by millions of barrels per day — and Russia is the largest non-Gulf producer.</p>

        <p>Each member country receives an individual production quota, calculated from a baseline reference level that itself is a subject of ongoing negotiation. Compliance with quotas is imperfect: some members consistently overproduce, others under-produce due to field decline or sanctions (Iran, Venezuela). The group's <strong>effective</strong> production is usually within 500,000 barrels per day of the quota target.</p>

        <p>Current policy, as of early 2026, allows for gradual quota increases through the spring and summer. The group recently announced an <a href="april-206k-bpd-increase-proceeds.html">April increase of 206,000 barrels per day</a>, signaling confidence in demand while retaining the flexibility to reverse course if prices weaken.</p>

        <h2>How OPEC+ Moves Oil Prices</h2>
        <p>Three mechanisms drive price impact:</p>

        <p><strong>The quota change itself.</strong> A 1 million barrel per day cut tightens global supply by roughly 1%, which historically translates to a $5-15 per barrel price response. The magnitude depends on where the global market is already balanced — in a tight market, even small cuts move prices sharply; in an oversupplied market, larger cuts can fail to move prices at all.</p>

        <p><strong>Forward guidance.</strong> What OPEC+ signals about future meetings often moves prices more than current decisions. A meeting communique that emphasizes "flexibility" and "readiness to act" is read as a floor under prices. Language about "market share" or "supply discipline" tends to be bullish. Vague language creates uncertainty and can trigger either direction.</p>

        <p><strong>Credibility.</strong> OPEC+ has meaningfully more price influence when the market believes the group will actually follow through on announced cuts. Saudi Arabia's willingness to unilaterally absorb quota overruns from other members — called its "swing producer" role — is the key to that credibility. When Saudi resolve is questioned, OPEC+ pricing power weakens.</p>

        <h2>Why OPEC+ Meetings Matter for Markets</h2>
        <p>Oil futures markets often move 2-4% on OPEC+ meeting days. Traders watch four specific signals: the headline quota decision, the next scheduled meeting date, any change in the JMMC's monitoring framework, and public statements from the Saudi and Russian energy ministers after the meeting.</p>

        <p>Meetings during crises matter even more. OPEC+ can convene emergency sessions within days when oil prices are dislocating — and has done so during the 2020 COVID demand collapse and during previous Middle East tensions. The group's role during the current <a href="what-happens-if-strait-of-hormuz-closes.html">Strait of Hormuz situation</a> has been to signal readiness to offset supply disruptions without actually changing quotas, which has partially anchored prices.</p>

        <h2>The Limits of OPEC+ Power</h2>
        <p>OPEC+ is not an oil cartel in the classic monopoly sense. Three factors limit its pricing power:</p>

        <p>First, U.S. shale producers are not in the group and respond to high prices by ramping up drilling. That "shale elasticity" effectively caps how high OPEC+ can push oil prices before losing market share. The group knows this and has repeatedly pulled back from aggressive cuts to avoid giving U.S. producers a permanent share gain.</p>

        <p>Second, electric vehicles, efficiency gains, and renewables are slowly reducing the growth rate of global oil demand. OPEC+ can influence the price path but cannot prevent the long-term demand trajectory from moderating.</p>

        <p>Third, internal discipline. Individual members facing budget stress consistently cheat on quotas. The monthly JMMC meetings exist precisely because compliance is the group's eternal problem.</p>

        <h2>Frequently Asked Questions</h2>

        <h3>Who are the most important members of OPEC+?</h3>
        <p>Saudi Arabia and Russia, by a wide margin. Together they account for roughly 40% of OPEC+ output and essentially all of the group's spare production capacity. Other significant voices include the UAE (which has argued for higher baselines), Iraq, Iran (on geopolitical matters more than quotas), and Kazakhstan.</p>

        <h3>How is OPEC+ different from regular OPEC?</h3>
        <p>Regular OPEC has 12 members and its own production quotas. OPEC+ is the 23-nation expanded alliance that includes OPEC plus 10 non-OPEC producers (most importantly Russia). All 23 coordinate on production policy. When news references "OPEC+ cuts" or "OPEC+ policy," it's the larger group; "OPEC alone" decisions are rare now.</p>

        <h3>Can the U.S. influence OPEC+ decisions?</h3>
        <p>Indirectly. U.S. shale production provides the largest non-OPEC supply response, which affects OPEC+'s strategic calculus. U.S. diplomacy — particularly with Saudi Arabia — can shift the group's posture before meetings. But the U.S. has no seat at the table and cannot directly vote on quotas.</p>

        <h3>Why do OPEC+ meetings move markets so much?</h3>
        <p>Because the group's production decisions directly change the global supply balance, and because their forward guidance reveals information markets couldn't otherwise access — specifically, what the largest producers think about demand, inventory levels, and prices. Even modest quota changes can shift the market's read on the next six months.</p>
""",
    },
]


# ================================================================
# HTML template — matches existing article structure
# ================================================================

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<script>
!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','957762016897581');fbq('track','PageView');
</script><noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=957762016897581&ev=PageView&noscript=1"/></noscript>
  <link rel="preconnect" href="https://api.oilpriceapi.com" crossorigin>
  <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="dns-prefetch" href="https://api.rss2json.com">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_tag}</title>
  <meta name="description" content="{meta_desc_esc}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="https://www.energypricestoday.com/articles/{slug}.html">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title_tag}">
  <meta property="og:description" content="{meta_desc_esc}">
  <meta property="og:url" content="https://www.energypricestoday.com/articles/{slug}.html">
  <meta property="og:site_name" content="EnergyPricesToday.com">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{title_tag}">
  <meta name="twitter:description" content="{meta_desc_esc}">
  <link rel="stylesheet" href="../css/styles.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{schema_headline_esc}","datePublished":"2026-04-18","dateModified":"2026-04-18","author":{{"@type":"Organization","name":"EnergyPricesToday.com"}},"publisher":{{"@type":"Organization","name":"EnergyPricesToday.com","url":"https://www.energypricestoday.com"}}}}</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FXGF8HZFWL"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-FXGF8HZFWL");</script>

  <link rel="icon" type="image/svg+xml" href="../images/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="../images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="../images/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="../images/apple-touch-icon.png">
</head>
<body>
  <header class="site-header" id="site-header"><noscript><nav style="padding:8px 20px;display:flex;flex-wrap:wrap;gap:8px;font-size:13px"><a href="../index.html" style="color:#3d8fd4">Home</a><a href="{category_href}" style="color:#8891a5">{category_label}</a></nav></noscript></header>
  <main>
    <article class="article-page">
      <div class="container">
        <nav aria-label="Breadcrumb" style="margin-bottom:16px;font-size:12px;color:var(--text-3);display:flex;flex-wrap:wrap;gap:6px;align-items:center">
          <a href="../index.html" style="color:var(--text-2);text-decoration:none">Home</a>
          <span style="color:var(--text-3)">&rsaquo;</span>
          <a href="{category_href}" style="color:var(--text-2);text-decoration:none">{category_label}</a>
          <span style="color:var(--text-3)">&rsaquo;</span>
          <span style="color:var(--text-2)">Explainer</span>
        </nav>
        <span class="cat-pill">{category_label}</span>
        <h1>{h1_esc}</h1>
        <div class="article-author-row"><div class="flex items-center gap-8"><div class="article-avatar" style="background:linear-gradient(140deg,var(--blue),var(--amber))"></div><div><div class="article-author-name">Staff</div><div class="article-author-date">April 18, 2026</div></div></div></div>
        <div class="article-body">
{body_html}
{continue_block}
{related_block}
        </div>
        <div class="article-tags">
{tags_html}
        </div>
        <div id="related-articles-section" style="margin-top:36px;padding-top:24px;border-top:1px solid var(--border)">
          <h3 style="font-size:17px;margin-bottom:14px">More from EnergyPricesToday</h3>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px" id="article-related"></div>
        </div>
      </div>
    </article>
  </main>
  <footer class="site-footer" id="site-footer"></footer>
  <script src="../js/data.js"></script><script src="../js/article-slugs.js"></script><script src="../js/main.js"></script><script src="../js/live-data.js"></script><script src="../js/news-feed.js"></script>
<script>
    // Related articles
    if (typeof FEATURED_ARTICLES !== 'undefined') {{
      var relEl = document.getElementById('article-related');
      if (relEl) {{
        relEl.innerHTML = FEATURED_ARTICLES.slice(0,4).map(function(a) {{
          return '<a href="' + articleUrl(a.title) + '" style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:14px;display:block;transition:border-color .15s"><h4 style="color:var(--text-1);font-size:13px;font-weight:600;line-height:1.4;margin:0 0 4px">' + a.title + '</h4><span style="color:var(--text-3);font-size:11px">' + (a.date || '') + '</span></a>';
        }}).join('');
      }}
    }}
</script>
</body>
</html>
"""


def get_h1(slug: str) -> str:
    """Read the H1 of an existing article so we can use it in Related Coverage."""
    path = ARTICLES_DIR / f"{slug}.html"
    if not path.exists():
        return slug.replace("-", " ").title()
    import re
    with open(path, encoding="utf-8") as f:
        c = f.read()
    m = re.search(r"<h1[^>]*>([^<]+)</h1>", c)
    if not m:
        return slug.replace("-", " ").title()
    t = m.group(1).strip()
    t = (t.replace("&mdash;", "\u2014").replace("&rsquo;", "'")
          .replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&amp;", "&"))
    return t


def build_continue_block(continue_slug: str) -> str:
    title = get_h1(continue_slug)
    return f'''
        <div style="margin-top:24px;padding:20px 24px;background:var(--surface);border:1px solid var(--border);border-radius:10px">
          <div style="font-size:11px;text-transform:uppercase;letter-spacing:0.1em;color:var(--text-3);font-weight:700;margin-bottom:8px">Continue Reading</div>
          <a href="{continue_slug}.html" style="color:var(--text-1);text-decoration:none;font-size:16px;font-weight:600;line-height:1.4;display:block">{title} &rarr;</a>
        </div>'''


def build_related_block(related_slugs: list[str]) -> str:
    items = []
    for s in related_slugs:
        title = get_h1(s)
        items.append(
            f'              <li style="padding:6px 0"><a href="{s}.html" style="color:var(--blue);text-decoration:none;font-weight:500">{title}</a></li>'
        )
    return f'''
        <div style="margin-top:40px;padding:24px;background:var(--surface-2);border-radius:10px;border-left:3px solid var(--blue)">
          <h3 style="margin:0 0 14px 0;font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-2);font-weight:700">Related Coverage</h3>
          <ul style="margin:0;padding:0;list-style:none;line-height:1.7">
{chr(10).join(items)}
          </ul>
        </div>'''


def build_tags_html(tags: list[tuple[str, str]]) -> str:
    return "\n".join(
        f'          <a href="{href}" class="article-tag">{label}</a>'
        for label, href in tags
    )


def main():
    print("[create_explainers] Generating 5 explainer articles...")
    written = 0
    for art in ARTICLES:
        slug = art["slug"]
        path = ARTICLES_DIR / f"{slug}.html"

        continue_block = build_continue_block(art["continue_reading_slug"])
        related_block = build_related_block(art["related_slugs"])
        tags_html = build_tags_html(art["tags"])

        html = TEMPLATE.format(
            slug=slug,
            title_tag=art["title_tag"],
            meta_desc_esc=htmllib.escape(art["meta_desc"], quote=True),
            schema_headline_esc=htmllib.escape(art["schema_headline"], quote=True),
            h1_esc=htmllib.escape(art["h1"], quote=False),
            category_href=art["category_href"],
            category_label=art["category_label"],
            body_html=art["body_html"],
            continue_block=continue_block,
            related_block=related_block,
            tags_html=tags_html,
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(html)

        # Word count
        import re
        body_text = re.sub(r"<[^>]+>", " ", art["body_html"])
        body_text = re.sub(r"\s+", " ", body_text).strip()
        word_count = len(body_text.split())

        print(f"  ✓ {slug}.html — {word_count} words")
        written += 1

    print(f"\n[create_explainers] Wrote {written} articles")


if __name__ == "__main__":
    main()
