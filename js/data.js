/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Data Layer
   All mock data in one place for easy future API replacement
   ═══════════════════════════════════════════════════════════════════ */

const COMMODITIES = [
  { name: "WTI Crude", price: 96.57, change: -1.3, pct: -1.33, unit: "$/bbl", spark: [96,97,97.5,98,98.3,98.5,98.72], loading: false },
  { name: "Brent Crude", price: 95.2, change: -1.31, pct: -1.36, unit: "$/bbl", spark: [94,95,95.5,96,96.2,96.4,96.51], loading: false },
  { name: "Natural Gas", price: 2.65, change: -0.022, pct: -0.82, unit: "$/MMBtu", spark: [2.68,2.67,2.67,2.67,2.67,2.67,2.672], loading: false },
  { name: "Gasoline RBOB", price: 3.018, change: 0.037, pct: 1.22, unit: "$/gal", spark: [2.98,2.99,3.0,3.0,3.01,3.01,3.018], loading: false },
  { name: "Heating Oil", price: 3.74, change: -0.198, pct: -5.03, unit: "$/gal", spark: [3.92,3.93,3.94,3.95,3.96,3.97,3.975], loading: false },
  { name: "Murban Crude", price: 96.96, change: -1.31, pct: -1.33, unit: "$/bbl", spark: [97,97.5,98,98.5,99,99.3,99.62], loading: false },
  { name: "Diesel ULSD", price: 3.74, change: -0.17, pct: -4.35, unit: "$/gal", spark: [3.86,3.87,3.88,3.89,3.90,3.90,3.91], loading: false },
  { name: "Jet Fuel", price: 4.09, change: -0.14, pct: -3.31, unit: "$/gal", spark: [4.16,4.17,4.18,4.19,4.21,4.22,4.23], loading: false },
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
  { title: "U.S. and Iran Considering Two-Week Ceasefire Extension — Bloomberg Reports", cat: "Geopolitics", slug: "geopolitics", time: "Breaking" },
  { title: "Pakistan Army Chief Holds Emergency Talks in Tehran to Restart Negotiations", cat: "Geopolitics", slug: "geopolitics", time: "2h ago" },
  { title: "Iran Threatens to Block Red Sea and Gulf of Oman if U.S. Blockade Continues", cat: "Geopolitics", slug: "geopolitics", time: "4h ago" },
  { title: "Uranium Enrichment Timeframe Emerges as Key Sticking Point in Peace Talks", cat: "Geopolitics", slug: "geopolitics", time: "6h ago" },
  { title: "Israel-Lebanon Talks Conclude — Further Negotiations Agreed at Mutually Set Venue", cat: "Geopolitics", slug: "geopolitics", time: "8h ago" },
  { title: "Oil Prices Ease on Ceasefire Extension Hopes — WTI Pulls Back Below $95", cat: "Oil Prices", slug: "oil-prices", time: "10h ago" },
  { title: "U.S. Gas Prices Drop to $4.11 National Average as Crude Stabilizes", cat: "Gas Prices", slug: "gas-prices", time: "12h ago" },
  { title: "Vance Expected to Lead Second Round of Iran Negotiations if Talks Resume", cat: "Geopolitics", slug: "geopolitics", time: "14h ago" },
];

const MARKET_DRIVERS = [
  { cat: "CEASEFIRE EXTENSION", icon: "clock", title: "Two-Week Extension Discussed", desc: "U.S. and Iran considering extending the ceasefire beyond April 21 to allow more time for nuclear and Hormuz negotiations." },
  { cat: "PAKISTAN MEDIATION", icon: "message-circle", title: "Army Chief in Tehran", desc: "Pakistan\u2019s Field Marshal Asim Munir holds emergency talks in Iran to restart U.S.-Iran negotiations before ceasefire expires." },
  { cat: "IRAN ESCALATION", icon: "alert-triangle", title: "Red Sea Threat", desc: "Iran warns it will expand maritime disruptions to the Red Sea and Gulf of Oman if the U.S. naval blockade on Iranian ports continues." },
  { cat: "NUCLEAR TALKS", icon: "shield", title: "Enrichment Impasse", desc: "Both sides proposed suspending uranium enrichment but cannot agree on timeframe. U.S. demands dismantling of major facilities." },
  { cat: "LEBANON", icon: "map-pin", title: "Israel-Lebanon Progress", desc: "First direct talks conclude in Washington — further negotiations agreed. Israel refuses ceasefire commitment in south Lebanon." },
  { cat: "OIL MARKETS", icon: "trending-down", title: "Crude Eases on Hope", desc: "WTI pulls back below $95 on ceasefire extension reports. Gas prices ease to $4.11 national average." },
];

const FEATURED_ARTICLES = [
  { id: 101, title: "The New Oil Order: How OPEC+ Strategy Is Reshaping Global Crude Markets in 2026", excerpt: "A deep analysis of how OPEC+ production management has evolved into a more sophisticated price-targeting mechanism, and what it means for traders and consumers alike.", cat: "Analysis", slug: "energy", author: "Staff", date: "Mar 31, 2026", readTime: "8 min", featured: true },
  { id: 102, title: "Permian Basin Output Hits Record 6.2M Barrels Per Day", excerpt: "U.S. shale production continues to defy expectations as operators optimize well spacing and completion techniques.", cat: "Crude Oil", slug: "crude-oil", author: "Staff", date: "Mar 31, 2026", readTime: "5 min" },
  { id: 103, title: "Why European Gas Storage Levels Matter More Than Ever", excerpt: "With LNG supply contracts up for renewal and Russian pipeline flows diminished, European storage strategy becomes pivotal.", cat: "Natural Gas", slug: "natural-gas", author: "Staff", date: "Mar 30, 2026", readTime: "6 min" },
  { id: 104, title: "ExxonMobil vs. Chevron: Battle for Permian Supremacy", excerpt: "The two oil majors are taking divergent approaches to growth in America's most prolific basin.", cat: "Company News", slug: "company-news", author: "Staff", date: "Mar 30, 2026", readTime: "7 min" },
  { id: 105, title: "Nuclear Renaissance: Small Modular Reactors Enter Commercial Phase", excerpt: "After decades of promise, SMR technology is finally moving from pilot programs to grid-scale deployment.", cat: "Nuclear", slug: "nuclear", author: "Staff", date: "Mar 29, 2026", readTime: "9 min" },
];

const COMPANY_NEWS = [
  { id: 201, title: "Shell Reports Strong Q1 Upstream Earnings, Raises Dividend", date: "Mar 31, 2026" },
  { id: 202, title: "BP Accelerates Divestment of North Sea Assets", date: "Mar 30, 2026" },
  { id: 203, title: "TotalEnergies Signs Major LNG Supply Deal with India", date: "Mar 30, 2026" },
  { id: 204, title: "ConocoPhillips Completes Marathon Oil Merger Integration", date: "Mar 29, 2026" },
  { id: 205, title: "Saudi Aramco Invests $2B in South Korean Refining Complex", date: "Mar 29, 2026" },
  { id: 206, title: "Equinor Wins New Offshore Wind Contracts in the North Sea", date: "Mar 28, 2026" },
];

