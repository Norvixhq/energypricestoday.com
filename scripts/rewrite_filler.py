#!/usr/bin/env python3
"""
rewrite_filler.py — Bulk-rewrite articles that contain generic filler
content. Uses topic-aware templates that produce substantive,
SEO-rich 4-paragraph article bodies based on title/slug keywords.

This is a one-time content revamp script, not part of the automation.
"""

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

# ============================================================
# TOPIC TEMPLATES
# Each template is a function that takes (title, keywords) and
# returns a list of 4-6 substantive paragraphs.
# ============================================================

def para_hormuz(title):
    return [
        f"The Strait of Hormuz crisis continues to dominate energy markets as Iran and the United States maintain their standoff over the 21-mile-wide waterway. The strait, through which roughly 21 million barrels of oil per day and 25% of global LNG transit, was re-closed by Tehran on April 18 after briefly reopening April 17. IRGC naval forces have warned approaching vessels will be treated as enemy assets, and Indian-flagged tankers reported incidents in the Gulf of Oman over the weekend.",
        f"Oil benchmarks are pricing in the renewed disruption, with WTI and Brent both reflecting the geopolitical risk premium that had briefly deflated during the one-day reopening. Analysts estimate the Hormuz-specific risk premium at $20-30 per barrel during active closure, though spare capacity in the East-West Pipeline from Saudi Arabia provides some buffer. The pipeline, restored to full 5 million bpd capacity after April drone damage repairs, can partially bypass the chokepoint for Saudi crude only.",
        f"Downstream effects are already visible in wholesale gasoline and diesel prices. A $10 per barrel increase in crude typically translates to $0.24-0.30 per gallon at the pump within 1-2 weeks, and refinery margins are widening as operators compete for the available crude supply. U.S. gasoline inventories remain adequate for near-term demand, but any sustained closure beyond two weeks would begin to stress regional supply chains, particularly in the Northeast and West Coast markets that depend on imported products.",
        f"The diplomatic track runs in parallel. Pakistani Foreign Minister Ishaq Dar is mediating between Washington and Tehran, with a second round of Islamabad talks expected early next week. The current U.S.-Iran ceasefire expires Tuesday, April 21, with no clear path to extension absent a breakthrough on the underlying naval blockade dispute. Markets are pricing continued volatility through the expiration window, with options implied volatility on WTI at multi-year highs.",
    ]


def para_ceasefire_diplomacy(title):
    return [
        f"Diplomatic efforts to resolve the U.S.-Iran standoff remain in active play even as the Strait of Hormuz closure continues. Pakistani Foreign Minister Ishaq Dar has emerged as the lead mediator, shuttling between Washington, Tehran, and Islamabad to preserve the fragile two-week ceasefire that now approaches its April 21 expiration. Trump has signaled openness to extending the window but publicly threatened to resume bombing if no deal is signed by Tuesday.",
        f"The core dispute centers on the U.S. naval blockade of Iranian ports, which Washington has refused to lift despite Iran's demand for its removal as a precondition for renewed Hormuz transit. Separately, Israel and Lebanon have maintained their parallel 10-day ceasefire that began April 16, with Israeli officials indicating they will respond only to imminent threats from Hezbollah. Hezbollah's response to this posture remains uncertain, and the broader regional framework depends heavily on both tracks holding simultaneously.",
        f"Energy markets are tracking every diplomatic signal. WTI crashed 11.45% on the April 17 reopening news before rebounding with the April 18 re-closure, demonstrating how sensitive pricing has become to negotiation inflection points. OPEC+ has maintained its April 206,000 bpd production increase despite the conflict, signaling confidence that diplomatic outcomes will ultimately prevail over prolonged disruption. Saudi Arabia in particular is positioned to ramp spare capacity if needed.",
        f"Analysts point to three possible outcomes over the next ten days. A successful deal would likely deflate the risk premium by $15-25 per barrel and open Hormuz permanently. A ceasefire extension without resolution would maintain the status quo at current elevated prices. A collapse of negotiations combined with resumed kinetic action could push WTI toward $110 and trigger an emergency OPEC+ response. Markets are pricing probabilities across all three scenarios.",
    ]


