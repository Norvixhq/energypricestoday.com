/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Data Layer
   All mock data in one place for easy future API replacement
   ═══════════════════════════════════════════════════════════════════ */

const COMMODITIES = [
  { name: "WTI Crude", price: 105.09, change: 3.15, pct: 3.09, unit: "$/bbl", spark: [99.93,103.40,105.80,108.20,111.05,101.94,105.09], loading: false },
  { name: "Brent Crude", price: 114.44, change: 6.27, pct: 5.80, unit: "$/bbl", spark: [111.26,112.50,113.40,114.10,114.05,108.17,114.44], loading: false },
  { name: "Natural Gas", price: 2.74, change: 0.06, pct: 2.24, unit: "$/MMBtu", spark: [2.61,2.63,2.65,2.66,2.69,2.68,2.74], loading: false },
  { name: "Gasoline RBOB", price: 3.51, change: 0.09, pct: 2.63, unit: "$/gal", spark: [3.34,3.36,3.39,3.42,3.46,3.42,3.51], loading: false },
  { name: "Heating Oil", price: 4.24, change: 0.12, pct: 2.91, unit: "$/gal", spark: [4.04,4.06,4.09,4.12,4.16,4.12,4.24], loading: false },
  { name: "Murban Crude", price: 116.50, change: 6.00, pct: 5.43, unit: "$/bbl", spark: [112.05,112.80,113.20,113.50,113.10,110.50,116.50], loading: false },
  { name: "Diesel ULSD", price: 4.24, change: 0.12, pct: 2.91, unit: "$/gal", spark: [4.04,4.06,4.09,4.12,4.16,4.12,4.24], loading: false },
  { name: "Jet Fuel", price: 4.62, change: 0.16, pct: 3.59, unit: "$/gal", spark: [4.38,4.40,4.42,4.44,4.50,4.46,4.62], loading: false },
  { name: "Coal", price: 140.2, change: 1.7, pct: 1.23, unit: "$/ton", spark: [137.4,137.6,137.8,138.0,138.2,138.5,140.2], loading: false },
  { name: "Gold", price: 4742.10, change: 31.25, pct: 0.66, unit: "$/oz", spark: [], loading: false },
];

const FULL_PRICES = {
  "All Prices": [
    ...COMMODITIES,
    { name: "Dubai Fateh", price: 73.56, change: 0.92, pct: 1.27, unit: "$/bbl", spark: [71,72,72.5,73,73.2,73.4,73.56] },
    { name: "Louisiana Light", price: 100.8, change: 1.10, pct: 1.53, unit: "$/bbl", spark: [70,71,71.5,72,72.3,72.6,72.85] },
  ],
  "OPEC Blends": [
    { name: "OPEC Basket", price: 94.8, change: 0.65, pct: 0.88, unit: "$/bbl", spark: [72,73,73.5,73.8,74,74.1,74.12] },
    { name: "Arab Light", price: 75.20, change: 0.78, pct: 1.05, unit: "$/bbl", spark: [73,74,74.5,74.8,75,75.1,75.2] },
    { name: "Bonny Light", price: 76.45, change: 1.02, pct: 1.35, unit: "$/bbl", spark: [74,75,75.5,75.8,76,76.2,76.45] },
    { name: "Iran Heavy", price: 70.88, change: 0.44, pct: 0.62, unit: "$/bbl", spark: [69,70,70.2,70.5,70.6,70.7,70.88] },
    { name: "Kuwait Export", price: 73.65, change: 0.55, pct: 0.75, unit: "$/bbl", spark: [72,72.5,73,73.2,73.4,73.5,73.65] },
  ],
  "U.S. Blends": [
    { name: "WTI Crude", price: 96.57, change: -1.3, pct: -1.33, unit: "$/bbl", spark: [68,69,70,69.5,70.2,71,71.48] },
    { name: "Louisiana Light", price: 72.85, change: 1.10, pct: 1.53, unit: "$/bbl", spark: [70,71,71.5,72,72.3,72.6,72.85] },
    { name: "WTI Midland", price: 100.12, change: 1.18, pct: 1.67, unit: "$/bbl", spark: [69,70,70.5,71,71.3,71.6,71.92] },
    { name: "Mars Blend", price: 69.50, change: 0.95, pct: 1.39, unit: "$/bbl", spark: [67,68,68.5,69,69.2,69.3,69.5] },
    { name: "Eagle Ford", price: 70.15, change: 1.05, pct: 1.52, unit: "$/bbl", spark: [68,69,69.5,69.8,70,70.1,70.15] },
  ],
  "Canadian Blends": [
    { name: "Western Canadian Select", price: 78.5, change: 0.85, pct: 1.51, unit: "$/bbl", spark: [55,56,56.5,56.8,57,57.1,57.2] },
    { name: "Syncrude Sweet", price: 71.10, change: 1.15, pct: 1.64, unit: "$/bbl", spark: [69,70,70.5,70.8,71,71.05,71.1] },
    { name: "Cold Lake Blend", price: 56.80, change: 0.72, pct: 1.28, unit: "$/bbl", spark: [55,55.5,56,56.3,56.5,56.7,56.8] },
    { name: "Peace Sour", price: 62.45, change: 0.90, pct: 1.46, unit: "$/bbl", spark: [60,61,61.5,62,62.2,62.3,62.45] },
  ],
  "Refined Products": [
    { name: "Gasoline RBOB", price: 3.018, change: 0.037, pct: 1.22, unit: "$/gal", spark: [2.1,2.12,2.14,2.15,2.16,2.17,2.18] },
    { name: "Heating Oil", price: 3.74, change: -0.198, pct: -5.03, unit: "$/gal", spark: [2.38,2.37,2.36,2.35,2.35,2.34,2.34] },
    { name: "Diesel", price: 2.41, change: 0.03, pct: 1.26, unit: "$/gal", spark: [2.35,2.36,2.38,2.39,2.4,2.405,2.41] },
    { name: "Jet Fuel", price: 4.09, change: -0.14, pct: -3.31, unit: "$/gal", spark: [2.44,2.46,2.48,2.49,2.5,2.51,2.52] },
    { name: "Naphtha", price: 618.50, change: 4.20, pct: 0.68, unit: "$/mt", spark: [610,612,614,616,617,618,618.5] },
  ],
  "Natural Gas": [
    { name: "Henry Hub", price: 3.42, change: -0.08, pct: -2.29, unit: "$/MMBtu", spark: [3.6,3.55,3.5,3.48,3.45,3.44,3.42] },
    { name: "TTF Dutch", price: 11.85, change: 0.32, pct: 2.77, unit: "€/MWh", spark: [11,11.2,11.4,11.5,11.6,11.7,11.85] },
    { name: "UK NBP", price: 0.92, change: 0.02, pct: 2.22, unit: "p/therm", spark: [0.88,0.89,0.9,0.905,0.91,0.915,0.92] },
    { name: "JKM LNG", price: 12.40, change: -0.15, pct: -1.20, unit: "$/MMBtu", spark: [12.8,12.7,12.6,12.55,12.5,12.45,12.4] },
  ],
};

const BREAKING_NEWS = [
  { title: "Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit", cat: "Geopolitics", slug: "geopolitics", time: "1h" },
  { title: "U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys", cat: "Geopolitics", slug: "geopolitics", time: "3h" },
  { title: "WTI Surges to $105, Brent Tops $114 on Hormuz Exchange of Fire", cat: "Oil Markets", slug: "oil-prices", time: "4h" },
  { title: "Iran Launches 19 Missiles and Drones at UAE; Air Defenses Intercept 15+", cat: "Geopolitics", slug: "geopolitics", time: "5h" },
  { title: "Trump's 'Project Freedom' Begins Reopening Hormuz Despite Iranian Fire", cat: "Geopolitics", slug: "geopolitics", time: "6h" },
  { title: "U.S. Gas Average Climbs to $4.46, Up Another 6 Cents Over Weekend", cat: "Gas Prices", slug: "gas-prices", time: "8h" },
  { title: "South Korean HMM Namu Hit by Explosion and Fire Off UAE Coast", cat: "Geopolitics", slug: "geopolitics", time: "12h" },
  { title: "ADNOC Tanker Barakah Struck by Drones North of Fujairah", cat: "Geopolitics", slug: "geopolitics", time: "1d" },
];

const MARKET_DRIVERS = [
  { cat: "Hormuz Escalation", icon: "alert-triangle", title: "Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit", desc: "Iran launched 19 missiles and drones at the UAE on Monday May 4. Most were intercepted by Emirati air defenses, but a drone struck the Fujairah Oil Industry Zone, sparking a major fire and wounding three Indian nationals. Fujairah is the terminus of the UAE's ADCOP pipeline that bypasses the strait. First major hit on bypass infrastructure since the conflict began." },
  { cat: "Oil Markets", icon: "trending-up", title: "WTI Surges to $105, Brent Tops $114 on Hormuz Exchange of Fire", desc: "WTI jumped 3% Monday to settle at $105.09 after intraday peak near $107. Brent rallied 5% to $114.44, highest settle since May 2022. Markets responding to weekend escalation: ADNOC tanker hit, HMM Namu fire, Iranian missile salvo at UAE, U.S. military sinking 7 small Iranian boats during Project Freedom convoy." },
  { cat: "U.S. Action", icon: "shield", title: "U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys", desc: "CENTCOM commander Adm. Brad Cooper said American forces opened a passage through the strait free of Iranian mines and sank seven small Iranian boats targeting civilian ships. Two U.S.-flagged merchant vessels successfully transited Hormuz under Project Freedom on Monday — first major U.S. action since the April 8 ceasefire." },
  { cat: "Pump Prices", icon: "fuel", title: "U.S. Gas Average Climbs to $4.46, Up 6 More Cents Over Weekend", desc: "AAA reported Monday the U.S. national average for regular gasoline reached $4.457 per gallon, up from $4.392 Friday. Tennessee crossed $4 for the first time since July 2022. California averaging above $6.11. Gas prices now $1.29 higher than year-ago. Pump-level pass-through from rolling crude rally continues with multi-day lag." },
  { cat: "Ceasefire Status", icon: "users", title: "Trump Declines to Confirm Ceasefire as Both Sides Trade Fire", desc: "President Trump on Monday declined to say whether the April 8 ceasefire remains in place after both sides exchanged fire in the strait. Trump told Congress Friday that 'hostilities have terminated' under the War Powers Resolution, citing no exchange of fire since April 7 — a claim now obviously false. Treasury Sec. Bessent said the U.S. has 'absolute control' of Hormuz and called Iran's navy 'a band of pirates.'" },
  { cat: "Hormuz", icon: "anchor", title: "Iran Threatens 'Aggressive' Foreign Military Forces Approaching Strait", desc: "Iranian Maj. Gen. Ali Abdollahi warned via state TV: 'Any foreign military force — especially the aggressive U.S. military — that intends to approach or enter the Strait of Hormuz will be targeted.' Iran has reportedly told vessels they need to coordinate with its armed forces, and signaled it will allow only Chinese vessels through. Conflict now in its eleventh week." },
];