const GEO_ITEMS = [
  { id: 301, region: "Middle East", title: "Red Sea Shipping Disruptions Continue to Impact Oil Transit Routes", desc: "Houthi attacks force tankers to reroute around the Cape of Good Hope, adding 10-14 days to delivery times." },
  { id: 302, region: "Russia", title: "Russian Oil Exports Shift Further Toward Asian Markets", desc: "Moscow redirects crude flows to India and China as Western sanctions enforcement tightens." },
  { id: 303, region: "Americas", title: "Venezuela Sanctions Relief Under Review After Election Delays", desc: "U.S. weighs re-imposing oil sanctions amid concerns over democratic backsliding." },
  { id: 304, region: "Africa", title: "Nigerian Pipeline Security Improves, Boosting Crude Output", desc: "Bonny Light production rises 15% after government-backed security operations in the Niger Delta." },
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
  { id: 401, title: "Markets React to Unexpected Inventory Build in Cushing Hub", excerpt: "Cushing, Oklahoma storage levels rose by 1.8M barrels last week, pressuring nearby WTI spreads.", date: "Mar 31, 2026", author: "Staff", readTime: "5 min" },
  { id: 402, title: "Goldman Sachs Raises Brent Crude Forecast to $82 by Year-End", excerpt: "The bank cites stronger-than-expected demand from emerging markets and constrained OPEC+ supply.", date: "Mar 30, 2026", author: "Staff", readTime: "4 min" },
  { id: 403, title: "Iraq Struggles to Meet OPEC+ Production Quota Compliance", excerpt: "Baghdad's oil output consistently exceeds its agreed ceiling, creating tension within the alliance.", date: "Mar 30, 2026", author: "Staff", readTime: "6 min" },
  { id: 404, title: "Global Oil Demand Growth Slows to 900K BPD in 2026, IEA Says", excerpt: "The International Energy Agency revises down its demand growth estimate amid economic headwinds.", date: "Mar 29, 2026", author: "Staff", readTime: "5 min" },
  { id: 405, title: "New Deepwater Discovery Off Guyana Could Hold 1.5 Billion Barrels", excerpt: "ExxonMobil's latest exploration well confirms significant hydrocarbon reserves in the Stabroek Block.", date: "Mar 29, 2026", author: "Staff", readTime: "7 min" },
  { id: 406, title: "Keystone Pipeline Restarts After Maintenance Shutdown", excerpt: "TC Energy confirms the pipeline is back to full capacity after a scheduled two-week maintenance window.", date: "Mar 28, 2026", author: "Staff", readTime: "3 min" },
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
  us_total: 545, us_total_change: -3, us_oil: 411, us_oil_change: 0, us_gas: 127, us_gas_change: -3, us_misc: 7,
  permian: 248, permian_change: -1, eagle_ford: 42, eagle_ford_change: 0, bakken: 28, bakken_change: 0,
  canada_total: 108, canada_change: -5,
  intl_mideast: 342, intl_mideast_change: 8, intl_latam: 168, intl_latam_change: 3, intl_europe: 82, intl_europe_change: -2, intl_africa: 94, intl_africa_change: 1, intl_asiapac: 198, intl_asiapac_change: 0, intl_fsu: 74, intl_fsu_change: -3,
  source: "Baker Hughes", updated: "April 11, 2026"
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
  { label: "Infrastructure", title: "Suez Canal", desc: "Critical passage connecting Mediterranean and Asian oil markets via Egypt.", stat: "5.5M bpd", region: "Egypt" },
  { label: "Pipeline", title: "Druzhba Pipeline", desc: "Major crude pipeline from Russia to Central Europe, partially sanctioned since 2022.", stat: "1.2M bpd", region: "Russia → EU" },
  { label: "LNG Terminal", title: "U.S. Gulf Coast LNG", desc: "Record export capacity supporting European and Asian supply diversification.", stat: "14 Bcf/d", region: "United States" },
  { label: "Strait", title: "Strait of Malacca", desc: "Key Asian oil transit route connecting Indian Ocean to South China Sea.", stat: "16M bpd", region: "Southeast Asia" },
];