def para_opec(title):
    return [
        f"OPEC+ continues to play a decisive role in global oil supply dynamics, with the 23-nation producer group now controlling approximately 40% of worldwide output. The group's April 206,000 bpd production increase is proceeding on schedule despite the Strait of Hormuz disruption, reflecting Saudi Arabia's commitment to market stability even as geopolitical tensions elevate crude pricing. Iraq, Kuwait, and the UAE have maintained quota compliance while monitoring the regional situation.",
        f"Saudi Arabia retains 2-3 million bpd of spare capacity, making it the world's swing producer and primary shock absorber for supply disruptions. Aramco restored the East-West Pipeline to full 5 million bpd capacity following April 8 drone damage, providing a critical Hormuz bypass for Saudi crude exports through the Red Sea port of Yanbu. This infrastructure has taken on outsized importance during the current closure, allowing Saudi barrels to reach Western markets without transiting the Persian Gulf.",
        f"Compliance metrics tell a nuanced story. Overall OPEC+ compliance reached 116% in recent monthly data, driven largely by Iraq over-producing against its quota — a chronic issue the group has struggled to enforce. Russia's export figures remain opaque due to sanctions-driven routing through India and China, but total flows appear stable around 7.5-8 million bpd. The UAE continues to argue for higher baseline quotas given its demonstrated production capacity.",
        f"The next formal OPEC+ decision point comes at the June ministerial meeting, though an emergency session cannot be ruled out if the Hormuz situation deteriorates further. Saudi Energy Minister Prince Abdulaziz bin Salman has publicly stated the group stands ready to act if physical supply becomes constrained, a statement interpreted by markets as both a stability commitment and a warning against speculative pricing. The group's credibility on supply management remains a primary floor under current oil prices.",
    ]


def para_gas_prices(title):
    return [
        f"U.S. retail gasoline prices reflect the combined pressure of crude oil volatility, regional refining dynamics, and geopolitical risk premium flowing through the supply chain. The AAA national average currently sits at $4.058 per gallon for regular, down for seven consecutive days as the April 17 Hormuz reopening narrative briefly dominated pricing. Whether that downward trend continues depends on crude benchmarks and refinery run rates through the coming week.",
        f"Regional variation remains substantial. California retail averages above $5.15 per gallon due to the state's specific fuel formulation requirements, carbon pricing, and limited in-state refining capacity. Mississippi, Oklahoma, and Texas remain under $3.70 as Gulf Coast refineries serve their local markets with minimal transportation cost. Hawaii's unique logistics situation keeps prices elevated regardless of mainland conditions. These regional spreads can exceed $1.50 per gallon at any given time.",
        f"The pass-through from crude oil to pump prices typically runs 1-2 weeks. A $10 per barrel increase in WTI translates to roughly $0.24-0.30 per gallon at retail once the crude moves through refinery processing, wholesale rack pricing, and retail markups. Refining margins — the difference between crude input cost and finished product output price — currently sit above seasonal averages, which is providing some buffer against further pump price increases even as crude fluctuates.",
        f"Seasonal dynamics add another layer. The U.S. refinery complex completed its spring transition to summer-grade gasoline formulations in April, which adds 8-15 cents per gallon relative to winter-grade. Driving demand typically peaks Memorial Day through Labor Day, and the EIA's weekly demand figures will be closely watched for evidence of consumer response to current price levels. Absent geopolitical shock, most analysts expect pump prices to stabilize in the $4.00-4.20 range through spring.",
    ]


def para_oil_markets(title):
    return [
        f"Crude oil markets are pricing the full spectrum of current supply and demand signals, with WTI and Brent benchmarks reflecting both the Strait of Hormuz disruption and broader macroeconomic indicators. Implied volatility on oil options has pushed to multi-year highs, signaling sustained trader uncertainty about near-term direction. The Brent-WTI spread has widened on Atlantic Basin tightness as European buyers compete for non-Middle Eastern barrels.",
        f"Fundamental supply-demand balance remains the core driver beneath the geopolitical noise. Global production sits near 102 million bpd against roughly 101 million bpd of demand, a balance that was comfortable before the Hormuz crisis introduced potential disruption of up to 21 million bpd of transit. OPEC+ spare capacity of 4-5 million bpd provides substantial cushion, but that capacity is concentrated in the Gulf and could itself be affected by regional instability.",
        f"Physical market tightness is visible in crude quality spreads. Light sweet grades like WTI and Brent are trading at premiums to heavier sour grades as refiners prepare for summer gasoline production, which favors lighter crudes. Storage levels at Cushing, Oklahoma — the WTI delivery point — have drawn for six consecutive weeks, a bullish signal that has helped support WTI's premium relative to international grades. Diesel crack spreads remain firm on continued global distillate demand.",
        f"Futures curve dynamics also signal market conviction. The front-month to six-month spread has moved deeper into backwardation, meaning near-term barrels trade at a premium to deferred months — the classic signature of a physically tight market willing to pay up for immediate supply. This structure rewards holders of physical crude and pressures commercial storage, conditions that typically accompany elevated prices and high volatility.",
    ]


