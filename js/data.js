/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Data Layer
   All mock data in one place for easy future API replacement
   ═══════════════════════════════════════════════════════════════════ */

const COMMODITIES = [
  { name: "WTI Crude", price: null, change: null, pct: null, unit: "$/bbl", spark: [], loading: true },
  { name: "Brent Crude", price: null, change: null, pct: null, unit: "$/bbl", spark: [], loading: true },
  { name: "Natural Gas", price: null, change: null, pct: null, unit: "$/MMBtu", spark: [], loading: true },
  { name: "Gasoline RBOB", price: null, change: null, pct: null, unit: "$/gal", spark: [], loading: true },
  { name: "Heating Oil", price: null, change: null, pct: null, unit: "$/gal", spark: [], loading: true },
  { name: "Murban Crude", price: null, change: null, pct: null, unit: "$/bbl", spark: [], loading: true },
  { name: "Diesel ULSD", price: null, change: null, pct: null, unit: "$/gal", spark: [], loading: true },
  { name: "Jet Fuel", price: null, change: null, pct: null, unit: "$/gal", spark: [], loading: true },
  { name: "Coal", price: null, change: null, pct: null, unit: "$/ton", spark: [], loading: true },
];

const FULL_PRICES = {
  "All Prices": [
    ...COMMODITIES,
    { name: "Dubai Fateh", price: 73.56, change: 0.92, pct: 1.27, unit: "$/bbl", spark: [71,72,72.5,73,73.2,73.4,73.56] },
    { name: "Louisiana Light", price: 72.85, change: 1.10, pct: 1.53, unit: "$/bbl", spark: [70,71,71.5,72,72.3,72.6,72.85] },
  ],
  "OPEC Blends": [
    { name: "OPEC Basket", price: 74.12, change: 0.65, pct: 0.88, unit: "$/bbl", spark: [72,73,73.5,73.8,74,74.1,74.12] },
    { name: "Arab Light", price: 75.20, change: 0.78, pct: 1.05, unit: "$/bbl", spark: [73,74,74.5,74.8,75,75.1,75.2] },
    { name: "Bonny Light", price: 76.45, change: 1.02, pct: 1.35, unit: "$/bbl", spark: [74,75,75.5,75.8,76,76.2,76.45] },
    { name: "Iran Heavy", price: 70.88, change: 0.44, pct: 0.62, unit: "$/bbl", spark: [69,70,70.2,70.5,70.6,70.7,70.88] },
    { name: "Kuwait Export", price: 73.65, change: 0.55, pct: 0.75, unit: "$/bbl", spark: [72,72.5,73,73.2,73.4,73.5,73.65] },
  ],
  "U.S. Blends": [
    { name: "WTI Crude", price: 71.48, change: 1.23, pct: 1.75, unit: "$/bbl", spark: [68,69,70,69.5,70.2,71,71.48] },
    { name: "Louisiana Light", price: 72.85, change: 1.10, pct: 1.53, unit: "$/bbl", spark: [70,71,71.5,72,72.3,72.6,72.85] },
    { name: "WTI Midland", price: 71.92, change: 1.18, pct: 1.67, unit: "$/bbl", spark: [69,70,70.5,71,71.3,71.6,71.92] },
    { name: "Mars Blend", price: 69.50, change: 0.95, pct: 1.39, unit: "$/bbl", spark: [67,68,68.5,69,69.2,69.3,69.5] },
    { name: "Eagle Ford", price: 70.15, change: 1.05, pct: 1.52, unit: "$/bbl", spark: [68,69,69.5,69.8,70,70.1,70.15] },
  ],
  "Canadian Blends": [
    { name: "Western Canadian Select", price: 57.20, change: 0.85, pct: 1.51, unit: "$/bbl", spark: [55,56,56.5,56.8,57,57.1,57.2] },
    { name: "Syncrude Sweet", price: 71.10, change: 1.15, pct: 1.64, unit: "$/bbl", spark: [69,70,70.5,70.8,71,71.05,71.1] },
    { name: "Cold Lake Blend", price: 56.80, change: 0.72, pct: 1.28, unit: "$/bbl", spark: [55,55.5,56,56.3,56.5,56.7,56.8] },
    { name: "Peace Sour", price: 62.45, change: 0.90, pct: 1.46, unit: "$/bbl", spark: [60,61,61.5,62,62.2,62.3,62.45] },
  ],
  "Refined Products": [
    { name: "Gasoline RBOB", price: 2.18, change: 0.04, pct: 1.87, unit: "$/gal", spark: [2.1,2.12,2.14,2.15,2.16,2.17,2.18] },
    { name: "Heating Oil", price: 2.34, change: -0.02, pct: -0.85, unit: "$/gal", spark: [2.38,2.37,2.36,2.35,2.35,2.34,2.34] },
    { name: "Diesel", price: 2.41, change: 0.03, pct: 1.26, unit: "$/gal", spark: [2.35,2.36,2.38,2.39,2.4,2.405,2.41] },
    { name: "Jet Fuel", price: 2.52, change: 0.05, pct: 2.02, unit: "$/gal", spark: [2.44,2.46,2.48,2.49,2.5,2.51,2.52] },
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
  { title: "U.S.-Iran Ceasefire Takes Effect After Pakistan-Brokered Deal Halts 40 Days of Conflict", cat: "Geopolitics", slug: "geopolitics", time: "Just now" },
  { title: "Crude Oil Crashes 15% as Strait of Hormuz Set to Reopen Under Ceasefire Terms", cat: "Oil Prices", slug: "oil-prices", time: "2h ago" },
  { title: "Gulf States Report Intercepting Iranian Drones and Missiles Hours After Truce Announced", cat: "Geopolitics", slug: "geopolitics", time: "4h ago" },
  { title: "Israel Continues Lebanon Strikes Despite Ceasefire — Netanyahu Says Hezbollah Not Included", cat: "Geopolitics", slug: "geopolitics", time: "5h ago" },
  { title: "OPEC+ Emergency Session Expected as Oil Prices Face Largest One-Day Drop Since 2020", cat: "OPEC", slug: "energy", time: "6h ago" },
  { title: "U.S. Gas Prices Expected to Drop Sharply if Ceasefire Holds and Hormuz Reopens", cat: "Gas Prices", slug: "gas-prices", time: "7h ago" },
  { title: "Trump Says Iran Nuclear Enrichment Must End — Talks Set for Friday in Islamabad", cat: "Geopolitics", slug: "geopolitics", time: "8h ago" },
  { title: "Kuwait Reports Significant Damage to Oil Facilities from Iranian Drone Attacks", cat: "Geopolitics", slug: "geopolitics", time: "10h ago" },
];

const MARKET_DRIVERS = [
  { cat: "CEASEFIRE", icon: "shield", title: "Iran Ceasefire Rocks Markets", desc: "Two-week truce between U.S. and Iran sends crude crashing 15% as Strait of Hormuz reopening lifts supply outlook." },
  { cat: "STRAIT OF HORMUZ", icon: "anchor", title: "Hormuz Reopening Imminent", desc: "Iran agrees to resume shipping through the strait — 21M bpd of oil transit set to normalize under ceasefire terms." },
  { cat: "OPEC", icon: "users", title: "OPEC+ Emergency Response", desc: "Alliance expected to convene emergency session as oil prices face worst single-day crash in six years." },
  { cat: "GULF STATES", icon: "alert-triangle", title: "Gulf Facilities Damaged", desc: "Kuwait, UAE, and Saudi Arabia report drone and missile interceptions. Abu Dhabi gas complex hit. Ceasefire violations alleged." },
  { cat: "GASOLINE", icon: "fuel", title: "Pump Price Relief Ahead", desc: "Analysts expect U.S. gas prices to drop $0.30-0.60/gallon within weeks if ceasefire holds and supply normalizes." },
  { cat: "DIPLOMACY", icon: "globe", title: "Islamabad Talks Friday", desc: "U.S. and Iran delegations set to meet in Pakistan on April 10 to negotiate permanent peace framework." },
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
  us_total: 584,
  us_total_change: -5,
  us_oil: 479,
  us_oil_change: -3,
  us_gas: 100,
  us_gas_change: -2,
  us_misc: 5,
  canada_total: 118,
  canada_change: 4,
  international: 958,
  last_updated: "March 28, 2026",
  permian: 302,
  eagle_ford: 48,
  bakken: 31,
  dj_niobrara: 14,
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
  { title: "Futures & Indexes", flag: "", subtitle: "Primary benchmarks — LIVE via API where marked, others 1-24hr delay", rows: [
    { name: "WTI Crude", price: 98.72, change: 0.85, pct: 0.87, apiCode: "WTI_USD" },
    { name: "Brent Crude", price: 96.51, change: 0.59, pct: 0.62, apiCode: "BRENT_CRUDE_USD" },
    { name: "Murban Crude", price: 99.62, change: 1.98, pct: 2.03 },
    { name: "Natural Gas", price: 2.672, change: 0.002, pct: 0.07, apiCode: "NATURAL_GAS_USD" },
    { name: "Gasoline RBOB", price: 3.018, change: 0.018, pct: 0.58, apiCode: "GASOLINE_USD" },
    { name: "Heating Oil", price: 3.975, change: 0.038, pct: 0.97, apiCode: "HEATING_OIL_USD" },
    { name: "Diesel ULSD", price: 3.91, change: 0.03, pct: 0.77, apiCode: "DIESEL_USD" },
    { name: "Jet Fuel", price: 4.23, change: 0.05, pct: 1.20, apiCode: "JET_FUEL_USD" },
    { name: "Coal (Newcastle)", price: 107.70, change: -2.10, pct: -1.91, apiCode: "COAL_USD" },
    { name: "WTI Midland", price: 102.55, change: 3.54, pct: 3.58 },
    { name: "Mars", price: 119.83, change: 4.90, pct: 4.26 },
    { name: "OPEC Basket", price: 107.00, change: -17.12, pct: -13.79 },
    { name: "DME Oman", price: 98.37, change: -20.25, pct: -17.07 },
    { name: "Mexican Basket", price: 106.89, change: -0.13, pct: -0.12 },
    { name: "Indian Basket", price: 115.52, change: -20.11, pct: -14.83 },
    { name: "Urals", price: 120.16, change: -4.69, pct: -3.76 },
    { name: "Western Canadian Select", price: 82.06, change: -18.54, pct: -18.43 },
    { name: "AECO C Natural Gas", price: 1.030, change: 0.040, pct: 4.04 },
    { name: "Dubai", price: 104.15, change: -14.90, pct: -12.52 },
    { name: "Brent Weighted Average", price: 93.91, change: -15.71, pct: -14.33 },
    { name: "Louisiana Light", price: 122.58, change: 0.57, pct: 0.47 },
    { name: "Domestic Swt. @ Cushing", price: 90.89, change: -18.54, pct: -16.94 },
    { name: "Giddings", price: 84.64, change: -18.54, pct: -17.97 },
    { name: "ANS West Coast", price: 118.06, change: -2.22, pct: -1.85 },
    { name: "Gulf Coast HSFO", price: 80.86, change: -7.75, pct: -8.75 },
    { name: "Ethanol", price: 1.925, change: -0.025, pct: -1.28 },
    { name: "Dutch TTF Natural Gas", price: 15.56, change: -2.54, pct: -14.02 },
    { name: "LNG Japan/Korea Marker", price: 19.49, change: -0.38, pct: -1.89 },
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
      { id: 1801, title: "Red Sea Attacks Force 60% of Tanker Traffic to Reroute Around Africa", excerpt: "Houthi missile and drone strikes continue to disrupt commercial shipping through the Bab el-Mandeb strait, adding $1-2/barrel to delivered crude costs.", date: "Apr 4, 2026", author: "Staff", readTime: "7 min" },
      { id: 1802, title: "U.S. Tightens Sanctions Enforcement on Russian Oil Price Cap", excerpt: "The Treasury Department blacklists 14 additional tankers suspected of transporting Russian crude above the $60/barrel ceiling.", date: "Apr 3, 2026", author: "Staff", readTime: "6 min" },
      { id: 1803, title: "Venezuela Sanctions Relief Under Review as Election Promises Stall", excerpt: "Washington weighs re-imposing oil sector restrictions after Caracas fails to meet democratic reform benchmarks.", date: "Apr 2, 2026", author: "Staff", readTime: "5 min" },
      { id: 1804, title: "Saudi-Iran Détente Reduces Persian Gulf Risk Premium", excerpt: "Diplomatic normalization between Riyadh and Tehran continues to ease tensions around the Strait of Hormuz chokepoint.", date: "Apr 1, 2026", author: "Staff", readTime: "5 min" },
      { id: 1805, title: "Nigeria Pipeline Security Improves 40% Under New Government Program", excerpt: "Reduced sabotage and theft in the Niger Delta enable Bonny Light production to recover toward 2019 levels.", date: "Mar 31, 2026", author: "Staff", readTime: "4 min" },
    ],
    stats: [
      { label: "Hormuz Transit", value: "21M", sub: "bpd" },
      { label: "Red Sea Impact", value: "+$1.50", sub: "/bbl premium" },
      { label: "Russian Exports", value: "4.8M", sub: "bpd to Asia" },
    ]
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
  { name: "Pioneer Natural Res.", ticker: "PXD", revenue: "$5.8B", profit: "$1.5B", production: "740K boe/d", dividend: "7.3%", sector: "E&P", hq: "Dallas, TX" },
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
  "oil-prices": [
    { q: "What determines the price of oil?", a: "Oil prices are driven by supply and demand fundamentals, OPEC+ production decisions, geopolitical risk premiums, inventory levels, currency movements, refinery demand, and speculative positioning in futures markets." },
    { q: "What is the difference between WTI and Brent?", a: "WTI (West Texas Intermediate) is the U.S. benchmark priced at Cushing, Oklahoma. Brent is the global benchmark based on North Sea production. Brent typically trades at a premium due to its role in pricing ~75% of global crude." },
    { q: "How often are oil prices updated?", a: "Futures markets trade nearly 24 hours on weekdays. Spot prices are assessed daily by pricing agencies like Platts and Argus. Our data updates from the EIA, which publishes daily settlement prices with a one-day lag." },
    { q: "What is the OPEC Basket price?", a: "The OPEC Reference Basket is a weighted average of oil prices from OPEC member countries. It typically trades at a $2-4 discount to Brent due to the heavier, more sour crude grades produced by many OPEC nations." },
    { q: "Why do oil prices fluctuate so much?", a: "Oil is priced in a global market where small supply-demand imbalances (even 1-2% of daily consumption) can move prices significantly. Geopolitical events, weather disruptions, OPEC decisions, inventory surprises, and macroeconomic data all create volatility." },
  ],
  "oil-futures": [
    { q: "What are oil futures?", a: "Oil futures are standardized contracts to buy or sell a specific quantity of crude oil at a predetermined price on a future date. WTI futures trade on NYMEX (1,000 barrels per contract) and Brent on ICE." },
    { q: "What is contango vs. backwardation?", a: "Contango means futures prices are higher than spot prices, suggesting markets expect prices to rise or that storage costs are being priced in. Backwardation means futures are below spot, signaling tight near-term supply or strong immediate demand." },
    { q: "Who trades oil futures?", a: "Producers (hedging future output), refiners (locking in input costs), airlines (fuel hedging), banks (market-making), hedge funds (speculation), and commodity trading firms. Physical participants and financial speculators interact in the same market." },
    { q: "What is the front-month contract?", a: "The front-month (or prompt-month) contract is the nearest expiring futures contract. It receives the most trading volume and is the most commonly quoted price. As expiration approaches, traders roll positions to the next month." },
    { q: "How do futures affect gas prices?", a: "Retail gasoline prices follow crude oil futures with a lag of 1-2 weeks. When front-month crude futures rise, wholesale gasoline costs increase, and retailers adjust pump prices accordingly. The crack spread (refining margin) also plays a role." },
  ],
  "crude-oil": [
    { q: "What are the main types of crude oil?", a: "Crude is classified by density (API gravity) and sulfur content. Light sweet crude (high API, low sulfur) like WTI commands premium pricing. Heavy sour crude (low API, high sulfur) like Maya or Arab Heavy trades at a discount due to higher refining costs." },
    { q: "Which countries produce the most crude oil?", a: "The U.S. leads at ~13M bpd, followed by Saudi Arabia (~10M bpd), Russia (~10M bpd), Canada (~5M bpd), Iraq (~4.5M bpd), China (~4M bpd), UAE (~3.5M bpd), and Brazil (~3.5M bpd). Together, the top 10 producers account for ~70% of global output." },
    { q: "What is the strategic petroleum reserve?", a: "The U.S. SPR is a government-owned emergency stockpile of crude oil stored in underground salt caverns along the Gulf Coast. Authorized capacity is 714M barrels. It can be released by presidential order during supply disruptions." },
    { q: "What is the crack spread?", a: "The crack spread measures the difference between crude oil input cost and refined product output value. A 3-2-1 crack spread uses 3 barrels of crude to produce 2 barrels of gasoline and 1 barrel of distillate. It indicates refining profitability." },
  ],
  "natural-gas": [
    { q: "What is Henry Hub?", a: "Henry Hub is the pricing point for natural gas futures on NYMEX, located in Erath, Louisiana. It serves as the North American benchmark due to its central location and connectivity to 13 major interstate and intrastate pipelines." },
    { q: "Why do natural gas prices vary so much by region?", a: "Unlike oil, natural gas is expensive to transport. Prices in Europe (TTF), Asia (JKM), and the U.S. (Henry Hub) can diverge by 3-5x due to pipeline constraints, LNG shipping costs, seasonal demand, and local supply dynamics." },
    { q: "What drives natural gas demand?", a: "Power generation (~40%), industrial use (~30%), residential/commercial heating (~20%), and LNG exports (~10%). Weather is the biggest short-term price mover — cold winters and hot summers both spike demand." },
    { q: "What is LNG?", a: "Liquefied Natural Gas is natural gas cooled to -162°C (-260°F), reducing its volume by ~600x for ship transport. Major exporters include the U.S., Qatar, Australia, and Russia. LNG enables gas trade between continents without pipeline infrastructure." },
    { q: "What is the storage report?", a: "The EIA publishes weekly natural gas storage data every Thursday at 10:30 AM ET. It reports the change in underground storage volumes. Deviations from consensus expectations frequently move gas prices by 3-5% within minutes of release." },
  ],
  "gas-prices": [
    { q: "What determines the price of gasoline?", a: "Crude oil costs account for ~55% of the pump price. Refining costs add ~15%, federal and state taxes add ~15-20%, and distribution/marketing add the remainder. State-specific regulations (like California fuel standards) can add $0.30-0.80/gallon." },
    { q: "Why do gas prices vary so much by state?", a: "State taxes range from $0.09/gal (Alaska) to $0.68/gal (California). Proximity to refineries, local supply/demand, environmental blend requirements, and transportation costs create additional regional differences." },
    { q: "What is the summer/winter blend difference?", a: "Summer-blend gasoline uses lower-volatility additives to reduce evaporative emissions in heat. It costs $0.10-0.15/gal more to produce. The switchover happens in spring, which is why gas prices typically rise March-May." },
    { q: "What is E85?", a: "E85 is a fuel blend of 51-83% ethanol and gasoline. It is only compatible with Flex Fuel vehicles. E85 typically costs $0.50-1.00 less per gallon than regular gasoline but delivers ~25% fewer miles per gallon due to ethanol's lower energy density." },
    { q: "How often do gas prices change?", a: "Wholesale gasoline prices change daily based on futures and spot markets. Retail stations adjust their prices 1-3 times per week on average, though high-traffic urban stations may reprice daily. Prices rise faster than they fall — a pattern economists call 'rockets and feathers.'" },
    { q: "Where does the EIA get its gas price data?", a: "The EIA surveys approximately 900 retail gasoline outlets weekly across all 50 states and DC through its Gasoline and Diesel Fuel Update. Prices are reported every Monday for the prior week. Our data sources from this EIA weekly survey." },
  ],
  "heating-oil": [
    { q: "What is heating oil?", a: "Heating oil (No. 2 fuel oil) is a refined petroleum product similar to diesel fuel used primarily for residential heating in the northeastern United States. About 5.3 million U.S. households use heating oil as their primary heating fuel." },
    { q: "Why is heating oil concentrated in the Northeast?", a: "Historical infrastructure patterns. The Northeast urbanized before natural gas pipeline networks were built, so homes were equipped with oil furnaces. Converting to gas requires significant plumbing work, and many older buildings lack gas connections." },
    { q: "What drives heating oil prices?", a: "Crude oil costs, refinery utilization, distillate inventory levels, winter weather severity, and competition with diesel fuel (which is chemically nearly identical). Cold snaps in the Northeast can spike prices 10-20% within days." },
    { q: "How is heating oil related to diesel?", a: "Heating oil and diesel fuel are both No. 2 distillates refined from the middle of the crude oil barrel. The main differences are sulfur content (ultra-low sulfur diesel vs. low sulfur heating oil) and tax treatment. Their prices move in near-lockstep." },
  ],
  "geopolitics": [
    { q: "How do geopolitics affect energy prices?", a: "Geopolitical events create risk premiums in commodity prices. Conflicts near production zones or transit chokepoints threaten supply, driving prices higher. Sanctions restrict market access. Trade wars affect demand. The Russia-Ukraine conflict alone redirected 4-5M bpd of crude flows." },
    { q: "What are the world's most critical energy chokepoints?", a: "Strait of Hormuz (21M bpd of oil transit), Strait of Malacca (16M bpd), Suez Canal (5.5M bpd), Bab el-Mandeb (4.8M bpd), and the Turkish Straits (2.4M bpd). A disruption at any of these would spike global oil prices within hours." },
    { q: "How do sanctions affect oil markets?", a: "Sanctions remove supply or redirect trade flows. Western sanctions on Russia created the price cap mechanism ($60/bbl) that requires shadow fleet tankers and opaque trading networks. Iranian sanctions keep ~1M bpd off markets. Venezuelan sanctions fluctuate with diplomatic cycles." },
    { q: "What is the petrodollar system?", a: "Most global oil trade is denominated in U.S. dollars. Oil-exporting nations receive dollars and reinvest them in U.S. assets, supporting dollar demand. Challenges to this system (e.g., China paying in yuan for Saudi crude) have geopolitical implications for currency markets." },
    { q: "How does the Russia-Ukraine war affect energy?", a: "The conflict disrupted Russian pipeline gas flows to Europe (down ~80%), redirected Russian crude exports toward Asia, prompted Europe to build LNG import capacity rapidly, accelerated renewable deployment, and created a two-tier global oil market with discounted Russian crude trading below Western benchmarks." },
  ],
  "company-news": [
    { q: "What are the supermajors?", a: "The six integrated oil supermajors are ExxonMobil, Shell, Chevron, BP, TotalEnergies, and ConocoPhillips. They operate across the full value chain — exploration, production, refining, chemicals, and retail. Combined, they produce over 15M boe/d." },
    { q: "What does E&P mean?", a: "Exploration and Production companies focus on finding and extracting oil and gas. Unlike integrated majors, pure E&P companies (like EOG, Pioneer, Devon) do not own refineries or retail networks. They are more directly exposed to commodity price swings." },
    { q: "What are national oil companies?", a: "NOCs are government-owned energy companies that control the majority of global oil reserves. Saudi Aramco, ADNOC, QatarEnergy, Kuwait Petroleum, ONGC, Petrobras, and Ecopetrol are major NOCs. They produce ~55% of global oil supply." },
    { q: "What drives energy company dividends?", a: "Cash flow from oil and gas production. When commodity prices are high, integrated majors generate strong free cash flow. Since 2022, most majors have committed to returning 30-50% of cash flow to shareholders through dividends and buybacks." },
  ],
  "alternative-energy": [
    { q: "What percentage of global electricity comes from renewables?", a: "As of 2025, renewables provided approximately 35% of global electricity, including hydro (15%), wind (10%), solar (7%), and biomass/geothermal (3%). Wind and solar are the fastest-growing segments." },
    { q: "Is renewable energy cheaper than fossil fuels?", a: "For new power generation in most markets, yes. Utility-scale solar LCOE is $20-40/MWh, onshore wind $25-50/MWh, vs. $45-75/MWh for new gas plants. However, intermittency requires backup or storage, adding system-level costs." },
    { q: "What is the energy transition?", a: "The global shift from fossil fuels to low-carbon energy. It encompasses electrification of transport, renewable power, green hydrogen, carbon capture, energy efficiency, and grid modernization. The IEA estimates $4 trillion in annual clean energy investment is needed by 2030." },
    { q: "What role does hydrogen play?", a: "Green hydrogen (made from renewable electricity) could decarbonize hard-to-electrify sectors like steel, shipping, and heavy industry. Current production is mostly 'gray' hydrogen from natural gas. Costs need to fall from ~$5/kg to $1-2/kg to be competitive." },
  ],
  "nuclear": [
    { q: "How many nuclear reactors operate globally?", a: "Approximately 440 reactors in 32 countries providing ~10% of global electricity. France leads with ~70% nuclear share. Major fleet expansions are underway in China (24 units under construction), India, and the UK." },
    { q: "What are Small Modular Reactors?", a: "SMRs are reactors under 300 MW designed for factory fabrication and modular deployment. NuScale received NRC certification for its 77 MWe design. SMRs promise lower upfront costs, enhanced passive safety, and flexible siting near demand centers." },
    { q: "What is driving the nuclear renaissance?", a: "Climate goals requiring carbon-free baseload power, energy security concerns, AI data center demand for reliable 24/7 electricity, government policy support (U.S. IRA tax credits, EU taxonomy inclusion), and the operational success of existing fleets." },
    { q: "What about nuclear waste?", a: "High-level waste (spent fuel) is currently stored at reactor sites in dry cask storage. No country has opened a permanent geological repository yet, though Finland's Onkalo facility is closest. Advanced reactors could use spent fuel as input, reducing waste volumes." },
  ],
  "solar": [
    { q: "How much solar capacity exists globally?", a: "Cumulative solar PV capacity exceeded 1,600 GW by end of 2025. China alone has ~750 GW. Annual additions reached 420 GW in 2025 — more than all other power sources combined." },
    { q: "How cheap is solar energy now?", a: "Utility-scale solar LCOE has fallen below $25/MWh in favorable markets. Module prices dropped below $0.10/watt in 2024. Record-low power purchase agreements below $0.02/kWh have been signed in the Middle East and Latin America." },
    { q: "What are the main solar technologies?", a: "Crystalline silicon (c-Si) dominates at ~95% market share. Thin-film (CdTe by First Solar, CIGS) holds niche applications. Perovskite technology is in development with potential for higher efficiency and lower cost but faces durability challenges." },
    { q: "What is the duck curve?", a: "A pattern in high-solar markets (like California) where midday solar generation creates oversupply, depressing wholesale prices, followed by a steep ramp in demand as the sun sets. This creates challenges for grid operators and increases the value of energy storage." },
  ],
  "wind": [
    { q: "What is the difference between onshore and offshore wind?", a: "Onshore is cheaper ($1,200-1,500/kW installed) but constrained by land and permitting. Offshore costs more ($2,500-4,000/kW) but has stronger, more consistent winds and can scale to GW-level projects without land use conflicts." },
    { q: "How big are modern wind turbines?", a: "The largest offshore turbines exceed 15 MW with rotor diameters over 230 meters — taller than the Statue of Liberty. A single rotation generates enough electricity to power a home for 2 days. Onshore turbines typically range 3-6 MW." },
    { q: "What is floating offshore wind?", a: "Floating platforms allow wind turbines in deep water (>60m) where fixed foundations are impractical. This opens vast ocean areas for wind development. Projects in Norway, France, and South Korea are proving the technology. Costs are falling but remain above fixed-bottom offshore." },
    { q: "Which countries lead in wind energy?", a: "China has the most installed capacity (~400 GW), followed by the U.S. (~150 GW), Germany (~70 GW), India (~45 GW), and the UK (~30 GW, mostly offshore). Denmark pioneered offshore wind and generates ~50% of its electricity from wind." },
  ],
  "renewable-energy": [
    { q: "What counts as renewable energy?", a: "Energy from naturally replenishing sources: solar, wind, hydroelectric, geothermal, biomass, wave/tidal. Nuclear is carbon-free but not technically renewable (uranium is finite). The EU and others increasingly classify nuclear as 'clean' alongside renewables." },
    { q: "Can renewables fully replace fossil fuels?", a: "Technically feasible for electricity with sufficient storage and grid upgrades. Harder for industrial heat, aviation, shipping, and petrochemicals. Most credible scenarios show renewables providing 60-80% of primary energy by 2050, with residual fossil fuels in hard-to-electrify sectors." },
    { q: "What is energy storage's role?", a: "Storage (primarily lithium-ion batteries) solves renewable intermittency by storing excess solar/wind generation for use when production is low. Battery costs have fallen 90% since 2010. Grid-scale storage deployments exceeded 45 GW in 2025." },
    { q: "How much is the world investing in clean energy?", a: "Global clean energy investment reached $1.8 trillion in 2025, outpacing fossil fuel investment for the first time. China accounts for ~$750B of this total. Solar attracted the most capital, followed by EVs, batteries, and wind." },
  ],
  "rig-count": [
    { q: "What is the rig count?", a: "The rig count measures drilling rigs actively exploring for or developing oil and gas. Published weekly by Baker Hughes (U.S.) and monthly (international), it serves as a leading indicator of future production capacity." },
    { q: "How often is it updated?", a: "Baker Hughes publishes the U.S. rig count every Friday at 1:00 PM ET. The international rig count is published monthly. Both are widely tracked by traders, analysts, and energy executives as forward-looking production signals." },
    { q: "What is the relationship between rig count and oil prices?", a: "Rig count follows prices with a 4-6 month lag. When prices rise, operators add rigs; when they fall, rigs are idled. However, improving well productivity (longer laterals, better completions) means each rig today produces more than a decade ago." },
    { q: "Why has the rig count been declining despite high prices?", a: "Capital discipline. After years of over-spending, U.S. shale operators now prioritize shareholder returns over volume growth. Companies achieve production growth with fewer rigs by drilling longer laterals and optimizing spacing." },
    { q: "Which basins have the most rigs?", a: "The Permian Basin (West Texas/New Mexico) accounts for 60%+ of U.S. oil rigs. Eagle Ford (South Texas), Bakken (North Dakota), and DJ-Niobrara (Colorado) make up most of the remainder. Offshore Gulf of Mexico rigs are counted separately." },
  ],
};

const GAS_PRICES_BY_STATE = [
  { state: "Alabama", region: "South", abbr: "AL", regular: 3.858, mid: 4.298, premium: 4.715, diesel: 5.439 },
  { state: "Alaska", region: "West Coast", abbr: "AK", regular: 4.623, mid: 4.852, premium: 5.082, diesel: 5.819 },
  { state: "Arizona", region: "Mountain", abbr: "AZ", regular: 4.749, mid: 5.126, premium: 5.444, diesel: 6.203 },
  { state: "Arkansas", region: "South", abbr: "AR", regular: 3.628, mid: 4.061, premium: 4.413, diesel: 5.139 },
  { state: "California", region: "West Coast", abbr: "CA", regular: 5.93, mid: 6.168, premium: 6.354, diesel: 7.728 },
  { state: "Colorado", region: "Mountain", abbr: "CO", regular: 3.809, mid: 4.203, premium: 4.527, diesel: 5.122 },
  { state: "Connecticut", region: "Northeast", abbr: "CT", regular: 4.096, mid: 4.605, premium: 5.006, diesel: 5.937 },
  { state: "Delaware", region: "Northeast", abbr: "DE", regular: 3.983, mid: 4.529, premium: 4.83, diesel: 5.879 },
  { state: "Florida", region: "South", abbr: "FL", regular: 4.181, mid: 4.626, premium: 4.959, diesel: 5.802 },
  { state: "Georgia", region: "South", abbr: "GA", regular: 3.733, mid: 4.2, premium: 4.61, diesel: 5.308 },
  { state: "Hawaii", region: "West Coast", abbr: "HI", regular: 5.604, mid: 5.872, premium: 6.082, diesel: 6.985 },
  { state: "Idaho", region: "Mountain", abbr: "ID", regular: 4.3, mid: 4.585, premium: 4.862, diesel: 5.511 },
  { state: "Illinois", region: "Midwest", abbr: "IL", regular: 4.362, mid: 4.931, premium: 5.402, diesel: 5.291 },
  { state: "Indiana", region: "Midwest", abbr: "IN", regular: 4.053, mid: 4.577, premium: 5.069, diesel: 5.378 },
  { state: "Iowa", region: "Midwest", abbr: "IA", regular: 3.484, mid: 3.702, premium: 4.341, diesel: 5.098 },
  { state: "Kansas", region: "Midwest", abbr: "KS", regular: 3.39, mid: 3.709, premium: 4.029, diesel: 4.725 },
  { state: "Kentucky", region: "South", abbr: "KY", regular: 3.974, mid: 4.539, premium: 4.961, diesel: 5.255 },
  { state: "Louisiana", region: "South", abbr: "LA", regular: 3.796, mid: 4.224, premium: 4.609, diesel: 5.316 },
  { state: "Maine", region: "Northeast", abbr: "ME", regular: 4.031, mid: 4.589, premium: 5.069, diesel: 5.897 },
  { state: "Maryland", region: "Northeast", abbr: "MD", regular: 4.168, mid: 4.712, premium: 5.048, diesel: 5.953 },
  { state: "Massachusetts", region: "Northeast", abbr: "MA", regular: 3.956, mid: 4.51, premium: 4.909, diesel: 5.872 },
  { state: "Michigan", region: "Midwest", abbr: "MI", regular: 4.01, mid: 4.564, premium: 5.119, diesel: 5.21 },
  { state: "Minnesota", region: "Midwest", abbr: "MN", regular: 3.585, mid: 4.029, premium: 4.518, diesel: 5.096 },
  { state: "Mississippi", region: "South", abbr: "MS", regular: 3.764, mid: 4.191, premium: 4.581, diesel: 5.288 },
  { state: "Missouri", region: "Midwest", abbr: "MO", regular: 3.568, mid: 3.997, premium: 4.302, diesel: 4.858 },
  { state: "Montana", region: "Mountain", abbr: "MT", regular: 3.842, mid: 4.152, premium: 4.51, diesel: 4.963 },
  { state: "Nebraska", region: "Midwest", abbr: "NE", regular: 3.538, mid: 3.706, premium: 4.176, diesel: 4.909 },
  { state: "Nevada", region: "Mountain", abbr: "NV", regular: 5.009, mid: 5.317, premium: 5.612, diesel: 6.401 },
  { state: "New Hampshire", region: "Northeast", abbr: "NH", regular: 3.97, mid: 4.51, premium: 4.973, diesel: 5.827 },
  { state: "New Jersey", region: "Northeast", abbr: "NJ", regular: 4.091, mid: 4.613, premium: 4.876, diesel: 5.905 },
  { state: "New Mexico", region: "Mountain", abbr: "NM", regular: 4.025, mid: 4.459, premium: 4.778, diesel: 5.484 },
  { state: "New York", region: "Northeast", abbr: "NY", regular: 4.102, mid: 4.599, premium: 4.979, diesel: 5.942 },
  { state: "North Carolina", region: "South", abbr: "NC", regular: 3.928, mid: 4.366, premium: 4.761, diesel: 5.813 },
  { state: "North Dakota", region: "Midwest", abbr: "ND", regular: 3.484, mid: 3.848, premium: 4.296, diesel: 4.771 },
  { state: "Ohio", region: "Midwest", abbr: "OH", regular: 3.864, mid: 4.392, premium: 4.905, diesel: 5.318 },
  { state: "Oklahoma", region: "South", abbr: "OK", regular: 3.347, mid: 3.753, premium: 4.037, diesel: 4.636 },
  { state: "Oregon", region: "West Coast", abbr: "OR", regular: 5.002, mid: 5.231, premium: 5.508, diesel: 6.284 },
  { state: "Pennsylvania", region: "Northeast", abbr: "PA", regular: 4.185, mid: 4.618, premium: 4.995, diesel: 6.105 },
  { state: "Rhode Island", region: "Northeast", abbr: "RI", regular: 4.013, mid: 4.674, premium: 5.09, diesel: 5.851 },
  { state: "South Carolina", region: "South", abbr: "SC", regular: 3.827, mid: 4.259, premium: 4.658, diesel: 5.6 },
  { state: "South Dakota", region: "Midwest", abbr: "SD", regular: 3.586, mid: 3.746, premium: 4.294, diesel: 4.793 },
  { state: "Tennessee", region: "South", abbr: "TN", regular: 3.887, mid: 4.367, premium: 4.761, diesel: 5.459 },
  { state: "Texas", region: "South", abbr: "TX", regular: 3.844, mid: 4.324, premium: 4.697, diesel: 5.286 },
  { state: "Utah", region: "Mountain", abbr: "UT", regular: 4.239, mid: 4.52, premium: 4.775, diesel: 5.428 },
  { state: "Vermont", region: "Northeast", abbr: "VT", regular: 4.112, mid: 4.574, premium: 5.029, diesel: 5.918 },
  { state: "Virginia", region: "South", abbr: "VA", regular: 4.073, mid: 4.527, premium: 4.91, diesel: 5.805 },
  { state: "Washington", region: "West Coast", abbr: "WA", regular: 5.392, mid: 5.634, premium: 5.881, diesel: 6.854 },
  { state: "West Virginia", region: "South", abbr: "WV", regular: 3.99, mid: 4.425, premium: 4.857, diesel: 5.563 },
  { state: "Wisconsin", region: "Midwest", abbr: "WI", regular: 3.816, mid: 4.307, premium: 4.905, diesel: 4.969 },
  { state: "Wyoming", region: "Mountain", abbr: "WY", regular: 3.858, mid: 4.169, premium: 4.472, diesel: 5.04 },
  { state: "Washington D.C.", region: "Northeast", abbr: "DC", regular: 4.289, mid: 4.837, premium: 5.245, diesel: 5.84 },
];

const US_GAS_NATIONAL = { regular: 4.140, mid: 4.583, premium: 4.953, diesel: 5.583, source: "AAA Daily Fuel Gauge Report", updated: "As of April 7, 2026" };
