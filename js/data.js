/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Data Layer
   All mock data in one place for easy future API replacement
   ═══════════════════════════════════════════════════════════════════ */

const COMMODITIES = [
  { name: "WTI Crude", price: 71.48, change: 1.23, pct: 1.75, unit: "$/bbl", spark: [68,69,70,69.5,70.2,71,71.48] },
  { name: "Brent Crude", price: 75.92, change: 0.87, pct: 1.16, unit: "$/bbl", spark: [73,74,74.5,75,74.8,75.5,75.92] },
  { name: "Natural Gas", price: 3.42, change: -0.08, pct: -2.29, unit: "$/MMBtu", spark: [3.6,3.55,3.5,3.48,3.45,3.44,3.42] },
  { name: "Gasoline RBOB", price: 2.18, change: 0.04, pct: 1.87, unit: "$/gal", spark: [2.1,2.12,2.14,2.15,2.16,2.17,2.18] },
  { name: "Heating Oil", price: 2.34, change: -0.02, pct: -0.85, unit: "$/gal", spark: [2.38,2.37,2.36,2.35,2.35,2.34,2.34] },
];

const FULL_PRICES = {
  "All Prices": [
    ...COMMODITIES,
    { name: "OPEC Basket", price: 74.12, change: 0.65, pct: 0.88, unit: "$/bbl", spark: [72,73,73.5,73.8,74,74.1,74.12] },
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
  { id: 1, title: "OPEC+ Signals Extended Production Cuts Through Q3 2026 Amid Demand Uncertainty", time: "12 min ago", cat: "OPEC", slug: "opec" },
  { id: 2, title: "WTI Crude Surges Past $71 on Tighter U.S. Inventory Data", time: "34 min ago", cat: "Oil Prices", slug: "oil-prices" },
  { id: 3, title: "European Natural Gas Prices Rally as Cold Snap Forecast Returns", time: "1 hr ago", cat: "Natural Gas", slug: "natural-gas" },
  { id: 4, title: "ExxonMobil Announces $4.2B Expansion of Permian Basin Operations", time: "2 hr ago", cat: "Company News", slug: "company-news" },
  { id: 5, title: "U.S. Rig Count Falls for Third Consecutive Week, Baker Hughes Reports", time: "3 hr ago", cat: "Rig Count", slug: "rig-count" },
  { id: 6, title: "Saudi Arabia Holds Firm on April OSP Despite Market Pressure", time: "4 hr ago", cat: "Geopolitics", slug: "geopolitics" },
  { id: 7, title: "Renewable Energy Investment Hits Record $1.8 Trillion Globally in 2025", time: "5 hr ago", cat: "Alternative Energy", slug: "alternative-energy" },
];

const MARKET_DRIVERS = [
  { icon: "globe", title: "Middle East Tensions Persist", desc: "Continued Houthi attacks in the Red Sea disrupt shipping routes, adding risk premiums to crude benchmarks.", cat: "Geopolitics" },
  { icon: "bar-chart", title: "U.S. Inventories Draw Down", desc: "EIA reports a 4.2M barrel draw in commercial crude stocks, well above the 1.8M consensus estimate.", cat: "Supply" },
  { icon: "users", title: "OPEC+ Holds Steady", desc: "The alliance reaffirms commitment to current production quotas, maintaining 2.2M bpd of voluntary cuts.", cat: "OPEC" },
  { icon: "thermometer", title: "Cold Snap Lifts Gas Prices", desc: "Extended winter weather across Northern Europe drives heating demand and boosts TTF gas futures.", cat: "Weather" },
  { icon: "factory", title: "Refinery Margins Under Pressure", desc: "Asian refining margins decline as oversupply of diesel meets weakened Chinese industrial demand.", cat: "Refining" },
  { icon: "zap", title: "Renewable Surge Continues", desc: "Global solar and wind capacity additions outpace forecasts, reshaping long-term energy price models.", cat: "Renewables" },
];

const FEATURED_ARTICLES = [
  { id: 101, title: "The New Oil Order: How OPEC+ Strategy Is Reshaping Global Crude Markets in 2026", excerpt: "A deep analysis of how OPEC+ production management has evolved into a more sophisticated price-targeting mechanism, and what it means for traders and consumers alike.", cat: "Analysis", slug: "energy", author: "Sarah Mitchell", date: "Mar 31, 2026", readTime: "8 min", featured: true },
  { id: 102, title: "Permian Basin Output Hits Record 6.2M Barrels Per Day", excerpt: "U.S. shale production continues to defy expectations as operators optimize well spacing and completion techniques.", cat: "Crude Oil", slug: "crude-oil", author: "James Carter", date: "Mar 31, 2026", readTime: "5 min" },
  { id: 103, title: "Why European Gas Storage Levels Matter More Than Ever", excerpt: "With LNG supply contracts up for renewal and Russian pipeline flows diminished, European storage strategy becomes pivotal.", cat: "Natural Gas", slug: "natural-gas", author: "Elena Petrova", date: "Mar 30, 2026", readTime: "6 min" },
  { id: 104, title: "ExxonMobil vs. Chevron: Battle for Permian Supremacy", excerpt: "The two oil majors are taking divergent approaches to growth in America's most prolific basin.", cat: "Company News", slug: "company-news", author: "David Chen", date: "Mar 30, 2026", readTime: "7 min" },
  { id: 105, title: "Nuclear Renaissance: Small Modular Reactors Enter Commercial Phase", excerpt: "After decades of promise, SMR technology is finally moving from pilot programs to grid-scale deployment.", cat: "Nuclear", slug: "nuclear", author: "Anna Kowalski", date: "Mar 29, 2026", readTime: "9 min" },
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
  { id: 401, title: "Markets React to Unexpected Inventory Build in Cushing Hub", excerpt: "Cushing, Oklahoma storage levels rose by 1.8M barrels last week, pressuring nearby WTI spreads.", date: "Mar 31, 2026", author: "Sarah Mitchell", readTime: "5 min" },
  { id: 402, title: "Goldman Sachs Raises Brent Crude Forecast to $82 by Year-End", excerpt: "The bank cites stronger-than-expected demand from emerging markets and constrained OPEC+ supply.", date: "Mar 30, 2026", author: "James Carter", readTime: "4 min" },
  { id: 403, title: "Iraq Struggles to Meet OPEC+ Production Quota Compliance", excerpt: "Baghdad's oil output consistently exceeds its agreed ceiling, creating tension within the alliance.", date: "Mar 30, 2026", author: "Elena Petrova", readTime: "6 min" },
  { id: 404, title: "Global Oil Demand Growth Slows to 900K BPD in 2026, IEA Says", excerpt: "The International Energy Agency revises down its demand growth estimate amid economic headwinds.", date: "Mar 29, 2026", author: "David Chen", readTime: "5 min" },
  { id: 405, title: "New Deepwater Discovery Off Guyana Could Hold 1.5 Billion Barrels", excerpt: "ExxonMobil's latest exploration well confirms significant hydrocarbon reserves in the Stabroek Block.", date: "Mar 29, 2026", author: "Anna Kowalski", readTime: "7 min" },
  { id: 406, title: "Keystone Pipeline Restarts After Maintenance Shutdown", excerpt: "TC Energy confirms the pipeline is back to full capacity after a scheduled two-week maintenance window.", date: "Mar 28, 2026", author: "Sarah Mitchell", readTime: "3 min" },
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
  {
    title: "Futures & Indexes",
    flag: "",
    rows: [
      { name: "WTI Crude", price: 71.48, change: 1.23, pct: 1.75 },
      { name: "Brent Crude", price: 75.92, change: 0.87, pct: 1.16 },
      { name: "Murban Crude", price: 76.84, change: 1.21, pct: 1.60 },
      { name: "Natural Gas", price: 3.42, change: -0.08, pct: -2.29 },
      { name: "Gasoline", price: 2.18, change: 0.04, pct: 1.87 },
      { name: "Heating Oil", price: 2.34, change: -0.02, pct: -0.85 },
      { name: "WTI Midland", price: 71.92, change: 1.18, pct: 1.67 },
      { name: "Mars", price: 69.50, change: 0.95, pct: 1.39 },
      { name: "OPEC Basket", price: 74.12, change: 0.65, pct: 0.88 },
      { name: "DME Oman", price: 73.66, change: -0.20, pct: -0.27 },
      { name: "Mexican Basket", price: 65.56, change: -0.45, pct: -0.68 },
      { name: "Indian Basket", price: 74.84, change: 0.31, pct: 0.42 },
      { name: "Urals", price: 66.17, change: 0.44, pct: 0.67 },
      { name: "Dubai", price: 74.52, change: 0.38, pct: 0.51 },
      { name: "Louisiana Light", price: 72.85, change: 1.10, pct: 1.53 },
      { name: "Domestic Swt. @ Cushing", price: 71.60, change: 1.23, pct: 1.75 },
      { name: "ANS West Coast", price: 74.22, change: 0.56, pct: 0.76 },
      { name: "Ethanol", price: 1.68, change: 0.02, pct: 1.20 },
      { name: "Dutch TTF Natural Gas", price: 11.85, change: 0.32, pct: 2.77 },
      { name: "LNG Japan/Korea Marker", price: 12.40, change: -0.15, pct: -1.20 },
    ]
  },
  {
    title: "OPEC Members",
    subtitle: "Daily Pricing",
    flag: "",
    rows: [
      { name: "Arab Light", price: 75.20, change: 0.78, pct: 1.05 },
      { name: "Basrah Medium", price: 73.25, change: 0.55, pct: 0.76 },
      { name: "Bonny Light", price: 76.45, change: 1.02, pct: 1.35 },
      { name: "Es Sider", price: 75.14, change: 0.86, pct: 1.16 },
      { name: "Iran Heavy", price: 70.88, change: 0.44, pct: 0.62 },
      { name: "Kuwait Export", price: 73.65, change: 0.55, pct: 0.75 },
      { name: "Merey", price: 58.31, change: 0.90, pct: 1.57 },
      { name: "Murban", price: 76.84, change: 1.21, pct: 1.60 },
      { name: "Saharan Blend", price: 77.59, change: 0.96, pct: 1.25 },
    ]
  },
  {
    title: "Australia", flag: "🇦🇺",
    rows: [
      { name: "Cossack", price: 76.41, change: 0.37, pct: 0.49 },
      { name: "NWS Condensate", price: 73.51, change: 0.37, pct: 0.51 },
      { name: "Ichthys Condensate", price: 78.46, change: 0.37, pct: 0.47 },
    ]
  },
  {
    title: "Angola", flag: "🇦🇴",
    rows: [
      { name: "Cabinda", price: 77.16, change: 0.37, pct: 0.48 },
      { name: "Nemba", price: 75.41, change: 0.37, pct: 0.49 },
      { name: "Dalia", price: 75.81, change: 0.37, pct: 0.49 },
    ]
  },
  {
    title: "Nigeria", flag: "🇳🇬",
    rows: [
      { name: "Brass River", price: 76.66, change: 0.37, pct: 0.48 },
      { name: "Qua Iboe", price: 76.56, change: 0.37, pct: 0.49 },
    ]
  },
  {
    title: "UAE", flag: "🇦🇪",
    rows: [
      { name: "Das", price: 74.14, change: 0.41, pct: 0.56 },
      { name: "Umm Lulu", price: 74.64, change: 0.41, pct: 0.55 },
      { name: "Upper Zakum", price: 76.99, change: 0.41, pct: 0.54 },
    ]
  },
  {
    title: "Qatar", flag: "🇶🇦",
    rows: [
      { name: "Qatar Land", price: 73.89, change: 0.41, pct: 0.56 },
      { name: "Al Shaheen", price: 76.99, change: 0.41, pct: 0.54 },
      { name: "D.F. Condensate", price: 65.32, change: 0.41, pct: 0.63 },
      { name: "L.S. Condensate", price: 65.02, change: 0.41, pct: 0.63 },
    ]
  },
  {
    title: "Iraq", flag: "🇮🇶",
    rows: [
      { name: "Basrah Heavy", price: 70.15, change: 0.49, pct: 0.70 },
      { name: "Basrah Medium", price: 73.25, change: 0.49, pct: 0.67 },
    ]
  },
  {
    title: "Saudi Arabia", flag: "🇸🇦",
    rows: [
      { name: "Arab Extra Light", price: 75.62, change: 0.82, pct: 1.10 },
      { name: "Arab Light", price: 75.20, change: 0.78, pct: 1.05 },
      { name: "Arab Medium", price: 73.37, change: 0.82, pct: 1.13 },
      { name: "Arab Heavy", price: 72.02, change: 0.82, pct: 1.15 },
    ]
  },
  {
    title: "Ecuador", flag: "🇪🇨",
    rows: [
      { name: "Oriente Crude", price: 64.45, change: 0.48, pct: 0.75 },
      { name: "Napo Crude", price: 60.96, change: 0.48, pct: 0.79 },
    ]
  },
  {
    title: "Mexico", flag: "🇲🇽",
    rows: [
      { name: "Maya (Gulf Coast)", price: 62.98, change: -0.25, pct: -0.40 },
      { name: "Isthmus (Gulf Coast)", price: 70.59, change: -0.32, pct: -0.45 },
      { name: "Olmeca", price: 71.21, change: -0.35, pct: -0.49 },
      { name: "Maya (West Coast)", price: 62.78, change: -0.25, pct: -0.40 },
      { name: "Maya (Far East)", price: 71.69, change: -0.20, pct: -0.28 },
    ]
  },
  {
    title: "Iran", flag: "🇮🇷",
    rows: [
      { name: "Iran Light (NW Europe)", price: 69.41, change: -0.29, pct: -0.42 },
      { name: "Iran Heavy (NW Europe)", price: 67.51, change: -0.29, pct: -0.43 },
      { name: "Forozan Blend", price: 67.76, change: -0.29, pct: -0.43 },
      { name: "Soroosh", price: 64.61, change: -0.29, pct: -0.45 },
    ]
  },
  {
    title: "Russia", flag: "🇷🇺",
    rows: [
      { name: "Sokol", price: 68.74, change: 0.41, pct: 0.60 },
      { name: "Urals", price: 66.17, change: 0.44, pct: 0.67 },
    ]
  },
  {
    title: "Azerbaijan", flag: "🇦🇿",
    rows: [{ name: "Azeri Light", price: 78.88, change: 0.78, pct: 1.00 }]
  },
  {
    title: "Brazil", flag: "🇧🇷",
    rows: [{ name: "Lula", price: 74.33, change: 0.78, pct: 1.06 }]
  },
  {
    title: "Kazakhstan", flag: "🇰🇿",
    rows: [{ name: "CPC Blend", price: 74.88, change: 0.78, pct: 1.05 }]
  },
  {
    title: "Canadian Blends", flag: "🇨🇦",
    rows: [
      { name: "Western Canadian Select", price: 57.20, change: 0.85, pct: 1.51 },
      { name: "Central Alberta", price: 62.97, change: -0.26, pct: -0.41 },
      { name: "Light Sour Blend", price: 63.37, change: -0.26, pct: -0.41 },
      { name: "Peace Sour", price: 62.45, change: 0.90, pct: 1.46 },
      { name: "Syncrude Sweet Premium", price: 71.10, change: 1.15, pct: 1.64 },
      { name: "Sweet Crude", price: 65.37, change: -0.26, pct: -0.40 },
      { name: "Cold Lake Blend", price: 56.80, change: 0.72, pct: 1.28 },
      { name: "Albian Heavy Synthetic", price: 70.62, change: -0.26, pct: -0.37 },
      { name: "Access Western Blend", price: 70.22, change: -0.26, pct: -0.37 },
      { name: "AECO C Natural Gas", price: 1.06, change: 0.03, pct: 2.91 },
    ]
  },
  {
    title: "United States — Texas", flag: "🇺🇸",
    rows: [
      { name: "West Texas Sour", price: 68.00, change: 0.49, pct: 0.73 },
      { name: "West Texas Intermediate", price: 71.60, change: 1.23, pct: 1.75 },
      { name: "Eagle Ford", price: 71.60, change: 1.23, pct: 1.75 },
      { name: "North Texas Sweet", price: 69.25, change: -0.30, pct: -0.43 },
      { name: "South Texas Sour", price: 62.85, change: -0.26, pct: -0.41 },
      { name: "South Texas Light", price: 63.00, change: -0.30, pct: -0.47 },
      { name: "Upper Texas Gulf Coast", price: 63.35, change: -0.26, pct: -0.41 },
    ]
  },
  {
    title: "United States — Oklahoma", flag: "🇺🇸",
    rows: [
      { name: "Oklahoma Sweet", price: 69.25, change: -0.30, pct: -0.43 },
      { name: "Oklahoma Sour", price: 60.25, change: -0.30, pct: -0.50 },
      { name: "Oklahoma Intermediate", price: 69.00, change: -0.30, pct: -0.43 },
    ]
  },
  {
    title: "United States — Other States", flag: "🇺🇸",
    rows: [
      { name: "Wyoming General Sour", price: 65.18, change: -0.26, pct: -0.40 },
      { name: "Wyoming General Sweet", price: 65.70, change: -0.26, pct: -0.39 },
      { name: "Colorado South East", price: 59.10, change: -0.26, pct: -0.44 },
      { name: "Nebraska Sweet", price: 59.90, change: -0.26, pct: -0.43 },
      { name: "Michigan Sour", price: 61.25, change: -0.30, pct: -0.49 },
      { name: "Michigan Sweet", price: 66.00, change: -0.30, pct: -0.45 },
      { name: "Louisiana (South)", price: 67.75, change: -0.30, pct: -0.44 },
      { name: "Kansas Common", price: 58.95, change: -0.26, pct: -0.44 },
      { name: "Arkansas Sweet", price: 67.50, change: -0.50, pct: -0.74 },
      { name: "Arkansas Sour", price: 66.25, change: -0.50, pct: -0.75 },
    ]
  },
];

// ─── UNIQUE CONTENT PER CATEGORY PAGE ──────────────────────────────
const CATEGORY_CONTENT = {
  "oil-prices": {
    articles: [
      { id: 1001, title: "WTI Crude Climbs Past $71 as U.S. Inventories Post Sharp Drawdown", excerpt: "Commercial crude stocks at Cushing fell 4.2M barrels, well above the 1.8M consensus, signaling strong refinery demand ahead of driving season.", date: "Apr 4, 2026", author: "Sarah Mitchell", readTime: "5 min" },
      { id: 1002, title: "Brent-WTI Spread Widens to $4.44 on Atlantic Basin Tightness", excerpt: "North Sea supply disruptions and strong European refinery margins are pulling Brent higher relative to WTI.", date: "Apr 3, 2026", author: "James Carter", readTime: "4 min" },
      { id: 1003, title: "Goldman Sachs Raises Brent Forecast to $82 by Year-End", excerpt: "The bank cites stronger-than-expected emerging market demand growth and disciplined OPEC+ supply management.", date: "Apr 2, 2026", author: "Elena Petrova", readTime: "4 min" },
      { id: 1004, title: "OPEC Basket Price Holds Above $74 Amid Production Cut Extensions", excerpt: "The reference basket used by OPEC member nations remains elevated as voluntary cuts of 2.2M bpd persist through Q3.", date: "Apr 1, 2026", author: "David Chen", readTime: "5 min" },
      { id: 1005, title: "Dubai Crude Fetches Premium as Asian Refiners Compete for Sour Barrels", excerpt: "The Dubai benchmark has firmed on strong buying from Indian and Chinese refiners seeking Middle Eastern grades.", date: "Mar 31, 2026", author: "Anna Kowalski", readTime: "4 min" },
    ],
    stats: [
      { label: "WTI Crude", value: "$71.48", sub: "+1.75%" },
      { label: "Brent Crude", value: "$75.92", sub: "+1.16%" },
      { label: "OPEC Basket", value: "$74.12", sub: "+0.88%" },
    ]
  },
  "oil-futures": {
    articles: [
      { id: 1101, title: "WTI Futures Curve Flips to Backwardation Through December 2026", excerpt: "Front-month contracts now trade at a premium to deferred months, signaling near-term supply tightness.", date: "Apr 4, 2026", author: "James Carter", readTime: "6 min" },
      { id: 1102, title: "Brent Futures Open Interest Hits 3-Month High Ahead of OPEC Meeting", excerpt: "Speculative positioning in Brent crude futures has surged as traders anticipate policy signals from Vienna.", date: "Apr 3, 2026", author: "Sarah Mitchell", readTime: "5 min" },
      { id: 1103, title: "Options Market Pricing Elevated Volatility Through Summer 2026", excerpt: "Implied volatility on WTI calls has risen 18% as geopolitical risk and demand uncertainty drive hedging activity.", date: "Apr 2, 2026", author: "David Chen", readTime: "5 min" },
      { id: 1104, title: "Managed Money Net Longs in Crude Futures Rise for Fourth Straight Week", excerpt: "CFTC data shows hedge funds increasing bullish bets on oil as macro headwinds appear to be easing.", date: "Apr 1, 2026", author: "Elena Petrova", readTime: "4 min" },
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
      { id: 1202, title: "Permian Basin Rigs Hold Steady at 302 Despite Overall U.S. Decline", excerpt: "The nation's most prolific basin continues to attract investment even as secondary plays see rig reductions.", date: "Apr 3, 2026", author: "James Carter", readTime: "5 min" },
      { id: 1203, title: "Canadian Rig Count Rebounds to 118 as Spring Drilling Season Begins", excerpt: "Freeze-thaw cycle restrictions are easing across Alberta and Saskatchewan, allowing crews to mobilize.", date: "Apr 2, 2026", author: "Elena Petrova", readTime: "4 min" },
      { id: 1204, title: "International Rig Count Stable at 958 as Middle East Activity Rises", excerpt: "Saudi Arabia and UAE are adding rigs to maintain production capacity even as OPEC+ quotas limit output.", date: "Apr 1, 2026", author: "David Chen", readTime: "4 min" },
    ],
    stats: [
      { label: "U.S. Total", value: "584", sub: "-5 w/w" },
      { label: "U.S. Oil Rigs", value: "479", sub: "-3 w/w" },
      { label: "Permian Basin", value: "302", sub: "Steady" },
    ]
  },
  "energy": {
    articles: [
      { id: 1301, title: "Global Energy Demand Growth Slows to 1.2% in 2026, IEA Reports", excerpt: "The International Energy Agency's latest monthly report shows moderating consumption growth driven by Chinese economic headwinds and efficiency gains.", date: "Apr 4, 2026", author: "Sarah Mitchell", readTime: "7 min" },
      { id: 1302, title: "U.S. Power Grid Faces Record Summer Demand From Data Center Expansion", excerpt: "AI-driven data center buildouts are straining electricity infrastructure across Texas, Virginia, and the Southwest.", date: "Apr 3, 2026", author: "Anna Kowalski", readTime: "6 min" },
      { id: 1303, title: "European Energy Security Improves as LNG Import Capacity Doubles Since 2022", excerpt: "New regasification terminals in Germany, Italy, and Greece have significantly reduced Europe's vulnerability to supply shocks.", date: "Apr 2, 2026", author: "Elena Petrova", readTime: "5 min" },
      { id: 1304, title: "India's Energy Consumption Surpasses Japan for First Time", excerpt: "Rapid industrialization and a growing middle class push India past Japan as the world's fourth-largest energy consumer.", date: "Apr 1, 2026", author: "David Chen", readTime: "5 min" },
      { id: 1305, title: "Carbon Capture Investment Reaches $12B Globally in 2025", excerpt: "Direct air capture and point-source CCS projects are scaling up as government subsidies and carbon pricing incentivize deployment.", date: "Mar 31, 2026", author: "James Carter", readTime: "6 min" },
    ],
    stats: [
      { label: "Global Demand", value: "104.2M", sub: "bpd (oil equiv.)" },
      { label: "U.S. Production", value: "13.4M", sub: "bpd crude" },
      { label: "LNG Exports", value: "14 Bcf/d", sub: "U.S. Gulf" },
    ]
  },
  "crude-oil": {
    articles: [
      { id: 1401, title: "Permian Basin Production Hits Record 6.2 Million Barrels Per Day", excerpt: "Improved well productivity and extended lateral lengths continue to push U.S. shale output higher despite a falling rig count.", date: "Apr 4, 2026", author: "James Carter", readTime: "6 min" },
      { id: 1402, title: "Guyana's Stabroek Block Delivers New 1.5 Billion Barrel Discovery", excerpt: "ExxonMobil's latest exploration well adds to what is already one of the most significant deepwater oil provinces found this century.", date: "Apr 3, 2026", author: "Sarah Mitchell", readTime: "7 min" },
      { id: 1403, title: "OPEC+ Compliance Reaches 116% as Iraq Over-Produces Again", excerpt: "Baghdad's output consistently exceeds its agreed ceiling, creating tension within the alliance and complicating quota negotiations.", date: "Apr 2, 2026", author: "Elena Petrova", readTime: "5 min" },
      { id: 1404, title: "North Sea Forties Pipeline Restart Eases Brent Supply Concerns", excerpt: "The 450,000 bpd system returns to full capacity after a 10-day maintenance shutdown that briefly tightened dated Brent.", date: "Apr 1, 2026", author: "David Chen", readTime: "4 min" },
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
      { id: 1502, title: "California Gas Prices Hit $5.18 as State-Specific Regulations Add Costs", excerpt: "The Golden State's unique fuel standards and carbon pricing continue to push pump prices well above the national average.", date: "Apr 3, 2026", author: "Anna Kowalski", readTime: "5 min" },
      { id: 1503, title: "Gulf Coast Refinery Margins Improve as Crack Spreads Widen", excerpt: "The 3-2-1 crack spread has expanded to $28/barrel, incentivizing higher refinery utilization rates.", date: "Apr 2, 2026", author: "James Carter", readTime: "4 min" },
      { id: 1504, title: "EIA: U.S. Summer Gasoline Demand Expected to Average 9.1M BPD", excerpt: "The Energy Information Administration forecasts steady consumption growth despite elevated prices and rising EV adoption.", date: "Apr 1, 2026", author: "Elena Petrova", readTime: "5 min" },
    ],
    stats: [
      { label: "U.S. National Avg", value: "$3.42", sub: "/gallon" },
      { label: "RBOB Futures", value: "$2.18", sub: "/gallon" },
      { label: "Crack Spread", value: "$28.00", sub: "3-2-1" },
    ]
  },
  "natural-gas": {
    articles: [
      { id: 1601, title: "Henry Hub Falls Below $3.50 as U.S. Storage Surplus Persists", excerpt: "Above-average inventories and record production continue to weigh on domestic natural gas prices despite rising export demand.", date: "Apr 4, 2026", author: "Elena Petrova", readTime: "5 min" },
      { id: 1602, title: "European TTF Gas Rallies 12% on Extended Cold Weather Forecast", excerpt: "A late-season cold snap across Northern Europe is drawing down storage reserves faster than seasonal norms.", date: "Apr 3, 2026", author: "Sarah Mitchell", readTime: "4 min" },
      { id: 1603, title: "U.S. LNG Exports Hit Record 14 Bcf/d as Golden Pass Begins Operations", excerpt: "The new Qatar-Exxon joint venture facility in Texas adds 2.5 Bcf/d of liquefaction capacity to the Gulf Coast.", date: "Apr 2, 2026", author: "James Carter", readTime: "6 min" },
      { id: 1604, title: "Japan LNG Spot Price Drops to $12.40/MMBtu on Mild Asian Demand", excerpt: "Warmer-than-normal temperatures across Northeast Asia reduce heating gas requirements heading into spring.", date: "Apr 1, 2026", author: "David Chen", readTime: "4 min" },
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
      { id: 1702, title: "Northeast Home Heating Costs Rose 8% This Winter vs. Last Year", excerpt: "The EIA's Winter Fuels Outlook post-mortem shows higher crude prices and cold January temps drove seasonal cost increases.", date: "Apr 3, 2026", author: "Anna Kowalski", readTime: "5 min" },
      { id: 1703, title: "Diesel and Heating Oil Margins Diverge as Trucking Demand Holds", excerpt: "While residential heating demand fades, strong freight activity keeps middle distillate markets well-supported.", date: "Apr 2, 2026", author: "James Carter", readTime: "4 min" },
      { id: 1704, title: "European Diesel Imports From Asia Rise as Arbitrage Window Opens", excerpt: "A widening East-West price differential is pulling Asian diesel cargoes toward Europe for the first time since January.", date: "Apr 1, 2026", author: "Elena Petrova", readTime: "5 min" },
    ],
    stats: [
      { label: "Heating Oil", value: "$2.34", sub: "/gallon" },
      { label: "Diesel", value: "$2.41", sub: "/gallon" },
      { label: "Distillate Stock", value: "118M", sub: "barrels" },
    ]
  },
  "geopolitics": {
    articles: [
      { id: 1801, title: "Red Sea Attacks Force 60% of Tanker Traffic to Reroute Around Africa", excerpt: "Houthi missile and drone strikes continue to disrupt commercial shipping through the Bab el-Mandeb strait, adding $1-2/barrel to delivered crude costs.", date: "Apr 4, 2026", author: "Elena Petrova", readTime: "7 min" },
      { id: 1802, title: "U.S. Tightens Sanctions Enforcement on Russian Oil Price Cap", excerpt: "The Treasury Department blacklists 14 additional tankers suspected of transporting Russian crude above the $60/barrel ceiling.", date: "Apr 3, 2026", author: "David Chen", readTime: "6 min" },
      { id: 1803, title: "Venezuela Sanctions Relief Under Review as Election Promises Stall", excerpt: "Washington weighs re-imposing oil sector restrictions after Caracas fails to meet democratic reform benchmarks.", date: "Apr 2, 2026", author: "Sarah Mitchell", readTime: "5 min" },
      { id: 1804, title: "Saudi-Iran Détente Reduces Persian Gulf Risk Premium", excerpt: "Diplomatic normalization between Riyadh and Tehran continues to ease tensions around the Strait of Hormuz chokepoint.", date: "Apr 1, 2026", author: "James Carter", readTime: "5 min" },
      { id: 1805, title: "Nigeria Pipeline Security Improves 40% Under New Government Program", excerpt: "Reduced sabotage and theft in the Niger Delta enable Bonny Light production to recover toward 2019 levels.", date: "Mar 31, 2026", author: "Anna Kowalski", readTime: "4 min" },
    ],
    stats: [
      { label: "Hormuz Transit", value: "21M", sub: "bpd" },
      { label: "Red Sea Impact", value: "+$1.50", sub: "/bbl premium" },
      { label: "Russian Exports", value: "4.8M", sub: "bpd to Asia" },
    ]
  },
  "company-news": {
    articles: [
      { id: 1901, title: "ExxonMobil Reports $9.2B Q1 Profit, Raises Dividend 4%", excerpt: "Strong upstream earnings from the Permian Basin and Guyana offset weaker downstream margins in the quarter.", date: "Apr 4, 2026", author: "David Chen", readTime: "5 min" },
      { id: 1902, title: "Shell Accelerates North Sea Asset Sales Worth $4.5B", excerpt: "The energy major continues divesting mature UK and Norwegian assets to focus capital on high-return deepwater projects.", date: "Apr 3, 2026", author: "Sarah Mitchell", readTime: "4 min" },
      { id: 1903, title: "Chevron Completes Hess Merger, Gains Guyana Stabroek Stake", excerpt: "The $53B deal closes after FTC review, giving Chevron a 30% stake in one of the world's fastest-growing oil provinces.", date: "Apr 2, 2026", author: "James Carter", readTime: "6 min" },
      { id: 1904, title: "TotalEnergies Signs 20-Year LNG Supply Agreement with India", excerpt: "The deal secures 3 MTPA of LNG from Mozambique's Area 1 project, supporting India's coal-to-gas transition strategy.", date: "Apr 1, 2026", author: "Elena Petrova", readTime: "5 min" },
      { id: 1905, title: "Saudi Aramco Invests $2B in South Korean Refinery Expansion", excerpt: "The investment strengthens Aramco's downstream integration strategy and secures long-term crude supply placement in Asia.", date: "Mar 31, 2026", author: "Anna Kowalski", readTime: "4 min" },
    ],
    stats: [
      { label: "ExxonMobil", value: "$9.2B", sub: "Q1 profit" },
      { label: "Aramco CapEx", value: "$50B", sub: "2026 plan" },
      { label: "M&A Volume", value: "$87B", sub: "YTD energy" },
    ]
  },
  "alternative-energy": {
    articles: [
      { id: 2001, title: "Global Renewable Investment Hits $1.8 Trillion in 2025, IRENA Reports", excerpt: "Solar, wind, and battery storage captured 80% of new power generation investment worldwide for the first time.", date: "Apr 4, 2026", author: "Anna Kowalski", readTime: "6 min" },
      { id: 2002, title: "Green Hydrogen Costs Fall 40% Since 2022 as Electrolyzer Scale Grows", excerpt: "Projects in Saudi Arabia, Australia, and Chile are proving that sub-$3/kg green hydrogen is achievable at scale.", date: "Apr 3, 2026", author: "James Carter", readTime: "5 min" },
      { id: 2003, title: "Battery Storage Deployments Triple Year-Over-Year in the U.S.", excerpt: "Grid-scale lithium-ion installations reached 18 GW in 2025 as utilities pair storage with solar to meet peak demand.", date: "Apr 2, 2026", author: "Sarah Mitchell", readTime: "5 min" },
      { id: 2004, title: "EU Carbon Price Stabilizes at €85/Tonne, Supporting Clean Energy Economics", excerpt: "The Emissions Trading System continues to make fossil fuel power generation more expensive relative to renewables.", date: "Apr 1, 2026", author: "Elena Petrova", readTime: "4 min" },
    ],
    stats: [
      { label: "Renewable CapEx", value: "$1.8T", sub: "2025 global" },
      { label: "Solar Cost", value: "$24", sub: "/MWh avg" },
      { label: "EV Sales Share", value: "22%", sub: "global 2025" },
    ]
  },
  "nuclear": {
    articles: [
      { id: 2101, title: "NuScale Small Modular Reactor Receives Full NRC Design Certification", excerpt: "The 77 MWe module becomes the first SMR to complete the U.S. regulatory approval process, clearing the path for commercial deployment.", date: "Apr 4, 2026", author: "Anna Kowalski", readTime: "7 min" },
      { id: 2102, title: "France Commits €10B to Build Six New EPR2 Reactors by 2040", excerpt: "President Macron's nuclear renaissance plan aims to replace aging reactors while supporting European energy independence.", date: "Apr 3, 2026", author: "Elena Petrova", readTime: "6 min" },
      { id: 2103, title: "Uranium Spot Price Surges to $92/lb as Utility Contracting Accelerates", excerpt: "After a decade of low prices, uranium has rallied 180% since 2023 on renewed nuclear ambitions from the U.S., China, and India.", date: "Apr 2, 2026", author: "David Chen", readTime: "5 min" },
      { id: 2104, title: "Microsoft Signs 20-Year Nuclear Power Purchase Agreement for Data Centers", excerpt: "The tech giant secures carbon-free baseload power from Constellation Energy's reactor fleet to support AI computing growth.", date: "Apr 1, 2026", author: "James Carter", readTime: "5 min" },
    ],
    stats: [
      { label: "Uranium Price", value: "$92", sub: "/lb U₃O₈" },
      { label: "Global Reactors", value: "440", sub: "operational" },
      { label: "Under Constr.", value: "62", sub: "reactors" },
    ]
  },
  "solar": {
    articles: [
      { id: 2201, title: "Global Solar Installations Reach Record 420 GW in 2025", excerpt: "China alone accounted for 230 GW of new solar capacity as module prices fell below $0.10/watt for the first time.", date: "Apr 4, 2026", author: "Anna Kowalski", readTime: "6 min" },
      { id: 2202, title: "U.S. Utility-Scale Solar Pipeline Exceeds 300 GW as IRA Credits Flow", excerpt: "The Inflation Reduction Act's tax credits continue to drive a massive buildout of solar farms across the Sun Belt states.", date: "Apr 3, 2026", author: "Sarah Mitchell", readTime: "5 min" },
      { id: 2203, title: "Perovskite-Silicon Tandem Cells Hit 33.9% Efficiency Record", excerpt: "Oxford PV's commercial-ready tandem cells promise to push rooftop solar economics further into mainstream territory.", date: "Apr 2, 2026", author: "James Carter", readTime: "5 min" },
      { id: 2204, title: "India's Solar Tariffs Drop to Record Low $0.029/kWh in Rajasthan Auction", excerpt: "The world's cheapest solar electricity bid underscores India's aggressive renewable deployment targets.", date: "Apr 1, 2026", author: "David Chen", readTime: "4 min" },
    ],
    stats: [
      { label: "2025 Installed", value: "420 GW", sub: "global" },
      { label: "Module Price", value: "$0.09", sub: "/watt" },
      { label: "LCOE", value: "$24", sub: "/MWh avg" },
    ]
  },
  "wind": {
    articles: [
      { id: 2301, title: "Offshore Wind Capacity Surpasses 80 GW Globally as Costs Stabilize", excerpt: "After a period of cost inflation driven by supply chain bottlenecks, offshore wind developers report stabilizing turbine and installation costs.", date: "Apr 4, 2026", author: "Elena Petrova", readTime: "6 min" },
      { id: 2302, title: "Vineyard Wind Achieves Full 800 MW Output Off Massachusetts Coast", excerpt: "America's first utility-scale offshore wind farm is now operating at rated capacity, powering 400,000 homes.", date: "Apr 3, 2026", author: "Sarah Mitchell", readTime: "5 min" },
      { id: 2303, title: "Vestas Unveils 17 MW Offshore Turbine, World's Most Powerful", excerpt: "The V236-17.0 MW platform can generate enough electricity for 20,000 households from a single installation.", date: "Apr 2, 2026", author: "James Carter", readTime: "4 min" },
      { id: 2304, title: "Texas Wind Generation Sets New Record at 35 GW During March Storm", excerpt: "ERCOT's wind fleet produced more power than natural gas for a 48-hour period during sustained high wind conditions.", date: "Apr 1, 2026", author: "Anna Kowalski", readTime: "4 min" },
    ],
    stats: [
      { label: "Offshore Global", value: "80 GW", sub: "installed" },
      { label: "U.S. Onshore", value: "155 GW", sub: "installed" },
      { label: "Largest Turbine", value: "17 MW", sub: "Vestas" },
    ]
  },
  "renewable-energy": {
    articles: [
      { id: 2401, title: "Renewables Provided 35% of Global Electricity in 2025, IEA Confirms", excerpt: "Wind, solar, hydro, and biomass generation surpassed coal for the first time on an annual basis worldwide.", date: "Apr 4, 2026", author: "Sarah Mitchell", readTime: "7 min" },
      { id: 2402, title: "Grid-Scale Battery Storage Hits 100 GW Global Milestone", excerpt: "Lithium-ion dominates the market but sodium-ion and iron-air chemistries are gaining ground for long-duration applications.", date: "Apr 3, 2026", author: "James Carter", readTime: "5 min" },
      { id: 2403, title: "Green Hydrogen Electrolyzer Orders Surge 300% in 2025", excerpt: "European and Middle Eastern projects drive demand for gigawatt-scale electrolysis systems from manufacturers like Plug Power and Nel.", date: "Apr 2, 2026", author: "David Chen", readTime: "5 min" },
      { id: 2404, title: "U.S. Clean Energy Jobs Surpass 4 Million for First Time", excerpt: "Solar installation, EV manufacturing, and battery production drive employment growth outpacing fossil fuel sector hiring.", date: "Apr 1, 2026", author: "Anna Kowalski", readTime: "4 min" },
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
