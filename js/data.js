/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Data Layer
   All mock data in one place for easy future API replacement
   ═══════════════════════════════════════════════════════════════════ */

const COMMODITIES = [
  { name: "WTI Crude", price: 94.70, change: -1.45, pct: -1.51, unit: "$/bbl", spark: [83.5,86.2,89.4,92.1,95.8,96.15,94.70], loading: false },
  { name: "Brent Crude", price: 104.40, change: -1.62, pct: -1.53, unit: "$/bbl", spark: [88.5,91.3,94.8,98.5,103.2,106.02,104.40], loading: false },
  { name: "Natural Gas", price: 2.52, change: -0.091, pct: -3.48, unit: "$/MMBtu", spark: [2.78,2.74,2.69,2.65,2.62,2.61,2.52], loading: false },
  { name: "Gasoline RBOB", price: 3.18, change: -0.007, pct: -0.21, unit: "$/gal", spark: [2.85,2.92,3.05,3.13,3.18,3.19,3.18], loading: false },
  { name: "Heating Oil", price: 3.86, change: -0.04, pct: -1.03, unit: "$/gal", spark: [3.45,3.58,3.71,3.82,3.89,3.90,3.86], loading: false },
  { name: "Murban Crude", price: 105.20, change: -1.55, pct: -1.45, unit: "$/bbl", spark: [89,92,96,100,104,106,105.20], loading: false },
  { name: "Diesel ULSD", price: 3.86, change: -0.04, pct: -1.03, unit: "$/gal", spark: [3.45,3.58,3.71,3.82,3.89,3.90,3.86], loading: false },
  { name: "Jet Fuel", price: 4.18, change: -0.05, pct: -1.18, unit: "$/gal", spark: [3.78,3.89,4.02,4.15,4.21,4.23,4.18], loading: false },
  { name: "Coal", price: 134.9, change: 2.5, pct: 1.89, unit: "$/ton", spark: [110,109.5,109,108.5,108,107.8,107.7], loading: false },
  { name: "Gold", price: 4750.43, change: -83.04, pct: -1.75, unit: "$/oz", spark: [], loading: false },
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
  { title: "Europe Emerges As Key Buyer Of U.S. Strategic Petroleum Reserve Oil", cat: "Oil Markets", slug: "oil-prices", time: "1h" },
  { title: "Current price of oil as of April 24, 2026", cat: "Oil Markets", slug: "oil-prices", time: "2h" },
  { title: "Brent crude oil spot prices surge past futures price in April", cat: "Oil Markets", slug: "oil-prices", time: "3h" },
  { title: "Goldman Sachs Raises Oil Price Forecast Yet Again", cat: "Oil Markets", slug: "oil-prices", time: "4h" },
  { title: "US Oil Drillers Scale Back as Global Supply Crunch Continues", cat: "Oil Markets", slug: "oil-prices", time: "5h" },
  { title: "America barely uses Middle East oil. So why did gas prices rise?", cat: "Oil Markets", slug: "oil-prices", time: "6h" },
  { title: "Brent oil heads for record monthly surge, WTI settles above $100 for first time since 2022", cat: "Oil Markets", slug: "oil-prices", time: "7h" },
  { title: "Oil prices today: Crude falls below $100 as Trump announces two-week ceasefire with Iran", cat: "Oil Markets", slug: "oil-prices", time: "8h" },
];

