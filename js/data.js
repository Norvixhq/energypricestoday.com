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