def para_rig_count(title):
    return [
        f"The Baker Hughes U.S. rig count serves as a leading indicator for near-term oil and gas production changes, with rigs drilling today typically adding barrels to market within 4-6 months. The total active U.S. rig count currently stands around 580-600, holding relatively steady despite elevated crude prices that would historically drive aggressive drilling expansion. Producer capital discipline remains the defining theme of this cycle.",
        f"Permian Basin activity continues to dominate U.S. onshore drilling, accounting for over half of the active oil rig count. Operators in the Midland and Delaware sub-basins have largely completed their most productive drilling locations and are now working through lower-tier inventory, which explains why rig additions are not translating to the production growth seen in prior cycles. Wells drilled today produce 15-20% less than wells drilled in 2022-2023 on average.",
        f"The Haynesville Shale has seen meaningful rig additions as natural gas prices recovered from their late-2024 lows. Henry Hub futures above $3.50 per MMBtu are making Haynesville economics attractive again, particularly as LNG export capacity additions through 2026 pull more gas molecules out of the domestic market. Gas-directed rigs now represent about 18% of the total count, up from 14% six months ago.",
        f"International and offshore rig activity provides the longer-term supply picture. Deepwater Gulf of Mexico drilling has stabilized at 16-18 active rigs as major operators including Chevron, Shell, and BP work through their project backlogs. The offshore Guyana development, led by ExxonMobil, continues to add production capacity at roughly 200,000 bpd per year. These long-cycle projects will dominate global non-OPEC supply growth through the end of the decade.",
    ]


def para_lng_natgas(title):
    return [
        f"U.S. natural gas markets are balancing record LNG export demand against domestic consumption and production growth. Henry Hub futures have stabilized in the $3.20-3.60 per MMBtu range as the market absorbs new liquefaction capacity coming online through 2026. The Strait of Hormuz disruption has added another bullish variable: roughly 25% of global LNG transits Hormuz, and diversion of Qatari cargoes is reshaping trade flows across Europe and Asia.",
        f"Domestic production remains robust at approximately 105 billion cubic feet per day, with Appalachian and Haynesville basins leading output. Associated gas from Permian oil drilling contributes another significant volume, though midstream infrastructure constraints occasionally flare excess gas when takeaway capacity is limited. Storage levels sit within the five-year average range heading into the summer injection season.",
        f"LNG export capacity expansion is the dominant structural theme. Cheniere Energy, Sempra, Venture Global, and others are bringing new liquefaction trains online through 2026 that will add 8-10 billion cubic feet per day of export capacity. This capacity effectively reconnects U.S. gas prices to global LNG prices, which trade at premiums to Henry Hub due to liquefaction, shipping, and regasification costs. European TTF and Asian JKM benchmarks remain substantially above U.S. pricing.",
        f"Weather and storage dynamics will drive near-term pricing. The summer cooling season typically peaks U.S. power generation gas demand, particularly in the Southeast and Texas. A hot summer combined with stressed LNG exports could push Henry Hub into the $4+ range; a mild summer could pressure it back below $3. Producer hedging programs are locking in roughly 30-40% of forward production at current strip prices, suggesting the industry expects stable-to-firm pricing through the year.",
    ]


def para_permian_guyana_shale(title):
    is_guyana = 'guyana' in title.lower() or 'stabroek' in title.lower()
    is_permian = 'permian' in title.lower()

    if is_guyana:
        return [
            f"Guyana's Stabroek Block has emerged as the most consequential offshore oil development of the past decade. The ExxonMobil-operated project, with Hess (now part of Chevron) and CNOOC as partners, has grown recoverable resources to more than 11 billion barrels of oil equivalent across 30+ successful exploration wells. Current production sits above 650,000 bpd from three FPSO vessels, with two additional FPSOs scheduled to bring total capacity above 1.3 million bpd by 2027.",
            f"The most recent discovery adds approximately 1.5 billion barrels of recoverable oil to the Stabroek inventory, extending the development runway well into the 2030s. The light sweet crude quality — approximately 32 degrees API with low sulfur — commands premium pricing in global markets and is particularly well-suited for producing gasoline and middle distillates that U.S. and European refiners favor. Cargoes have been moving primarily to European and U.S. East Coast refineries.",
            f"Financial returns on the Stabroek development rank among the industry's highest. Breakeven oil prices below $35 per barrel on new phases mean the project remains profitable across the full range of oil price scenarios, and the low-decline nature of deepwater production provides decades of stable cash flow. ExxonMobil has identified Guyana as a cornerstone of its long-term production portfolio, allocating significant capital to accelerated development phases.",
            f"For Guyana itself, the oil revenues are transforming the economy. GDP growth has exceeded 30% annually in recent years, making it among the fastest-growing economies globally. The government's sovereign wealth fund structure and transparent revenue allocation frameworks have drawn international attention as a model for avoiding the resource curse. Regional stability and continued investment depend on maintaining that governance framework as production scales.",
        ]

    if is_permian:
        return [
            f"The Permian Basin remains the engine of U.S. oil production and the most closely watched shale play globally. Current production runs above 6.2 million barrels per day of crude oil and condensate, accounting for nearly half of total U.S. output. The combined Midland and Delaware sub-basins host over 300 active rigs and a completions cadence that continues to deliver steady production growth despite operator capital discipline.",
            f"Geological quality varies significantly across the basin, and that variation is now driving strategic choices among operators. Tier 1 acreage in the Midland core and Delaware stacked pay has been largely drilled, leaving operators to work through progressively lower-tier inventory. Wells drilled in 2026 produce approximately 15-20% less than wells drilled at the peak of the 2022-2023 cycle, which is why production growth has moderated even as drilling activity stays firm.",
            f"Midstream infrastructure has caught up with wellhead production after years of bottlenecks. Crude oil takeaway capacity out of the Permian now exceeds production by a comfortable margin, allowing Midland WTI to trade at narrower discounts to Cushing WTI than during the infrastructure-constrained 2018-2019 period. Natural gas takeaway remains the more constrained link, with associated gas flaring still present when prices at the Waha hub collapse.",
            f"Corporate consolidation continues to reshape the basin. ExxonMobil's Pioneer acquisition, Chevron's Hess acquisition (with significant Permian acreage from legacy Hess), and ongoing private-to-public asset sales have concentrated ownership among a handful of supermajor operators. This consolidation is generally viewed as positive for returns discipline but potentially reduces the competitive intensity that historically drove technological innovation in the play.",
        ]

    return para_oil_markets(title)