const MARKET_DRIVERS = [
  { cat: "Talks Collapse", icon: "users", title: "Araghchi Leaves Pakistan Without Meeting U.S. Officials as Talks Collapse", desc: "Iran's FM Araghchi departed Islamabad Sunday April 26 without any direct meeting with U.S. officials, after Trump cancelled the Witkoff-Kushner trip Saturday. Pakistani PM Sharif and Iranian President Pezeshkian held a 50-minute phone call. Pakistani mediation continues but direct talks remain stalled." },
  { cat: "Oil Markets", icon: "trending-up", title: "WTI Up 13% on Week, Brent Up 18% on Hormuz Closure and Stalled Talks", desc: "WTI closed Friday at $94.70, Brent at $104.40 — both posting their biggest weekly gains since early March. Geopolitical risk premium fully embedded as Hormuz remains closed and U.S.-Iran diplomacy fails. Markets expected to push higher Monday on weekend talks collapse." },
  { cat: "Escalation", icon: "zap", title: "Trump Orders Navy to 'Shoot and Kill' Iranian Mine-Laying Vessels", desc: "Trump's April 22 escalation order moved U.S. naval rules of engagement from defensive clearance to active interdiction with lethal force authorized. U.S. forces also boarded a supertanker carrying Iranian oil in the Indian Ocean — interdiction now extends well beyond the Persian Gulf blockade zone." },
  { cat: "Lebanon", icon: "alert-triangle", title: "Israeli Strikes Kill 6 Including Lebanese Journalist Despite Ceasefire", desc: "Israeli strikes Saturday killed six in south Lebanon, including journalist Amal Khalil on April 22. Netanyahu ordered military to 'forcefully attack Hezbollah targets.' Truce extended three weeks but cycle of breaches threatens collapse. Lebanon front complicates parallel Iran negotiations." },
  { cat: "Hormuz", icon: "anchor", title: "Strait Remains Closed; Iran Lost Track of Mines It Planted", desc: "Hormuz remains essentially closed as the conflict enters its third month. Iran reportedly lost track of mines it laid in the strait, complicating any reopening even if diplomacy succeeds. Analysts say full normalization could take months even after a deal. Dual blockade continues." },
  { cat: "Diplomacy", icon: "users", title: "Pakistan Continues Back-Channel Mediation as Direct Talks Fail", desc: "Pakistan's Field Marshal Munir and PM Sharif remain primary mediators after second round of direct U.S.-Iran talks failed. Sharif-Pezeshkian phone call Saturday night lasted 50 minutes. Pakistan still ready to host talks 'at a moment's notice' if both sides agree to engage." },
];

const FEATURED_ARTICLES = [
  { id: 101, title: "Araghchi Leaves Pakistan Without Meeting U.S. Officials as Talks Collapse", excerpt: "Iran's Foreign Minister Abbas Araghchi left Islamabad on Sunday without meeting any U.S. officials, ending what had been billed as a potential second round of U.S.-Iran peace talks. Araghchi met only with Pakistani mediators after Trump cancelled the Witkoff-Kushner trip on Saturday. Pakistani back-channel diplomacy continues despite the failed direct meetings.", cat: "Geopolitics", slug: "geopolitics", author: "Staff", date: "Apr 26, 2026", readTime: "5 min", featured: true },
  { id: 102, title: "WTI Surges 13% on Week as Hormuz Stays Closed and Talks Stall", excerpt: "U.S. crude oil benchmarks posted their biggest weekly gain since early March, with WTI up 13% and Brent up roughly 18% on the week. Friday's session ended with WTI at $94.70 and Brent at $104.40 — Friday saw a brief pullback on talk-resumption hopes that collapsed by Saturday when Trump cancelled U.S. envoys' trip.", cat: "Oil Markets", slug: "oil-prices", author: "Staff", date: "Apr 24, 2026", readTime: "6 min" },
  { id: 103, title: "Trump Cancels Witkoff-Kushner Pakistan Trip as Iran Talks Stall", excerpt: "President Trump cancelled the planned trip of U.S. envoys Steve Witkoff and Jared Kushner to Islamabad on Saturday, halting what was expected to be the second formal round of U.S.-Iran peace talks. The cancellation followed mixed signals from Tehran about whether Iranian officials were prepared to engage substantively with U.S. demands.", cat: "Geopolitics", slug: "geopolitics", author: "Staff", date: "Apr 25, 2026", readTime: "6 min" },
  { id: 104, title: "Trump Orders Navy to 'Shoot and Kill' Iranian Mine-Laying Vessels in Strait", excerpt: "President Trump on Thursday ordered the U.S. Navy to 'shoot and kill' Iranian small boats observed laying mines in the Strait of Hormuz, marking the sharpest escalation in U.S. enforcement posture since the naval blockade began. U.S. forces also boarded a supertanker carrying Iranian oil in the Indian Ocean.", cat: "Geopolitics", slug: "geopolitics", author: "Staff", date: "Apr 22, 2026", readTime: "6 min" },
  { id: 105, title: "Israeli Strikes Kill Lebanese Journalist Amal Khalil During Extended Ceasefire", excerpt: "Lebanese journalist Amal Khalil was killed in an Israeli strike on April 22, sharply straining the extended Israel-Lebanon ceasefire. Multiple new Israeli strikes followed, killing six on Saturday despite the ceasefire's recent extension. Netanyahu ordered the military to 'forcefully attack Hezbollah targets' after the army accused the group of breaching the truce.", cat: "Geopolitics", slug: "geopolitics", author: "Staff", date: "Apr 23, 2026", readTime: "5 min" },
];