const FEATURED_ARTICLES = [
  { id: 101, title: "Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit", excerpt: "Iran launched 19 missiles and drones at the UAE on Monday May 4. Most were intercepted by Emirati air defenses, but a drone struck the Fujairah Oil Industry Zone, sparking a major fire and wounding three Indian nationals. Fujairah is the terminus of the UAE's ADCOP pipeline that bypasses the strait — the first major hit on bypass infrastructure since the conflict began.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "May 4, 2026", readTime: "6 min", featured: true },
  { id: 102, title: "U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys", excerpt: "CENTCOM commander Adm. Brad Cooper said Monday that U.S. forces opened a passage through the strait free of Iranian mines and sank seven small Iranian boats targeting civilian ships. Two U.S.-flagged merchant vessels successfully transited Hormuz under Project Freedom — the first major U.S. military action against Iranian targets since the April 8 ceasefire.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "May 4, 2026", readTime: "5 min" },
  { id: 103, title: "WTI Surges to $105, Brent Tops $114 on Hormuz Exchange of Fire", excerpt: "WTI jumped 3% Monday to settle at $105.09, Brent rallied 5% to $114.44 — its highest settle since May 2022. Both benchmarks briefly spiked higher intraday on Iranian state media reports of a U.S. frigate strike, before pulling back when CENTCOM denied any U.S. Navy ships had been hit. Markets responding to the weekend escalation.", cat: "Oil Markets", slug: "oil-prices", author: "EnergyPricesToday Editorial", date: "May 4, 2026", readTime: "5 min" },
  { id: 104, title: "Trump Declines to Confirm Ceasefire as Both Sides Trade Fire in Strait", excerpt: "President Trump on Monday declined to say whether the April 8 ceasefire with Iran remains in place after both sides exchanged fire in the strait. The hostilities directly contradict Trump's letter to Congress on Friday claiming 'no exchange of fire' since April 7 and that 'hostilities have terminated' under the War Powers Resolution.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "May 4, 2026", readTime: "5 min" },
  { id: 105, title: "U.S. Gas Average Climbs to $4.46, Up Another 6 Cents Over Weekend", excerpt: "AAA reported Monday the U.S. national average for regular gasoline reached $4.457 per gallon, up from $4.392 on Friday. Tennessee crossed $4 for the first time since July 2022. California is averaging above $6.11. Gas prices now $1.29 higher than this time last year, as ongoing crude rally continues passing through to retail with a multi-day lag.", cat: "Gas Prices", slug: "gas-prices", author: "EnergyPricesToday Editorial", date: "May 4, 2026", readTime: "4 min" },
];

const COMPANY_NEWS = [
  { id: 201, title: "ADNOC Tanker Barakah Struck by Drones North of Fujairah", date: "May 4, 2026" },
  { id: 202, title: "South Korean HMM Namu Hit by Explosion and Fire Off UAE Coast", date: "May 4, 2026" },
  { id: 203, title: "Cheniere Energy, Venture Global Ride LNG Premium as Qatar Flows Disrupted", date: "May 3, 2026" },
  { id: 204, title: "ExxonMobil Q1 Profit Falls to 5-Year Low at $4.2B Despite Beating Estimates", date: "May 1, 2026" },
  { id: 205, title: "Chevron Posts Biggest Earnings Beat Since 2020 on Record Production", date: "May 1, 2026" },
  { id: 206, title: "Saudi Aramco East-West Pipeline Continues at Full Capacity Through Blockade", date: "Apr 30, 2026" },
];

const GEO_ITEMS = [
  { id: 301, region: "United Arab Emirates", title: "Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit", desc: "Iran launched 19 missiles and drones at the UAE on Monday May 4 — the first major attack since the April 8 ceasefire. Most were intercepted, but a drone struck the Fujairah Oil Industry Zone, sparking a major fire and wounding three Indian nationals. Fujairah is the terminus of the UAE's ADCOP pipeline that bypasses the strait. The Emirati Foreign Ministry called the attack 'a dangerous escalation and an unacceptable violation.'" },
  { id: 302, region: "Persian Gulf", title: "U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys", desc: "CENTCOM commander Adm. Brad Cooper said Monday May 4 that American forces opened a passage through the strait free of Iranian mines and sank seven small Iranian boats targeting civilian ships. Two U.S.-flagged merchant vessels successfully transited Hormuz under the new Project Freedom initiative. Iran's Fars news agency claimed a U.S. frigate had been hit; CENTCOM denied any U.S. Navy ships were struck." },
  { id: 303, region: "United States", title: "Trump Declines to Confirm Ceasefire as Both Sides Trade Fire in Strait", desc: "President Trump on Monday declined to say whether the April 8 ceasefire remains in place. Treasury Sec. Bessent said the U.S. has 'absolute control' of Hormuz and dismissed Iran's navy as 'a band of pirates.' Trump's letter to Congress on Friday April 30 — claiming 'no exchange of fire since April 7' and that 'hostilities have terminated' — was directly contradicted by Monday's exchange of fire." },
  { id: 304, region: "Iran", title: "Iran Threatens 'Aggressive' Foreign Military Forces Approaching Strait", desc: "Iranian Maj. Gen. Ali Abdollahi warned via state TV: 'Any foreign military force — especially the aggressive U.S. military — that intends to approach or enter the Strait of Hormuz will be targeted.' Iran has reportedly told vessels they need to coordinate with Iranian armed forces to transit, and signaled it will allow only Chinese vessels through. Conflict now in its eleventh week." },
  { id: 305, region: "Persian Gulf", title: "ADNOC Tanker Barakah Struck by Drones; HMM Namu Hit by Explosion", desc: "Sunday May 3: ADNOC's empty tanker Barakah was hit by two drones north of Fujairah; no injuries. Monday May 4: an explosion caused a fire aboard the South Korean-operated HMM Namu while anchored off the UAE. The British military's Maritime Trade Operations center reported two cargo vessels ablaze in the strait. The pace of maritime incidents has accelerated sharply this week." },
  { id: 306, region: "Lebanon", title: "Hezbollah-IDF Firefight Wounds Two Israeli Soldiers Amid Lebanon Ceasefire", desc: "Lebanon's National News Agency reported clashes Monday between Hezbollah and Israeli forces in the south. Both Hezbollah and the Israeli military acknowledged a firefight that wounded two Israeli soldiers. Lebanese authorities say Israeli operations have killed more than 2,600 people and displaced more than 1 million. Preparatory talks for further Israel-Lebanon negotiations expected in Washington." },
];

const CATEGORIES = {
  "oil-prices":        { name: "Oil Prices",        icon: "trending-up",  desc: "Live crude oil pricing, benchmarks, and historical data for WTI, Brent, and global blends." },
  "oil-futures":       { name: "Oil Futures",        icon: "line-chart",   desc: "Futures contracts, forward curves, and derivatives market analysis for crude oil." },
  "rig-count":         { name: "Rig Count",          icon: "hard-hat",     desc: "Weekly rig count data for U.S. and international drilling activity." },
  "energy":            { name: "Energy",             icon: "zap",          desc: "Comprehensive energy sector news spanning oil, gas, power, and renewables." },
  "crude-oil":         { name: "Crude Oil",          icon: "droplets",     desc: "Production, refining, and trade news for global crude oil markets." },
  "gas-prices":        { name: "Gas Prices",         icon: "fuel",         desc: "Retail and wholesale gasoline pricing across the United States." },
  "natural-gas":       { name: "Natural Gas",        icon: "flame",        desc: "Henry Hub, TTF, and global natural gas market coverage." },
  "heating-oil":       { name: "Heating Oil",        icon: "thermometer",  desc: "Heating oil prices, supply, and seasonal demand analysis." },
  "geopolitics":       { name: "Geopolitics",        icon: "globe",        desc: "How global politics, sanctions, and conflicts shape energy markets." },
  "company-news":      { name: "Company News",       icon: "building",     desc: "Earnings, deals, and strategy from the world's biggest energy companies." },
  "alternative-energy":{ name: "Alternative Energy",  icon: "sun",          desc: "Solar, wind, hydrogen, and emerging clean energy technologies." },
  "nuclear":           { name: "Nuclear",            icon: "atom",         desc: "Nuclear energy policy, reactor development, and uranium market news." },
  "solar":             { name: "Solar",              icon: "sun",          desc: "Solar energy deployment, policy, and technology developments." },
  "wind":              { name: "Wind",               icon: "wind",         desc: "Onshore and offshore wind energy projects and market trends." },
  "renewable-energy":  { name: "Renewable Energy",   icon: "leaf",         desc: "The transition to sustainable energy sources and its market impacts." },
};

const CATEGORY_ARTICLES = [
  { id: 401, title: "Markets React to Unexpected Inventory Build in Cushing Hub", excerpt: "Cushing, Oklahoma storage levels rose by 1.8M barrels last week, pressuring nearby WTI spreads.", date: "Apr 13, 2026", author: "Staff", readTime: "5 min" },
  { id: 402, title: "Goldman Sachs Raises Brent Crude Forecast to $82 by Year-End", excerpt: "The bank cites stronger-than-expected demand from emerging markets and constrained OPEC+ supply.", date: "Apr 13, 2026", author: "Staff", readTime: "4 min" },
  { id: 403, title: "Iraq Struggles to Meet OPEC+ Production Quota Compliance", excerpt: "Baghdad's oil output consistently exceeds its agreed ceiling, creating tension within the alliance.", date: "Apr 13, 2026", author: "Staff", readTime: "6 min" },
  { id: 404, title: "Global Oil Demand Growth Slows to 900K BPD in 2026, IEA Says", excerpt: "The International Energy Agency revises down its demand growth estimate amid economic headwinds.", date: "Apr 13, 2026", author: "Staff", readTime: "5 min" },
  { id: 405, title: "New Deepwater Discovery Off Guyana Could Hold 1.5 Billion Barrels", excerpt: "ExxonMobil's latest exploration well confirms significant hydrocarbon reserves in the Stabroek Block.", date: "Apr 13, 2026", author: "Staff", readTime: "7 min" },
  { id: 406, title: "Keystone Pipeline Restarts After Maintenance Shutdown", excerpt: "TC Energy confirms the pipeline is back to full capacity after a scheduled two-week maintenance window.", date: "Apr 13, 2026", author: "Staff", readTime: "3 min" },
];

const TRENDING_TOPICS = [
  "OPEC+ Production Cuts",
  "Permian Basin Output",
  "LNG Export Boom",
  "Red Sea Disruptions",
  "Energy Transition",
];

const CATEGORY_LIST_FOR_SPOTLIGHTS = [
  { slug: "oil-prices",         name: "Oil Prices",        icon: "trending-up" },
  { slug: "natural-gas",        name: "Natural Gas",        icon: "flame" },
  { slug: "geopolitics",        name: "Geopolitics",        icon: "globe" },
  { slug: "company-news",       name: "Company News",       icon: "building" },
  { slug: "alternative-energy", name: "Alternative Energy",  icon: "sun" },
  { slug: "rig-count",          name: "Rig Count",          icon: "hard-hat" },
];

const RIG_COUNT_DATA = {
  // U.S. — Baker Hughes North America Rig Count, May 1, 2026
  us_total: 545, us_total_change: 1, us_oil: 408, us_oil_change: 1, us_gas: 129, us_gas_change: 0, us_misc: 8, us_misc_change: 0,
  us_land: 534, us_offshore: 11, us_inland: 0,
  us_directional: 48, us_horizontal: 485, us_vertical: 12,
  us_yoy: -42, us_yoy_total: 587,
  us_gom: 10,
  // Canada — May 1, 2026 (spring breakup continues)
  canada_total: 122, canada_change: -8, canada_oil: 74, canada_gas: 48,
  canada_yoy: -10, canada_yoy_total: 132,
  // North America
  na_total: 667, na_change: -7, na_yoy: -52, na_yoy_total: 719,
  // International — March 2026 (monthly report; April report due May 4)
  intl_total: 1058, intl_change: -54, intl_yoy: -37, intl_yoy_total: 1095,
  intl_mideast: 500, intl_mideast_change: -38,
  intl_latam: 143, intl_latam_change: 5,
  intl_europe: 124, intl_europe_change: -2,
  intl_africa: 101, intl_africa_change: -2,
  intl_asiapac: 190, intl_asiapac_change: -17,
  // Worldwide
  ww_total: 1732, ww_change: -53,
  source: "Baker Hughes", updated: "U.S./Canada: April 24, 2026 | International: March 2026"
};

const OIL_FUTURES_DATA = [
  { contract: "WTI May 2026", price: 71.48, change: 1.23, pct: 1.75 },
  { contract: "WTI Jun 2026", price: 70.92, change: 1.10, pct: 1.58 },
  { contract: "WTI Jul 2026", price: 70.35, change: 0.98, pct: 1.41 },
  { contract: "WTI Aug 2026", price: 69.80, change: 0.85, pct: 1.23 },
  { contract: "WTI Dec 2026", price: 68.15, change: 0.62, pct: 0.92 },
  { contract: "WTI Dec 2027", price: 65.40, change: 0.35, pct: 0.54 },
  { contract: "Brent May 2026", price: 75.92, change: 0.87, pct: 1.16 },
  { contract: "Brent Jun 2026", price: 75.30, change: 0.78, pct: 1.05 },
  { contract: "Brent Jul 2026", price: 74.72, change: 0.70, pct: 0.95 },
  { contract: "Brent Dec 2026", price: 72.50, change: 0.48, pct: 0.67 },
];

const SUPPLY_CHOKEPOINTS = [
  { label: "Chokepoint", title: "Strait of Hormuz", desc: "21M bpd of crude transit daily. Any disruption impacts global benchmarks and insurance premiums.", stat: "21M bpd", region: "Persian Gulf" },
  { label: "Shipping", title: "Red Sea / Bab el-Mandeb", desc: "Houthi attacks reroute tankers around Cape of Good Hope, adding 10-14 days to delivery.", stat: "4.8M bpd", region: "Middle East" },
  { label: "Pipeline", title: "Druzhba Pipeline", desc: "Major crude pipeline from Russia to Central Europe, partially sanctioned since 2022.", stat: "1.2M bpd", region: "Russia → EU" },
  { label: "LNG Terminal", title: "U.S. Gulf Coast LNG", desc: "Record export capacity supporting European and Asian supply diversification.", stat: "14 Bcf/d", region: "United States" },
  { label: "Strait", title: "Strait of Malacca", desc: "Key Asian oil transit route connecting Indian Ocean to South China Sea.", stat: "16M bpd", region: "Southeast Asia" },
];

// ─── COMPREHENSIVE OIL PRICE DATA (mirrors OilPrice.com structure) ────
const OIL_PRICE_SECTIONS = [
  
];

// ─── UFutures & IndexesORY PAGE ──────────────────────────────
const CATEGORY_CONTENT = {
  "oil-prices": {
    articles: [
      { id: 1700, title: "Why Do Oil Prices Change Every Day?", excerpt: "Supply data, demand signals, geopolitics, the U.S. dollar, and trader positioning — the five daily drivers that move WTI and Brent in real time.", date: "Apr 18, 2026", author: "Staff", readTime: "7 min" },
      { id: 1100, title: "What's the Oil Price Per Barrel Today? WTI & Brent Explained", excerpt: "A plain-English explainer on how crude oil is priced per barrel, why there are two benchmarks, and the five forces that move the price every day.", date: "Apr 18, 2026", author: "Staff", readTime: "6 min" },
      { id: 1101, title: "WTI vs Brent: What's the Difference and Why It Matters", excerpt: "WTI is landlocked in Oklahoma; Brent is seaborne in the North Sea. Why the spread exists, what it signals, and how it affects U.S. gasoline prices.", date: "Apr 18, 2026", author: "Staff", readTime: "6 min" },
      { id: 1001, title: "WTI Crude Climbs Past $71 as U.S. Inventories Post Sharp Drawdown", excerpt: "Commercial crude stocks at Cushing fell 4.2M barrels, well above the 1.8M consensus, signaling strong refinery demand ahead of driving season.", date: "Apr 16, 2026", author: "Staff", readTime: "5 min" },
      { id: 1002, title: "Brent-WTI Spread Widens to $4.44 on Atlantic Basin Tightness", excerpt: "North Sea supply disruptions and strong European refinery margins are pulling Brent higher relative to WTI.", date: "Apr 15, 2026", author: "Staff", readTime: "4 min" },
      { id: 1003, title: "Goldman Sachs Raises Brent Forecast to $82 by Year-End", excerpt: "The bank cites stronger-than-expected emerging market demand growth and disciplined OPEC+ supply management.", date: "Apr 14, 2026", author: "Staff", readTime: "4 min" },
      { id: 1004, title: "OPEC Basket Price Holds Above $74 Amid Production Cut Extensions", excerpt: "The reference basket used by OPEC member nations remains elevated as voluntary cuts of 2.2M bpd persist through Q3.", date: "Apr 13, 2026", author: "Staff", readTime: "5 min" },
      { id: 1005, title: "Dubai Crude Fetches Premium as Asian Refiners Compete for Sour Barrels", excerpt: "The Dubai benchmark has firmed on strong buying from Indian and Chinese refiners seeking Middle Eastern grades.", date: "Apr 13, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "WTI Crude", value: "$71.48", sub: "+1.75%" },
      { label: "Brent Crude", value: "$75.92", sub: "+1.16%" },
      { label: "OPEC Basket", value: "$74.12", sub: "+0.88%" },
    ]
  },
  "oil-futures": {
    articles: [
      { id: 1600, title: "Oil Futures vs Spot Prices: What's the Difference?", excerpt: "Spot price is oil for immediate delivery; futures is oil for later. Why the two diverge, how contango and backwardation work, and which one the news actually quotes.", date: "Apr 18, 2026", author: "Staff", readTime: "7 min" },
      { id: 1101, title: "WTI Futures Curve Flips to Backwardation Through December 2026", excerpt: "Front-month contracts now trade at a premium to deferred months, signaling near-term supply tightness.", date: "Apr 16, 2026", author: "Staff", readTime: "6 min" },
      { id: 1102, title: "Brent Futures Open Interest Hits 3-Month High Ahead of OPEC Meeting", excerpt: "Speculative positioning in Brent crude futures has surged as traders anticipate policy signals from Vienna.", date: "Apr 15, 2026", author: "Staff", readTime: "5 min" },
      { id: 1103, title: "Options Market Pricing Elevated Volatility Through Summer 2026", excerpt: "Implied volatility on WTI calls has risen 18% as geopolitical risk and demand uncertainty drive hedging activity.", date: "Apr 14, 2026", author: "Staff", readTime: "5 min" },
      { id: 1104, title: "Managed Money Net Longs in Crude Futures Rise for Fourth Straight Week", excerpt: "CFTC data shows hedge funds increasing bullish bets on oil as macro headwinds appear to be easing.", date: "Apr 13, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "WTI Front Month", value: "$71.48", sub: "May 2026" },
      { label: "Brent Front Month", value: "$75.92", sub: "May 2026" },
      { label: "Curve Shape", value: "Backwardation", sub: "-$2.58 12-mo" },
    ]
  },
  "rig-count": {
    articles: [
      { id: 1201, title: "U.S. Rig Count Falls to 584, Down 5 From Prior Week", excerpt: "Baker Hughes data shows continued drilling pullback as operators prioritize capital discipline over volume growth.", date: "Apr 16, 2026", author: "Staff", readTime: "3 min" },
      { id: 1202, title: "Permian Basin Rigs Hold Steady at 302 Despite Overall U.S. Decline", excerpt: "The nation's most prolific basin continues to attract investment even as secondary plays see rig reductions.", date: "Apr 15, 2026", author: "Staff", readTime: "5 min" },
      { id: 1203, title: "Canadian Rig Count Rebounds to 118 as Spring Drilling Season Begins", excerpt: "Freeze-thaw cycle restrictions are easing across Alberta and Saskatchewan, allowing crews to mobilize.", date: "Apr 14, 2026", author: "Staff", readTime: "4 min" },
      { id: 1204, title: "International Rig Count Stable at 958 as Middle East Activity Rises", excerpt: "Saudi Arabia and UAE are adding rigs to maintain production capacity even as OPEC+ quotas limit output.", date: "Apr 13, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "U.S. Total", value: "544", sub: "+1 w/w" },
      { label: "U.S. Oil Rigs", value: "407", sub: "-3 w/w" },
      { label: "Texas (Top State)", value: "234", sub: "+2 w/w" },
    ]
  },
  "energy": {
    articles: [
      { id: 1301, title: "Global Energy Demand Growth Slows to 1.2% in 2026, IEA Reports", excerpt: "The International Energy Agency's latest monthly report shows moderating consumption growth driven by Chinese economic headwinds and efficiency gains.", date: "Apr 16, 2026", author: "Staff", readTime: "7 min" },
      { id: 1302, title: "U.S. Power Grid Faces Record Summer Demand From Data Center Expansion", excerpt: "AI-driven data center buildouts are straining electricity infrastructure across Texas, Virginia, and the Southwest.", date: "Apr 15, 2026", author: "Staff", readTime: "6 min" },
      { id: 1303, title: "European Energy Security Improves as LNG Import Capacity Doubles Since 2022", excerpt: "New regasification terminals in Germany, Italy, and Greece have significantly reduced Europe's vulnerability to supply shocks.", date: "Apr 14, 2026", author: "Staff", readTime: "5 min" },
      { id: 1304, title: "India's Energy Consumption Surpasses Japan for First Time", excerpt: "Rapid industrialization and a growing middle class push India past Japan as the world's fourth-largest energy consumer.", date: "Apr 13, 2026", author: "Staff", readTime: "5 min" },
      { id: 1305, title: "Carbon Capture Investment Reaches $12B Globally in 2025", excerpt: "Direct air capture and point-source CCS projects are scaling up as government subsidies and carbon pricing incentivize deployment.", date: "Apr 13, 2026", author: "Staff", readTime: "6 min" },
    ],
    stats: [
      { label: "Global Demand", value: "104.2M", sub: "bpd (oil equiv.)" },
      { label: "U.S. Production", value: "13.4M", sub: "bpd crude" },
      { label: "LNG Exports", value: "14 Bcf/d", sub: "U.S. Gulf" },
    ]
  },
  "crude-oil": {
    articles: [
      { id: 1401, title: "Permian Basin Production Hits Record 6.2 Million Barrels Per Day", excerpt: "Improved well productivity and extended lateral lengths continue to push U.S. shale output higher despite a falling rig count.", date: "Apr 16, 2026", author: "Staff", readTime: "6 min" },
      { id: 1402, title: "Guyana's Stabroek Block Delivers New 1.5 Billion Barrel Discovery", excerpt: "ExxonMobil's latest exploration well adds to what is already one of the most significant deepwater oil provinces found this century.", date: "Apr 15, 2026", author: "Staff", readTime: "7 min" },
      { id: 1403, title: "OPEC+ Compliance Reaches 116% as Iraq Over-Produces Again", excerpt: "Baghdad's output consistently exceeds its agreed ceiling, creating tension within the alliance and complicating quota negotiations.", date: "Apr 14, 2026", author: "Staff", readTime: "5 min" },
      { id: 1404, title: "North Sea Forties Pipeline Restart Eases Brent Supply Concerns", excerpt: "The 450,000 bpd system returns to full capacity after a 10-day maintenance shutdown that briefly tightened dated Brent.", date: "Apr 13, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "U.S. Production", value: "13.4M", sub: "bpd" },
      { label: "OPEC Output", value: "26.8M", sub: "bpd" },
      { label: "Global Supply", value: "102.6M", sub: "bpd" },
    ]
  },
  "gas-prices": {
    articles: [
      { id: 1400, title: "Why Are Gas Prices Different in Every State?", excerpt: "State fuel taxes, refinery proximity, unique fuel blends, and local competition together explain the $2+ gap between the cheapest and most expensive states.", date: "Apr 18, 2026", author: "Staff", readTime: "6 min" },
      { id: 1401, title: "Cheapest Gas Prices Right Now \u2014 State Rankings", excerpt: "Oklahoma, Mississippi, Texas, Louisiana, and Alabama anchor the bottom of the AAA rankings. Why these states are consistently cheapest, plus the 10 most expensive.", date: "Apr 18, 2026", author: "Staff", readTime: "5 min" },
      { id: 1200, title: "How Are Gas Prices Set? From Crude Oil to the Pump", excerpt: "The full chain that builds up the pump price: crude oil, refining, distribution, and taxes. Why prices vary by state and season, in plain English.", date: "Apr 18, 2026", author: "Staff", readTime: "7 min" },
      { id: 1501, title: "U.S. Average Gas Price Rises to $3.42/Gallon Ahead of Spring Driving Season", excerpt: "AAA reports retail gasoline prices are up 12 cents from a month ago as refiners switch to costlier summer-blend formulations.", date: "Apr 16, 2026", author: "Staff", readTime: "3 min" },
      { id: 1502, title: "California Gas Prices Hit $5.18 as State-Specific Regulations Add Costs", excerpt: "The Golden State's unique fuel standards and carbon pricing continue to push pump prices well above the national average.", date: "Apr 15, 2026", author: "Staff", readTime: "5 min" },
      { id: 1503, title: "Gulf Coast Refinery Margins Improve as Crack Spreads Widen", excerpt: "The 3-2-1 crack spread has expanded to $28/barrel, incentivizing higher refinery utilization rates.", date: "Apr 14, 2026", author: "Staff", readTime: "4 min" },
      { id: 1504, title: "EIA: U.S. Summer Gasoline Demand Expected to Average 9.1M BPD", excerpt: "The Energy Information Administration forecasts steady consumption growth despite elevated prices and rising EV adoption.", date: "Apr 13, 2026", author: "Staff", readTime: "5 min" },
    ],
    stats: [
      { label: "U.S. National Avg", value: "$3.42", sub: "/gallon" },
      { label: "RBOB Futures", value: "$2.18", sub: "/gallon" },
      { label: "Crack Spread", value: "$28.00", sub: "3-2-1" },
    ]
  },
  "natural-gas": {
    articles: [
      { id: 1601, title: "Henry Hub Falls Below $3.50 as U.S. Storage Surplus Persists", excerpt: "Above-average inventories and record production continue to weigh on domestic natural gas prices despite rising export demand.", date: "Apr 16, 2026", author: "Staff", readTime: "5 min" },
      { id: 1602, title: "European TTF Gas Rallies 12% on Extended Cold Weather Forecast", excerpt: "A late-season cold snap across Northern Europe is drawing down storage reserves faster than seasonal norms.", date: "Apr 15, 2026", author: "Staff", readTime: "4 min" },
      { id: 1603, title: "U.S. LNG Exports Hit Record 14 Bcf/d as Golden Pass Begins Operations", excerpt: "The new Qatar-Exxon joint venture facility in Texas adds 2.5 Bcf/d of liquefaction capacity to the Gulf Coast.", date: "Apr 14, 2026", author: "Staff", readTime: "6 min" },
      { id: 1604, title: "Japan LNG Spot Price Drops to $12.40/MMBtu on Mild Asian Demand", excerpt: "Warmer-than-normal temperatures across Northeast Asia reduce heating gas requirements heading into spring.", date: "Apr 13, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "Henry Hub", value: "$3.42", sub: "/MMBtu" },
      { label: "TTF Dutch", value: "€11.85", sub: "/MWh" },
      { label: "JKM LNG", value: "$12.40", sub: "/MMBtu" },
    ]
  },
  "heating-oil": {
    articles: [
      { id: 1701, title: "Heating Oil Futures Ease as Winter Demand Season Winds Down", excerpt: "NYMEX heating oil contracts slip as warmer spring temperatures reduce residential heating demand across the Northeast.", date: "Apr 16, 2026", author: "Staff", readTime: "3 min" },
      { id: 1702, title: "Northeast Home Heating Costs Rose 8% This Winter vs. Last Year", excerpt: "The EIA's Winter Fuels Outlook post-mortem shows higher crude prices and cold January temps drove seasonal cost increases.", date: "Apr 15, 2026", author: "Staff", readTime: "5 min" },
      { id: 1703, title: "Diesel and Heating Oil Margins Diverge as Trucking Demand Holds", excerpt: "While residential heating demand fades, strong freight activity keeps middle distillate markets well-supported.", date: "Apr 14, 2026", author: "Staff", readTime: "4 min" },
      { id: 1704, title: "European Diesel Imports From Asia Rise as Arbitrage Window Opens", excerpt: "A widening East-West price differential is pulling Asian diesel cargoes toward Europe for the first time since January.", date: "Apr 13, 2026", author: "Staff", readTime: "5 min" },
    ],
    stats: [
      { label: "Heating Oil", value: "$2.34", sub: "/gallon" },
      { label: "Diesel", value: "$2.41", sub: "/gallon" },
      { label: "Distillate Stock", value: "118M", sub: "barrels" },
    ]
  },
  "geopolitics": {
    articles: [
      { id: 1400, title: "Iran Strikes UAE Fujairah Oil Hub; First Major Bypass Infrastructure Hit", excerpt: "Iran launched 19 missiles and drones at the UAE on Monday May 4. Most were intercepted by Emirati air defenses, but a drone struck the Fujairah Oil Industry Zone, sparking a major fire and wounding three Indian nationals. Fujairah is the terminus of the UAE's ADCOP pipeline that bypasses the strait — the first major hit on bypass infrastructure since the conflict began.", date: "May 4, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1401, title: "U.S. Sinks Seven Iranian Boats as Project Freedom Launches Hormuz Convoys", excerpt: "CENTCOM commander Adm. Brad Cooper said Monday May 4 that American forces opened a passage through the strait free of Iranian mines and sank seven small Iranian boats targeting civilian ships. Two U.S.-flagged merchant vessels successfully transited Hormuz under Project Freedom — the first major U.S. military action against Iranian targets since the April 8 ceasefire.", date: "May 4, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1402, title: "Trump Declines to Confirm Ceasefire as Both Sides Trade Fire in Strait", excerpt: "President Trump on Monday May 4 declined to say whether the April 8 ceasefire with Iran remains in place after both sides exchanged fire in the strait. The hostilities directly contradict Trump's letter to Congress on Friday claiming 'no exchange of fire' since April 7 and that 'hostilities have terminated' under the War Powers Resolution.", date: "May 4, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1403, title: "ADNOC Tanker Barakah Struck by Drones; HMM Namu Hit by Explosion Off UAE", excerpt: "Two major maritime incidents over the weekend: ADNOC's empty tanker Barakah was hit by two drones north of Fujairah on Sunday May 3 with no injuries reported. On Monday May 4, an explosion caused a fire aboard the South Korean-operated HMM Namu while it was anchored off the UAE coast.", date: "May 4, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1404, title: "Iran Sends Updated Peace Proposal Through Pakistan; Trump 'Not Satisfied'", excerpt: "Pakistani officials confirmed Friday May 1 that Iranian mediators delivered an updated peace proposal to the U.S. through Islamabad. President Trump told reporters: 'Iran wants to make a deal, but I'm not satisfied with it.' WTI fell 3% to $101.94, Brent down 2% to $108.17 on the proposal news.", date: "May 1, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1405, title: "Trump Briefed on Expanded Iran Military Options as Crude Hit 4-Year High", excerpt: "Reports Thursday April 30 that CENTCOM Adm. Brad Cooper briefed Trump on expanded military options against Iran, including a planned short-and-intense wave of strikes reportedly under review. WTI hit a 4-year intraday high of $111, Brent reached $114.", date: "Apr 30, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1406, title: "Mojtaba Khamenei Vows to Retain Nuclear and Missile Capabilities", excerpt: "Iran's Supreme Leader Mojtaba Khamenei pledged not to relinquish the country's nuclear or missile capabilities and indicated Tehran would retain control over the strait. The hardline posture from Tehran's leadership complicates any path to a comprehensive deal.", date: "Apr 30, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1407, title: "Iran Proposes Hormuz Reopening if U.S. Lifts Naval Blockade", excerpt: "Iran on Monday April 27 submitted a formal proposal to reopen the Strait of Hormuz if the U.S. lifts its naval blockade and ends military operations, with nuclear talks deferred. Trump and his national security team discussed the offer; CNN reports Trump is unlikely to accept in current form.", date: "Apr 27, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1408, title: "Trump Says Iran in 'State of Collapse' as Hormuz Standoff Drags Into Ninth Week", excerpt: "President Trump posted on Truth Social Tuesday morning April 28 that Iran had 'informed us' it was in 'a State of Collapse' and wanted Hormuz reopened. The post came as the White House continues weighing Iran's Monday proposal.", date: "Apr 28, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1409, title: "WTI Tops $100, Brent $111 on Iran Hormuz Proposal Uncertainty", excerpt: "U.S. crude oil futures jumped more than 3% Tuesday April 28 to settle at $99.93/bbl, with Brent at $111.26 — the seventh consecutive session of gains. Markets weighed Iran's Monday Hormuz proposal against Trump's skepticism.", date: "Apr 28, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1410, title: "Araghchi Leaves Pakistan Without Meeting U.S. Officials as Talks Collapse", excerpt: "Iran's Foreign Minister Abbas Araghchi left Islamabad on Sunday April 26 without meeting any U.S. officials after Trump cancelled the Witkoff-Kushner trip Saturday. Pakistani back-channel mediation continues but direct talks remain stalled.", date: "Apr 26, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1411, title: "Trump Cancels Witkoff-Kushner Pakistan Trip as Iran Talks Stall", excerpt: "President Trump cancelled the planned Saturday trip of U.S. envoys Steve Witkoff and Jared Kushner to Islamabad, halting what was expected to be the second formal round of U.S.-Iran peace talks before it could begin.", date: "Apr 25, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1412, title: "Trump Orders Navy to 'Shoot and Kill' Iranian Mine-Laying Vessels in Strait", excerpt: "Trump's April 22 escalation order moved U.S. naval rules of engagement from defensive clearance to active interdiction with lethal force authorized. U.S. forces also boarded a supertanker carrying Iranian oil in the Indian Ocean.", date: "Apr 22, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1413, title: "Israeli Strikes Kill Lebanese Journalist Amal Khalil During Extended Ceasefire", excerpt: "Lebanese journalist Amal Khalil was killed in an Israeli strike on April 22, sharply straining the extended Israel-Lebanon ceasefire. Multiple new strikes followed, killing six on Saturday despite the truce extension.", date: "Apr 23, 2026", author: "Staff", readTime: "5 min" },
      { id: 1500, title: "U.S.-Iran Ceasefire Explained: Timeline, Terms, and Extension", excerpt: "The Pakistan-mediated U.S.-Iran ceasefire: what it covers, what it doesn\u0027t, Trump\u0027s April 21 indefinite extension, and what markets expect next.", date: "Apr 21, 2026", author: "Staff", readTime: "6 min" },
      { id: 1300, title: "What Happens If the Strait of Hormuz Closes?", excerpt: "Hour-by-hour and week-by-week scenario analysis: oil prices, gasoline, shipping, and the countries most exposed if the world\u0027s most important chokepoint shuts.", date: "Apr 18, 2026", author: "Staff", readTime: "7 min" },
      { id: 1301, title: "What Is OPEC+ and How Does It Affect Oil Prices?", excerpt: "The 23-nation producer alliance that controls roughly 40% of global oil output. Who\u0027s in it, how it sets quotas, and why its decisions move prices within minutes.", date: "Apr 18, 2026", author: "Staff", readTime: "6 min" },
      { id: 1801, title: "Islamabad Talks Collapse After 21-Hour Marathon — No Deal Reached Between U.S. and Iran", excerpt: "The highest-level U.S.-Iran negotiations since 1979 ended without agreement. Vance blamed Iran for refusing nuclear commitments. Trump announces full naval blockade of Hormuz.", date: "Apr 17, 2026", author: "Staff", readTime: "8 min" },
      { id: 1802, title: "Trump Announces Full Naval Blockade of Strait of Hormuz", excerpt: "Following failed Islamabad talks, President Trump orders U.S. Navy to blockade the strait and interdict all vessels that paid transit tolls to Iran.", date: "Apr 17, 2026", author: "Staff", readTime: "6 min" },
      { id: 1803, title: "Ceasefire Expires April 22 With No Extension in Sight", excerpt: "The two-week truce brokered by Pakistan runs out in 10 days. Without a deal, the conflict could resume with even greater intensity.", date: "Apr 17, 2026", author: "Staff", readTime: "5 min" },
      { id: 1804, title: "Iran Nuclear Program Remains Central Sticking Point in U.S. Negotiations", excerpt: "Tehran refuses to commit to ending uranium enrichment — Washington calls it the core requirement for any deal.", date: "Apr 17, 2026", author: "Staff", readTime: "7 min" },
      { id: 1805, title: "Israel Struck 200+ Hezbollah Targets During Islamabad Peace Talks", excerpt: "Military operations in Lebanon continued unabated even as diplomats negotiated in Pakistan, complicating ceasefire prospects.", date: "Apr 17, 2026", author: "Staff", readTime: "5 min" },
      { id: 1806, title: "Pakistan Urges Continued Diplomacy After U.S.-Iran Talks End Without Deal", excerpt: "PM Sharif calls on both sides to uphold ceasefire commitments while keeping diplomatic channels open.", date: "Apr 17, 2026", author: "Staff", readTime: "4 min" },
      { id: 1807, title: "Oil Markets Face Renewed Volatility as Islamabad Talks Fail", excerpt: "Crude prices expected to surge when markets open Monday as geopolitical risk premium rebuilds after diplomatic breakdown.", date: "Apr 17, 2026", author: "Staff", readTime: "6 min" },
      { id: 1808, title: "Strait of Hormuz: From Iranian Blockade to U.S. Naval Blockade", excerpt: "The world's most critical oil chokepoint faces competing closure threats from both sides of the conflict.", date: "Apr 17, 2026", author: "Staff", readTime: "7 min" },
      { id: 1809, title: "Israel-Lebanon Direct Negotiations Set for Tuesday in Washington", excerpt: "First official talks between the two countries in decades aim to address Hezbollah disarmament and border security.", date: "Apr 17, 2026", author: "Staff", readTime: "5 min" },
      { id: 1810, title: "Global Energy Crisis Deepens as Diplomatic Off-Ramp Narrows", excerpt: "IEA warns current crisis could exceed 1970s oil shocks. European gas prices remain elevated. U.S. consumers face $4+ gas.", date: "Apr 17, 2026", author: "Staff", readTime: "6 min" },
    ],
    stats: []
  },
  "company-news": {
    articles: [
      { id: 1900, title: "Saudi Aramco East-West Pipeline Continues at Full Capacity Through Blockade", excerpt: "Aramco's 5M bpd Hormuz bypass remains the global oil market's most critical piece of working infrastructure as the dual blockade enters its third month.", date: "Apr 24, 2026", author: "Staff", readTime: "6 min" },
      { id: 1901, title: "Energy Stocks Mixed as Ceasefire Extension Eases but Blockade Stays", excerpt: "Integrated majors traded mixed on the day of the ceasefire extension. Refiners held a more stable bid with crack spreads supported. LNG names benefited from continued Qatari disruption.", date: "Apr 22, 2026", author: "Staff", readTime: "7 min" },
      { id: 1902, title: "Maersk, Hapag-Lloyd Maintain Hormuz Transit Suspension Amid Continued Uncertainty", excerpt: "Both carriers cited continued threats to commercial shipping. Vessels continue routing around the Cape of Good Hope, adding 10-14 days per voyage and effectively reducing global container capacity.", date: "Apr 25, 2026", author: "Staff", readTime: "6 min" },
      { id: 1903, title: "Cheniere Energy, Venture Global Ride LNG Premium as Qatar Flows Still Disrupted", excerpt: "U.S. LNG terminals operating near 14 Bcf/d combined export capacity. European buyers returning to premium bidding for U.S. cargoes. JKM trading premium to TTF for first time since early 2025.", date: "Apr 23, 2026", author: "Staff", readTime: "7 min" },
      { id: 1904, title: "ExxonMobil Q1 Earnings Preview: Hormuz Disruption Hits Trading Timing", excerpt: "ExxonMobil's April 8 Q1 considerations supplement flagged $3.5-4.9B in negative timing effects from the Middle East conflict. Earnings call scheduled for April 30 will detail the full impact.", date: "Apr 22, 2026", author: "Staff", readTime: "5 min" },
      { id: 1905, title: "OPEC+ April Output Increase Proceeding Despite Market Volatility", excerpt: "206,000 bpd April increase on schedule. Saudi Arabia holding current production. No emergency JMMC meeting called following ceasefire extension.", date: "Apr 22, 2026", author: "Staff", readTime: "8 min" },
    ],
    stats: []
  },
  "alternative-energy": {
    articles: [
      { id: 2001, title: "Global Renewable Investment Hits $1.8 Trillion in 2025, IRENA Reports", excerpt: "Solar, wind, and battery storage captured 80% of new power generation investment worldwide for the first time.", date: "Apr 16, 2026", author: "Staff", readTime: "6 min" },
      { id: 2002, title: "Green Hydrogen Costs Fall 40% Since 2022 as Electrolyzer Scale Grows", excerpt: "Projects in Saudi Arabia, Australia, and Chile are proving that sub-$3/kg green hydrogen is achievable at scale.", date: "Apr 15, 2026", author: "Staff", readTime: "5 min" },
      { id: 2003, title: "Battery Storage Deployments Triple Year-Over-Year in the U.S.", excerpt: "Grid-scale lithium-ion installations reached 18 GW in 2025 as utilities pair storage with solar to meet peak demand.", date: "Apr 14, 2026", author: "Staff", readTime: "5 min" },
      { id: 2004, title: "EU Carbon Price Stabilizes at €85/Tonne, Supporting Clean Energy Economics", excerpt: "The Emissions Trading System continues to make fossil fuel power generation more expensive relative to renewables.", date: "Apr 13, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "Renewable CapEx", value: "$1.8T", sub: "2025 global" },
      { label: "Solar Cost", value: "$24", sub: "/MWh avg" },
      { label: "EV Sales Share", value: "22%", sub: "global 2025" },
    ]
  },
  "nuclear": {
    articles: [
      { id: 2101, title: "NuScale Small Modular Reactor Receives Full NRC Design Certification", excerpt: "The 77 MWe module becomes the first SMR to complete the U.S. regulatory approval process, clearing the path for commercial deployment.", date: "Apr 16, 2026", author: "Staff", readTime: "7 min" },
      { id: 2102, title: "France Commits €10B to Build Six New EPR2 Reactors by 2040", excerpt: "President Macron's nuclear renaissance plan aims to replace aging reactors while supporting European energy independence.", date: "Apr 15, 2026", author: "Staff", readTime: "6 min" },
      { id: 2103, title: "Uranium Spot Price Surges to $92/lb as Utility Contracting Accelerates", excerpt: "After a decade of low prices, uranium has rallied 180% since 2023 on renewed nuclear ambitions from the U.S., China, and India.", date: "Apr 14, 2026", author: "Staff", readTime: "5 min" },
      { id: 2104, title: "Microsoft Signs 20-Year Nuclear Power Purchase Agreement for Data Centers", excerpt: "The tech giant secures carbon-free baseload power from Constellation Energy's reactor fleet to support AI computing growth.", date: "Apr 13, 2026", author: "Staff", readTime: "5 min" },
    ],
    stats: [
      { label: "Uranium Price", value: "$92", sub: "/lb U₃O₈" },
      { label: "Global Reactors", value: "440", sub: "operational" },
      { label: "Under Constr.", value: "62", sub: "reactors" },
    ]
  },
  "solar": {
    articles: [
      { id: 2201, title: "Global Solar Installations Reach Record 420 GW in 2025", excerpt: "China alone accounted for 230 GW of new solar capacity as module prices fell below $0.10/watt for the first time.", date: "Apr 16, 2026", author: "Staff", readTime: "6 min" },
      { id: 2202, title: "U.S. Utility-Scale Solar Pipeline Exceeds 300 GW as IRA Credits Flow", excerpt: "The Inflation Reduction Act's tax credits continue to drive a massive buildout of solar farms across the Sun Belt states.", date: "Apr 15, 2026", author: "Staff", readTime: "5 min" },
      { id: 2203, title: "Perovskite-Silicon Tandem Cells Hit 33.9% Efficiency Record", excerpt: "Oxford PV's commercial-ready tandem cells promise to push rooftop solar economics further into mainstream territory.", date: "Apr 14, 2026", author: "Staff", readTime: "5 min" },
      { id: 2204, title: "India's Solar Tariffs Drop to Record Low $0.029/kWh in Rajasthan Auction", excerpt: "The world's cheapest solar electricity bid underscores India's aggressive renewable deployment targets.", date: "Apr 13, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "2025 Installed", value: "420 GW", sub: "global" },
      { label: "Module Price", value: "$0.09", sub: "/watt" },
      { label: "LCOE", value: "$24", sub: "/MWh avg" },
    ]
  },
  "wind": {
    articles: [
      { id: 2301, title: "Offshore Wind Capacity Surpasses 80 GW Globally as Costs Stabilize", excerpt: "After a period of cost inflation driven by supply chain bottlenecks, offshore wind developers report stabilizing turbine and installation costs.", date: "Apr 16, 2026", author: "Staff", readTime: "6 min" },
      { id: 2302, title: "Vineyard Wind Achieves Full 800 MW Output Off Massachusetts Coast", excerpt: "America's first utility-scale offshore wind farm is now operating at rated capacity, powering 400,000 homes.", date: "Apr 15, 2026", author: "Staff", readTime: "5 min" },
      { id: 2303, title: "Vestas Unveils 17 MW Offshore Turbine, World's Most Powerful", excerpt: "The V236-17.0 MW platform can generate enough electricity for 20,000 households from a single installation.", date: "Apr 14, 2026", author: "Staff", readTime: "4 min" },
      { id: 2304, title: "Texas Wind Generation Sets New Record at 35 GW During March Storm", excerpt: "ERCOT's wind fleet produced more power than natural gas for a 48-hour period during sustained high wind conditions.", date: "Apr 13, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "Offshore Global", value: "80 GW", sub: "installed" },
      { label: "U.S. Onshore", value: "155 GW", sub: "installed" },
      { label: "Largest Turbine", value: "17 MW", sub: "Vestas" },
    ]
  },
  "renewable-energy": {
    articles: [
      { id: 2401, title: "Renewables Provided 35% of Global Electricity in 2025, IEA Confirms", excerpt: "Wind, solar, hydro, and biomass generation surpassed coal for the first time on an annual basis worldwide.", date: "Apr 16, 2026", author: "Staff", readTime: "7 min" },
      { id: 2402, title: "Grid-Scale Battery Storage Hits 100 GW Global Milestone", excerpt: "Lithium-ion dominates the market but sodium-ion and iron-air chemistries are gaining ground for long-duration applications.", date: "Apr 15, 2026", author: "Staff", readTime: "5 min" },
      { id: 2403, title: "Green Hydrogen Electrolyzer Orders Surge 300% in 2025", excerpt: "European and Middle Eastern projects drive demand for gigawatt-scale electrolysis systems from manufacturers like Plug Power and Nel.", date: "Apr 14, 2026", author: "Staff", readTime: "5 min" },
      { id: 2404, title: "U.S. Clean Energy Jobs Surpass 4 Million for First Time", excerpt: "Solar installation, EV manufacturing, and battery production drive employment growth outpacing fossil fuel sector hiring.", date: "Apr 13, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "Global Share", value: "35%", sub: "of electricity" },
      { label: "Storage", value: "100 GW", sub: "global installed" },
      { label: "Clean Jobs (U.S.)", value: "4M+", sub: "employed" },
    ]
  },
};

const GEO_TRENDING = [
  { title: "Red Sea & Houthi Attacks", heat: "🔥", desc: "Shipping reroutes adding $1-2/bbl to crude costs" },
  { title: "Russia-Ukraine Energy War", heat: "🔥", desc: "Sanctions enforcement tightening on price cap violations" },
  { title: "Iran Nuclear Deal Stalls", heat: "⚡", desc: "Diplomatic freeze keeps 1M bpd off global markets" },
  { title: "U.S.-China Trade Tensions", heat: "⚡", desc: "Tariff escalation threatens LNG and energy trade flows" },
  { title: "OPEC+ Quota Compliance", heat: "📊", desc: "Iraq and Kazakhstan repeatedly exceeding production limits" },
  { title: "Strait of Hormuz Risk", heat: "🌍", desc: "21M bpd transit — any disruption would spike prices globally" },
  { title: "Venezuela Sanctions Review", heat: "🌍", desc: "U.S. weighing re-imposition after election delays" },
  { title: "Nigeria Security Improvements", heat: "📊", desc: "Niger Delta sabotage drops, Bonny Light output recovers" },
  { title: "Saudi-Iran Détente", heat: "✅", desc: "Diplomatic normalization reduces Persian Gulf tensions" },
  { title: "Arctic Drilling Debate", heat: "🌍", desc: "Environmental vs. energy security interests clash" },
];

// ─── COMPREHENSIVE ENERGY COMPANY DATA ─────────────────────────────
const ENERGY_COMPANIES = [
  { name: "ExxonMobil", ticker: "XOM", revenue: "$84.3B", profit: "$9.2B", production: "3.7M boe/d", dividend: "3.4%", sector: "Integrated", hq: "Houston, TX" },
  { name: "Saudi Aramco", ticker: "2222.SR", revenue: "$97.5B", profit: "$27.3B", production: "12.9M bpd", dividend: "5.8%", sector: "National Oil", hq: "Dhahran, Saudi Arabia" },
  { name: "Chevron", ticker: "CVX", revenue: "$47.2B", profit: "$5.8B", production: "3.1M boe/d", dividend: "4.1%", sector: "Integrated", hq: "San Ramon, CA" },
  { name: "Shell", ticker: "SHEL", revenue: "$72.8B", profit: "$7.4B", production: "2.8M boe/d", dividend: "3.8%", sector: "Integrated", hq: "London, UK" },
  { name: "TotalEnergies", ticker: "TTE", revenue: "$54.6B", profit: "$5.1B", production: "2.5M boe/d", dividend: "5.2%", sector: "Integrated", hq: "Paris, France" },
  { name: "BP", ticker: "BP", revenue: "$48.7B", profit: "$3.9B", production: "2.3M boe/d", dividend: "4.8%", sector: "Integrated", hq: "London, UK" },
  { name: "ConocoPhillips", ticker: "COP", revenue: "$15.4B", profit: "$3.2B", production: "1.7M boe/d", dividend: "2.9%", sector: "E&P", hq: "Houston, TX" },
  { name: "Equinor", ticker: "EQNR", revenue: "$25.8B", profit: "$4.1B", production: "2.1M boe/d", dividend: "6.2%", sector: "Integrated", hq: "Stavanger, Norway" },
  { name: "Petrobras", ticker: "PBR", revenue: "$22.3B", profit: "$5.6B", production: "2.8M boe/d", dividend: "8.1%", sector: "National Oil", hq: "Rio de Janeiro, Brazil" },
  { name: "EOG Resources", ticker: "EOG", revenue: "$6.1B", profit: "$1.8B", production: "1.0M boe/d", dividend: "2.6%", sector: "E&P", hq: "Houston, TX" },
  { name: "Devon Energy", ticker: "DVN", revenue: "$4.2B", profit: "$1.1B", production: "650K boe/d", dividend: "5.4%", sector: "E&P", hq: "Oklahoma City, OK" },
  { name: "Schlumberger (SLB)", ticker: "SLB", revenue: "$8.9B", profit: "$1.4B", production: "—", dividend: "2.1%", sector: "Services", hq: "Houston, TX" },
  { name: "Halliburton", ticker: "HAL", revenue: "$5.8B", profit: "$0.8B", production: "—", dividend: "1.8%", sector: "Services", hq: "Houston, TX" },
  { name: "Baker Hughes", ticker: "BKR", revenue: "$6.4B", profit: "$0.7B", production: "—", dividend: "2.4%", sector: "Services", hq: "Houston, TX" },
  { name: "Cheniere Energy", ticker: "LNG", revenue: "$4.1B", profit: "$1.2B", production: "45 MTPA LNG", dividend: "0.9%", sector: "LNG", hq: "Houston, TX" },
  { name: "Diamondback Energy", ticker: "FANG", revenue: "$3.5B", profit: "$1.0B", production: "460K boe/d", dividend: "4.8%", sector: "E&P", hq: "Midland, TX" },
  { name: "Marathon Petroleum", ticker: "MPC", revenue: "$35.2B", profit: "$3.8B", production: "—", dividend: "2.2%", sector: "Refining", hq: "Findlay, OH" },
  { name: "Valero Energy", ticker: "VLO", revenue: "$32.4B", profit: "$3.1B", production: "—", dividend: "3.0%", sector: "Refining", hq: "San Antonio, TX" },
  { name: "Phillips 66", ticker: "PSX", revenue: "$36.8B", profit: "$2.4B", production: "—", dividend: "3.5%", sector: "Refining", hq: "Houston, TX" },
  { name: "Eni", ticker: "ENI.MI", revenue: "€23.8B", profit: "€3.2B", production: "1.7M boe/d", dividend: "5.6%", sector: "Integrated", hq: "Rome, Italy" },
  { name: "Repsol", ticker: "REP.MC", revenue: "€15.2B", profit: "€1.8B", production: "600K boe/d", dividend: "5.1%", sector: "Integrated", hq: "Madrid, Spain" },
  { name: "CNOOC", ticker: "0883.HK", revenue: "¥260B", profit: "¥68B", production: "1.7M boe/d", dividend: "6.2%", sector: "E&P", hq: "Beijing, China" },
  { name: "PetroChina", ticker: "0857.HK", revenue: "¥2.9T", profit: "¥162B", production: "4.7M boe/d", dividend: "4.8%", sector: "National Oil", hq: "Beijing, China" },
  { name: "Woodside Energy", ticker: "WDS", revenue: "$13.4B", profit: "$4.2B", production: "480K boe/d", dividend: "7.8%", sector: "LNG / E&P", hq: "Perth, Australia" },
  { name: "Canadian Natural", ticker: "CNQ", revenue: "$8.9B", profit: "$2.4B", production: "1.3M boe/d", dividend: "4.2%", sector: "E&P", hq: "Calgary, Canada" },
  { name: "Suncor Energy", ticker: "SU", revenue: "$10.2B", profit: "$2.1B", production: "780K boe/d", dividend: "4.5%", sector: "Integrated", hq: "Calgary, Canada" },
  { name: "ADNOC", ticker: "ADNOCDIST.AD", revenue: "$52B", profit: "$15B", production: "4.0M bpd", dividend: "4.0%", sector: "National Oil", hq: "Abu Dhabi, UAE" },
  { name: "QatarEnergy", ticker: "Private", revenue: "$42B", profit: "—", production: "6.5M boe/d", dividend: "—", sector: "National Oil", hq: "Doha, Qatar" },
  { name: "Kuwait Petroleum", ticker: "Private", revenue: "$38B", profit: "—", production: "2.8M bpd", dividend: "—", sector: "National Oil", hq: "Kuwait City, Kuwait" },
  { name: "ONGC", ticker: "ONGC.NS", revenue: "₹1.4T", profit: "₹340B", production: "1.2M boe/d", dividend: "3.8%", sector: "National Oil", hq: "New Delhi, India" },
  { name: "Ecopetrol", ticker: "EC", revenue: "$8.4B", profit: "$2.1B", production: "680K boe/d", dividend: "12.5%", sector: "National Oil", hq: "Bogotá, Colombia" },
  { name: "YPF", ticker: "YPF", revenue: "$5.2B", profit: "$0.9B", production: "530K boe/d", dividend: "1.2%", sector: "Integrated", hq: "Buenos Aires, Argentina" },
  { name: "Gazprom", ticker: "GAZP.ME", revenue: "₽4.2T", profit: "₽620B", production: "9.5M boe/d", dividend: "—", sector: "Gas / Integrated", hq: "Moscow, Russia" },
];

// ─── CATEGORY FAQs ─────────────────────────────────────────────────


// ─── U.S. GAS PRICES BY STATE (structure for future API integration) ──



const CATEGORY_FAQS = {
  "energy": [
    { q: "What drives energy prices?", a: "Energy prices are driven by supply-demand dynamics, geopolitical events, weather patterns, inventory levels, OPEC+ production decisions, and macroeconomic conditions. The U.S.-Iran conflict has added significant risk premiums to crude oil and natural gas prices in 2026." },
    { q: "How are oil and natural gas prices related?", a: "While historically correlated, oil and natural gas prices have diverged in recent years. Oil is globally traded with prices set by international benchmarks, while U.S. natural gas prices (Henry Hub) are more influenced by domestic supply, weather demand, and LNG export capacity." },
    { q: "What is the energy transition?", a: "The energy transition refers to the global shift from fossil fuels to renewable energy sources. While renewables are growing rapidly, oil and gas still provide roughly 55% of global primary energy. The transition is expected to take decades." },
    { q: "How do I read energy market data?", a: "Key metrics include spot prices (current market value), futures prices (forward-looking contracts), inventory levels (supply indicator), and production data. Prices marked LIVE update every 5 minutes. Others show delayed reference data." },
  ],
  "alternative-energy": [
    { q: "What are the main alternative energy sources?", a: "Solar, wind, hydroelectric, nuclear, geothermal, and hydrogen. Solar and wind have seen the fastest growth, with global installations reaching 420 GW and 120 GW respectively in 2025." },
    { q: "How does renewable energy affect oil prices?", a: "In the short term, renewables primarily displace coal and natural gas in electricity generation rather than oil. Long-term EV adoption is the main channel through which renewables reduce oil demand — currently displacing about 1.5 million bpd globally." },
    { q: "What is green hydrogen?", a: "Green hydrogen is produced by splitting water using renewable electricity. Costs have fallen 40% since 2022, approaching $3/kg in optimal locations. It's seen as critical for decarbonizing heavy industry, shipping, and aviation." },
  ],
  "nuclear": [
    { q: "Is nuclear energy considered clean?", a: "Nuclear power produces virtually zero carbon emissions during operation. A nuclear plant generates about 1/50th the lifecycle CO2 of a coal plant. Many climate scientists and the IEA consider nuclear essential for reaching net-zero targets." },
    { q: "What are Small Modular Reactors (SMRs)?", a: "SMRs are nuclear reactors with output under 300 MWe that can be factory-built and transported to site. NuScale received full NRC design certification in 2026. SMRs promise lower capital costs, faster construction, and enhanced safety." },
    { q: "Why is uranium rising in price?", a: "Uranium has surged to over $89/lb due to renewed nuclear ambitions globally, supply deficits from mine closures, and utility contracting acceleration. The market was underinvested for a decade after Fukushima." },
  ],
  "solar": [
    { q: "How cheap is solar energy now?", a: "Solar LCOE (levelized cost of energy) has fallen to $24/MWh on average — cheaper than any fossil fuel in most markets. Module prices dropped below $0.10/watt in 2025. India recorded the world's cheapest solar bid at $0.029/kWh." },
    { q: "What limits solar energy growth?", a: "Grid integration, energy storage, and intermittency remain key challenges. Solar only produces during daylight hours, requiring battery storage or backup generation. Permitting delays and transmission constraints also limit deployment." },
  ],
  "wind": [
    { q: "How much electricity does wind generate globally?", a: "Wind power generated approximately 2,300 TWh in 2025, about 8% of global electricity. Offshore wind is the fastest-growing segment, with costs falling below $50/MWh in competitive markets." },
    { q: "What is the outlook for offshore wind?", a: "Offshore wind capacity is expected to grow from 75 GW in 2025 to over 300 GW by 2035. The U.S., UK, and East Asia are leading markets. Floating offshore wind technology is opening up deeper water sites." },
  ],
  "gas-prices": [
    { q: "Why are gas prices so high right now?", a: "Gas prices are elevated due to the U.S.-Iran conflict disrupting oil shipments through the Strait of Hormuz, which handles 21% of global oil. Crude oil above $95/barrel drives pump prices above $4 nationally." },
    { q: "How often do gas prices change?", a: "Wholesale gasoline prices change daily on commodity exchanges. Retail stations typically adjust 1-3 times per week, with a 1-2 week lag behind crude oil movements." },
    { q: "Which state has the cheapest gas?", a: "Oklahoma consistently has the lowest gas prices due to proximity to refineries, low state taxes, and domestic crude production. Kansas, Arkansas, and Missouri also rank among the cheapest." },
    { q: "Why is California gas so expensive?", a: "California has the highest gas taxes ($0.68/gal), strict low-carbon fuel standards requiring special blends, limited refinery capacity, and geographic isolation from Gulf Coast supply." },
  ],
  "geopolitics": [
    { q: "How does the Iran war affect oil prices?", a: "The U.S.-Iran conflict has disrupted the Strait of Hormuz, reducing global oil transit by over 90%. This has pushed crude prices up 40%+ since February 2026 and created the worst supply disruption since the 1970s." },
    { q: "What is the Strait of Hormuz?", a: "A 21-mile-wide waterway between Iran and Oman connecting the Persian Gulf to open ocean. Approximately 21 million barrels of oil per day — 21% of global consumption — normally transits the strait." },
    { q: "What is OPEC+ and why does it matter?", a: "OPEC+ is an alliance of 23 oil-producing nations led by Saudi Arabia and Russia that coordinates production levels. Their output decisions directly influence global oil supply and prices." },
    { q: "How do sanctions affect energy markets?", a: "Sanctions restrict countries from selling oil or buying energy equipment. U.S. sanctions on Iran, Russia, and Venezuela have removed millions of barrels from legal markets, tightening supply." },
  ],
  "company-news": [
    { q: "Which are the largest oil companies?", a: "By revenue: Saudi Aramco, ExxonMobil, Shell, TotalEnergies, Chevron, and BP. By production: Aramco leads at 12.9M bpd, followed by national oil companies in Iraq, Kuwait, and UAE." },
    { q: "What is an integrated oil company?", a: "An integrated company operates across the full value chain — upstream (exploration/production), midstream (pipelines/transport), and downstream (refining/retail). ExxonMobil, Shell, and Chevron are examples." },
    { q: "How do oil company stocks react to price changes?", a: "Oil company stocks generally rise with crude prices but with varying sensitivity. E&P companies are most leveraged to price changes, while integrated majors and refiners have more diversified exposure." },
  ],
  "crude-oil": [
    { q: "What makes crude oil light or heavy?", a: "API gravity measures density — light crude (above 31° API) flows easily and yields more gasoline. Heavy crude (below 22° API) requires complex refining but trades at a discount." },
    { q: "Why are there so many crude oil benchmarks?", a: "Different regions produce crude with varying density and sulfur content. WTI represents U.S. light sweet crude, Brent represents global seaborne trade, and Dubai represents Middle Eastern exports." },
    { q: "How is crude oil priced?", a: "Crude trades on commodity exchanges (NYMEX, ICE) as futures contracts. Spot prices reflect immediate delivery, while futures prices reflect expected future value. Prices are quoted in USD per barrel." },
  ],
  "natural-gas": [
    { q: "What is Henry Hub?", a: "Henry Hub is a natural gas pipeline junction in Louisiana that serves as the pricing point for U.S. natural gas futures. It is the benchmark for North American gas prices." },
    { q: "How does LNG differ from pipeline gas?", a: "LNG (liquefied natural gas) is cooled to -260°F for shipping by tanker. Pipeline gas flows domestically. LNG enables global trade but costs more due to liquefaction and regasification." },
    { q: "What drives natural gas prices?", a: "Weather (heating/cooling demand), storage levels, production rates, LNG exports, and industrial consumption. Winter cold snaps and summer heat waves cause the largest price spikes." },
  ],
  "heating-oil": [
    { q: "What is heating oil?", a: "Heating oil (No. 2 fuel oil) is a refined petroleum product used primarily for home heating in the northeastern United States. It is chemically similar to diesel fuel." },
    { q: "Why is heating oil more expensive than gasoline?", a: "Heating oil has higher refining costs and is subject to seasonal demand spikes in winter. Federal and state taxes differ between heating oil and gasoline, also affecting relative prices." },
    { q: "How is heating oil priced?", a: "Heating oil futures trade on NYMEX in USD per gallon. Retail prices include delivery charges, dealer margins, and local taxes. Prices peak during winter heating season (Oct-Mar)." },
  ],
  "oil-futures": [
    { q: "What are oil futures?", a: "Futures are standardized contracts to buy or sell oil at a predetermined price on a specific future date. They trade on exchanges like NYMEX (WTI) and ICE (Brent) and are used for hedging and speculation." },
    { q: "What is contango vs backwardation?", a: "Contango: future prices higher than spot (oversupply signal). Backwardation: spot prices higher than futures (tight supply signal). The current market is in backwardation due to Hormuz disruptions." },
    { q: "Who trades oil futures?", a: "Producers (hedging output), refiners (locking input costs), airlines (fuel hedging), banks (market-making), and speculators. Commercial hedgers represent about 40% of open interest." },
  ],
  "oil-prices": [
    { q: "What determines daily oil price movements?", a: "Supply disruptions, OPEC+ decisions, inventory data (EIA weekly report), geopolitical events, currency movements, and macroeconomic indicators. The Strait of Hormuz crisis is currently the dominant factor." },
    { q: "What is the difference between spot and futures prices?", a: "Spot price is for immediate delivery. Futures price is for delivery at a future date. The spread between them indicates market expectations about supply tightness or surplus." },
    { q: "How do oil prices affect the economy?", a: "Higher oil prices increase transportation, manufacturing, and heating costs. They act as a tax on consumers, reduce discretionary spending, and can trigger inflation. Central banks may raise rates in response." },
  ],
  "renewable-energy": [
    { q: "How much energy comes from renewables?", a: "Renewables generated approximately 30% of global electricity in 2025, led by hydroelectric (16%), wind (8%), and solar (6%). However, renewables represent only about 15% of total primary energy when including transportation and heating." },
    { q: "Are renewables cheaper than fossil fuels?", a: "For electricity generation, solar and wind are now cheaper than new coal and gas plants in most markets. Solar LCOE has fallen to $24/MWh. However, intermittency requires backup storage, adding to total system costs." },
    { q: "What is the duck curve?", a: "The duck curve describes the gap between peak solar generation (midday) and peak electricity demand (evening). As solar capacity grows, utilities must rapidly ramp up other generation sources at sunset." },
  ],
  "rig-count": [
    { q: "What is the Baker Hughes rig count?", a: "A weekly census of active drilling rigs in the U.S. and internationally, published every Friday by Baker Hughes. It is the most widely followed indicator of upstream drilling activity and future production trends." },
    { q: "Why does the rig count matter for oil prices?", a: "Rising rig counts signal increasing future production, which can pressure prices lower. Falling counts suggest production declines ahead, supporting prices. Markets react to week-over-week changes." },
    { q: "What is the difference between oil and gas rigs?", a: "Oil rigs drill for crude oil, gas rigs target natural gas formations. The U.S. currently has roughly 480 oil rigs and 100 gas rigs active. Permian Basin accounts for about 45% of all U.S. oil rigs." },
    { q: "How long does it take a new rig to produce oil?", a: "From spudding (starting) a well to first production typically takes 2-4 months for horizontal shale wells. Wells reach peak production in the first 1-3 months, then decline 60-70% in the first year." },
  ],
};





const GAS_PRICES_BY_STATE = [
  { state:"Alabama", abbr:"AL", regular:4.157, mid:4.648, premium:5.096, diesel:5.892 },
  { state:"Alaska", abbr:"AK", regular:5.061, mid:5.303, premium:5.559, diesel:6.486 },
  { state:"Arizona", abbr:"AZ", regular:5.055, mid:5.478, premium:5.825, diesel:6.577 },
  { state:"Arkansas", abbr:"AR", regular:3.961, mid:4.459, premium:4.868, diesel:5.625 },
  { state:"California", abbr:"CA", regular:6.401, mid:6.67, premium:6.865, diesel:8.336 },
  { state:"Colorado", abbr:"CO", regular:4.298, mid:4.74, premium:5.096, diesel:5.624 },
  { state:"Connecticut", abbr:"CT", regular:4.463, mid:5.062, premium:5.492, diesel:6.467 },
  { state:"Delaware", abbr:"DE", regular:4.312, mid:4.976, premium:5.312, diesel:6.298 },
  { state:"District of Columbia", abbr:"DC", regular:4.707, mid:5.363, premium:5.78, diesel:6.459 },
  { state:"Florida", abbr:"FL", regular:4.498, mid:5.011, premium:5.374, diesel:6.117 },
  { state:"Georgia", abbr:"GA", regular:3.988, mid:4.497, premium:4.961, diesel:5.713 },
  { state:"Hawaii", abbr:"HI", regular:6.223, mid:6.482, premium:6.746, diesel:7.831 },
  { state:"Idaho", abbr:"ID", regular:4.724, mid:5.054, premium:5.351, diesel:6.027 },
  { state:"Illinois", abbr:"IL", regular:4.739, mid:5.376, premium:5.89, diesel:5.922 },
  { state:"Indiana", abbr:"IN", regular:4.198, mid:4.801, premium:5.346, diesel:5.916 },
  { state:"Iowa", abbr:"IA", regular:3.951, mid:4.195, premium:4.869, diesel:5.516 },
  { state:"Kansas", abbr:"KS", regular:3.809, mid:4.168, premium:4.535, diesel:5.188 },
  { state:"Kentucky", abbr:"KY", regular:4.317, mid:4.932, premium:5.4, diesel:5.839 },
  { state:"Louisiana", abbr:"LA", regular:4.064, mid:4.546, premium:4.972, diesel:5.711 },
  { state:"Maine", abbr:"ME", regular:4.366, mid:4.961, premium:5.496, diesel:6.405 },
  { state:"Maryland", abbr:"MD", regular:4.45, mid:5.123, premium:5.472, diesel:6.35 },
  { state:"Massachusetts", abbr:"MA", regular:4.342, mid:4.994, premium:5.413, diesel:6.429 },
  { state:"Michigan", abbr:"MI", regular:4.241, mid:4.898, premium:5.521, diesel:5.734 },
  { state:"Minnesota", abbr:"MN", regular:4.023, mid:4.498, premium:5.037, diesel:5.55 },
  { state:"Mississippi", abbr:"MS", regular:4.064, mid:4.535, premium:4.972, diesel:5.704 },
  { state:"Missouri", abbr:"MO", regular:3.987, mid:4.437, premium:4.78, diesel:5.337 },
  { state:"Montana", abbr:"MT", regular:4.241, mid:4.577, premium:4.954, diesel:5.46 },
  { state:"Nebraska", abbr:"NE", regular:3.944, mid:4.131, premium:4.639, diesel:5.339 },
  { state:"Nevada", abbr:"NV", regular:5.402, mid:5.753, premium:6.069, diesel:6.866 },
  { state:"New Hampshire", abbr:"NH", regular:4.316, mid:4.925, premium:5.433, diesel:6.359 },
  { state:"New Jersey", abbr:"NJ", regular:4.351, mid:4.959, premium:5.25, diesel:6.375 },
  { state:"New Mexico", abbr:"NM", regular:4.274, mid:4.744, premium:5.084, diesel:5.912 },
  { state:"New York", abbr:"NY", regular:4.524, mid:5.079, premium:5.497, diesel:6.524 },
  { state:"North Carolina", abbr:"NC", regular:4.181, mid:4.671, premium:5.11, diesel:6.223 },
  { state:"North Dakota", abbr:"ND", regular:3.929, mid:4.305, premium:4.761, diesel:5.324 },
  { state:"Ohio", abbr:"OH", regular:4.103, mid:4.691, premium:5.256, diesel:5.876 },
  { state:"Oklahoma", abbr:"OK", regular:3.749, mid:4.207, premium:4.523, diesel:5.2 },
  { state:"Oregon", abbr:"OR", regular:5.444, mid:5.693, premium:5.992, diesel:6.894 },
  { state:"Pennsylvania", abbr:"PA", regular:4.488, mid:4.974, premium:5.388, diesel:6.608 },
  { state:"Rhode Island", abbr:"RI", regular:4.337, mid:5.073, premium:5.54, diesel:6.327 },
  { state:"South Carolina", abbr:"SC", regular:4.101, mid:4.59, premium:5.031, diesel:6.09 },
  { state:"South Dakota", abbr:"SD", regular:4.004, mid:4.197, premium:4.719, diesel:5.281 },
  { state:"Tennessee", abbr:"TN", regular:4.18, mid:4.69, premium:5.121, diesel:5.914 },
  { state:"Texas", abbr:"TX", regular:4.072, mid:4.597, premium:5.01, diesel:5.737 },
  { state:"Utah", abbr:"UT", regular:4.581, mid:4.889, premium:5.162, diesel:5.854 },
  { state:"Vermont", abbr:"VT", regular:4.469, mid:5.012, premium:5.519, diesel:6.421 },
  { state:"Virginia", abbr:"VA", regular:4.305, mid:4.826, premium:5.242, diesel:6.255 },
  { state:"Washington", abbr:"WA", regular:5.879, mid:6.18, premium:6.438, diesel:7.582 },
  { state:"West Virginia", abbr:"WV", regular:4.269, mid:4.726, premium:5.229, diesel:6.034 },
  { state:"Wisconsin", abbr:"WI", regular:4.096, mid:4.655, premium:5.302, diesel:5.419 },
  { state:"Wyoming", abbr:"WY", regular:4.211, mid:4.553, premium:4.876, diesel:5.515 }
];

const US_GAS_NATIONAL = {
  regular: 4.457,
  mid: 5.021,
  premium: 5.421,
  diesel: 6.118,
  source: "AAA Daily Fuel Gauge Report",
  updated: "As of May 4, 2026"
};
const ELECTRICITY_PRICES_BY_STATE = [
  { state:"Alabama", abbr:"AL", region:"Southeast", residential:16.79, commercial:14.46, residential_yoy:4.0, commercial_yoy:3.1 },
  { state:"Alaska", abbr:"AK", region:"West", residential:26.57, commercial:23.12, residential_yoy:4.4, commercial_yoy:4.4 },
  { state:"Arizona", abbr:"AZ", region:"West", residential:15.62, commercial:13.09, residential_yoy:3.1, commercial_yoy:2.3 },
  { state:"Arkansas", abbr:"AR", region:"South Central", residential:13.32, commercial:10.77, residential_yoy:2.3, commercial_yoy:2.9 },
  { state:"California", abbr:"CA", region:"West", residential:33.75, commercial:29.46, residential_yoy:8.9, commercial_yoy:6.3 },
  { state:"Colorado", abbr:"CO", region:"West", residential:16.33, commercial:13.32, residential_yoy:4.7, commercial_yoy:3.2 },
  { state:"Connecticut", abbr:"CT", region:"Northeast", residential:27.84, commercial:23.89, residential_yoy:7.0, commercial_yoy:8.0 },
  { state:"Delaware", abbr:"DE", region:"Northeast", residential:18.39, commercial:12.69, residential_yoy:5.3, commercial_yoy:4.1 },
  { state:"District of Columbia", abbr:"DC", region:"Northeast", residential:24.03, commercial:20.86, residential_yoy:4.8, commercial_yoy:4.7 },
  { state:"Florida", abbr:"FL", region:"Southeast", residential:15.77, commercial:11.55, residential_yoy:3.4, commercial_yoy:3.3 },
  { state:"Georgia", abbr:"GA", region:"Southeast", residential:14.6, commercial:11.44, residential_yoy:3.0, commercial_yoy:3.5 },
  { state:"Hawaii", abbr:"HI", region:"West", residential:39.89, commercial:38.79, residential_yoy:7.5, commercial_yoy:8.9 },
  { state:"Idaho", abbr:"ID", region:"West", residential:12.51, commercial:8.19, residential_yoy:2.1, commercial_yoy:1.6 },
  { state:"Illinois", abbr:"IL", region:"Midwest", residential:18.82, commercial:14.01, residential_yoy:6.0, commercial_yoy:6.0 },
  { state:"Indiana", abbr:"IN", region:"Midwest", residential:17.42, commercial:14.16, residential_yoy:5.1, commercial_yoy:4.4 },
  { state:"Iowa", abbr:"IA", region:"Midwest", residential:13.54, commercial:13.31, residential_yoy:2.6, commercial_yoy:3.1 },
  { state:"Kansas", abbr:"KS", region:"Midwest", residential:15.23, commercial:12.05, residential_yoy:3.7, commercial_yoy:3.7 },
  { state:"Kentucky", abbr:"KY", region:"Southeast", residential:13.68, commercial:12.15, residential_yoy:2.9, commercial_yoy:2.7 },
  { state:"Louisiana", abbr:"LA", region:"South Central", residential:12.44, commercial:10.93, residential_yoy:1.8, commercial_yoy:3.0 },
  { state:"Maine", abbr:"ME", region:"Northeast", residential:29.55, commercial:21.4, residential_yoy:8.1, commercial_yoy:7.3 },
  { state:"Maryland", abbr:"MD", region:"Northeast", residential:22.4, commercial:15.18, residential_yoy:6.4, commercial_yoy:6.4 },
  { state:"Massachusetts", abbr:"MA", region:"Northeast", residential:31.51, commercial:23.4, residential_yoy:7.7, commercial_yoy:7.7 },
  { state:"Michigan", abbr:"MI", region:"Midwest", residential:20.55, commercial:14.92, residential_yoy:6.1, commercial_yoy:6.6 },
  { state:"Minnesota", abbr:"MN", region:"Midwest", residential:16.44, commercial:13.22, residential_yoy:4.0, commercial_yoy:3.7 },
  { state:"Mississippi", abbr:"MS", region:"Southeast", residential:14.53, commercial:12.67, residential_yoy:2.7, commercial_yoy:3.1 },
  { state:"Missouri", abbr:"MO", region:"Midwest", residential:13.01, commercial:12.51, residential_yoy:2.5, commercial_yoy:4.2 },
  { state:"Montana", abbr:"MT", region:"West", residential:14.33, commercial:12.61, residential_yoy:3.3, commercial_yoy:3.5 },
  { state:"Nebraska", abbr:"NE", region:"Midwest", residential:13.19, commercial:9.58, residential_yoy:2.4, commercial_yoy:2.3 },
  { state:"Nevada", abbr:"NV", region:"West", residential:13.83, commercial:9.91, residential_yoy:3.1, commercial_yoy:3.2 },
  { state:"New Hampshire", abbr:"NH", region:"Northeast", residential:27.39, commercial:20.54, residential_yoy:7.3, commercial_yoy:8.3 },
  { state:"New Jersey", abbr:"NJ", region:"Northeast", residential:22.65, commercial:18.78, residential_yoy:6.6, commercial_yoy:9.1 },
  { state:"New Mexico", abbr:"NM", region:"West", residential:15.0, commercial:12.24, residential_yoy:3.5, commercial_yoy:4.0 },
  { state:"New York", abbr:"NY", region:"Northeast", residential:27.07, commercial:22.54, residential_yoy:7.1, commercial_yoy:7.0 },
  { state:"North Carolina", abbr:"NC", region:"Southeast", residential:15.12, commercial:10.09, residential_yoy:3.2, commercial_yoy:3.3 },
  { state:"North Dakota", abbr:"ND", region:"Midwest", residential:12.87, commercial:7.44, residential_yoy:2.0, commercial_yoy:1.3 },
  { state:"Ohio", abbr:"OH", region:"Midwest", residential:17.93, commercial:11.55, residential_yoy:5.6, commercial_yoy:5.5 },
  { state:"Oklahoma", abbr:"OK", region:"South Central", residential:14.48, commercial:10.04, residential_yoy:3.4, commercial_yoy:3.7 },
  { state:"Oregon", abbr:"OR", region:"West", residential:16.23, commercial:11.36, residential_yoy:3.9, commercial_yoy:3.4 },
  { state:"Pennsylvania", abbr:"PA", region:"Northeast", residential:20.58, commercial:12.79, residential_yoy:6.3, commercial_yoy:6.2 },
  { state:"Rhode Island", abbr:"RI", region:"Northeast", residential:31.3, commercial:22.44, residential_yoy:8.4, commercial_yoy:8.6 },
  { state:"South Carolina", abbr:"SC", region:"Southeast", residential:15.71, commercial:10.88, residential_yoy:3.6, commercial_yoy:3.8 },
  { state:"South Dakota", abbr:"SD", region:"Midwest", residential:14.15, commercial:10.99, residential_yoy:2.8, commercial_yoy:3.2 },
  { state:"Tennessee", abbr:"TN", region:"Southeast", residential:13.12, commercial:13.02, residential_yoy:2.3, commercial_yoy:2.9 },
  { state:"Texas", abbr:"TX", region:"South Central", residential:16.18, commercial:9.12, residential_yoy:4.3, commercial_yoy:4.2 },
  { state:"Utah", abbr:"UT", region:"West", residential:13.75, commercial:10.87, residential_yoy:2.7, commercial_yoy:3.0 },
  { state:"Vermont", abbr:"VT", region:"Northeast", residential:24.89, commercial:19.33, residential_yoy:6.7, commercial_yoy:6.7 },
  { state:"Virginia", abbr:"VA", region:"Southeast", residential:16.43, commercial:9.73, residential_yoy:4.1, commercial_yoy:4.1 },
  { state:"Washington", abbr:"WA", region:"West", residential:14.12, commercial:11.9, residential_yoy:3.0, commercial_yoy:3.3 },
  { state:"West Virginia", abbr:"WV", region:"Southeast", residential:16.26, commercial:11.65, residential_yoy:4.5, commercial_yoy:4.4 },
  { state:"Wisconsin", abbr:"WI", region:"Midwest", residential:18.45, commercial:13.7, residential_yoy:5.8, commercial_yoy:5.7 },
  { state:"Wyoming", abbr:"WY", region:"West", residential:15.18, commercial:9.79, residential_yoy:3.6, commercial_yoy:3.5 }
];

const ELECTRICITY_NATIONAL = {
  residential: 18.05,
  commercial:  14.12,
  residential_yoy: 5.4,
  commercial_yoy:  5.0,
  source: "ElectricChoice.com (EIA data)",
  updated: "April 2026"
};