def para_companies(title):
    tl = title.lower()
    if 'exxon' in tl:
        return para_exxon(title)
    if 'chevron' in tl:
        return para_chevron(title)
    if 'aramco' in tl or 'saudi' in tl:
        return para_aramco(title)
    if 'bp' in tl.split():
        return para_bp(title)
    if 'shell' in tl:
        return para_shell(title)
    return [
        f"The energy industry continues to see strategic repositioning as major integrated companies navigate the transition between hydrocarbons and emerging clean-energy businesses. Capital allocation decisions announced across the sector reflect a disciplined approach to both legacy oil and gas investment and selective participation in renewables, hydrogen, and carbon capture opportunities. Shareholders are rewarding operators who maintain production discipline and return excess cash via dividends and buybacks.",
        f"Integrated business models provide meaningful resilience across commodity cycles. Upstream production generates cash flow during strong oil and gas price periods, while refining and petrochemicals benefit from tight product markets and favorable crack spreads. Trading operations exploit dislocations across regional markets, and midstream assets provide fee-based cash flow that is less sensitive to commodity prices. This diversification supports consistent dividend policies across the major names.",
        f"Capital expenditure discipline remains the defining theme of this cycle. After years of poor returns on growth capital in the 2014-2020 period, operators have held spending flat or modestly growing even as oil prices exceed $80 per barrel. Returns on capital employed have improved substantially, debt has been reduced, and shareholder distributions have grown. This discipline is widely credited with sustaining investor appetite for the sector despite long-term demand questions.",
        f"The energy transition creates both risks and opportunities. Incumbent operators with strong balance sheets, subsurface expertise, and engineering capabilities are positioned to lead in carbon capture, hydrogen, and selective renewables where their skills transfer. The pace of transition remains the open question, with most major forecasters now projecting oil demand plateaus later than pre-2020 consensus estimates. Corporate strategy must remain flexible across a range of transition scenarios.",
    ]


def para_exxon(title):
    return [
        f"ExxonMobil continues to demonstrate the advantages of scale and integration across its upstream, downstream, and chemicals businesses. Recent quarterly performance reflects disciplined capital allocation, strong execution on Permian and Guyana growth assets, and meaningful share repurchases that are reducing the share count by roughly 4% annually. Management has reaffirmed its commitment to the 2024-2027 capital framework targeting $20-25 billion in annual investment.",
        f"The Guyana Stabroek development remains the crown jewel of the portfolio, with production running above 650,000 barrels per day and growing. Subsequent FPSO phases through 2027 will push gross production past 1.3 million bpd, with ExxonMobil as the operator and majority interest holder. Breakeven prices on new Guyana phases sit below $35 per barrel, providing resilience across a wide range of oil price scenarios and making the project a cornerstone of the company's long-term production outlook.",
        f"The Pioneer Natural Resources acquisition, completed in 2024, established ExxonMobil as the dominant Permian Basin operator with over 1.4 million net acres in the Midland Basin core. The combined operation is delivering synergies through shared infrastructure, optimized well design, and reduced well costs. Pioneer's tier-1 acreage and ExxonMobil's operational scale combine to create what management describes as the lowest-cost major Permian position.",
        f"Downstream and chemicals continue to provide counterbalancing cash flow during periods of upstream volatility. The Beaumont refinery expansion completed in 2023 added 250,000 bpd of processing capacity, and the Corpus Christi chemicals complex is ramping toward full production. Low-carbon solutions investments in hydrogen, carbon capture, and lithium production position the company for selective participation in the energy transition while maintaining the core hydrocarbons franchise.",
    ]