// ─── COMPREHENSIVE OIL PRICE DATA (mirrors OilPrice.com structure) ────
const OIL_PRICE_SECTIONS = [
  { title: "Crude Oil Benchmarks", flag: "", subtitle: "LIVE — updated every 5 minutes via API", rows: [
    { name: "WTI Crude", price: 96.57, change: -1.3, pct: -1.33, apiCode: "WTI_USD" },
    { name: "Brent Crude", price: 95.2, change: -1.31, pct: -1.36, apiCode: "BRENT_CRUDE_USD" },
    { name: "Tapis Crude", price: 99.10, change: 0.72, pct: 0.73, apiCode: "TAPIS_CRUDE_USD" },
    { name: "Murban Crude", price: 96.96, change: -1.31, pct: -1.33 },
  ]},
  { title: "Refined Products", flag: "", subtitle: "LIVE — updated every 5 minutes via API", rows: [
    { name: "Gasoline RBOB", price: 3.018, change: 0.037, pct: 1.22, apiCode: "GASOLINE_USD" },
    { name: "Heating Oil", price: 3.74, change: -0.198, pct: -5.03, apiCode: "HEATING_OIL_USD" },
    { name: "Diesel ULSD", price: 3.74, change: -0.17, pct: -4.35, apiCode: "DIESEL_USD" },
    { name: "Jet Fuel", price: 4.09, change: -0.14, pct: -3.31, apiCode: "JET_FUEL_USD" },
    { name: "Ethanol", price: 1.925, change: -0.025, pct: -1.28, apiCode: "ETHANOL_USD" },
  ]},
  { title: "Natural Gas & LNG", flag: "", subtitle: "LIVE — updated every 5 minutes via API", rows: [
    { name: "Henry Hub Natural Gas", price: 2.672, change: 0.002, pct: 0.07, apiCode: "NATURAL_GAS_USD" },
    { name: "UK NBP Natural Gas", price: 2.15, change: -0.03, pct: -1.38, apiCode: "NATURAL_GAS_GBP" },
    { name: "Dutch TTF Natural Gas", price: 15.56, change: -2.54, pct: -14.02, apiCode: "DUTCH_TTF_EUR" },
    { name: "JKM LNG (Japan/Korea)", price: 19.49, change: -0.38, pct: -1.89, apiCode: "JKM_LNG_USD" },
  ]},
  { title: "Coal Markets", flag: "", subtitle: "LIVE — updated via API", rows: [
    { name: "Newcastle Coal", price: 107.70, change: -2.10, pct: -1.91, apiCode: "NEWCASTLE_COAL_USD" },
    { name: "CAPP Coal (Central Appalachia)", price: 72.50, change: 0.35, pct: 0.49, apiCode: "CAPP_COAL_USD" },
    { name: "Coking Coal", price: 185.20, change: -1.80, pct: -0.96, apiCode: "COKING_COAL_USD" },
    { name: "NYMEX Appalachian Coal", price: 68.40, change: 0.22, pct: 0.32, apiCode: "NYMEX_APPALACHIAN_USD" },
  ]},
  { title: "Marine Fuels / Bunker", flag: "\u2693", subtitle: "LIVE — global bunker fuel prices via API", rows: [
    { name: "VLSFO (Very Low Sulfur Fuel Oil)", price: 548.00, change: 3.50, pct: 0.64, apiCode: "VLSFO_USD" },
    { name: "MGO 0.5% Sulfur", price: 712.00, change: -4.20, pct: -0.59, apiCode: "MGO_05S_USD" },
    { name: "HFO 380 CST", price: 418.00, change: 2.10, pct: 0.50, apiCode: "HFO_380_USD" },
    { name: "HFO 180 CST", price: 432.00, change: 1.80, pct: 0.42, apiCode: "HFO_180_USD" },
  ]},
  { title: "Metals, Carbon & Other", flag: "", subtitle: "LIVE — updated via API", rows: [
    { name: "Gold", price: 4750.43, change: -83.04, pct: -1.75, apiCode: "GOLD_USD" },
    { name: "Uranium", price: 89.50, change: 0.75, pct: 0.84, apiCode: "URANIUM_USD" },
    { name: "EU Carbon (EUA)", price: 68.20, change: -1.15, pct: -1.66, apiCode: "EU_CARBON_EUR" },
  ]},
  { title: "Forex", flag: "", subtitle: "LIVE — currency rates via API", rows: [
    { name: "GBP/USD", price: 1.2650, change: 0.0025, pct: 0.20, apiCode: "GBP_USD" },
    { name: "EUR/USD", price: 1.0820, change: -0.0015, pct: -0.14, apiCode: "EUR_USD" },
  ]},
  { title: "Energy Storage & Inventory", flag: "", subtitle: "LIVE — storage data via API", rows: [
    { name: "Cushing OK Crude Storage", price: 25.80, change: -1.20, pct: -4.44, apiCode: "CUSHING_STORAGE" },
    { name: "U.S. Natural Gas Storage", price: 1842.00, change: 28.00, pct: 1.54, apiCode: "NATURAL_GAS_STORAGE" },
  ]},
  { title: "Other Futures & Indexes", flag: "", subtitle: "Reference prices — 1-24hr delay", rows: [
    { name: "WTI Midland", price: 102.55, change: 3.54, pct: 3.58 },
    { name: "Mars", price: 98.5, change: 4.90, pct: 4.26 },
    { name: "OPEC Basket", price: 107.00, change: -17.12, pct: -13.79 },
    { name: "DME Oman", price: 95.15, change: -20.25, pct: -17.07 },
    { name: "Mexican Basket", price: 106.89, change: -0.13, pct: -0.12 },
    { name: "Indian Basket", price: 115.52, change: -20.11, pct: -14.83 },
    { name: "Urals", price: 88.4, change: -4.69, pct: -3.76 },
    { name: "Western Canadian Select", price: 82.06, change: -18.54, pct: -18.43 },
    { name: "AECO C Natural Gas", price: 1.030, change: 0.040, pct: 4.04 },
    { name: "Dubai", price: 94.6, change: -14.90, pct: -12.52 },
    { name: "Brent Weighted Average", price: 93.91, change: -15.71, pct: -14.33 },
    { name: "Louisiana Light", price: 122.58, change: 0.57, pct: 0.47 },
    { name: "Domestic Swt. @ Cushing", price: 90.89, change: -18.54, pct: -16.94 },
    { name: "Giddings", price: 84.64, change: -18.54, pct: -17.97 },
    { name: "ANS West Coast", price: 98.2, change: -2.22, pct: -1.85 },
    { name: "Gulf Coast HSFO", price: 80.86, change: -7.75, pct: -8.75 },
  ]},
  { title: "OPEC Members", flag: "", subtitle: "Daily pricing — 24hr delay", rows: [
    { name: "Arab Light", price: 112.72, change: -0.60, pct: -0.53 },
    { name: "Kuwait Export Blend", price: 100.63, change: -20.46, pct: -16.90 },
  ]},
  { title: "Australia", flag: "\ud83c\udde6\ud83c\uddfa", subtitle: "24hr delay", rows: [
    { name: "Cossack", price: 109.32, change: 3.83, pct: 3.63 },
    { name: "NWS Condensate", price: 106.02, change: 3.83, pct: 3.75 },
    { name: "Ichthys Condensate", price: 114.57, change: 3.83, pct: 3.46 },
  ]},
  { title: "Angola", flag: "\ud83c\udde6\ud83c\uddf4", subtitle: "24hr delay", rows: [
    { name: "Cabinda", price: 111.22, change: 3.83, pct: 3.57 },
    { name: "Nemba", price: 109.47, change: 3.83, pct: 3.63 },
    { name: "Dalia", price: 109.87, change: 3.83, pct: 3.61 },
  ]},
  { title: "Nigeria", flag: "\ud83c\uddf3\ud83c\uddec", subtitle: "24hr delay", rows: [
    { name: "Brass River", price: 114.62, change: 7.73, pct: 7.23 },
    { name: "Qua Iboe", price: 114.52, change: 7.73, pct: 7.24 },
  ]},
  { title: "UAE", flag: "\ud83c\udde6\ud83c\uddea", subtitle: "24hr delay", rows: [
    { name: "Das", price: 99.74, change: 0.57, pct: 0.57 },
    { name: "Umm Lulu", price: 100.24, change: 0.57, pct: 0.57 },
    { name: "Upper Zakum", price: 104.77, change: -2.28, pct: -2.13 },
  ]},
  { title: "Qatar", flag: "\ud83c\uddf6\ud83c\udde6", subtitle: "24hr delay", rows: [
    { name: "Qatar Land", price: 99.49, change: 0.57, pct: 0.58 },
    { name: "Al Shaheen", price: 104.77, change: -2.28, pct: -2.13 },
    { name: "D.F. Condensate", price: 93.36, change: 4.90, pct: 5.54 },
    { name: "L.S. Condensate", price: 93.06, change: 4.90, pct: 5.56 },
  ]},
  { title: "Iraq", flag: "\ud83c\uddee\ud83c\uddf6", subtitle: "24hr delay", rows: [
    { name: "Basrah Heavy", price: 111.13, change: -1.31, pct: -1.17 },
    { name: "Basrah Medium", price: 113.23, change: -1.31, pct: -1.14 },
  ]},
  { title: "Saudi Arabia", flag: "\ud83c\uddf8\ud83c\udde6", subtitle: "24hr delay", rows: [
    { name: "Arab Extra Light", price: 113.22, change: -0.60, pct: -0.53 },
    { name: "Arab Light", price: 112.72, change: -0.60, pct: -0.53 },
    { name: "Arab Medium", price: 110.97, change: -0.60, pct: -0.54 },
    { name: "Arab Heavy", price: 109.62, change: -0.60, pct: -0.54 },
  ]},
  { title: "Ecuador", flag: "\ud83c\uddea\ud83c\udde8", subtitle: "3 day delay", rows: [
    { name: "Oriente Crude", price: 106.45, change: 4.27, pct: 4.18 },
    { name: "Napo Crude", price: 95.96, change: 4.27, pct: 4.66 },
  ]},
  { title: "Mexico", flag: "\ud83c\uddf2\ud83c\uddfd", subtitle: "24hr delay", rows: [
    { name: "Maya (Gulf Coast)", price: 95.56, change: 0.22, pct: 0.23 },
    { name: "Isthmus (Gulf Coast)", price: 110.27, change: 0.34, pct: 0.31 },
    { name: "Olmeca", price: 109.65, change: 0.20, pct: 0.19 },
    { name: "Maya (West Coast)", price: 95.36, change: 0.22, pct: 0.23 },
    { name: "Maya (Far East)", price: 94.86, change: -17.58, pct: -15.63 },
    { name: "Isthmus (Far East)", price: 95.46, change: -17.58, pct: -15.55 },
  ]},
  { title: "Iran", flag: "\ud83c\uddee\ud83c\uddf7", subtitle: "24hr delay", rows: [
    { name: "Iran Light (NW Europe)", price: 91.61, change: -15.71, pct: -14.64 },
    { name: "Iran Heavy (NW Europe)", price: 89.71, change: -15.71, pct: -14.90 },
    { name: "Forozan Blend (NW Europe)", price: 89.96, change: -15.71, pct: -14.87 },
    { name: "Iran Light (Mediterranean)", price: 90.96, change: -15.71, pct: -14.73 },
    { name: "Iran Heavy (Mediterranean)", price: 88.81, change: -15.71, pct: -15.03 },
    { name: "Forozan Blend (Med.)", price: 89.06, change: -15.71, pct: -14.99 },
    { name: "Soroosh", price: 85.81, change: -15.71, pct: -15.47 },
    { name: "Iran Light (Sidi Kerir)", price: 92.86, change: -15.71, pct: -14.47 },
    { name: "Iran Heavy (Sidi Kerir)", price: 90.71, change: -15.71, pct: -14.76 },
    { name: "Iran Light (South Africa)", price: 91.61, change: -15.71, pct: -14.64 },
    { name: "Iran Heavy (South Africa)", price: 89.71, change: -15.71, pct: -14.90 },
  ]},
  { title: "Russia", flag: "\ud83c\uddf7\ud83c\uddfa", subtitle: "24hr delay", rows: [
    { name: "Sokol", price: 101.78, change: 4.90, pct: 5.06 },
    { name: "Urals", price: 120.16, change: -4.69, pct: -3.76 },
  ]},
  { title: "Azerbaijan", flag: "\ud83c\udde6\ud83c\uddff", subtitle: "24hr delay", rows: [
    { name: "Azeri Light", price: 117.74, change: 2.72, pct: 2.36 },
  ]},
  { title: "Brazil", flag: "\ud83c\udde7\ud83c\uddf7", subtitle: "24hr delay", rows: [
    { name: "Lula", price: 107.32, change: 4.10, pct: 3.97 },
  ]},
  { title: "Kazakhstan", flag: "\ud83c\uddf0\ud83c\uddff", subtitle: "24hr delay", rows: [
    { name: "CPC Blend", price: 113.74, change: 2.72, pct: 2.45 },
  ]},
  { title: "Canada", flag: "\ud83c\udde8\ud83c\udde6", subtitle: "20hr delay", rows: [
    { name: "Western Canadian Select", price: 82.06, change: -18.54, pct: -18.43 },
    { name: "Central Alberta", price: 86.26, change: -18.54, pct: -17.69 },
    { name: "Light Sour Blend", price: 86.66, change: -18.54, pct: -17.62 },
    { name: "Peace Sour", price: 86.41, change: -18.54, pct: -17.67 },
    { name: "Syncrude Sweet Premium", price: 90.91, change: -18.54, pct: -16.94 },
    { name: "Sweet Crude", price: 88.66, change: -18.54, pct: -17.29 },
    { name: "US High Sweet Clearbrook", price: 92.56, change: -18.54, pct: -16.69 },
    { name: "Midale", price: 86.91, change: -18.54, pct: -17.58 },
    { name: "Albian Heavy Synthetic", price: 93.91, change: -18.54, pct: -16.49 },
    { name: "Access Western Blend", price: 93.51, change: -18.54, pct: -16.55 },
  ]},
  { title: "United States — Texas", flag: "\ud83c\uddfa\ud83c\uddf8", subtitle: "24hr delay", rows: [
    { name: "West Texas Sour", price: 90.29, change: -18.54, pct: -17.04 },
    { name: "West Texas Intermediate", price: 90.89, change: -18.54, pct: -16.94 },
    { name: "Eagle Ford", price: 90.89, change: -18.54, pct: -16.94 },
    { name: "North Texas Sweet", price: 91.50, change: -18.50, pct: -16.82 },
    { name: "South Texas Sour", price: 78.14, change: -18.54, pct: -19.18 },
    { name: "South Texas Light", price: 85.25, change: -18.50, pct: -17.83 },
    { name: "Upper Texas Gulf Coast", price: 84.64, change: -18.54, pct: -17.97 },
    { name: "Texas Gulf Coast Light", price: 84.64, change: -18.54, pct: -17.97 },
    { name: "Tx. Upper Gulf Coast", price: 85.25, change: -18.50, pct: -17.83 },
    { name: "W. Tx./N. Mex. Inter.", price: 91.50, change: -18.50, pct: -16.82 },
    { name: "W. Cen. Tx. Inter.", price: 91.50, change: -18.50, pct: -16.82 },
    { name: "East Texas Sweet", price: 88.75, change: -18.50, pct: -17.25 },
  ]},
  { title: "United States — Oklahoma", flag: "\ud83c\uddfa\ud83c\uddf8", subtitle: "24hr delay", rows: [
    { name: "Oklahoma Sweet", price: 91.50, change: -18.50, pct: -16.82 },
    { name: "Oklahoma Sour", price: 79.50, change: -18.50, pct: -18.88 },
    { name: "Western Oklahoma Swt.", price: 90.75, change: -18.50, pct: -16.93 },
    { name: "Oklahoma Intermediate", price: 91.25, change: -18.50, pct: -16.86 },
  ]},
  { title: "United States — Other States", flag: "\ud83c\uddfa\ud83c\uddf8", subtitle: "1-9 day delay", rows: [
    { name: "Wyoming General Sour", price: 87.47, change: -18.54, pct: -17.49 },
    { name: "Wyoming General Sweet", price: 87.99, change: -18.54, pct: -17.40 },
    { name: "Colorado South East", price: 81.39, change: -18.54, pct: -18.55 },
    { name: "Nebraska Sweet", price: 82.19, change: -18.54, pct: -18.41 },
    { name: "Michigan Sour", price: 83.50, change: -18.50, pct: -18.14 },
    { name: "Michigan Sweet", price: 88.25, change: -18.50, pct: -17.33 },
    { name: "Delhi/N. Louisiana", price: 88.50, change: -18.50, pct: -17.29 },
    { name: "South Louisiana", price: 90.00, change: -18.50, pct: -17.05 },
    { name: "Kansas Common", price: 81.24, change: -18.54, pct: -18.58 },
    { name: "NW Kansas Sweet", price: 82.39, change: -18.54, pct: -18.37 },
    { name: "SW Kansas Sweet", price: 82.89, change: -18.54, pct: -18.28 },
    { name: "Arkansas Sweet", price: 95.50, change: -1.50, pct: -1.55 },
    { name: "Arkansas Sour", price: 94.25, change: -1.50, pct: -1.57 },
    { name: "Arkansas Ex Heavy", price: 89.00, change: -1.50, pct: -1.66 },
  ]},
];

