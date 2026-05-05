#!/usr/bin/env python3
"""
Generate 4 new article files covering May 4, 2026 — the day the ceasefire effectively shattered.
Uses EnergyPricesToday Editorial byline + NewsMediaOrganization schema author.
Same template/style as generate_may1_articles.py.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

STORIES = [
    {
        "slug": "iran-strikes-uae-fujairah-oil-hub-first-major-bypass-infrastructure-hit",
        "title_variants": [
            "Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit",
            "Iranian Drone Sets Fujairah Oil Industry Zone Ablaze; Three Indians Wounded",
            "UAE Air Defenses Engage 19 Iranian Missiles, Drones; Fujairah Hub on Fire",
            "Fujairah Oil Hub Struck by Iranian Drone in Largest UAE Attack Since Ceasefire",
            "Iran Hits Fujairah Oil Industry Zone — First Strike on Strait Bypass Infrastructure",
        ],
        "display_title": "Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 4, 2026",
        "iso_date": "2026-05-04T16:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "6 min",
        "meta_desc": "Iran launched 19 missiles and drones at the UAE on Monday May 4. Most were intercepted, but a drone struck the Fujairah Oil Industry Zone, sparking a major fire and wounding three Indian nationals. Fujairah is the terminus of the UAE pipeline that bypasses the Strait of Hormuz.",
        "keywords": "Fujairah oil hub strike, UAE Iran missile attack, Hormuz bypass infrastructure, ADCOP pipeline, Iran drones UAE, Persian Gulf escalation",
        "paragraphs": [
            "Iran launched a barrage of 19 missiles and drones at the United Arab Emirates on Monday, May 4, 2026 &mdash; the largest direct attack on the UAE since the April 8 ceasefire took hold &mdash; with the UAE Defense Ministry confirming its air defenses engaged 15 missiles and four drones in the assault. The Emirati Foreign Ministry called the attack &ldquo;a dangerous escalation and an unacceptable violation,&rdquo; signaling the strongest public response from Abu Dhabi since the conflict began in late February.",
            "Most of the projectiles were intercepted, but Emirati authorities confirmed that one Iranian drone struck the Fujairah Oil Industry Zone &mdash; sparking a &ldquo;major fire&rdquo; and moderately wounding three Indian nationals working at the facility. Four missile alerts were issued across the UAE during the day, the first such alerts since the ceasefire began nearly a month ago. Commercial planes bound for Dubai and Abu Dhabi turned around midair as the attack unfolded.",
            "The strategic significance of the Fujairah strike extends far beyond the immediate damage. Fujairah, located on the Gulf of Oman beyond the Strait of Hormuz, is the terminus of the UAE&rsquo;s Abu Dhabi Crude Oil Pipeline (ADCOP) &mdash; one of just two operational pipelines that bypass the strait, with a capacity of roughly 1.8 million barrels per day. Throughout the conflict, Saudi Arabia&rsquo;s East-West Pipeline to Yanbu and the UAE&rsquo;s ADCOP to Fujairah have provided the only meaningful escape routes for trapped Persian Gulf oil. Monday&rsquo;s strike marks the first time Iran has targeted bypass infrastructure directly.",
            "The pace of maritime incidents in and around the strait has accelerated sharply over the past 72 hours. On Sunday May 3, an unidentified bulk carrier was attacked by small boats west of Bandar Sirik, Iran. Later that same day, an Abu Dhabi National Oil Company (ADNOC) tanker, the Barakah, was struck by two drones north of Fujairah while empty &mdash; no injuries were reported, but the attack underlined Iranian capability and intent. Then on Monday May 4, an explosion caused a fire aboard the South Korean-operated HMM Namu while it was anchored off the UAE coast.",
            "President Trump on Truth Social said Iran had &ldquo;taken some shot&rdquo; at a South Korean cargo ship, without further detail. The British military&rsquo;s Maritime Trade Operations center reported two cargo vessels ablaze in the strait area. The U.K. Maritime Trade Operations (UKMTO) office said it had received reports of a tanker hit by projectiles approximately seven nautical miles north of Fujairah, with all crew safe and no environmental impact reported.",
            "Markets responded with the largest single-day rally in weeks. WTI crude futures jumped roughly 3% to settle at $105.09 per barrel, after spiking near $107 intraday. Brent crude rallied nearly 6% to settle at $114.44 &mdash; its highest closing price since May 2022. Both benchmarks briefly traded higher still on Iranian state media reports of a strike on a U.S. frigate, before pulling back when CENTCOM denied the report.",
            "&ldquo;The UAE has sustained more incoming fire from Iran than any other country over the past two months,&rdquo; CNN reported, noting that the UAE and Israel normalized relations under the Abraham Accords during President Trump&rsquo;s first term. The Fujairah strike represents both retaliation for U.S. naval activity in the strait and a calculated demonstration that Iran can degrade the strategic value of regional bypass infrastructure if pushed. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a> and <a href=\"strait-of-hormuz-explained.html\" style=\"color:var(--blue);text-decoration:none\">Strait of Hormuz explainer</a>.",
        ],
        "related": [
            ("U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys", "us-sinks-seven-iranian-boats-as-project-freedom-launches-hormuz-convoys"),
            ("WTI Surges to $105, Brent Tops $114 on Hormuz Exchange of Fire", "wti-surges-to-105-brent-tops-114-on-hormuz-exchange-of-fire"),
            ("Trump Declines to Confirm Ceasefire as Both Sides Trade Fire in Strait", "trump-declines-to-confirm-ceasefire-as-both-sides-trade-fire-in-strait"),
        ],
    },
    {
        "slug": "us-sinks-seven-iranian-boats-as-project-freedom-launches-hormuz-convoys",
        "title_variants": [
            "U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys",
            "CENTCOM: U.S. Forces Sink Seven Iranian Boats; Project Freedom Convoys Begin",
            "American Forces Destroy Iranian Small Craft as Two U.S. Ships Transit Hormuz",
            "Adm. Brad Cooper: U.S. Sinks Seven Iranian Boats Targeting Civilian Vessels",
            "Project Freedom Launches; U.S. Military Sinks Seven Iranian Boats in Strait",
        ],
        "display_title": "U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 4, 2026",
        "iso_date": "2026-05-04T15:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "5 min",
        "meta_desc": "CENTCOM commander Adm. Brad Cooper said Monday May 4 that U.S. forces opened a passage through the Strait of Hormuz free of Iranian mines and sank seven small Iranian boats targeting civilian ships. Two U.S.-flagged merchant vessels successfully transited Hormuz under Project Freedom.",
        "keywords": "Project Freedom Hormuz, US Navy Iran boats, CENTCOM Brad Cooper, Hormuz convoy, US Iran exchange of fire, Persian Gulf naval operations",
        "paragraphs": [
            "U.S. Central Command (CENTCOM) commander Adm. Brad Cooper announced Monday, May 4, 2026, that American forces had opened a passage through the Strait of Hormuz free of Iranian mines and sank seven small Iranian boats that had targeted civilian ships under U.S. military protection. The announcement marked the first major U.S. military action against Iranian targets since the April 8 ceasefire and the formal launch of &ldquo;Project Freedom&rdquo; &mdash; the Trump administration&rsquo;s initiative to restore commercial shipping through the strait.",
            "&ldquo;Iran launched multiple cruise missiles, drones and small boats at civilian ships under the U.S. military&rsquo;s protection,&rdquo; Cooper told reporters at a Pentagon briefing. &ldquo;U.S. military helicopters sank six of the small boats. Each and every threat had been defeated. The U.S. commanders who are on the scene have all the authority necessary to defend their unit and to defend commercial shipping.&rdquo; A subsequent CENTCOM update raised the count to seven boats destroyed.",
            "CENTCOM said two American-flagged merchant vessels successfully transited the Strait of Hormuz on Monday under the new initiative &mdash; the first commercial transits the U.S. has confirmed since shipping was effectively suspended in February. &ldquo;American forces are actively assisting efforts to restore transit for commercial shipping,&rdquo; CENTCOM wrote on X. &ldquo;As a first step, two U.S.-flagged merchant vessels have successfully transited through the Strait of Hormuz and are safely headed on their journey.&rdquo;",
            "Iran disputed the U.S. account through state media. Iran&rsquo;s Fars News Agency, aligned with the Islamic Revolutionary Guard Corps (IRGC), reported that a U.S. Navy frigate had been struck by two missiles after &ldquo;ignoring a warning from the Islamic Republic of Iran&rsquo;s Navy&rdquo; and was &ldquo;forced to retreat and flee the area.&rdquo; CENTCOM responded with an emphatic denial: &ldquo;No U.S. Navy ships have been struck. U.S. forces are supporting Project Freedom and enforcing the naval blockade on Iranian ports.&rdquo;",
            "Iran also disputed that any commercial transit had occurred. State-run news outlets claimed the U.S. military lied about helping two commercial vessels safely transit the strait, asserting that &ldquo;no commercial vessels or oil tankers have passed through the Strait of Hormuz in recent hours.&rdquo; The competing narratives reflect the high-stakes information warfare around what Treasury Secretary Scott Bessent on Fox News called &ldquo;absolute control&rdquo; of the strait by the U.S. Bessent dismissed Iran&rsquo;s navy as &ldquo;a band of pirates.&rdquo;",
            "Iran responded with explicit warnings. Maj. Gen. Ali Abdollahi told state broadcaster IRIB: &ldquo;We warn that any foreign military force &mdash; especially the aggressive U.S. military &mdash; that intends to approach or enter the Strait of Hormuz will be targeted.&rdquo; Iran has reportedly told vessels they need to coordinate with Iranian armed forces to transit, and signaled it would allow only Chinese-flagged ships through. The Chinese position is significant: President Trump is scheduled to visit Beijing next week, and unresolved hostilities could complicate his talks with Xi Jinping.",
            "President Trump described Project Freedom in humanitarian terms. He said Sunday that the U.S. would &ldquo;assist stranded vessels in the Persian Gulf&rdquo; under an operation aimed at ensuring safe passage, citing humanitarian concerns for crews facing food and water shortages on hundreds of ships stuck in the Persian Gulf since the war began. Shipping executives have responded cautiously: Simon Kaye of NorthStandard reinsurance told reporters there was &ldquo;no specificity about which countries have asked for this humanitarian mission, nor how this may be coordinated with Iran, if at all.&rdquo; For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>.",
        ],
        "related": [
            ("Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit", "iran-strikes-uae-fujairah-oil-hub-first-major-bypass-infrastructure-hit"),
            ("Trump Declines to Confirm Ceasefire as Both Sides Trade Fire in Strait", "trump-declines-to-confirm-ceasefire-as-both-sides-trade-fire-in-strait"),
            ("WTI Surges to $105, Brent Tops $114 on Hormuz Exchange of Fire", "wti-surges-to-105-brent-tops-114-on-hormuz-exchange-of-fire"),
        ],
    },
    {
        "slug": "wti-surges-to-105-brent-tops-114-on-hormuz-exchange-of-fire",
        "title_variants": [
            "WTI Surges to $105, Brent Tops $114 on Hormuz Exchange of Fire",
            "Crude Rallies as U.S., Iran Trade Fire in Strait; Brent Hits 4-Year High",
            "Oil Jumps 3-6% as Hormuz Exchange of Fire Shatters Ceasefire",
            "WTI Jumps to $105 and Brent Settles $114.44 — Highest Since May 2022",
            "Oil Markets Rally on Hormuz Hostilities; WTI $105, Brent $114",
        ],
        "display_title": "WTI Surges to $105, Brent Tops $114 on Hormuz Exchange of Fire",
        "category": "Oil Markets",
        "category_url": "../category/oil-prices.html",
        "date": "May 4, 2026",
        "iso_date": "2026-05-04T17:00:00-04:00",
        "section": "Oil Prices",
        "read_time": "5 min",
        "meta_desc": "WTI jumped 3% Monday to settle at $105.09. Brent rallied nearly 6% to settle at $114.44 — its highest close since May 2022. Both benchmarks briefly spiked higher intraday on reports of a U.S. frigate strike that CENTCOM later denied.",
        "keywords": "WTI crude price May 4, Brent crude price May 4, Hormuz exchange of fire oil, Project Freedom oil rally, Iran oil shock",
        "paragraphs": [
            "Crude oil markets rallied sharply Monday, May 4, 2026, on the heels of the largest single-day escalation since the U.S.-Iran ceasefire took hold in early April. WTI crude futures jumped approximately 3% to settle at $105.09 per barrel after touching $107 intraday. Brent crude rallied nearly 6% to settle at $114.44 &mdash; its highest closing price since May 2022. Both benchmarks briefly traded higher still on Iranian state media reports of a U.S. frigate strike, before pulling back when U.S. Central Command denied any U.S. Navy ships had been hit.",
            "The price action capped a weekend of escalating maritime incidents and culminated Monday with Iran launching 19 missiles and drones at the United Arab Emirates and the U.S. military sinking seven small Iranian boats during the launch of Project Freedom &mdash; the new American initiative to restore commercial shipping through the strait. Two U.S.-flagged merchant vessels transited the strait Monday under U.S. naval escort, the first such transits the U.S. has confirmed since February.",
            "The intraday volatility was extreme. Brent briefly spiked to $114.10 then surged again to settle at $114.44 after Iran&rsquo;s Fars News Agency claimed a U.S. Navy frigate near the Gulf of Oman port of Jask had been struck by two missiles. CENTCOM denied the claim within hours, but the volatility itself underlined how thinly priced the market is for any direct U.S.-Iran kinetic exchange. Traders paid up for both upside and downside protection through option markets, and implied volatility on near-dated WTI calls climbed to multi-month highs.",
            "Underlying the rally is the structural reality that Persian Gulf oil flows remain deeply impaired. Saudi Arabia continues to divert as much crude as possible via the East-West Pipeline to Yanbu (5 million bpd capacity), and the UAE via ADCOP to Fujairah (1.8 million bpd capacity). Combined bypass capacity of about 7 million bpd is far below the roughly 20 million bpd that normally transits Hormuz. The Iranian strike on the Fujairah Oil Industry Zone Monday added a new layer of risk: bypass infrastructure itself is now targetable.",
            "U.S. crude exports continue to set records as global buyers turn to American producers. Cushing crude inventories remain below the five-year average. Refiners are running hard, but the gasoline crack spread has compressed as U.S. retail pump prices catch up with crude. Rig counts have not yet responded materially: Baker Hughes data Friday showed 584 active U.S. land rigs, down five from the prior week and down 47 year-over-year &mdash; an indication that producers are prioritizing free cash flow over volume growth even at $100+ crude.",
            "European and Asian benchmarks moved in tandem. Murban crude rallied nearly 6% to $116.50, jet fuel jumped 3.6% to $4.62 per gallon. Heating oil and ULSD diesel both rose 3% to $4.24, the highest since 2022. Coal firmed to $140.20 per ton on power-sector substitution demand as natural gas prices remain elevated. The breadth of the rally signals that traders are now repricing not just the Iranian war risk but the medium-term structural premium for energy security globally.",
            "AAA reported the U.S. national average for regular gasoline reached $4.457 per gallon Monday, up from $4.392 Friday and $4.144 a week earlier. Tennessee crossed $4 for the first time since July 2022. California is averaging above $6.11. The pump-level pass-through from Tuesday April 28&rsquo;s crude rally is still flowing through to retail with a multi-day lag, and Monday&rsquo;s settle suggests another leg up later this week. For continuing coverage, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices dashboard</a> and <a href=\"../category/gas-prices.html\" style=\"color:var(--blue);text-decoration:none\">U.S. gas prices</a>.",
        ],
        "related": [
            ("Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit", "iran-strikes-uae-fujairah-oil-hub-first-major-bypass-infrastructure-hit"),
            ("U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys", "us-sinks-seven-iranian-boats-as-project-freedom-launches-hormuz-convoys"),
            ("U.S. Gas Average Climbs to $4.46, Up Another 6 Cents Over Weekend", "us-gas-average-climbs-to-446-up-another-6-cents-over-weekend"),
        ],
    },
    {
        "slug": "trump-declines-to-confirm-ceasefire-as-both-sides-trade-fire-in-strait",
        "title_variants": [
            "Trump Declines to Confirm Ceasefire as Both Sides Trade Fire in Strait",
            "Ceasefire in Doubt as Trump Refuses to Confirm Truce Amid Hormuz Hostilities",
            "Trump Won't Say if Iran Ceasefire Holds After Both Sides Exchange Fire",
            "Bessent: U.S. Has 'Absolute Control' of Hormuz; Trump Silent on Ceasefire",
            "April 8 Ceasefire in Question After Monday's Hormuz Exchange of Fire",
        ],
        "display_title": "Trump Declines to Confirm Ceasefire as Both Sides Trade Fire in Strait",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 4, 2026",
        "iso_date": "2026-05-04T18:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "5 min",
        "meta_desc": "President Trump on Monday May 4 declined to say whether the April 8 ceasefire with Iran remains in place. The hostilities directly contradict Trump's letter to Congress on Friday claiming 'no exchange of fire' since April 7 and that 'hostilities have terminated' under the War Powers Resolution.",
        "keywords": "Trump ceasefire Iran, War Powers Resolution Iran, hostilities terminated Iran, Bessent absolute control Hormuz, April 8 ceasefire",
        "paragraphs": [
            "President Donald Trump on Monday, May 4, 2026, declined to say whether the fragile U.S.-Iran ceasefire that took hold in early April remains in place after both sides exchanged fire in the Strait of Hormuz. Speaking briefly to reporters at the White House, the President was asked directly whether the truce still applied; he sidestepped the question, leaving open whether the United States now considers itself to be at a renewed state of hostilities with Iran.",
            "The presidential silence is significant for legal and political reasons that go beyond the symbolic. On Friday, April 30, Trump sent nearly identical letters to House Speaker Mike Johnson and Senate leader Chuck Grassley invoking the 1973 War Powers Resolution. &ldquo;There has been no exchange of fire between the United States Forces and Iran since April 7, 2026,&rdquo; the President wrote. &ldquo;The hostilities that began on February 28, 2026 have terminated.&rdquo; The April 30 letters &mdash; sent at the 60-day mark of the conflict &mdash; were intended to satisfy War Powers Resolution requirements that a president must withdraw forces within 60 days of notifying Congress unless lawmakers authorize the action.",
            "Monday&rsquo;s exchange of fire directly contradicts both factual claims in those letters. CENTCOM acknowledged sinking seven Iranian boats. Iran launched 19 missiles and drones at the UAE. The Fujairah Oil Industry Zone is on fire. The HMM Namu and ADNOC Barakah have both been hit. The framing of &ldquo;hostilities terminated&rdquo; is no longer factually defensible, and several members of Congress &mdash; both Republican and Democratic &mdash; have already pushed back on the administration&rsquo;s broader War Powers interpretation.",
            "Treasury Secretary Scott Bessent struck a defiant tone in a Fox News appearance Monday morning, saying the U.S. has &ldquo;absolute control&rdquo; of the Strait of Hormuz and dismissing Iran&rsquo;s navy as &ldquo;a band of pirates.&rdquo; The framing aligns with the administration&rsquo;s position that Project Freedom is a defensive, humanitarian operation rather than a resumption of hostilities &mdash; but the on-the-ground reality is harder to fit into that frame. CENTCOM has acknowledged that U.S. military helicopters destroyed Iranian vessels under direct fire engagement.",
            "Iran&rsquo;s response has been blunt. Maj. Gen. Ali Abdollahi, an Iranian senior commander, told state TV: &ldquo;We warn that any foreign military force &mdash; especially the aggressive U.S. military &mdash; that intends to approach or enter the Strait of Hormuz will be targeted.&rdquo; Iran has reportedly told vessels they need to coordinate with Iranian armed forces, signaled it would allow only Chinese-flagged ships through, and questioned U.S. claims about what is happening in the strait. State-run Iranian media on Monday claimed no commercial vessels or oil tankers had transited the strait, contradicting CENTCOM.",
            "The geopolitical dimension extends to Beijing. Trump is scheduled to visit Beijing next week &mdash; a trip he initially delayed from April while the conflict raged. China has called for the Strait of Hormuz to be reopened, and a meaningful share of the energy products China relies upon transits the strait. Arriving in Beijing with hostilities at best unresolved &mdash; or at worst actively underway &mdash; would place Trump in a weakened negotiating position with Xi Jinping. The administration has not commented on whether Monday&rsquo;s events affect the Beijing visit.",
            "The legal status matters because the ceasefire has been the formal predicate for the administration&rsquo;s position that the conflict is over. If hostilities have resumed, Congress&rsquo;s leverage to compel withdrawal or authorization grows. If they have not &mdash; per the administration&rsquo;s framing &mdash; then the U.S. is conducting active naval combat operations under War Powers cover for the indefinite future. Either reading is tenable; neither is comfortable. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>.",
        ],
        "related": [
            ("U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys", "us-sinks-seven-iranian-boats-as-project-freedom-launches-hormuz-convoys"),
            ("Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit", "iran-strikes-uae-fujairah-oil-hub-first-major-bypass-infrastructure-hit"),
            ("WTI Surges to $105, Brent Tops $114 on Hormuz Exchange of Fire", "wti-surges-to-105-brent-tops-114-on-hormuz-exchange-of-fire"),
        ],
    },
    {
        "slug": "us-gas-average-climbs-to-446-up-another-6-cents-over-weekend",
        "title_variants": [
            "U.S. Gas Average Climbs to $4.46, Up Another 6 Cents Over Weekend",
            "AAA: National Gas Average Hits $4.457 — Highest in Four Years",
            "Tennessee Crosses $4 as National Gas Average Climbs to $4.46",
            "U.S. Gasoline Surges to $4.457; California Above $6.11",
            "Gas Prices Continue Climb; National Average Reaches $4.46 on May 4",
        ],
        "display_title": "U.S. Gas Average Climbs to $4.46, Up Another 6 Cents Over Weekend",
        "category": "Gas Prices",
        "category_url": "../category/gas-prices.html",
        "date": "May 4, 2026",
        "iso_date": "2026-05-04T14:00:00-04:00",
        "section": "Gas Prices",
        "read_time": "4 min",
        "meta_desc": "AAA reported Monday May 4 the U.S. national average for regular gasoline reached $4.457 per gallon, up from $4.392 Friday. Tennessee crossed $4 for the first time since July 2022. California averaging above $6.11. National average $1.29 higher than year-ago.",
        "keywords": "AAA gas prices May 4, US gas average $4.46, Tennessee gas $4, California gas $6, Iran conflict pump prices",
        "paragraphs": [
            "AAA reported Monday, May 4, 2026, that the U.S. national average for a gallon of regular unleaded gasoline reached $4.457, up roughly six cents from Friday&rsquo;s $4.392 and approximately 31 cents higher than two weeks ago. The reading is the highest national average since late July 2022, and reflects the continued pass-through of crude oil&rsquo;s rally amid the ongoing Iran-Hormuz conflict to retail pump prices.",
            "Tennessee&rsquo;s state average crossed $4.00 per gallon for the first time since July 2022. The state average reached $4.03, up 18 cents from a month ago and $1.31 higher than a year ago. &ldquo;We saw a 26-cent jump in our state gas price average over last week,&rdquo; said Megan Cooper, AAA spokeswoman for The Auto Club Group. &ldquo;Another surge in crude oil prices due to the ongoing Iranian conflict and closure of the Strait of Hormuz is placing additional upward pressure on pump prices. It&rsquo;s likely that drivers will continue to see increases in pump prices again this week.&rdquo;",
            "Regional variation remains extreme. California is now averaging above $6.11 per gallon &mdash; well into territory that historically has prompted state-level political intervention. The Midwest spike that began with the Indiana refinery issue continues to ripple through neighboring states; Michigan averages $4.86, Illinois (anchored by Chicago) sits near $5.10, and Ohio has crossed $4.40. The lowest-priced states &mdash; Mississippi, Oklahoma, Louisiana &mdash; remain below $4.00 but are climbing fast.",
            "The national average is now $1.29 higher than it was at this time last year. Gas prices reflect a multi-day lag from crude price changes, which means Monday&rsquo;s WTI rally to $105.09 and Brent surge to $114.44 will continue to push pump prices higher into next week even if the Hormuz situation stabilizes. EIA data released last week showed gasoline demand increased to 9.10 million barrels per day; total domestic gasoline supply decreased to 222.3 million barrels; gasoline production fell to an average of 9.8 million barrels per day &mdash; the combination of rising demand and falling production is the textbook recipe for higher retail prices.",
            "Diesel prices have rallied even harder than gasoline. The U.S. diesel average sits at $6.118 per gallon, with rural agricultural states &mdash; whose economies depend heavily on diesel for trucking, farming, and rail &mdash; particularly exposed. Heating oil futures rallied 3% Monday to $4.24 per gallon, just below the all-time record. The diesel-to-gasoline price differential is now the widest since 2022, signaling tight middle distillate supply globally.",
            "EIA reports crude inventories decreased by 6.2 million barrels last week from the prior week. At 459.5 million barrels, U.S. crude inventories are about 1% above the five-year average for this time of year &mdash; a comfortable buffer historically, but rapidly shrinking as refiners run hard to capture record gasoline crack spreads. The EIA&rsquo;s next weekly inventory report is due Wednesday, May 6. For continuing coverage, see our <a href=\"../category/gas-prices.html\" style=\"color:var(--blue);text-decoration:none\">U.S. gas prices dashboard</a> and <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices</a>.",
        ],
        "related": [
            ("WTI Surges to $105, Brent Tops $114 on Hormuz Exchange of Fire", "wti-surges-to-105-brent-tops-114-on-hormuz-exchange-of-fire"),
            ("Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit", "iran-strikes-uae-fujairah-oil-hub-first-major-bypass-infrastructure-hit"),
            ("U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys", "us-sinks-seven-iranian-boats-as-project-freedom-launches-hormuz-convoys"),
        ],
    },
]


def render(s):
    title_safe = s["display_title"].replace('"', '&quot;')
    headline_safe = s["display_title"].replace('"', '\\"').replace("'", "\u2019")
    desc_safe = s["meta_desc"].replace('"', '\\"').replace("'", "\u2019")
    canonical = f"https://www.energypricestoday.com/articles/{s['slug']}.html"
    cat_label = s["category"]

    word_count = sum(len(p.split()) for p in s["paragraphs"])
    paragraphs = "\n          ".join(f"<p>{p}</p>" for p in s["paragraphs"])

    related_items = "\n            ".join(
        f'<li><a href="{slug}.html" style="color:var(--text-1);text-decoration:none">{title}</a></li>'
        for title, slug in s["related"]
    )

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
  <link rel="stylesheet" href="../css/styles.css?v=23">
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
          <a href="strait-of-hormuz-explained.html" class="btn-secondary">Hormuz Explainer</a>
        </div>
      </div>
    </article>
  </main>
  <footer class="site-footer" id="site-footer"></footer>
  <script src="../js/data.js?v=23"></script>
  <script src="../js/article-slugs.js?v=23"></script>
  <script src="../js/main.js?v=23"></script>
</body>
</html>
'''


def main():
    for s in STORIES:
        out = ARTICLES_DIR / f"{s['slug']}.html"
        out.write_text(render(s), encoding="utf-8")
        print(f"  wrote {out.name}")
    print(f"✓ Generated {len(STORIES)} articles for May 4, 2026.")


if __name__ == "__main__":
    main()