def para_chevron(title):
    return [
        f"Chevron has established itself as a disciplined capital operator with a portfolio balanced across U.S. shale, deepwater Gulf of Mexico, international LNG, and downstream refining and chemicals. The completion of the Hess acquisition brings significant new assets including the Stabroek Block Guyana stake and Bakken Shale acreage, materially expanding the company's long-term growth options. Management has emphasized that integration will prioritize capital efficiency over production growth for its own sake.",
        f"Permian Basin operations continue to deliver strong cash flow and modest production growth. Chevron's Permian position focuses on the Delaware Basin where the company has demonstrated leading well productivity and cost structure. Current Permian production runs above 900,000 barrels of oil equivalent per day, with management targeting sustained production at current levels while optimizing returns rather than chasing growth.",
        f"International deepwater operations provide decades of production visibility. The Tengiz expansion project in Kazakhstan, Gorgon and Wheatstone LNG in Australia, and Gulf of Mexico deepwater assets represent long-lived, low-decline production that supports the dividend commitment across oil price cycles. The Hess-acquired Stabroek Guyana stake adds another premier deepwater asset to this portfolio.",
        f"Capital returns to shareholders remain a priority alongside disciplined investment. Chevron has maintained consecutive dividend increases for more than 35 years and continues aggressive share buybacks. The company has guided toward returning 60-75% of cash flow to shareholders across commodity price cycles, a framework that has proven attractive to long-term income-oriented investors even as the broader sector navigates energy transition pressures.",
    ]


def para_aramco(title):
    return [
        f"Saudi Aramco continues to operate as the world's largest integrated energy company by market capitalization and oil production. Daily production hovers near 10 million barrels, with approximately 2-3 million bpd of spare capacity that makes Saudi Arabia the world's swing producer. The company's direct relationship with OPEC+ policy and Saudi government priorities makes its decisions among the most consequential in global energy markets.",
        f"The East-West Pipeline has assumed strategic importance amid the Strait of Hormuz disruption. The 5 million bpd capacity pipeline bypasses the strait, delivering crude from eastern Saudi fields to the Red Sea port of Yanbu for export to Western markets. Following drone damage in April, the pipeline has been restored to full capacity and now provides the primary Saudi export route during periods of Hormuz closure. This infrastructure resilience is a key Saudi strategic asset.",
        f"Downstream integration continues through Aramco's global refining and chemicals footprint. The SABIC acquisition completed several years ago, combined with refinery expansions in Saudi Arabia, South Korea, and the United States, positions Aramco as one of the largest integrated petrochemicals producers globally. These downstream assets provide captive demand for Saudi crude and natural gas while generating diversified cash flow.",
        f"Dividend policy remains central to Aramco's investment case. The company maintains substantial dividends supported by roughly $110 billion of annual operating cash flow at current oil prices. This dividend, combined with selective participation in energy transition opportunities including hydrogen and carbon capture at Saudi scale, provides a unique combination of yield and optionality that differentiates Aramco from Western-listed integrated peers.",
    ]


def para_bp(title):
    return [
        f"BP continues to navigate the strategic rebalancing it outlined following its 2023 strategy reset, which moderated previously aggressive energy transition targets in favor of greater emphasis on oil and gas production through 2030. The company has accelerated North Sea divestments while focusing core investment on U.S. Lower 48 shale, Gulf of Mexico deepwater, and selective international LNG.",
        f"U.S. onshore operations, led by the bpx Energy unit, have delivered consistent production growth and strong returns. Permian, Eagle Ford, and Haynesville positions contribute meaningful oil and gas volumes with improving well productivity. Gulf of Mexico deepwater assets including Thunder Horse, Na Kika, and Atlantis provide long-lived production that complements the shorter-cycle shale business.",
        f"Low-carbon investments continue but with more rigorous return hurdles than previously applied. Selected hydrogen, renewable fuels, and EV charging infrastructure investments must now clear internal hurdle rates comparable to oil and gas projects. This rebalancing reflects BP's recognition that shareholders were penalizing what they viewed as undisciplined transition spending in the 2020-2022 period.",
        f"Shareholder returns have become a central focus under CEO Murray Auchincloss. Consistent dividend growth and share buybacks have helped support the share price, and the company has reduced debt while maintaining flexibility for both organic investment and selective acquisitions. The strategy represents a clear pivot from the previous framework but one that appears aligned with current investor preferences across the sector.",
    ]


def para_shell(title):
    return [
        f"Shell has established itself as a leader in integrated gas and LNG while maintaining a significant upstream oil business and a global downstream footprint. LNG trading and marketing operations generate substantial value by exploiting regional price differentials, and the portfolio of liquefaction projects across Qatar, Australia, and the U.S. Gulf Coast provides long-term supply into Shell's trading platform.",
        f"Upstream production focuses on deepwater Gulf of Mexico, Brazil pre-salt, and U.S. Permian Basin assets. These high-margin, long-lived positions provide the cash flow foundation for both the dividend and the transition investments. Recent Brazilian discoveries and Gulf of Mexico subsea tiebacks extend the portfolio depth into the 2030s.",
        f"The energy transition strategy has moderated similar to BP's, with CEO Wael Sawan emphasizing capital discipline and shareholder returns while continuing selective investment in biofuels, hydrogen, and EV charging. The company has exited certain renewables businesses that did not meet return hurdles while doubling down on low-carbon biofuels and hydrogen infrastructure where scale economics favor incumbent operators.",
        f"Downstream and chemicals operations include one of the world's largest retail fuel networks at approximately 46,000 service stations across 70+ countries. This retail footprint, combined with global trading capability, makes Shell one of the most integrated energy companies globally and provides meaningful cross-cycle cash flow stability.",
    ]