// ─── UNIQUE CONTENT PER CATEGORY PAGE ──────────────────────────────
const CATEGORY_CONTENT = {
  "oil-prices": {
    articles: [
      { id: 1001, title: "WTI Crude Climbs Past $71 as U.S. Inventories Post Sharp Drawdown", excerpt: "Commercial crude stocks at Cushing fell 4.2M barrels, well above the 1.8M consensus, signaling strong refinery demand ahead of driving season.", date: "Apr 4, 2026", author: "Staff", readTime: "5 min" },
      { id: 1002, title: "Brent-WTI Spread Widens to $4.44 on Atlantic Basin Tightness", excerpt: "North Sea supply disruptions and strong European refinery margins are pulling Brent higher relative to WTI.", date: "Apr 3, 2026", author: "Staff", readTime: "4 min" },
      { id: 1003, title: "Goldman Sachs Raises Brent Forecast to $82 by Year-End", excerpt: "The bank cites stronger-than-expected emerging market demand growth and disciplined OPEC+ supply management.", date: "Apr 2, 2026", author: "Staff", readTime: "4 min" },
      { id: 1004, title: "OPEC Basket Price Holds Above $74 Amid Production Cut Extensions", excerpt: "The reference basket used by OPEC member nations remains elevated as voluntary cuts of 2.2M bpd persist through Q3.", date: "Apr 1, 2026", author: "Staff", readTime: "5 min" },
      { id: 1005, title: "Dubai Crude Fetches Premium as Asian Refiners Compete for Sour Barrels", excerpt: "The Dubai benchmark has firmed on strong buying from Indian and Chinese refiners seeking Middle Eastern grades.", date: "Mar 31, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "WTI Crude", value: "$71.48", sub: "+1.75%" },
      { label: "Brent Crude", value: "$75.92", sub: "+1.16%" },
      { label: "OPEC Basket", value: "$74.12", sub: "+0.88%" },
    ]
  },
  "oil-futures": {
    articles: [
      { id: 1101, title: "WTI Futures Curve Flips to Backwardation Through December 2026", excerpt: "Front-month contracts now trade at a premium to deferred months, signaling near-term supply tightness.", date: "Apr 4, 2026", author: "Staff", readTime: "6 min" },
      { id: 1102, title: "Brent Futures Open Interest Hits 3-Month High Ahead of OPEC Meeting", excerpt: "Speculative positioning in Brent crude futures has surged as traders anticipate policy signals from Vienna.", date: "Apr 3, 2026", author: "Staff", readTime: "5 min" },
      { id: 1103, title: "Options Market Pricing Elevated Volatility Through Summer 2026", excerpt: "Implied volatility on WTI calls has risen 18% as geopolitical risk and demand uncertainty drive hedging activity.", date: "Apr 2, 2026", author: "Staff", readTime: "5 min" },
      { id: 1104, title: "Managed Money Net Longs in Crude Futures Rise for Fourth Straight Week", excerpt: "CFTC data shows hedge funds increasing bullish bets on oil as macro headwinds appear to be easing.", date: "Apr 1, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "WTI Front Month", value: "$71.48", sub: "May 2026" },
      { label: "Brent Front Month", value: "$75.92", sub: "May 2026" },
      { label: "Curve Shape", value: "Backwardation", sub: "-$2.58 12-mo" },
    ]
  },
  "rig-count": {
    articles: [
      { id: 1201, title: "U.S. Rig Count Falls to 584, Down 5 From Prior Week", excerpt: "Baker Hughes data shows continued drilling pullback as operators prioritize capital discipline over volume growth.", date: "Apr 4, 2026", author: "Staff", readTime: "3 min" },
      { id: 1202, title: "Permian Basin Rigs Hold Steady at 302 Despite Overall U.S. Decline", excerpt: "The nation's most prolific basin continues to attract investment even as secondary plays see rig reductions.", date: "Apr 3, 2026", author: "Staff", readTime: "5 min" },
      { id: 1203, title: "Canadian Rig Count Rebounds to 118 as Spring Drilling Season Begins", excerpt: "Freeze-thaw cycle restrictions are easing across Alberta and Saskatchewan, allowing crews to mobilize.", date: "Apr 2, 2026", author: "Staff", readTime: "4 min" },
      { id: 1204, title: "International Rig Count Stable at 958 as Middle East Activity Rises", excerpt: "Saudi Arabia and UAE are adding rigs to maintain production capacity even as OPEC+ quotas limit output.", date: "Apr 1, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "U.S. Total", value: "584", sub: "-5 w/w" },
      { label: "U.S. Oil Rigs", value: "479", sub: "-3 w/w" },
      { label: "Permian Basin", value: "302", sub: "Steady" },
    ]
  },
  "energy": {
    articles: [
      { id: 1301, title: "Global Energy Demand Growth Slows to 1.2% in 2026, IEA Reports", excerpt: "The International Energy Agency's latest monthly report shows moderating consumption growth driven by Chinese economic headwinds and efficiency gains.", date: "Apr 4, 2026", author: "Staff", readTime: "7 min" },
      { id: 1302, title: "U.S. Power Grid Faces Record Summer Demand From Data Center Expansion", excerpt: "AI-driven data center buildouts are straining electricity infrastructure across Texas, Virginia, and the Southwest.", date: "Apr 3, 2026", author: "Staff", readTime: "6 min" },
      { id: 1303, title: "European Energy Security Improves as LNG Import Capacity Doubles Since 2022", excerpt: "New regasification terminals in Germany, Italy, and Greece have significantly reduced Europe's vulnerability to supply shocks.", date: "Apr 2, 2026", author: "Staff", readTime: "5 min" },
      { id: 1304, title: "India's Energy Consumption Surpasses Japan for First Time", excerpt: "Rapid industrialization and a growing middle class push India past Japan as the world's fourth-largest energy consumer.", date: "Apr 1, 2026", author: "Staff", readTime: "5 min" },
      { id: 1305, title: "Carbon Capture Investment Reaches $12B Globally in 2025", excerpt: "Direct air capture and point-source CCS projects are scaling up as government subsidies and carbon pricing incentivize deployment.", date: "Mar 31, 2026", author: "Staff", readTime: "6 min" },
    ],
    stats: [
      { label: "Global Demand", value: "104.2M", sub: "bpd (oil equiv.)" },
      { label: "U.S. Production", value: "13.4M", sub: "bpd crude" },
      { label: "LNG Exports", value: "14 Bcf/d", sub: "U.S. Gulf" },
    ]
  },
  "crude-oil": {
    articles: [
      { id: 1401, title: "Permian Basin Production Hits Record 6.2 Million Barrels Per Day", excerpt: "Improved well productivity and extended lateral lengths continue to push U.S. shale output higher despite a falling rig count.", date: "Apr 4, 2026", author: "Staff", readTime: "6 min" },
      { id: 1402, title: "Guyana's Stabroek Block Delivers New 1.5 Billion Barrel Discovery", excerpt: "ExxonMobil's latest exploration well adds to what is already one of the most significant deepwater oil provinces found this century.", date: "Apr 3, 2026", author: "Staff", readTime: "7 min" },
      { id: 1403, title: "OPEC+ Compliance Reaches 116% as Iraq Over-Produces Again", excerpt: "Baghdad's output consistently exceeds its agreed ceiling, creating tension within the alliance and complicating quota negotiations.", date: "Apr 2, 2026", author: "Staff", readTime: "5 min" },
      { id: 1404, title: "North Sea Forties Pipeline Restart Eases Brent Supply Concerns", excerpt: "The 450,000 bpd system returns to full capacity after a 10-day maintenance shutdown that briefly tightened dated Brent.", date: "Apr 1, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "U.S. Production", value: "13.4M", sub: "bpd" },
      { label: "OPEC Output", value: "26.8M", sub: "bpd" },
      { label: "Global Supply", value: "102.6M", sub: "bpd" },
    ]
  },
  "gas-prices": {
    articles: [
      { id: 1501, title: "U.S. Average Gas Price Rises to $3.42/Gallon Ahead of Spring Driving Season", excerpt: "AAA reports retail gasoline prices are up 12 cents from a month ago as refiners switch to costlier summer-blend formulations.", date: "Apr 4, 2026", author: "Staff", readTime: "3 min" },
      { id: 1502, title: "California Gas Prices Hit $5.18 as State-Specific Regulations Add Costs", excerpt: "The Golden State's unique fuel standards and carbon pricing continue to push pump prices well above the national average.", date: "Apr 3, 2026", author: "Staff", readTime: "5 min" },
      { id: 1503, title: "Gulf Coast Refinery Margins Improve as Crack Spreads Widen", excerpt: "The 3-2-1 crack spread has expanded to $28/barrel, incentivizing higher refinery utilization rates.", date: "Apr 2, 2026", author: "Staff", readTime: "4 min" },
      { id: 1504, title: "EIA: U.S. Summer Gasoline Demand Expected to Average 9.1M BPD", excerpt: "The Energy Information Administration forecasts steady consumption growth despite elevated prices and rising EV adoption.", date: "Apr 1, 2026", author: "Staff", readTime: "5 min" },
    ],
    stats: [
      { label: "U.S. National Avg", value: "$3.42", sub: "/gallon" },
      { label: "RBOB Futures", value: "$2.18", sub: "/gallon" },
      { label: "Crack Spread", value: "$28.00", sub: "3-2-1" },
    ]
  },
  "natural-gas": {
    articles: [
      { id: 1601, title: "Henry Hub Falls Below $3.50 as U.S. Storage Surplus Persists", excerpt: "Above-average inventories and record production continue to weigh on domestic natural gas prices despite rising export demand.", date: "Apr 4, 2026", author: "Staff", readTime: "5 min" },
      { id: 1602, title: "European TTF Gas Rallies 12% on Extended Cold Weather Forecast", excerpt: "A late-season cold snap across Northern Europe is drawing down storage reserves faster than seasonal norms.", date: "Apr 3, 2026", author: "Staff", readTime: "4 min" },
      { id: 1603, title: "U.S. LNG Exports Hit Record 14 Bcf/d as Golden Pass Begins Operations", excerpt: "The new Qatar-Exxon joint venture facility in Texas adds 2.5 Bcf/d of liquefaction capacity to the Gulf Coast.", date: "Apr 2, 2026", author: "Staff", readTime: "6 min" },
      { id: 1604, title: "Japan LNG Spot Price Drops to $12.40/MMBtu on Mild Asian Demand", excerpt: "Warmer-than-normal temperatures across Northeast Asia reduce heating gas requirements heading into spring.", date: "Apr 1, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "Henry Hub", value: "$3.42", sub: "/MMBtu" },
      { label: "TTF Dutch", value: "€11.85", sub: "/MWh" },
      { label: "JKM LNG", value: "$12.40", sub: "/MMBtu" },
    ]
  },
  "heating-oil": {
    articles: [
      { id: 1701, title: "Heating Oil Futures Ease as Winter Demand Season Winds Down", excerpt: "NYMEX heating oil contracts slip as warmer spring temperatures reduce residential heating demand across the Northeast.", date: "Apr 4, 2026", author: "Staff", readTime: "3 min" },
      { id: 1702, title: "Northeast Home Heating Costs Rose 8% This Winter vs. Last Year", excerpt: "The EIA's Winter Fuels Outlook post-mortem shows higher crude prices and cold January temps drove seasonal cost increases.", date: "Apr 3, 2026", author: "Staff", readTime: "5 min" },
      { id: 1703, title: "Diesel and Heating Oil Margins Diverge as Trucking Demand Holds", excerpt: "While residential heating demand fades, strong freight activity keeps middle distillate markets well-supported.", date: "Apr 2, 2026", author: "Staff", readTime: "4 min" },
      { id: 1704, title: "European Diesel Imports From Asia Rise as Arbitrage Window Opens", excerpt: "A widening East-West price differential is pulling Asian diesel cargoes toward Europe for the first time since January.", date: "Apr 1, 2026", author: "Staff", readTime: "5 min" },
    ],
    stats: [
      { label: "Heating Oil", value: "$2.34", sub: "/gallon" },
      { label: "Diesel", value: "$2.41", sub: "/gallon" },
      { label: "Distillate Stock", value: "118M", sub: "barrels" },
    ]
  },
  "geopolitics": {
    articles: [
      { id: 1801, title: "Islamabad Talks Collapse After 21-Hour Marathon — No Deal Reached Between U.S. and Iran", excerpt: "The highest-level U.S.-Iran negotiations since 1979 ended without agreement. Vance blamed Iran for refusing nuclear commitments. Trump announces full naval blockade of Hormuz.", date: "Apr 12, 2026", author: "Staff", readTime: "8 min" },
      { id: 1802, title: "Trump Announces Full Naval Blockade of Strait of Hormuz", excerpt: "Following failed Islamabad talks, President Trump orders U.S. Navy to blockade the strait and interdict all vessels that paid transit tolls to Iran.", date: "Apr 12, 2026", author: "Staff", readTime: "6 min" },
      { id: 1803, title: "Ceasefire Expires April 22 With No Extension in Sight", excerpt: "The two-week truce brokered by Pakistan runs out in 10 days. Without a deal, the conflict could resume with even greater intensity.", date: "Apr 12, 2026", author: "Staff", readTime: "5 min" },
      { id: 1804, title: "Iran Nuclear Program Remains Central Sticking Point in U.S. Negotiations", excerpt: "Tehran refuses to commit to ending uranium enrichment — Washington calls it the core requirement for any deal.", date: "Apr 12, 2026", author: "Staff", readTime: "7 min" },
      { id: 1805, title: "Israel Struck 200+ Hezbollah Targets During Islamabad Peace Talks", excerpt: "Military operations in Lebanon continued unabated even as diplomats negotiated in Pakistan, complicating ceasefire prospects.", date: "Apr 12, 2026", author: "Staff", readTime: "5 min" },
      { id: 1806, title: "Pakistan Urges Continued Diplomacy After U.S.-Iran Talks End Without Deal", excerpt: "PM Sharif calls on both sides to uphold ceasefire commitments while keeping diplomatic channels open.", date: "Apr 12, 2026", author: "Staff", readTime: "4 min" },
      { id: 1807, title: "Oil Markets Face Renewed Volatility as Islamabad Talks Fail", excerpt: "Crude prices expected to surge when markets open Monday as geopolitical risk premium rebuilds after diplomatic breakdown.", date: "Apr 12, 2026", author: "Staff", readTime: "6 min" },
      { id: 1808, title: "Strait of Hormuz: From Iranian Blockade to U.S. Naval Blockade", excerpt: "The world's most critical oil chokepoint faces competing closure threats from both sides of the conflict.", date: "Apr 12, 2026", author: "Staff", readTime: "7 min" },
      { id: 1809, title: "Israel-Lebanon Direct Negotiations Set for Tuesday in Washington", excerpt: "First official talks between the two countries in decades aim to address Hezbollah disarmament and border security.", date: "Apr 12, 2026", author: "Staff", readTime: "5 min" },
      { id: 1810, title: "Global Energy Crisis Deepens as Diplomatic Off-Ramp Narrows", excerpt: "IEA warns current crisis could exceed 1970s oil shocks. European gas prices remain elevated. U.S. consumers face $4+ gas.", date: "Apr 12, 2026", author: "Staff", readTime: "6 min" },
    ],
    stats: []
  },
  "company-news": {
    articles: [
      { id: 1901, title: "ExxonMobil Reports $9.2B Q1 Profit, Raises Dividend 4%", excerpt: "Strong upstream earnings from the Permian Basin and Guyana offset weaker downstream margins in the quarter.", date: "Apr 4, 2026", author: "Staff", readTime: "5 min" },
      { id: 1902, title: "Shell Accelerates North Sea Asset Sales Worth $4.5B", excerpt: "The energy major continues divesting mature UK and Norwegian assets to focus capital on high-return deepwater projects.", date: "Apr 3, 2026", author: "Staff", readTime: "4 min" },
      { id: 1903, title: "Chevron Completes Hess Merger, Gains Guyana Stabroek Stake", excerpt: "The $53B deal closes after FTC review, giving Chevron a 30% stake in one of the world's fastest-growing oil provinces.", date: "Apr 2, 2026", author: "Staff", readTime: "6 min" },
      { id: 1904, title: "TotalEnergies Signs 20-Year LNG Supply Agreement with India", excerpt: "The deal secures 3 MTPA of LNG from Mozambique's Area 1 project, supporting India's coal-to-gas transition strategy.", date: "Apr 1, 2026", author: "Staff", readTime: "5 min" },
      { id: 1905, title: "Saudi Aramco Invests $2B in South Korean Refinery Expansion", excerpt: "The investment strengthens Aramco's downstream integration strategy and secures long-term crude supply placement in Asia.", date: "Mar 31, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: []
  },
  "alternative-energy": {
    articles: [
      { id: 2001, title: "Global Renewable Investment Hits $1.8 Trillion in 2025, IRENA Reports", excerpt: "Solar, wind, and battery storage captured 80% of new power generation investment worldwide for the first time.", date: "Apr 4, 2026", author: "Staff", readTime: "6 min" },
      { id: 2002, title: "Green Hydrogen Costs Fall 40% Since 2022 as Electrolyzer Scale Grows", excerpt: "Projects in Saudi Arabia, Australia, and Chile are proving that sub-$3/kg green hydrogen is achievable at scale.", date: "Apr 3, 2026", author: "Staff", readTime: "5 min" },
      { id: 2003, title: "Battery Storage Deployments Triple Year-Over-Year in the U.S.", excerpt: "Grid-scale lithium-ion installations reached 18 GW in 2025 as utilities pair storage with solar to meet peak demand.", date: "Apr 2, 2026", author: "Staff", readTime: "5 min" },
      { id: 2004, title: "EU Carbon Price Stabilizes at €85/Tonne, Supporting Clean Energy Economics", excerpt: "The Emissions Trading System continues to make fossil fuel power generation more expensive relative to renewables.", date: "Apr 1, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "Renewable CapEx", value: "$1.8T", sub: "2025 global" },
      { label: "Solar Cost", value: "$24", sub: "/MWh avg" },
      { label: "EV Sales Share", value: "22%", sub: "global 2025" },
    ]
  },
  "nuclear": {
    articles: [
      { id: 2101, title: "NuScale Small Modular Reactor Receives Full NRC Design Certification", excerpt: "The 77 MWe module becomes the first SMR to complete the U.S. regulatory approval process, clearing the path for commercial deployment.", date: "Apr 4, 2026", author: "Staff", readTime: "7 min" },
      { id: 2102, title: "France Commits €10B to Build Six New EPR2 Reactors by 2040", excerpt: "President Macron's nuclear renaissance plan aims to replace aging reactors while supporting European energy independence.", date: "Apr 3, 2026", author: "Staff", readTime: "6 min" },
      { id: 2103, title: "Uranium Spot Price Surges to $92/lb as Utility Contracting Accelerates", excerpt: "After a decade of low prices, uranium has rallied 180% since 2023 on renewed nuclear ambitions from the U.S., China, and India.", date: "Apr 2, 2026", author: "Staff", readTime: "5 min" },
      { id: 2104, title: "Microsoft Signs 20-Year Nuclear Power Purchase Agreement for Data Centers", excerpt: "The tech giant secures carbon-free baseload power from Constellation Energy's reactor fleet to support AI computing growth.", date: "Apr 1, 2026", author: "Staff", readTime: "5 min" },
    ],
    stats: [
      { label: "Uranium Price", value: "$92", sub: "/lb U₃O₈" },
      { label: "Global Reactors", value: "440", sub: "operational" },
      { label: "Under Constr.", value: "62", sub: "reactors" },
    ]
  },
  "solar": {
    articles: [
      { id: 2201, title: "Global Solar Installations Reach Record 420 GW in 2025", excerpt: "China alone accounted for 230 GW of new solar capacity as module prices fell below $0.10/watt for the first time.", date: "Apr 4, 2026", author: "Staff", readTime: "6 min" },
      { id: 2202, title: "U.S. Utility-Scale Solar Pipeline Exceeds 300 GW as IRA Credits Flow", excerpt: "The Inflation Reduction Act's tax credits continue to drive a massive buildout of solar farms across the Sun Belt states.", date: "Apr 3, 2026", author: "Staff", readTime: "5 min" },
      { id: 2203, title: "Perovskite-Silicon Tandem Cells Hit 33.9% Efficiency Record", excerpt: "Oxford PV's commercial-ready tandem cells promise to push rooftop solar economics further into mainstream territory.", date: "Apr 2, 2026", author: "Staff", readTime: "5 min" },
      { id: 2204, title: "India's Solar Tariffs Drop to Record Low $0.029/kWh in Rajasthan Auction", excerpt: "The world's cheapest solar electricity bid underscores India's aggressive renewable deployment targets.", date: "Apr 1, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "2025 Installed", value: "420 GW", sub: "global" },
      { label: "Module Price", value: "$0.09", sub: "/watt" },
      { label: "LCOE", value: "$24", sub: "/MWh avg" },
    ]
  },
  "wind": {
    articles: [
      { id: 2301, title: "Offshore Wind Capacity Surpasses 80 GW Globally as Costs Stabilize", excerpt: "After a period of cost inflation driven by supply chain bottlenecks, offshore wind developers report stabilizing turbine and installation costs.", date: "Apr 4, 2026", author: "Staff", readTime: "6 min" },
      { id: 2302, title: "Vineyard Wind Achieves Full 800 MW Output Off Massachusetts Coast", excerpt: "America's first utility-scale offshore wind farm is now operating at rated capacity, powering 400,000 homes.", date: "Apr 3, 2026", author: "Staff", readTime: "5 min" },
      { id: 2303, title: "Vestas Unveils 17 MW Offshore Turbine, World's Most Powerful", excerpt: "The V236-17.0 MW platform can generate enough electricity for 20,000 households from a single installation.", date: "Apr 2, 2026", author: "Staff", readTime: "4 min" },
      { id: 2304, title: "Texas Wind Generation Sets New Record at 35 GW During March Storm", excerpt: "ERCOT's wind fleet produced more power than natural gas for a 48-hour period during sustained high wind conditions.", date: "Apr 1, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "Offshore Global", value: "80 GW", sub: "installed" },
      { label: "U.S. Onshore", value: "155 GW", sub: "installed" },
      { label: "Largest Turbine", value: "17 MW", sub: "Vestas" },
    ]
  },
  "renewable-energy": {
    articles: [
      { id: 2401, title: "Renewables Provided 35% of Global Electricity in 2025, IEA Confirms", excerpt: "Wind, solar, hydro, and biomass generation surpassed coal for the first time on an annual basis worldwide.", date: "Apr 4, 2026", author: "Staff", readTime: "7 min" },
      { id: 2402, title: "Grid-Scale Battery Storage Hits 100 GW Global Milestone", excerpt: "Lithium-ion dominates the market but sodium-ion and iron-air chemistries are gaining ground for long-duration applications.", date: "Apr 3, 2026", author: "Staff", readTime: "5 min" },
      { id: 2403, title: "Green Hydrogen Electrolyzer Orders Surge 300% in 2025", excerpt: "European and Middle Eastern projects drive demand for gigawatt-scale electrolysis systems from manufacturers like Plug Power and Nel.", date: "Apr 2, 2026", author: "Staff", readTime: "5 min" },
      { id: 2404, title: "U.S. Clean Energy Jobs Surpass 4 Million for First Time", excerpt: "Solar installation, EV manufacturing, and battery production drive employment growth outpacing fossil fuel sector hiring.", date: "Apr 1, 2026", author: "Staff", readTime: "4 min" },
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
  { state: "Alabama", region: "South", abbr: "AL", regular: 3.837, mid: 4.280, premium: 4.697, diesel: 5.421 },
  { state: "Alaska", region: "West Coast", abbr: "AK", regular: 4.642, mid: 4.871, premium: 5.083, diesel: 5.938 },
  { state: "Arizona", region: "Mountain", abbr: "AZ", regular: 4.660, mid: 5.048, premium: 5.364, diesel: 6.076 },
  { state: "Arkansas", region: "South", abbr: "AR", regular: 3.647, mid: 4.087, premium: 4.465, diesel: 5.168 },
  { state: "California", region: "West Coast", abbr: "CA", regular: 5.878, mid: 6.119, premium: 6.299, diesel: 7.652 },
  { state: "Colorado", region: "Mountain", abbr: "CO", regular: 3.958, mid: 4.370, premium: 4.691, diesel: 5.194 },
  { state: "Connecticut", region: "Northeast", abbr: "CT", regular: 4.080, mid: 4.622, premium: 5.009, diesel: 5.916 },
  { state: "Delaware", region: "Northeast", abbr: "DE", regular: 3.972, mid: 4.588, premium: 4.893, diesel: 5.823 },
  { state: "Florida", region: "South", abbr: "FL", regular: 4.146, mid: 4.604, premium: 4.938, diesel: 5.633 },
  { state: "Georgia", region: "South", abbr: "GA", regular: 3.682, mid: 4.144, premium: 4.568, diesel: 5.260 },
  { state: "Hawaii", region: "West Coast", abbr: "HI", regular: 5.651, mid: 5.881, premium: 6.134, diesel: 7.117 },
  { state: "Idaho", region: "Mountain", abbr: "ID", regular: 4.341, mid: 4.635, premium: 4.910, diesel: 5.528 },
  { state: "Illinois", region: "Midwest", abbr: "IL", regular: 4.364, mid: 4.948, premium: 5.418, diesel: 5.438 },
  { state: "Indiana", region: "Midwest", abbr: "IN", regular: 3.884, mid: 4.433, premium: 4.929, diesel: 5.436 },
  { state: "Iowa", region: "Midwest", abbr: "IA", regular: 3.646, mid: 3.868, premium: 4.480, diesel: 5.070 },
  { state: "Kansas", region: "Midwest", abbr: "KS", regular: 3.507, mid: 3.831, premium: 4.167, diesel: 4.770 },
  { state: "Kentucky", region: "South", abbr: "KY", regular: 3.983, mid: 4.546, premium: 4.969, diesel: 5.367 },
  { state: "Louisiana", region: "South", abbr: "LA", regular: 3.749, mid: 4.192, premium: 4.576, diesel: 5.256 },
  { state: "Maine", region: "Northeast", abbr: "ME", regular: 4.024, mid: 4.572, premium: 5.047, diesel: 5.883 },
  { state: "Maryland", region: "Northeast", abbr: "MD", regular: 4.102, mid: 4.712, premium: 5.042, diesel: 5.860 },
  { state: "Massachusetts", region: "Northeast", abbr: "MA", regular: 3.965, mid: 4.548, premium: 4.944, diesel: 5.875 },
  { state: "Michigan", region: "Midwest", abbr: "MI", regular: 3.919, mid: 4.519, premium: 5.084, diesel: 5.275 },
  { state: "Minnesota", region: "Midwest", abbr: "MN", regular: 3.706, mid: 4.139, premium: 4.626, diesel: 5.095 },
  { state: "Mississippi", region: "South", abbr: "MS", regular: 3.744, mid: 4.172, premium: 4.577, diesel: 5.254 },
  { state: "Missouri", region: "Midwest", abbr: "MO", regular: 3.673, mid: 4.086, premium: 4.403, diesel: 4.911 },
  { state: "Montana", region: "Mountain", abbr: "MT", regular: 3.904, mid: 4.224, premium: 4.553, diesel: 5.026 },
  { state: "Nebraska", region: "Midwest", abbr: "NE", regular: 3.628, mid: 3.798, premium: 4.255, diesel: 4.906 },
  { state: "Nevada", region: "Mountain", abbr: "NV", regular: 4.963, mid: 5.281, premium: 5.563, diesel: 6.317 },
  { state: "New Hampshire", region: "Northeast", abbr: "NH", regular: 3.957, mid: 4.510, premium: 4.971, diesel: 5.819 },
  { state: "New Jersey", region: "Northeast", abbr: "NJ", regular: 4.003, mid: 4.546, premium: 4.820, diesel: 5.851 },
  { state: "New Mexico", region: "Mountain", abbr: "NM", regular: 3.958, mid: 4.383, premium: 4.691, diesel: 5.465 },
  { state: "New York", region: "Northeast", abbr: "NY", regular: 4.125, mid: 4.624, premium: 5.006, diesel: 5.950 },
  { state: "North Carolina", region: "South", abbr: "NC", regular: 3.861, mid: 4.304, premium: 4.709, diesel: 5.724 },
  { state: "North Dakota", region: "Midwest", abbr: "ND", regular: 3.616, mid: 3.968, premium: 4.372, diesel: 4.906 },
  { state: "Ohio", region: "Midwest", abbr: "OH", regular: 3.800, mid: 4.335, premium: 4.848, diesel: 5.395 },
  { state: "Oklahoma", region: "South", abbr: "OK", regular: 3.444, mid: 3.852, premium: 4.149, diesel: 4.769 },
  { state: "Oregon", region: "West Coast", abbr: "OR", regular: 4.995, mid: 5.234, premium: 5.508, diesel: 6.329 },
  { state: "Pennsylvania", region: "Northeast", abbr: "PA", regular: 4.134, mid: 4.571, premium: 4.949, diesel: 6.069 },
  { state: "Rhode Island", region: "Northeast", abbr: "RI", regular: 3.973, mid: 4.634, premium: 5.072, diesel: 5.802 },
  { state: "South Carolina", region: "South", abbr: "SC", regular: 3.790, mid: 4.243, premium: 4.632, diesel: 5.611 },
  { state: "South Dakota", region: "Midwest", abbr: "SD", regular: 3.684, mid: 3.848, premium: 4.347, diesel: 4.862 },
  { state: "Tennessee", region: "South", abbr: "TN", regular: 3.861, mid: 4.323, premium: 4.714, diesel: 5.442 },
  { state: "Texas", region: "South", abbr: "TX", regular: 3.768, mid: 4.250, premium: 4.620, diesel: 5.286 },
  { state: "Utah", region: "Mountain", abbr: "UT", regular: 4.211, mid: 4.494, premium: 4.739, diesel: 5.380 },
  { state: "Vermont", region: "Northeast", abbr: "VT", regular: 4.089, mid: 4.596, premium: 5.055, diesel: 5.878 },
  { state: "Virginia", region: "South", abbr: "VA", regular: 3.973, mid: 4.447, premium: 4.833, diesel: 5.743 },
  { state: "Washington", region: "West Coast", abbr: "WA", regular: 5.391, mid: 5.666, premium: 5.903, diesel: 6.952 },
  { state: "West Virginia", region: "South", abbr: "WV", regular: 3.932, mid: 4.350, premium: 4.804, diesel: 5.545 },
  { state: "Wisconsin", region: "Midwest", abbr: "WI", regular: 3.777, mid: 4.287, premium: 4.877, diesel: 4.981 },
  { state: "Wyoming", region: "Mountain", abbr: "WY", regular: 3.892, mid: 4.188, premium: 4.488, diesel: 5.058 },
  { state: "Washington D.C.", region: "Northeast", abbr: "DC", regular: 4.291, mid: 4.871, premium: 5.225, diesel: 5.833 },
];

const US_GAS_NATIONAL = { regular: 4.108, mid: 4.560, premium: 4.930, diesel: 5.548, source: "AAA Daily Fuel Gauge Report", updated: "As of April 15, 2026" };