const COMPANY_NEWS = [
  { id: 201, title: "WTI Surges 13% on Week as Hormuz Stays Closed and Talks Stall", date: "Apr 24, 2026" },
  { id: 202, title: "Maersk, Hapag-Lloyd Maintain Hormuz Transit Suspension Amid Continued Uncertainty", date: "Apr 25, 2026" },
  { id: 203, title: "Saudi Aramco East-West Pipeline Continues at Full Capacity Through Blockade", date: "Apr 24, 2026" },
  { id: 204, title: "Cheniere Energy, Venture Global Ride LNG Premium as Qatar Flows Still Disrupted", date: "Apr 23, 2026" },
  { id: 205, title: "Energy Stocks Mixed as Ceasefire Extension Eases but Blockade Stays", date: "Apr 22, 2026" },
  { id: 206, title: "OPEC+ April Output Increase Proceeding Despite Market Volatility", date: "Apr 22, 2026" },
];

const GEO_ITEMS = [
  { id: 301, region: "Pakistan", title: "Araghchi Leaves Pakistan Without Meeting U.S. Officials as Talks Collapse", desc: "Iran's FM Araghchi departed Islamabad Sunday April 26 without any direct meeting with American counterparts. Met only with Pakistan's Field Marshal Munir and PM Sharif. Trump cancelled the Witkoff-Kushner trip Saturday. Sharif-Pezeshkian phone call Saturday night ran 50 minutes. Direct talks remain stalled." },
  { id: 303, region: "United States", title: "Trump Orders Navy to 'Shoot and Kill' Iranian Mine-Laying Vessels in Strait", desc: "Trump's April 22 escalation order moved U.S. naval rules of engagement from defensive clearance to active interdiction. Trump described blockade as 'unbelievably effective.' U.S. forces also boarded a supertanker carrying Iranian oil in the Indian Ocean — interdiction now extends well beyond the Persian Gulf." },
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
  // U.S. — Baker Hughes North America Rig Count, April 24, 2026
  us_total: 544, us_total_change: 1, us_oil: 407, us_oil_change: -3, us_gas: 129, us_gas_change: 4, us_misc: 8, us_misc_change: 0,
  us_land: 533, us_offshore: 11, us_inland: 0,
  us_directional: 48, us_horizontal: 484, us_vertical: 12,
  us_yoy: -43, us_yoy_total: 587,
  us_gom: 10,
  // Canada — April 24, 2026
  canada_total: 130, canada_change: 0, canada_oil: 80, canada_gas: 50,
  canada_yoy: -8, canada_yoy_total: 138,
  // North America
  na_total: 674, na_change: 1, na_yoy: -51, na_yoy_total: 725,
  // International — March 2026 (monthly report; April report due May 2)
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
      { id: 1410, title: "Araghchi Leaves Pakistan Without Meeting U.S. Officials as Talks Collapse", excerpt: "Iran's Foreign Minister Abbas Araghchi left Islamabad on Sunday April 26 without meeting any U.S. officials after Trump cancelled the Witkoff-Kushner trip Saturday. Pakistani back-channel mediation continues but direct talks remain stalled.", date: "Apr 26, 2026", author: "Staff", readTime: "5 min" },
      { id: 1411, title: "Trump Cancels Witkoff-Kushner Pakistan Trip as Iran Talks Stall", excerpt: "President Trump cancelled the planned Saturday trip of U.S. envoys Steve Witkoff and Jared Kushner to Islamabad, halting what was expected to be the second formal round of U.S.-Iran peace talks before it could begin.", date: "Apr 25, 2026", author: "Staff", readTime: "6 min" },
      { id: 1412, title: "Trump Orders Navy to 'Shoot and Kill' Iranian Mine-Laying Vessels in Strait", excerpt: "Trump's April 22 escalation order moved U.S. naval rules of engagement from defensive clearance to active interdiction with lethal force authorized. U.S. forces also boarded a supertanker carrying Iranian oil in the Indian Ocean.", date: "Apr 22, 2026", author: "Staff", readTime: "6 min" },
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
  { state:"Alabama", abbr:"AL", regular:3.76, mid:4.203, premium:4.609, diesel:5.329 },
  { state:"Alaska", abbr:"AK", regular:4.577, mid:4.797, premium:5.028, diesel:5.866 },
  { state:"Arizona", abbr:"AZ", regular:4.572, mid:4.954, premium:5.268, diesel:5.948 },
  { state:"Arkansas", abbr:"AR", regular:3.583, mid:4.033, premium:4.403, diesel:5.087 },
  { state:"California", abbr:"CA", regular:5.79, mid:6.033, premium:6.209, diesel:7.539 },
  { state:"Colorado", abbr:"CO", regular:3.887, mid:4.287, premium:4.609, diesel:5.086 },
  { state:"Connecticut", abbr:"CT", regular:4.037, mid:4.578, premium:4.967, diesel:5.849 },
  { state:"Delaware", abbr:"DE", regular:3.9, mid:4.5, premium:4.804, diesel:5.696 },
  { state:"District of Columbia", abbr:"DC", regular:4.257, mid:4.851, premium:5.227, diesel:5.842 },
  { state:"Florida", abbr:"FL", regular:4.068, mid:4.532, premium:4.861, diesel:5.533 },
  { state:"Georgia", abbr:"GA", regular:3.607, mid:4.067, premium:4.487, diesel:5.167 },
  { state:"Hawaii", abbr:"HI", regular:5.628, mid:5.862, premium:6.102, diesel:7.082 },
  { state:"Idaho", abbr:"ID", regular:4.272, mid:4.571, premium:4.839, diesel:5.451 },
  { state:"Illinois", abbr:"IL", regular:4.286, mid:4.863, premium:5.327, diesel:5.356 },
  { state:"Indiana", abbr:"IN", regular:3.797, mid:4.342, premium:4.835, diesel:5.351 },
  { state:"Iowa", abbr:"IA", regular:3.573, mid:3.795, premium:4.404, diesel:4.989 },
  { state:"Kansas", abbr:"KS", regular:3.444, mid:3.769, premium:4.102, diesel:4.691 },
  { state:"Kentucky", abbr:"KY", regular:3.905, mid:4.461, premium:4.884, diesel:5.281 },
  { state:"Louisiana", abbr:"LA", regular:3.676, mid:4.112, premium:4.496, diesel:5.165 },
  { state:"Maine", abbr:"ME", regular:3.948, mid:4.487, premium:4.971, diesel:5.794 },
  { state:"Maryland", abbr:"MD", regular:4.024, mid:4.633, premium:4.949, diesel:5.743 },
  { state:"Massachusetts", abbr:"MA", regular:3.927, mid:4.516, premium:4.896, diesel:5.814 },
  { state:"Michigan", abbr:"MI", regular:3.835, mid:4.43, premium:4.993, diesel:5.186 },
  { state:"Minnesota", abbr:"MN", regular:3.638, mid:4.068, premium:4.556, diesel:5.019 },
  { state:"Mississippi", abbr:"MS", regular:3.676, mid:4.102, premium:4.496, diesel:5.159 },
  { state:"Missouri", abbr:"MO", regular:3.606, mid:4.013, premium:4.323, diesel:4.827 },
  { state:"Montana", abbr:"MT", regular:3.835, mid:4.139, premium:4.48, diesel:4.938 },
  { state:"Nebraska", abbr:"NE", regular:3.567, mid:3.736, premium:4.195, diesel:4.829 },
  { state:"Nevada", abbr:"NV", regular:4.885, mid:5.203, premium:5.488, diesel:6.21 },
  { state:"New Hampshire", abbr:"NH", regular:3.904, mid:4.454, premium:4.914, diesel:5.751 },
  { state:"New Jersey", abbr:"NJ", regular:3.936, mid:4.485, premium:4.748, diesel:5.765 },
  { state:"New Mexico", abbr:"NM", regular:3.866, mid:4.291, premium:4.598, diesel:5.347 },
  { state:"New York", abbr:"NY", regular:4.091, mid:4.593, premium:4.972, diesel:5.901 },
  { state:"North Carolina", abbr:"NC", regular:3.781, mid:4.225, premium:4.621, diesel:5.628 },
  { state:"North Dakota", abbr:"ND", regular:3.553, mid:3.893, premium:4.306, diesel:4.815 },
  { state:"Ohio", abbr:"OH", regular:3.711, mid:4.243, premium:4.754, diesel:5.314 },
  { state:"Oklahoma", abbr:"OK", regular:3.39, mid:3.805, premium:4.09, diesel:4.703 },
  { state:"Oregon", abbr:"OR", regular:4.924, mid:5.149, premium:5.42, diesel:6.234 },
  { state:"Pennsylvania", abbr:"PA", regular:4.059, mid:4.498, premium:4.872, diesel:5.976 },
  { state:"Rhode Island", abbr:"RI", regular:3.923, mid:4.588, premium:5.011, diesel:5.723 },
  { state:"South Carolina", abbr:"SC", regular:3.709, mid:4.152, premium:4.55, diesel:5.508 },
  { state:"South Dakota", abbr:"SD", regular:3.621, mid:3.796, premium:4.267, diesel:4.776 },
  { state:"Tennessee", abbr:"TN", regular:3.78, mid:4.242, premium:4.631, diesel:5.349 },
  { state:"Texas", abbr:"TX", regular:3.683, mid:4.157, premium:4.531, diesel:5.189 },
  { state:"Utah", abbr:"UT", regular:4.143, mid:4.422, premium:4.669, diesel:5.295 },
  { state:"Vermont", abbr:"VT", regular:4.042, mid:4.533, premium:4.992, diesel:5.807 },
  { state:"Virginia", abbr:"VA", regular:3.893, mid:4.365, premium:4.741, diesel:5.657 },
  { state:"Washington", abbr:"WA", regular:5.317, mid:5.589, premium:5.823, diesel:6.857 },
  { state:"West Virginia", abbr:"WV", regular:3.861, mid:4.274, premium:4.729, diesel:5.457 },
  { state:"Wisconsin", abbr:"WI", regular:3.704, mid:4.21, premium:4.796, diesel:4.901 },
  { state:"Wyoming", abbr:"WY", regular:3.809, mid:4.119, premium:4.41, diesel:4.988 }
];

const US_GAS_NATIONAL = {
  regular: 4.044,
  mid: 4.655,
  premium: 5.024,
  diesel: 5.403,
  source: "EIA Weekly Retail Gasoline Prices",
  updated: "As of April 27, 2026"
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