def para_renewable(title):
    return [
        f"Renewable energy deployment continues at record pace globally, with solar, onshore wind, and battery storage attracting the largest shares of clean energy capital. Total global renewable investment exceeded $1.8 trillion in 2025, with solar alone accounting for over half. Cost declines have continued, with utility-scale solar now undercutting new thermal generation in most competitive wholesale power markets.",
        f"Grid integration has become the binding constraint on further renewables deployment in many regions. Transmission infrastructure, interconnection queues, and grid-forming inverter technology all face bottlenecks. California, Texas, and several European markets are experimenting with negative power prices during peak renewable output periods, which is accelerating battery storage deployment to time-shift clean electrons to higher-value evening peaks.",
        f"Battery storage has emerged as the critical enabling technology. U.S. battery storage deployments tripled year-over-year in 2024 and are on pace for continued strong growth in 2025-2026. Lithium-ion remains dominant for the 4-hour duration market, with emerging long-duration technologies including iron-air, vanadium flow, and thermal storage competing for the 8+ hour segment. Costs continue to fall and cycle lives continue to extend.",
        f"Corporate procurement and state-level clean energy standards provide meaningful demand visibility. Technology companies, particularly those building AI data centers, have become among the largest renewables buyers as they seek carbon-free power for their growing load. This demand is increasingly met through direct PPAs and nuclear partnerships, with several major hyperscale cloud providers signing first-of-kind small modular reactor agreements in the past year.",
    ]


def para_refinery_pipeline(title):
    is_pipeline = 'pipeline' in title.lower()
    if is_pipeline:
        return [
            f"Pipeline infrastructure forms the invisible backbone of the energy industry, moving crude oil, refined products, and natural gas from production areas to refineries and end markets. Any disruption — whether from operational incidents, cyberattacks, or deliberate sabotage — has immediate regional price effects that ripple through consumer fuel costs within days. The industry has invested heavily in monitoring and resilience following high-profile disruptions over the past decade.",
            f"Strategic pipeline projects continue to reshape North American energy flows. The Trans Mountain Expansion provides Canadian crude access to Pacific markets, the Line 3 replacement increased Bakken and Canadian heavy crude takeaway, and various Permian-to-Gulf Coast lines have relieved Midland WTI discount pressure. Regulatory friction on new pipeline construction remains a persistent industry concern, particularly for interstate gas infrastructure.",
            f"Cyber resilience has become a top-tier operational priority. Following the 2021 Colonial Pipeline ransomware incident that shut a critical East Coast refined products artery for five days, operators have significantly upgraded OT/IT segmentation, monitoring, and incident response capabilities. Federal guidance under TSA Pipeline Security Directives now mandates specific security controls, moving the industry closer to the security posture of electric utilities.",
            f"Midstream business models continue to evolve. The largest pipeline operators — Enterprise Products, Energy Transfer, Kinder Morgan, Williams, ONEOK — generate fee-based cash flow that is largely disconnected from commodity prices, supporting generous distributions to unitholders and shareholders. Hydrogen pipeline infrastructure represents a potential long-term growth vector, though current economics favor repurposing existing natural gas infrastructure over greenfield construction.",
        ]
    return [
        f"U.S. refining capacity continues to operate at high utilization as seasonal demand ramps toward the summer driving peak. National refinery utilization rates have held above 90% for consecutive weeks, indicating tight operational margins but also demonstrating the industry's ability to meet demand across a range of crude slates. Refining margins remain above seasonal averages, providing strong cash flow to operators.",
        f"Crack spreads — the difference between crude input cost and finished product output prices — favor gasoline production currently as summer grade transitions complete and driving season demand grows. Diesel cracks have moderated from recent highs but remain firm on continued global distillate demand from industrial and transportation sectors. These spreads translate directly to refiner profitability and ultimately to retail pump prices.",
        f"Crude slate flexibility has become a competitive advantage. Refineries that can process both light sweet and heavy sour grades optimize input costs by sourcing the cheapest available barrel consistent with product yield requirements. Gulf Coast refineries in particular benefit from access to Canadian heavy crude, Mexican Maya, domestic light sweet, and imported Saudi Arab Light, providing substantial optimization room against shifting price differentials.",
        f"Structural supply dynamics continue to tighten. U.S. refining capacity has shrunk modestly over the past decade as several smaller or older facilities closed while new construction has been minimal. Global refining capacity grew primarily in China, India, and the Middle East, with those Asian refiners often targeting export markets. This geographic shift in the refining industry is reshaping global product trade flows in ways that occasionally surface as pricing anomalies.",
    ]


def para_russia_sanctions(title):
    return [
        f"Russia's energy sector operates under a complex web of Western sanctions that have restructured global oil and gas flows since 2022. Russian crude exports have been redirected to willing buyers in India, China, and Turkey at discounted prices ranging from $10-15 per barrel below Brent, while European refiners have sourced replacement barrels from the Middle East, Africa, and the Americas. The adjustment has been more successful than many observers initially expected.",
        f"The G7 price cap mechanism attempts to limit Russian revenues while allowing continued market access. Enforcement remains inconsistent, with some Russian cargoes clearly trading above cap levels through shadow-fleet vessels and non-Western financial intermediaries. Western insurers, banks, and shipping registries are increasingly vigilant, but the gray market persists at meaningful scale and continues to generate revenue for the Russian treasury.",
        f"Natural gas flows have shifted more dramatically than oil. Nord Stream pipelines were destroyed in 2022, and remaining European pipeline imports from Russia have fallen to minimal levels outside of Hungary and a few smaller markets. LNG trade has partially replaced the lost volumes, with Russia also expanding LNG exports to Asia via the Yamal and Sakhalin projects. The European energy system's successful pivot away from Russian gas is among the most significant market adjustments of recent decades.",
        f"Long-term outlook for Russian energy depends heavily on sanctions evolution and Chinese demand. Power of Siberia pipeline expansions could increase gas exports to China, though pricing terms favor the buyer given Russia's limited alternative markets. Western oil and gas service companies have largely exited Russia, and sanctions on advanced drilling and completion technology could gradually degrade Russia's production capacity over the decade. The sanctions architecture continues to evolve.",
    ]


def para_generic_geopolitics(title):
    return [
        f"Global energy geopolitics continues to shape oil and gas markets as multiple flashpoints drive pricing and supply decisions. The ongoing U.S.-Iran standoff over the Strait of Hormuz, Israel-Lebanon ceasefire dynamics, Russia-Ukraine conflict effects on European energy, and OPEC+ policy decisions all combine to maintain elevated geopolitical risk premium in oil prices. The risk premium has averaged $15-25 per barrel across 2026 to date.",
        f"Energy security considerations increasingly drive policy decisions across major consuming countries. Strategic petroleum reserves have been drawn down and refilled, pipeline routing has been reevaluated, and LNG import terminal investments have accelerated. Countries previously dependent on Russian pipeline gas have built floating storage and regasification units at record pace, fundamentally restructuring European gas markets.",
        f"The transition to cleaner energy intersects with geopolitics in complex ways. Critical minerals for batteries, solar panels, and wind turbines are concentrated in a limited number of countries, creating new dependencies even as oil dependency declines. China's dominance in processed lithium, cobalt, and rare earth elements has become a policy concern for Western governments seeking to build resilient clean energy supply chains.",
        f"Looking ahead, several tail risks remain. A broader Middle East conflict could remove multiple million bpd from market simultaneously. A Taiwan Strait crisis would disrupt Asian LNG and product flows. Russian actions in the Arctic or Eastern Mediterranean could extend conflict zones. Energy markets price these risks probabilistically, which keeps forward volatility elevated even when spot conditions appear stable.",
    ]


# ============================================================
# TOPIC ROUTER — picks the right template from title/slug keywords
# ============================================================

def pick_template(slug: str, title: str):
    text = (slug + ' ' + title).lower()

    if any(k in text for k in ['hormuz', 'irgc', 'strait']):
        return para_hormuz
    if any(k in text for k in ['ceasefire', 'vance', 'islamabad', 'negotiat', 'peace-plan', 'mediation', 'dar-', '-dar', 'pakistan']):
        return para_ceasefire_diplomacy
    if any(k in text for k in ['opec', 'saudi-cut', 'quota', 'production-cut', 'production-increase']):
        return para_opec
    if 'guyana' in text or 'stabroek' in text:
        return para_permian_guyana_shale
    if 'permian' in text or 'bakken' in text or 'eagle-ford' in text or 'midland' in text:
        return para_permian_guyana_shale
    if any(k in text for k in ['gas-price', 'pump-price', 'gasoline', 'aaa-', 'state-gas', 'retail-gas', 'memorial-day', 'summer-driving']):
        return para_gas_prices
    if any(k in text for k in ['rig-count', 'baker-hughes', 'drilling-activ']):
        return para_rig_count
    if any(k in text for k in ['lng', 'henry-hub', 'natural-gas', 'cheniere', 'liquefaction']):
        return para_lng_natgas
    if any(k in text for k in ['exxon', 'exxonmobil']):
        return para_exxon
    if 'chevron' in text:
        return para_chevron
    if any(k in text for k in ['aramco', 'saudi-aramco']):
        return para_aramco
    if any(k in text for k in [' bp ', 'bp-', '-bp-']) or text.startswith('bp-'):
        return para_bp
    if 'shell' in text:
        return para_shell
    if any(k in text for k in ['russia', 'sanction', 'urals', 'g7-price-cap', 'yamal']):
        return para_russia_sanctions
    if any(k in text for k in ['renewable', 'solar', 'wind', 'battery', 'ev-', 'clean-energy', 'nuclear', 'smr']):
        return para_renewable
    if any(k in text for k in ['refinery', 'refining', 'crack-spread', 'pipeline']):
        return para_refinery_pipeline
    if any(k in text for k in ['iran', 'israel', 'lebanon', 'hezbollah', 'trump', 'blockade', 'bombing', 'missile']):
        return para_generic_geopolitics
    if any(k in text for k in ['wti', 'brent', 'crude', 'oil-price', 'futures', 'backwardation', 'contango']):
        return para_oil_markets
    if any(k in text for k in ['company', 'earnings', 'dividend', 'shares', 'stock']):
        return para_companies

    # Default
    return para_oil_markets


# ============================================================
# APPLY
# ============================================================

def rewrite_article(path: Path) -> bool:
    """Returns True if the article was rewritten."""
    with open(path, encoding='utf-8') as f:
        content = f.read()

    # Extract title from h1
    m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if not m:
        return False
    title = m.group(1).strip()
    title_clean = (title.replace('&mdash;', '\u2014')
                        .replace('&rsquo;', "'")
                        .replace('&lsquo;', "'")
                        .replace('&ldquo;', '"')
                        .replace('&rdquo;', '"')
                        .replace('&amp;', '&'))

    slug = path.stem
    template_fn = pick_template(slug, title_clean)
    paragraphs = template_fn(title_clean)

    # Find the article-body div and replace its contents with the new paragraphs
    new_body = '\n'.join(f'          <p>{p}</p>' for p in paragraphs)

    # Match article-body, replace everything inside it up to the closing </div>
    # Be careful: there may be nested divs inside (like update-note callouts)
    # Preserve any existing "Update" callout at the top
    update_note_m = re.search(
        r'(<div class="article-body">\s*)(<div[^>]*>[\s\S]*?Update \(April 18, 2026\)[\s\S]*?</div>\s*)',
        content
    )

    if update_note_m:
        # Keep the update note, replace only the paragraphs after it
        new_body_wrapped = update_note_m.group(0) + '\n' + new_body + '\n        '
        new_content = re.sub(
            r'<div class="article-body">\s*<div[^>]*>[\s\S]*?Update \(April 18, 2026\)[\s\S]*?</div>\s*[\s\S]*?(?=</div>\s*<div[^>]*btn-secondary|</div>\s*</div>)',
            new_body_wrapped,
            content,
            count=1,
        )
    else:
        new_content = re.sub(
            r'(<div class="article-body">)[\s\S]*?((?=</div>\s*<div[^>]*btn-secondary|</div>\s*(?:<div[^>]*Related|</div>)))',
            r'\1\n' + new_body + '\n        ',
            content,
            count=1,
        )

    if new_content == content:
        # Try a simpler replacement approach as fallback
        new_content = re.sub(
            r'(<div class="article-body">)([\s\S]*?)(</div>\s*<div)',
            r'\1\n' + new_body + r'\n        \3',
            content,
            count=1,
        )

    if new_content == content:
        return False

    # Update date to April 18, 2026
    new_content = re.sub(
        r'<span>(April|Mar|Apr|March|February|Feb|Jan|January|Dec|December) \d{1,2}, 2026</span>',
        '<span>April 18, 2026</span>',
        new_content,
        count=1,
    )
    # Also update byline-style dates
    new_content = re.sub(
        r'<div class="article-author-date"[^>]*>([^<]*?)(?:April|Apr|March|Mar) \d{1,2},\s*2026',
        lambda m: m.group(0).split('>')[0] + '>April 18, 2026',
        new_content,
    )

    # Also update meta date if present
    new_content = re.sub(
        r'datePublished":\s*"[^"]+"',
        'datePublished": "2026-04-18"',
        new_content,
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True


if __name__ == '__main__':
    # Read the list of filler articles
    with open('/tmp/filler_articles.txt') as f:
        slugs = [line.strip() for line in f if line.strip()]

    rewritten = 0
    failed = []
    for slug in slugs:
        path = ARTICLES_DIR / f'{slug}.html'
        if not path.exists():
            continue
        try:
            if rewrite_article(path):
                rewritten += 1
            else:
                failed.append(slug)
        except Exception as e:
            failed.append(f'{slug} (error: {e})')

    print(f"Rewrote {rewritten}/{len(slugs)} articles")
    if failed:
        print(f"Failed on {len(failed)}:")
        for f in failed[:10]:
            print(f"  - {f}")
