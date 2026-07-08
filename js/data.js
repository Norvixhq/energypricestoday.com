/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Data Layer
   All mock data in one place for easy future API replacement
   ═══════════════════════════════════════════════════════════════════ */

const COMMODITIES = [
  { name: "WTI Crude", price: 70.44, change: 1.92, pct: 2.80, unit: "$/bbl", spark: [68.9,68.6,69.2,69.0,68.8,69.3,70.44], loading: false },
  { name: "Brent Crude", price: 74.16, change: 2.17, pct: 3.01, unit: "$/bbl", spark: [72.4,72.1,72.6,72.3,72.0,72.5,74.16], loading: false },
  { name: "Natural Gas", price: 3.34, change: 0.03, pct: 0.91, unit: "$/MMBtu", spark: [3.30,3.31,3.32,3.31,3.33,3.32,3.34], loading: false },
  { name: "Gasoline RBOB", price: 2.36, change: 0.06, pct: 2.61, unit: "$/gal", spark: [2.31,2.30,2.32,2.31,2.30,2.32,2.36], loading: false },
  { name: "Heating Oil", price: 2.58, change: 0.07, pct: 2.79, unit: "$/gal", spark: [2.52,2.51,2.53,2.52,2.51,2.53,2.58], loading: false },
  { name: "Murban Crude", price: 74.40, change: 2.15, pct: 2.98, unit: "$/bbl", spark: [72.6,72.3,72.8,72.5,72.2,72.7,74.4], loading: false },
  { name: "Diesel ULSD", price: 2.61, change: 0.07, pct: 2.76, unit: "$/gal", spark: [2.55,2.54,2.56,2.55,2.54,2.56,2.61], loading: false },
  { name: "Jet Fuel", price: 2.80, change: 0.07, pct: 2.56, unit: "$/gal", spark: [2.74,2.73,2.75,2.74,2.73,2.75,2.80], loading: false },
  { name: "Coal", price: 140.0, change: 0.0, pct: 0.00, unit: "$/ton", spark: [140.0,140.0,140.0,140.0,140.0,140.0,140.0], loading: false },
  { name: "Gold", price: 4980.50, change: 15.30, pct: 0.31, unit: "$/oz", spark: [], loading: false },
];

const FULL_PRICES = {
  "All Prices": [
    ...COMMODITIES,
    { name: "Dubai Fateh", price: 72.60, change: 2.10, pct: 2.98, unit: "$/bbl", spark: [70.9,70.6,71.1,70.8,70.5,71.0,72.6] },
    { name: "Louisiana Light", price: 73.10, change: 2.10, pct: 2.96, unit: "$/bbl", spark: [71.4,71.1,71.6,71.3,71.0,71.5,73.1] },
  ],
  "OPEC Blends": [
    { name: "OPEC Basket", price: 73.80, change: 2.10, pct: 2.93, unit: "$/bbl", spark: [72.1,71.8,72.3,72.0,71.7,72.2,73.8] },
    { name: "Arab Light", price: 74.90, change: 2.10, pct: 2.89, unit: "$/bbl", spark: [73.2,72.9,73.4,73.1,72.8,73.3,74.9] },
    { name: "Bonny Light", price: 75.60, change: 2.10, pct: 2.86, unit: "$/bbl", spark: [73.9,73.6,74.1,73.8,73.5,74.0,75.6] },
    { name: "Iran Heavy", price: 68.70, change: 2.10, pct: 3.15, unit: "$/bbl", spark: [67.0,66.7,67.2,66.9,66.6,67.1,68.7] },
    { name: "Kuwait Export", price: 72.90, change: 2.10, pct: 2.97, unit: "$/bbl", spark: [71.2,70.9,71.4,71.1,70.8,71.3,72.9] },
  ],
  "U.S. Blends": [
    { name: "WTI Crude", price: 70.44, change: 1.92, pct: 2.80, unit: "$/bbl", spark: [68.9,68.6,69.2,69.0,68.8,69.3,70.44] },
    { name: "Louisiana Light", price: 73.10, change: 2.10, pct: 2.96, unit: "$/bbl", spark: [71.4,71.1,71.6,71.3,71.0,71.5,73.1] },
    { name: "WTI Midland", price: 71.50, change: 2.10, pct: 3.03, unit: "$/bbl", spark: [69.8,69.5,70.0,69.7,69.4,69.9,71.5] },
    { name: "Mars Blend", price: 69.20, change: 2.10, pct: 3.13, unit: "$/bbl", spark: [67.5,67.2,67.7,67.4,67.1,67.6,69.2] },
    { name: "Eagle Ford", price: 70.60, change: 2.10, pct: 3.07, unit: "$/bbl", spark: [68.9,68.6,69.1,68.8,68.5,69.0,70.6] },
  ],
  "Canadian Blends": [
    { name: "Western Canadian Select", price: 59.70, change: 1.90, pct: 3.29, unit: "$/bbl", spark: [58.1,57.8,58.3,58.0,57.7,58.2,59.7] },
    { name: "Syncrude Sweet", price: 69.70, change: 2.10, pct: 3.11, unit: "$/bbl", spark: [68.0,67.7,68.2,67.9,67.6,68.1,69.7] },
    { name: "Cold Lake Blend", price: 59.10, change: 1.90, pct: 3.32, unit: "$/bbl", spark: [57.5,57.2,57.7,57.4,57.1,57.6,59.1] },
    { name: "Peace Sour", price: 63.90, change: 1.90, pct: 3.06, unit: "$/bbl", spark: [62.3,62.0,62.5,62.2,61.9,62.4,63.9] },
  ],
  "Refined Products": [
    { name: "Gasoline RBOB", price: 2.36, change: 0.06, pct: 2.61, unit: "$/gal", spark: [2.31,2.30,2.32,2.31,2.30,2.32,2.36] },
    { name: "Heating Oil", price: 2.58, change: 0.07, pct: 2.79, unit: "$/gal", spark: [2.52,2.51,2.53,2.52,2.51,2.53,2.58] },
    { name: "Diesel", price: 2.61, change: 0.07, pct: 2.76, unit: "$/gal", spark: [2.55,2.54,2.56,2.55,2.54,2.56,2.61] },
    { name: "Jet Fuel", price: 2.80, change: 0.07, pct: 2.56, unit: "$/gal", spark: [2.74,2.73,2.75,2.74,2.73,2.75,2.80] },
    { name: "Naphtha", price: 563.00, change: 16.00, pct: 2.93, unit: "$/mt", spark: [551,549,552,550,548,551,563] },
  ],
  "Natural Gas": [
    { name: "Henry Hub", price: 3.46, change: -0.04, pct: -1.14, unit: "$/MMBtu", spark: [3.55,3.52,3.50,3.49,3.48,3.47,3.46] },
    { name: "TTF Dutch", price: 52.40, change: -0.85, pct: -1.60, unit: "€/MWh", spark: [53.1,54.0,56.2,55.0,53.8,53.0,52.4] },
    { name: "UK NBP", price: 128.50, change: -2.10, pct: -1.61, unit: "p/therm", spark: [130.2,132.4,137.8,134.9,132.0,130.1,128.5] },
    { name: "JKM LNG", price: 27.80, change: -0.45, pct: -1.59, unit: "$/MMBtu", spark: [28.1,28.6,29.8,29.2,28.6,28.2,27.8] },
  ],
};

const BREAKING_NEWS = [
  { title: "Iran Strikes Qatari LNG Tanker Near Hormuz; Second Vessel Hit by Projectile", cat: "Geopolitics", slug: "geopolitics", time: "1h" },
  { title: "U.S. Revokes Iran\u2019s Oil-Sale License; Brent Pops to $76 After Hours", cat: "Geopolitics", slug: "geopolitics", time: "2h" },
  { title: "Oil Jumps on Hormuz Attacks but Holds Near Four-Month Lows", cat: "Oil Markets", slug: "oil-prices", time: "4h" },
  { title: "OPEC+ Approves 188,000 bpd Quota Increase for Next Month", cat: "Oil Markets", slug: "oil-prices", time: "6h" },
  { title: "Saudi Aramco Cuts Arab Light to Asia by $11 to First Discount Since 2020", cat: "Geopolitics", slug: "geopolitics", time: "8h" },
  { title: "AAA National Average Slips to $3.790 as July 4th Travelers Get Relief", cat: "Gas Prices", slug: "gas-prices", time: "10h" },
  { title: "Hormuz Traffic Keeps Recovering as Supertankers Exit via Route Near Iran", cat: "Geopolitics", slug: "geopolitics", time: "12h" },
  { title: "Iraq Presses OPEC for a Higher Quota, Signals Possible Exit", cat: "Oil Markets", slug: "oil-prices", time: "1d" },
];

const MARKET_DRIVERS = [
  { cat: "Tanker Attack", icon: "alert-triangle", title: "Iran Strikes Qatari LNG Tanker Near Hormuz; Second Vessel Hit by Projectile", desc: "The reopening hit its most serious test yet. Iran attacked the Qatari liquefied natural gas tanker Al-Rekayyat as it transited near the Strait of Hormuz, and a second tanker was struck by an unidentified projectile and is believed to have suffered structural damage. The incidents reaffirmed the fragility of the interim U.S.-Iran peace agreement and sent oil sharply higher: Brent settled 3% higher at $74.16 and jumped further after hours, while WTI advanced to $70.44. The waterway typically handles around a fifth of the world\u2019s oil trade." },
  { cat: "License Revoked", icon: "file-x", title: "U.S. Revokes Iran\u2019s Oil-Sale License as Prices Extend Gains After Hours", desc: "In response to the tanker attacks, the United States revoked the license that had authorized Iran to sell its oil, with a U.S. official stressing that the memorandum of understanding is \u201Centirely performance-based.\u201D Prices extended their advance after the announcement, with Brent popping 5.6% to $76.04 and WTI jumping 5.4% to $72.25 in after-hours trading. The move sharpens the standoff over the MOU even as both sides signal an interest in containing the conflict, and it reintroduces a supply risk the market had largely written off." },
  { cat: "OPEC+ Adds Barrels", icon: "trending-down", title: "OPEC+ Approves 188,000 bpd Quota Increase as Supply Unwind Continues", desc: "Working against the security premium, OPEC+ members led by Saudi Arabia agreed over the weekend to raise production quotas by 188,000 barrels per day for next month, continuing a progressive unwinding of long-standing curbs as conditions normalize. Persian Gulf producers are rapidly accelerating output, with Saudi exports approaching pre-war levels and the UAE having fully restored its shipping flows. The added barrels reinforce expectations of ample global supply that have kept prices near their lowest levels since late February." },
  { cat: "Saudi Discounts Asia", icon: "bar-chart", title: "Saudi Aramco Cuts Arab Light to Asia by $11 to First Discount Since 2020", desc: "In a striking signal of softer conditions, Saudi Aramco cut the price of its Arab Light crude for Asian buyers next month by $11 a barrel, widening the differential to a $1.50 discount against the regional benchmark. The last two times Aramco offered the grade at a discount were during the oil price wars of 2020 and 2015. The cut, coming alongside the OPEC+ quota hike, underscores that the cartel is prioritizing volume and market share as returning Gulf barrels compete for buyers." },
  { cat: "Prices Near Lows", icon: "activity", title: "Oil Holds Near Four-Month Lows Despite the Security Spike", desc: "The defining tension of the market: even after the tanker attacks and license revocation drove a sharp intraday rally, crude remains close to its lowest levels since late February, before the conflict began. Vessel traffic through Hormuz kept recovering \u2014 at least eight Japan-linked ships, including five supertankers, exited via a route near Iran \u2014 and the supply-driven bearish trend reasserted itself between the flare-ups. The market is now balancing a re-rated security risk against an unmistakable wave of returning supply." },
  { cat: "Gas Keeps Falling", icon: "fuel", title: "AAA National Average Slips to $3.790 as July 4th Travelers Get Relief", desc: "AAA\u2019s national average for regular gasoline slipped to $3.790, extending a steady decline that gave July 4th travelers a break at the pump. Indiana is the cheapest market at $3.06, with Oklahoma ($3.32) and Texas ($3.32) close behind, while California ($5.37) and Hawaii ($5.46) remain the most expensive. Because pump prices lag crude by one to two weeks, the recent slide still has room to run \u2014 though today\u2019s security-driven spike in oil is a reminder that the direction could turn if the Hormuz standoff escalates." },
];

const FEATURED_ARTICLES = [
  { id: 101, title: "Iran Strikes Qatari LNG Tanker Near Hormuz as U.S. Revokes Oil-Sale License", excerpt: "Iran attacked the Qatari LNG tanker Al-Rekayyat near the Strait of Hormuz and a second vessel was hit by a projectile, sending oil sharply higher. The U.S. revoked Iran\u2019s license to sell its oil; Brent settled at $74.16 and jumped further after hours.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "July 7, 2026", readTime: "6 min", featured: true },
  { id: 102, title: "Oil Jumps on Hormuz Tanker Attacks but Holds Near Four-Month Lows", excerpt: "Brent settled 3% higher at $74.16 and WTI advanced to $70.44 after the tanker strikes, with both popping further after hours on the license revocation. Yet prices remain close to their lowest since late February as returning supply weighs on the market.", cat: "Oil Markets", slug: "oil-prices", author: "EnergyPricesToday Editorial", date: "July 7, 2026", readTime: "5 min" },
  { id: 103, title: "OPEC+ Approves 188,000 bpd Quota Increase as Supply Unwind Continues", excerpt: "OPEC+ members led by Saudi Arabia agreed to raise quotas by 188,000 bpd for next month, continuing to unwind long-standing curbs. Saudi exports are approaching pre-war levels and the UAE has fully restored its shipping flows.", cat: "Oil Markets", slug: "oil-prices", author: "EnergyPricesToday Editorial", date: "July 7, 2026", readTime: "5 min" },
  { id: 104, title: "Saudi Aramco Cuts Arab Light to Asia by $11 in First Discount Since 2020", excerpt: "Aramco cut its Arab Light price for Asian buyers by $11 a barrel to a $1.50 discount against the regional benchmark \u2014 the first discount since the price wars of 2020 and 2015 \u2014 signaling a pivot to volume and market share as Gulf barrels return.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "July 7, 2026", readTime: "5 min" },
  { id: 105, title: "AAA National Average Slips to $3.790 as July 4th Travelers Get Relief", excerpt: "AAA\u2019s national average slipped to $3.790 as crude trades near four-month lows. Indiana is cheapest at $3.06, with Oklahoma ($3.32) and Texas ($3.32) close behind; California ($5.37) and Hawaii ($5.46) remain highest.", cat: "Gas Prices", slug: "gas-prices", author: "EnergyPricesToday Editorial", date: "July 7, 2026", readTime: "4 min" },
  { id: 106, title: "Hormuz Traffic Keeps Recovering as Supertankers Exit via Route Near Iran", excerpt: "At least eight Japan-linked ships, including five supertankers capable of carrying 2 million barrels each, exited Hormuz via a route near Iran, underscoring that commercial flows keep normalizing even as isolated attacks re-rate the security risk.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "July 7, 2026", readTime: "5 min" },
];

const COMPANY_NEWS = [
  { id: 201, title: "Iran Strikes Qatari LNG Tanker Near Hormuz as U.S. Revokes Oil-Sale License", date: "July 7, 2026" },
  { id: 202, title: "Oil Jumps on Hormuz Tanker Attacks but Holds Near Four-Month Lows", date: "July 7, 2026" },
  { id: 203, title: "OPEC+ Approves 188,000 bpd Quota Increase as Supply Unwind Continues", date: "July 7, 2026" },
  { id: 204, title: "Saudi Aramco Cuts Arab Light to Asia by $11 in First Discount Since 2020", date: "July 7, 2026" },
  { id: 205, title: "AAA National Average Slips to $3.790 as July 4th Travelers Get Relief", date: "July 7, 2026" },
  { id: 206, title: "Hormuz Traffic Keeps Recovering as Supertankers Exit via Route Near Iran", date: "July 7, 2026" },
];

const GEO_ITEMS = [
  { id: 301, region: "Strait of Hormuz", title: "Iran Strikes Qatari LNG Tanker; Second Vessel Hit by Projectile", desc: "The reopening hit its most serious test yet. Iran attacked the Qatari liquefied natural gas tanker Al-Rekayyat as it transited near the Strait of Hormuz, and a second tanker was struck by an unidentified projectile with believed structural damage. Qatar\u2019s foreign ministry confirmed the strike on the Al-Rekayyat. The incidents reaffirmed the fragility of the interim U.S.-Iran peace agreement and sent oil sharply higher, with Brent settling 3% up at $74.16 and climbing further after hours." },
  { id: 302, region: "U.S.-Iran Standoff", title: "Washington Revokes Iran\u2019s Oil-Sale License in Response to Attacks", desc: "The United States revoked the license authorizing Iran to sell its oil after the tanker attacks, with a U.S. official stressing the memorandum of understanding is \u201Centirely performance-based.\u201D Prices extended gains after the announcement \u2014 Brent popped 5.6% to $76.04 and WTI jumped 5.4% to $72.25 in after-hours trading. The move sharpens the standoff over the MOU and reintroduces a supply risk the market had largely written off, even as both sides signal an interest in containing the conflict." },
  { id: 303, region: "OPEC & Supply", title: "OPEC+ Approves 188,000 bpd Quota Increase; Saudi Cuts Arab Light to Asia", desc: "Working against the security premium, OPEC+ members led by Saudi Arabia agreed over the weekend to raise quotas by 188,000 barrels per day for next month. Saudi Aramco separately cut its Arab Light price for Asian buyers by $11 a barrel to a $1.50 discount \u2014 the first discount since the price wars of 2020 and 2015. Saudi exports are approaching pre-war levels and the UAE has fully restored flows, reinforcing expectations of ample supply." },
  { id: 304, region: "Global Markets", title: "Oil Holds Near Four-Month Lows Despite the Security Spike", desc: "The defining tension: even after the attacks and license revocation drove a sharp rally, crude remains close to its lowest levels since late February. Vessel traffic through Hormuz kept recovering \u2014 at least eight Japan-linked ships, including five supertankers, exited via a route near Iran \u2014 and the supply-driven bearish trend reasserted itself between the flare-ups. The market is balancing a re-rated security risk against an unmistakable wave of returning supply." },
  { id: 305, region: "OPEC Cohesion", title: "Iraq Presses for a Higher Quota and Signals It Could Follow the UAE Out", desc: "OPEC faces the possibility of another exit by its second-largest producer: Iraq has reportedly sought a higher production quota and told the group it could leave if its demands are not met, after the UAE departed the cartel in May. The friction over quotas comes as the group unwinds curbs and members race to recoup wartime revenue losses, adding a layer of internal strain to an already bearish supply outlook." },
  { id: 306, region: "U.S. Consumers", title: "AAA National Average Slips to $3.790 as July 4th Travelers Get Relief", desc: "AAA\u2019s national average for regular gasoline slipped to $3.790, extending a steady decline that gave July 4th travelers a break at the pump. Indiana is the cheapest market at $3.06, with Oklahoma ($3.32) and Texas ($3.32) close behind, while California ($5.37) and Hawaii ($5.46) remain the most expensive. With the one-to-two-week pump lag, the recent crude slide still has room to reach drivers \u2014 though today\u2019s spike is a reminder the trend could turn." },
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
  { id: 462, title: "Iran Strikes Qatari LNG Tanker Near Hormuz as U.S. Revokes Oil-Sale License", excerpt: "Iran attacked the Qatari LNG tanker Al-Rekayyat near the Strait of Hormuz and a second vessel was hit by a projectile, sending oil sharply higher. The U.S. revoked Iran\u2019s license to sell its oil; Brent settled at $74.16 and jumped further after hours.", date: "Jul 7, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
  { id: 463, title: "OPEC+ Approves 188,000 bpd Quota Increase as Saudi Cuts Arab Light to Asia", excerpt: "OPEC+ agreed to raise quotas by 188,000 bpd for next month while Saudi Aramco cut Arab Light to Asian buyers by $11 \u2014 its first discount since 2020 \u2014 keeping the supply picture bearish even as security risk re-rates.", date: "Jul 7, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
  { id: 460, title: "Hormuz Transits Surge as Gulf Exports Recover to ~75% of Pre-War Levels", excerpt: "The reopening is now visibly underway: transits have accelerated, restoring Persian Gulf exports to roughly 75% of pre-war levels. Saudi Arabia began loading at Ras Tanura, and the UAE, Kuwait, and Qatar are boosting supply \u2014 constrained mainly by tanker availability.", date: "Jun 28, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
  { id: 461, title: "Container Ship Struck Off Oman, but Trump Confirms the Strait Stays Open", excerpt: "The Ever Lovely was struck by a projectile southeast of Oman, briefly lifting oil ~2%. But Trump confirmed Hormuz remains open and traffic continued. Residual security risk lingers even as commercial traffic returns in force.", date: "Jun 28, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
  { id: 450, title: "Crude Sinks to Pre-War Levels as Gulf Supply Returns: WTI Below $70, Brent Below $74", excerpt: "Oil extended its slide for a fourth straight session to the lowest since late February, down ~40% from the wartime peak. Tankers are resuming Hormuz transits with signals on, the IEA estimates the UAE is exporting at ~85% of pre-war levels, and Brent\u2019s curve flipped into contango.", date: "Jun 24, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
  { id: 451, title: "Hormuz Baffles Markets: Half-Open, Half-Closed After Iran\u2019s Renewed Closure Signal", excerpt: "Confusion over the strait persists as Iran and the U.S. issue conflicting statements. Windward said transits fell to 12 Sunday from 21 Saturday after Tehran\u2019s renewed closure signal. Insurers still treat the region as a war zone; full recovery appears weeks away.", date: "Jun 24, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" }
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
  // U.S. — Baker Hughes North America Rig Count, July 2, 2026 (released early ahead of Independence Day)
  us_total: 580, us_total_change: 6, us_oil: 445, us_oil_change: 5, us_gas: 124, us_gas_change: 0, us_misc: 11, us_misc_change: 1,
  us_land: 551, us_offshore: 10, us_inland: 4,
  us_directional: 64, us_horizontal: 483, us_vertical: 13,
  us_yoy: 4, us_yoy_total: 576,
  us_gom: 10,
  // Canada — June 5, 2026 (+7 w/w)
  canada_total: 169, canada_change: 7,
  // North America — June 5, 2026 (monthly: June 2026 = 732 vs June 2025 = 687)
  na_total: 732, na_change: 8, na_yoy: 45, na_yoy_total: 687,
  // International — April 2026 (monthly report released early May)
  intl_total: 1042, intl_change: -16, intl_yoy: -53, intl_yoy_total: 1095,
  intl_mideast: 488, intl_mideast_change: -12,
  intl_latam: 145, intl_latam_change: 2,
  intl_europe: 122, intl_europe_change: -2,
  intl_africa: 100, intl_africa_change: -1,
  intl_asiapac: 187, intl_asiapac_change: -3,
  // Worldwide
  ww_total: 1717, ww_change: -13,
  source: "Baker Hughes", updated: "U.S./Canada: June 12, 2026 (released June 18) | International: May 2026"
};

const OIL_FUTURES_DATA = [
  { contract: "WTI Aug 2026", price: 70.44, change: 1.92, pct: 2.80 },
  { contract: "WTI Sep 2026", price: 70.60, change: 1.88, pct: 2.74 },
  { contract: "WTI Oct 2026", price: 70.80, change: 1.82, pct: 2.64 },
  { contract: "WTI Nov 2026", price: 71.05, change: 1.76, pct: 2.54 },
  { contract: "WTI Dec 2026", price: 71.35, change: 1.68, pct: 2.41 },
  { contract: "WTI Dec 2027", price: 72.10, change: 1.40, pct: 1.98 },
  { contract: "Brent Sep 2026", price: 74.16, change: 2.17, pct: 3.01 },
  { contract: "Brent Oct 2026", price: 74.35, change: 2.10, pct: 2.91 },
  { contract: "Brent Nov 2026", price: 74.60, change: 2.02, pct: 2.78 },
  { contract: "Brent Dec 2026", price: 74.95, change: 1.94, pct: 2.66 },
];

const SUPPLY_CHOKEPOINTS = [
  { label: "Chokepoint", title: "Strait of Hormuz", desc: "Normally 21M bpd of crude transits daily; effectively closed since Feb 28 under a dual U.S.-Iran blockade. Fitch sees a possible reopening around the end of July.", stat: "Closed wk 15", region: "Persian Gulf" },
  { label: "Shipping", title: "Red Sea / Bab el-Mandeb", desc: "Tankers reroute around the Cape of Good Hope, adding 10-14 days; Iran has threatened to open a Bab el-Mandeb front during the conflict.", stat: "4.8M bpd", region: "Middle East" },
  { label: "Pipeline", title: "Druzhba Pipeline", desc: "Major crude pipeline from Russia to Central Europe, partially sanctioned since 2022.", stat: "1.2M bpd", region: "Russia → EU" },
  { label: "LNG Terminal", title: "U.S. Gulf Coast LNG", desc: "Record export capacity backfilling Qatari volumes lost to the Hormuz closure; EIA forecasts 17.0 Bcf/d of U.S. LNG exports for 2026.", stat: "17 Bcf/d", region: "United States" },
  { label: "Strait", title: "Strait of Malacca", desc: "Key Asian oil transit route connecting Indian Ocean to South China Sea.", stat: "16M bpd", region: "Southeast Asia" },
];

// ─── COMPREHENSIVE OIL PRICE DATA (mirrors OilPrice.com structure) ────
const OIL_PRICE_SECTIONS = [
  
];

// ─── UFutures & IndexesORY PAGE ──────────────────────────────
const CATEGORY_CONTENT = {
  "oil-prices": {
    articles: [
      { id: 1511, title: "Oil Jumps on Hormuz Tanker Attacks but Holds Near Four-Month Lows", excerpt: "Brent settled 3% higher at $74.16 and WTI advanced to $70.44 after the tanker strikes, popping further after hours on the license revocation. Yet prices remain near their lowest since late February as OPEC+ adds barrels and Saudi discounts to Asia.", date: "July 7, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1501, title: "Brent Near $72, Lowest Since February 27, After an Over-10% Weekly Drop", excerpt: "Crude has settled at pre-war levels: Brent fell to around $72, its lowest since February 27, and WTI traded in the high-$60s, leaving Brent down more than 10% on the week. The war-risk premium that pushed Brent above $120 has been almost entirely erased as the supply outlook normalizes.", date: "June 28, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1490, title: "Crude Sinks to Pre-War Levels as Gulf Supply Returns: WTI Below $70, Brent Below $74", excerpt: "Oil extended its slide for a fourth straight session to the lowest since late February, down ~40% from the wartime peak. The IEA estimates the UAE is exporting at ~85% of pre-war levels, and Brent\u2019s prompt spread flipped into bearish contango \u2014 a structural signal that near-term supply is now ample.", date: "June 24, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1481, title: "Crude Holds Near Multi-Month Lows: WTI About $74.82, Brent $77.90", excerpt: "Oil settled near multi-month lows as a holding interim peace met a slow physical reopening of Hormuz. Brent is down ~36% from its conflict peak. The U.S. Treasury issued a 60-day license authorizing the sale of Iranian oil, payable in dollars.", date: "June 22, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1471, title: "Crude Falls to Multi-Month Lows as Supply Returns: WTI Near $75.83, Brent $78.41", excerpt: "Oil fell again Thursday as the interim peace deal took effect. WTI dropped to $75.83 and Brent to $78.41, extending a slide from above $107 at the peak. The IEA said the market could move into a significant supply surplus by 2027 once Hormuz reopens.", date: "June 18, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1461, title: "Crude Holds Near a Three-Month Low With Markets Closed for the Weekend", excerpt: "Oil markets are closed Saturday after crude fell to a three-month low Friday \u2014 WTI settled $84.88, its lowest since April 17, and Brent $87.33. OPEC cut its 2026 demand-growth forecast to 970,000 bpd. Monday\u2019s open hinges on whether a memorandum is signed over the weekend.", date: "June 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1451, title: "Crude Falls to a Three-Month Low: WTI Settles $84.88, Brent $87.33 on Deal Optimism", excerpt: "Oil fell sharply Friday as the U.S. and Iran neared a deal to reopen the Strait of Hormuz. WTI settled down 3.2% at $84.88 and Brent lost 3.4% to $87.33, its lowest since early March. Both lost about 6% on the week but remain up 20%+ since the war began.", date: "June 12, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1402, title: "Oil Falls Below $90 After Touching $95; Crude Surrenders the Escalation Spike", excerpt: "Crude fell below $90 Tuesday, surrendering most of Monday\u2019s gains, as the Iran-Israel halt in attacks revived the diplomatic track. OPEC+ approved a July quota increase of 188,000 bpd; Fitch sees Hormuz reopening around the end of July with possible 4Q26 oversupply.", date: "June 9, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1700, title: "Why Do Oil Prices Change Every Day?", excerpt: "Supply data, demand signals, geopolitics, the U.S. dollar, and trader positioning — the five daily drivers that move WTI and Brent in real time.", date: "Apr 18, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1100, title: "What's the Oil Price Per Barrel Today? WTI & Brent Explained", excerpt: "A plain-English explainer on how crude oil is priced per barrel, why there are two benchmarks, and the five forces that move the price every day.", date: "Apr 18, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1101, title: "WTI vs Brent: What's the Difference and Why It Matters", excerpt: "WTI is landlocked in Oklahoma; Brent is seaborne in the North Sea. Why the spread exists, what it signals, and how it affects U.S. gasoline prices.", date: "Apr 18, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1001, title: "WTI Crude Climbs Past $71 as U.S. Inventories Post Sharp Drawdown", excerpt: "Commercial crude stocks at Cushing fell 4.2M barrels, well above the 1.8M consensus, signaling strong refinery demand ahead of driving season.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1002, title: "Brent-WTI Spread Widens to $4.44 on Atlantic Basin Tightness", excerpt: "North Sea supply disruptions and strong European refinery margins are pulling Brent higher relative to WTI.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1003, title: "Goldman Sachs Raises Brent Forecast to $82 by Year-End", excerpt: "The bank cites stronger-than-expected emerging market demand growth and disciplined OPEC+ supply management.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1004, title: "OPEC Basket Price Holds Above $74 Amid Production Cut Extensions", excerpt: "The reference basket used by OPEC member nations remains elevated as voluntary cuts of 2.2M bpd persist through Q3.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1005, title: "Dubai Crude Fetches Premium as Asian Refiners Compete for Sour Barrels", excerpt: "The Dubai benchmark has firmed on strong buying from Indian and Chinese refiners seeking Middle Eastern grades.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
    ],
    stats: [
      { label: "WTI Crude", value: "$70.44", sub: "+2.80%" },
      { label: "Brent Crude", value: "$74.16", sub: "+3.01%" },
      { label: "OPEC Basket", value: "$73.80", sub: "+2.93%" },
    ]
  },
  "oil-futures": {
    articles: [
      { id: 1600, title: "Oil Futures vs Spot Prices: What's the Difference?", excerpt: "Spot price is oil for immediate delivery; futures is oil for later. Why the two diverge, how contango and backwardation work, and which one the news actually quotes.", date: "Apr 18, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1101, title: "WTI Futures Curve Flips to Backwardation Through December 2026", excerpt: "Front-month contracts now trade at a premium to deferred months, signaling near-term supply tightness.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1102, title: "Brent Futures Open Interest Hits 3-Month High Ahead of OPEC Meeting", excerpt: "Speculative positioning in Brent crude futures has surged as traders anticipate policy signals from Vienna.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1103, title: "Options Market Pricing Elevated Volatility Through Summer 2026", excerpt: "Implied volatility on WTI calls has risen 18% as geopolitical risk and demand uncertainty drive hedging activity.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1104, title: "Managed Money Net Longs in Crude Futures Rise for Fourth Straight Week", excerpt: "CFTC data shows hedge funds increasing bullish bets on oil as macro headwinds appear to be easing.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
    ],
    stats: [
      { label: "WTI Front Month", value: "$70.44", sub: "Aug 2026" },
      { label: "Brent Front Month", value: "$74.16", sub: "Sep 2026" },
      { label: "Curve Shape", value: "Backwardation", sub: "-$3.40 to Dec-26" },
    ]
  },
  "rig-count": {
    articles: [
      { id: 1201, title: "U.S. Rig Count Falls to 584, Down 5 From Prior Week", excerpt: "Baker Hughes data shows continued drilling pullback as operators prioritize capital discipline over volume growth.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "3 min" },
      { id: 1202, title: "Permian Basin Rigs Hold Steady at 302 Despite Overall U.S. Decline", excerpt: "The nation's most prolific basin continues to attract investment even as secondary plays see rig reductions.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1203, title: "Canadian Rig Count Rebounds to 118 as Spring Drilling Season Begins", excerpt: "Freeze-thaw cycle restrictions are easing across Alberta and Saskatchewan, allowing crews to mobilize.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1204, title: "International Rig Count Stable at 958 as Middle East Activity Rises", excerpt: "Saudi Arabia and UAE are adding rigs to maintain production capacity even as OPEC+ quotas limit output.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
    ],
    stats: [
      { label: "U.S. Total", value: "565", sub: "+2 w/w" },
      { label: "U.S. Oil Rigs", value: "433", sub: "+2 w/w" },
      { label: "Canada Total", value: "169", sub: "+7 w/w" },
    ]
  },
  "energy": {
    articles: [
      { id: 1301, title: "Global Energy Demand Growth Slows to 1.2% in 2026, IEA Reports", excerpt: "The International Energy Agency's latest monthly report shows moderating consumption growth driven by Chinese economic headwinds and efficiency gains.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1302, title: "U.S. Power Grid Faces Record Summer Demand From Data Center Expansion", excerpt: "AI-driven data center buildouts are straining electricity infrastructure across Texas, Virginia, and the Southwest.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1303, title: "European Energy Security Improves as LNG Import Capacity Doubles Since 2022", excerpt: "New regasification terminals in Germany, Italy, and Greece have significantly reduced Europe's vulnerability to supply shocks.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1304, title: "India's Energy Consumption Surpasses Japan for First Time", excerpt: "Rapid industrialization and a growing middle class push India past Japan as the world's fourth-largest energy consumer.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1305, title: "Carbon Capture Investment Reaches $12B Globally in 2025", excerpt: "Direct air capture and point-source CCS projects are scaling up as government subsidies and carbon pricing incentivize deployment.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
    ],
    stats: [
      { label: "Global Demand", value: "~103M", sub: "bpd (oil equiv.)" },
      { label: "U.S. Production", value: "13.6M", sub: "bpd crude" },
      { label: "LNG Exports", value: "17 Bcf/d", sub: "U.S. 2026 fcst (EIA)" },
    ]
  },
  "crude-oil": {
    articles: [
      { id: 1404, title: "OPEC+ Approves July Quota Increase of 188,000 BPD Despite Persistent Supply Risks", excerpt: "OPEC+ added modest barrels into a market where ~10.5M bpd of Persian Gulf production remains shut in. Chinese crude imports pulled back aggressively as the top importer leans on inventories.", date: "June 9, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1401, title: "Permian Basin Production Hits Record 6.2 Million Barrels Per Day", excerpt: "Improved well productivity and extended lateral lengths continue to push U.S. shale output higher despite a falling rig count.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1402, title: "Guyana's Stabroek Block Delivers New 1.5 Billion Barrel Discovery", excerpt: "ExxonMobil's latest exploration well adds to what is already one of the most significant deepwater oil provinces found this century.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1403, title: "OPEC+ Compliance Reaches 116% as Iraq Over-Produces Again", excerpt: "Baghdad's output consistently exceeds its agreed ceiling, creating tension within the alliance and complicating quota negotiations.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1404, title: "North Sea Forties Pipeline Restart Eases Brent Supply Concerns", excerpt: "The 450,000 bpd system returns to full capacity after a 10-day maintenance shutdown that briefly tightened dated Brent.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
    ],
    stats: [
      { label: "U.S. Production", value: "13.6M", sub: "bpd" },
      { label: "Gulf Shut-In", value: "~10.5M", sub: "bpd (EIA est.)" },
      { label: "Global Supply", value: "~95M", sub: "bpd (disrupted)" },
    ]
  },
  "gas-prices": {
    articles: [
      { id: 1512, title: "AAA National Average Slips to $3.790 as July 4th Travelers Get Relief", excerpt: "AAA\u2019s national average slipped to $3.790 as crude trades near four-month lows. Indiana is cheapest at $3.06, Oklahoma $3.32, Texas $3.32; California ($5.37) and Hawaii ($5.46) remain highest. Today\u2019s security-driven oil spike is a risk to further relief.", date: "July 7, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1502, title: "AAA National Average Slips to $3.867 as Pump Relief Broadens", excerpt: "AAA\u2019s national average slipped to $3.867 as crude trades at pre-war lows and Gulf supply returns. Indiana is cheapest at $3.23, Texas $3.31, Oklahoma $3.38; California ($5.46) and Washington ($5.20) remain highest. More relief is likely as the crude collapse reaches the pump.", date: "June 28, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1492, title: "AAA National Average Eases to $3.928; Diesel Slips Back Below $5", excerpt: "AAA\u2019s national average eased to $3.928 as crude trades at pre-war lows, and diesel slipped below $5 to $4.980. Indiana is cheapest at $3.33, Texas $3.38, Oklahoma $3.43; California ($5.54) and Washington ($5.30) remain highest. More relief is likely as the crude collapse reaches the pump.", date: "June 24, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1482, title: "AAA National Average Slides to $3.938 as Summer Travel Heats Up", excerpt: "AAA\u2019s national average fell to $3.938, holding below $4 as crude trades near multi-month lows. Diesel eased to $5.040. Indiana is cheapest at $3.34, Oklahoma and Texas near $3.44; California ($5.58) and Washington ($5.36) remain highest.", date: "June 22, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1472, title: "AAA National Average Falls Below $4 for the First Time Since the War to $3.999", excerpt: "AAA\u2019s national average fell to $3.999 Thursday, below $4 for the first time since the war began, as crude tumbles on the peace deal. Diesel eased to $5.129. More relief is likely as the Strait of Hormuz reopens.", date: "June 18, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1462, title: "What a Signed Deal Would Mean for Gas Prices: A 30-Day Hormuz Reopening and the Pump Lag", excerpt: "Both draft texts commit to reopening the Strait of Hormuz within 30 days of a final deal. With pump prices lagging crude by one to two weeks, a confirmed signing would extend the decline well into summer. AAA national holds at $4.108.", date: "June 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1452, title: "AAA National Average Falls to $4.108 as Pump Prices Drop for a Third Straight Week", excerpt: "AAA\u2019s national average fell to $4.108 Friday, a third consecutive weekly decline as crude slides on U.S.-Iran peace-deal optimism. Diesel eased to $5.259. A signed deal reopening Hormuz would accelerate the relief into summer.", date: "June 12, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1403, title: "AAA National Average Falls to $4.161 \u2014 Down Nearly 20 Cents in a Week \u2014 as EIA Maps the Fuel-Price Peak", excerpt: "AAA\u2019s national average fell to $4.161 Tuesday, down nearly 20 cents in one week per the motor club, as May\u2019s crude slide works through the pump lag. The EIA\u2019s June outlook sees the largest fuel-price impacts of the conflict landing this quarter.", date: "June 9, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1400, title: "Why Are Gas Prices Different in Every State?", excerpt: "State fuel taxes, refinery proximity, unique fuel blends, and local competition together explain the $2+ gap between the cheapest and most expensive states.", date: "Apr 18, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1401, title: "Cheapest Gas Prices Right Now \u2014 State Rankings", excerpt: "Oklahoma, Mississippi, Texas, Louisiana, and Alabama anchor the bottom of the AAA rankings. Why these states are consistently cheapest, plus the 10 most expensive.", date: "Apr 18, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1200, title: "How Are Gas Prices Set? From Crude Oil to the Pump", excerpt: "The full chain that builds up the pump price: crude oil, refining, distribution, and taxes. Why prices vary by state and season, in plain English.", date: "Apr 18, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1501, title: "U.S. Average Gas Price Rises to $3.42/Gallon Ahead of Spring Driving Season", excerpt: "AAA reports retail gasoline prices are up 12 cents from a month ago as refiners switch to costlier summer-blend formulations.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "3 min" },
      { id: 1502, title: "California Gas Prices Hit $5.18 as State-Specific Regulations Add Costs", excerpt: "The Golden State's unique fuel standards and carbon pricing continue to push pump prices well above the national average.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1503, title: "Gulf Coast Refinery Margins Improve as Crack Spreads Widen", excerpt: "The 3-2-1 crack spread has expanded to $28/barrel, incentivizing higher refinery utilization rates.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1504, title: "EIA: U.S. Summer Gasoline Demand Expected to Average 9.1M BPD", excerpt: "The Energy Information Administration forecasts steady consumption growth despite elevated prices and rising EV adoption.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
    ],
    stats: [
      { label: "U.S. National Avg", value: "$3.790", sub: "/gallon (AAA 7/7)" },
      { label: "RBOB Futures", value: "$2.36", sub: "/gallon" },
      { label: "Crack Spread", value: "$30.60", sub: "3-2-1" },
    ]
  },
  "natural-gas": {
    articles: [
      { id: 1601, title: "Henry Hub Falls Below $3.50 as U.S. Storage Surplus Persists", excerpt: "Above-average inventories and record production continue to weigh on domestic natural gas prices despite rising export demand.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1602, title: "European TTF Gas Rallies 12% on Extended Cold Weather Forecast", excerpt: "A late-season cold snap across Northern Europe is drawing down storage reserves faster than seasonal norms.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1603, title: "U.S. LNG Exports Hit Record 14 Bcf/d as Golden Pass Begins Operations", excerpt: "The new Qatar-Exxon joint venture facility in Texas adds 2.5 Bcf/d of liquefaction capacity to the Gulf Coast.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1604, title: "Japan LNG Spot Price Drops to $12.40/MMBtu on Mild Asian Demand", excerpt: "Warmer-than-normal temperatures across Northeast Asia reduce heating gas requirements heading into spring.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
    ],
    stats: [
      { label: "Henry Hub", value: "$3.46", sub: "/MMBtu" },
      { label: "TTF Dutch", value: "€52.40", sub: "/MWh" },
      { label: "JKM LNG", value: "$27.80", sub: "/MMBtu" },
    ]
  },
  "heating-oil": {
    articles: [
      { id: 1701, title: "Heating Oil Futures Ease as Winter Demand Season Winds Down", excerpt: "NYMEX heating oil contracts slip as warmer spring temperatures reduce residential heating demand across the Northeast.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "3 min" },
      { id: 1702, title: "Northeast Home Heating Costs Rose 8% This Winter vs. Last Year", excerpt: "The EIA's Winter Fuels Outlook post-mortem shows higher crude prices and cold January temps drove seasonal cost increases.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1703, title: "Diesel and Heating Oil Margins Diverge as Trucking Demand Holds", excerpt: "While residential heating demand fades, strong freight activity keeps middle distillate markets well-supported.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1704, title: "European Diesel Imports From Asia Rise as Arbitrage Window Opens", excerpt: "A widening East-West price differential is pulling Asian diesel cargoes toward Europe for the first time since January.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
    ],
    stats: [
      { label: "Heating Oil", value: "$3.18", sub: "/gal futures" },
      { label: "Diesel (retail)", value: "$5.34", sub: "/gal AAA" },
      { label: "Distillate Stock", value: "118M", sub: "barrels" },
    ]
  },
  "geopolitics": {
    articles: [
      { id: 1510, title: "Iran Strikes Qatari LNG Tanker Near Hormuz as U.S. Revokes Oil-Sale License", excerpt: "Iran attacked the Qatari LNG tanker Al-Rekayyat near the Strait of Hormuz and a second vessel was struck by a projectile, sending oil sharply higher. The U.S. revoked Iran\u2019s oil-sale license; Brent settled at $74.16 and jumped further after hours.", date: "July 7, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1500, title: "Hormuz Transits Surge as Gulf Exports Recover to ~75% of Pre-War Levels", excerpt: "The reopening of the Strait of Hormuz is now visibly underway: shipping transits have accelerated, restoring Persian Gulf exports to roughly 75% of pre-war levels. Saudi Arabia began loading tankers at Ras Tanura, and the UAE, Kuwait, and Qatar are boosting supply \u2014 constrained mainly by tanker availability rather than the conflict.", date: "June 28, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1491, title: "Hormuz Baffles Markets: Half-Open, Half-Closed After Iran\u2019s Renewed Closure Signal", excerpt: "Confusion over the Strait of Hormuz persists as Iran and the U.S. issue conflicting statements. Windward said transits fell to 12 Sunday from 21 Saturday after Tehran\u2019s renewed closure signal, with traffic dark and sanctioned. Insurers still treat the region as a war zone even as the IEA estimates the UAE is exporting at ~85% of pre-war levels.", date: "June 24, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1480, title: "Geneva Signing Ceremony Postponed; U.S. and Iran Turn to a 60-Day Roadmap", excerpt: "The formal Geneva ceremony set for June 19 was abruptly called off; Switzerland said the B\u00FCrgenstock talks would not proceed and Vance no longer traveled. Mediators Qatar and Pakistan said the sides agreed on a roadmap to a final deal within 60 days. The interim deal that took effect June 18 remains in force, but Trump has threatened renewed strikes.", date: "June 22, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1470, title: "U.S. and Iran Sign Peace Deal; Interim Agreement Takes Effect, Ending the War", excerpt: "The interim accord took effect June 18, ending the three-month war. Trump and Pezeshkian signed the MOU electronically June 15; Trump signed at the G7 in France, with a Geneva ceremony set for June 19. Iran agreed to forgo nuclear weapons and dilute enriched uranium; the U.S. agreed to release $25 billion in frozen assets.", date: "June 18, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1460, title: "Pakistan Says U.S. and Iran Reach a Final Text \u2014 the Islamabad Declaration", excerpt: "PM Sharif said the two sides reached a final, agreed-upon text, with electronic signing likely within 24 hours and a Geneva ceremony to follow. But Iran\u2019s team called the Sunday-Geneva claim \u201Ccompletely false,\u201D and Trump and Vance disputed leaked details. No text is confirmed signed by both sides.", date: "June 13, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1450, title: "U.S. and Iran Near a Peace Deal; Trump Says It Could Be Signed This Weekend in Europe", excerpt: "The U.S. and Iran moved to the brink of a peace agreement Friday. Trump said a deal could be signed as soon as this weekend in Europe; a senior official said Washington is 85% confident. Iran\u2019s Mehr published a 14-point draft, though the U.S. version diverges and no final text is approved.", date: "June 12, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1401, title: "Iran and Israel Agree to Halt Attacks After Weekend Exchange; Trump Says New Ceasefire Is Close", excerpt: "Iran and Israel agreed Tuesday to halt attacks against each other after a weekend exchange of strikes threatened the fragile ceasefire. Iran ended its military operations Monday; Israel signaled it would hold fire. Trump says both are close to a new ceasefire \u2014 though Iran warns operations resume if Israel continues in Lebanon.", date: "June 9, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1400, title: "Israel Strikes Hezbollah Targets in Southern Beirut, Imperiling U.S.-Iran Talks", excerpt: "Israeli forces struck Hezbollah targets in southern Beirut Sunday in response to missiles fired into northern Israel. The IRGC had warned it would strike Israel and could halt U.S. negotiations if Beirut were hit \u2014 the trigger for the weekend\u2019s exchange that ended in Tuesday\u2019s mutual halt.", date: "June 7, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1397, title: "Trump-Xi Summit in Beijing: Both Sides Agree Strait of Hormuz Must Remain Open", excerpt: "President Trump and President Xi held a two-day summit in Beijing concluding Thursday May 14. The White House readout said both leaders agreed Hormuz must remain open and that Iran cannot have a nuclear weapon. Trump told Fox News Xi offered to help broker peace. Xi opposed militarization of the strait and any effort to charge a toll, and expressed interest in purchasing more American oil.", date: "May 15, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1398, title: "Trump Warns Iran to Reach a Deal or Face 'Annihilation'", excerpt: "Speaking after the Beijing summit, President Trump warned Iran to reach a deal or face annihilation, saying his patience with Tehran was running out. The administration has reportedly proposed a 20-year verified moratorium on Iran's nuclear program, surrender of all highly enriched uranium, and free commercial traffic through Hormuz as conditions to end hostilities. Pakistan has been acting as an intermediary.", date: "May 15, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1392, title: "IEA: Global Oil Inventories Drawing at Record 4M bpd Pace; Severe Undersupply Through October", excerpt: "The International Energy Agency warned Wednesday May 13 that global observed oil inventories fell at a record pace of around 4 million barrels per day in March and April. The market could remain severely undersupplied until October even if the conflict ends sooner. Middle East tensions continue to disrupt flows, with Asian refiners seeking Persian Gulf alternatives.", date: "May 13, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1393, title: "EIA Crude Stocks Drop 4.3M Barrels — Nearly Double Expectations", excerpt: "The Energy Information Administration's Weekly Petroleum Status Report Wednesday showed U.S. commercial crude oil inventories fell by 4.3 million barrels last week — nearly double consensus expectations of a 2.2 million barrel draw. Distillate inventories rose by 190,000 barrels, the first weekly increase since March.", date: "May 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1394, title: "UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", excerpt: "The EIA's May Short-Term Energy Outlook released Tuesday incorporates the UAE's departure from OPEC, effective May 1, 2026. OPEC production numbers in the outlook now exclude UAE data. EIA now expects OPEC's spare capacity to average 2.5 million bpd in 2027, compared with a previous forecast of 3.8 million bpd. The structural shift reduces producer-group response capability.", date: "May 13, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1395, title: "Iranian Oil Export Shipments Stall — First Sustained Interruption Since Conflict Began", excerpt: "Reports Wednesday May 13 indicated Iranian oil export shipments have recently stalled, marking the first sustained interruption since the conflict started February 28. Iranian crude has been one of the few continuing supply paths from the Persian Gulf despite the broader Hormuz disruption.", date: "May 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1388, title: "WTI Tops $102, Brent $108 as Hormuz Stalemate Deepens", excerpt: "WTI June futures advanced 4.2% Tuesday to settle at $102.18; Brent July futures gained 3.4% to $107.77. Both benchmarks are now up more than 45% since the U.S.-Israeli war against Iran began February 28. Citi: 'Oil prices have been volatile and can rise further if US-Iran dealmaking remains thorny.' Implied volatility climbed; Kalshi odds of WTI reaching $127 in 2026 moved above 70%.", date: "May 12, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1389, title: "Hochstein: 'Frozen Conflict, No War, No Oil, No Straits'; Sees $90-100 Through 2027", excerpt: "Amos Hochstein, former senior energy advisor to President Biden, told CNBC's 'Squawk Box' Tuesday: 'We're in a stalemate, a frozen conflict. In the meantime, the straits are closed so we're in a no war, no oil, no straits condition.' He expects oil to remain in a $90-100 range through 2026 and into 2027 even if Hormuz reopens in early June. A breakthrough this week is unlikely as Trump heads to China.", date: "May 12, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1390, title: "Trump Heads to Beijing This Week; Set to Press Xi to Lean on Iran", excerpt: "President Trump is scheduled to travel to Beijing later this week to meet with President Xi Jinping. Trump may ask Xi to press Iran to accept U.S. terms during their talks, according to Henry Wilkinson of Dragonfly. China has called for the Strait of Hormuz to reopen given how much of its energy supply transits the waterway. The visit functions as a hard deadline.", date: "May 12, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1391, title: "Trump Rejects Iran's Counterproposal as 'Totally Unacceptable'; Threatens to Resume Bombing", excerpt: "President Trump on Sunday May 10 publicly rejected Iran's counterproposal to end the 10-week war via Truth Social. Iran's counter, delivered through Pakistan, demanded the U.S. lift OFAC sanctions on Iranian oil sales for 30 days and end the naval blockade. Trump threatened: 'If they don't agree, the bombing starts.' Iran vowed to 'never bow.'", date: "May 11, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1392, title: "Oil Rallies 5% as Hormuz Deal Collapses; WTI $100, Brent $106", excerpt: "Crude futures surged Monday May 11 after Trump's Sunday rejection of Iran's counterproposal. WTI June futures advanced 4.96% to $100.30 per barrel; Brent July futures gained 4.92% to $105.76. The rally undoes last week's relief move and re-embeds the geopolitical risk premium. Trump said the ceasefire is on 'massive life support… 1% chance of living.'", date: "May 11, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1393, title: "Drones Strike Qatari Waters; UAE and Kuwait Intercept Iranian Drones", excerpt: "Multiple Gulf states reported drone attacks over the weekend. A drone struck a ship in Qatari waters Sunday May 10. The UAE intercepted two drones and openly blamed Tehran. Kuwait separately intercepted hostile drones. Qatar's Foreign Ministry called the strike 'a dangerous and unacceptable escalation.' Qatar serves as a mediator in the conflict alongside Pakistan.", date: "May 11, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1394, title: "Aramco CEO: Hormuz Normalization Could Slip Into 2027 as 100M Barrels Lost Weekly", excerpt: "Saudi Aramco CEO Amin Nasser warned on a Monday May 11 analyst call that the market is losing roughly 100 million barrels of supply each week and that if reopening of the Strait of Hormuz is 'delayed by a few more weeks, then normalization will last into 2027.' The IEA has called this the largest supply shock on record.", date: "May 11, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1395, title: "U.S. Awaits Iran Response to 14-Point Memorandum to End Hormuz War", excerpt: "U.S. officials told Axios this week the U.S. and Iran are close to a 14-point memorandum of understanding that would end the war and reopen the Strait of Hormuz. Iran would commit to a uranium enrichment moratorium; the U.S. would lift sanctions and release frozen funds. Sec. of State Rubio said Friday he expected Iran's formal response that day; reports indicate it will travel through Pakistan within two days.", date: "May 8, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1396, title: "Oil Crashes 13% Intraday as U.S.-Iran MOU Talks Emerge", excerpt: "WTI crude crashed as much as 13.2% intraday Tuesday May 5 to a low of $88.71 — the first time below $90 since April 21. Brent plummeted as much as 12% to a low of $96.77. The crash came on news that the U.S. and Iran were close to a one-page, 14-point memorandum of understanding. Trump paused Project Freedom shipping operations to allow space for the deal.", date: "May 5, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1397, title: "U.S. Navy Disables Two Iranian Tankers; Trump Calls Strike a 'Love Tap'", excerpt: "U.S. forces fired Friday May 8 on two empty Iranian oil tankers — M/T Sea Star III and M/T Sevda — that attempted to evade the naval blockade. CENTCOM said a Navy warplane fired into the smokestacks and disabled both vessels. President Trump told ABC News the strikes were 'just a love tap' and insisted the ceasefire remains in effect.", date: "May 8, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1398, title: "AAA Gas Average Hits $4.55, Up 25 Cents for Second Straight Week", excerpt: "AAA reported the U.S. national average for regular gasoline reached $4.546 per gallon Friday May 8 — up 25 cents from a week earlier and from $4.05 two weeks ago. Pump prices are now $1.40 higher than a year ago and at their highest level since 2022. Despite crude pulling back below $100, retail prices continue to climb on multi-day pass-through lag.", date: "May 8, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1399, title: "Iran's Mohsen Rezaei Demands U.S. Reparations Before Any Deal", excerpt: "Mohsen Rezaei, member of Iran's Expediency Council, said via state news agency PressTV that the U.S. must pay reparations for damage done to Iran before any settlement. Tehran said it will not allow the U.S. to dictate terms unilaterally. The hardline framing complicates the 14-point memorandum even as Iranian negotiators continue Pakistan-mediated talks.", date: "May 7, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
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
      { id: 1413, title: "Israeli Strikes Kill Lebanese Journalist Amal Khalil During Extended Ceasefire", excerpt: "Lebanese journalist Amal Khalil was killed in an Israeli strike on April 22, sharply straining the extended Israel-Lebanon ceasefire. Multiple new strikes followed, killing six on Saturday despite the truce extension.", date: "Apr 23, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1500, title: "U.S.-Iran Ceasefire Explained: Timeline, Terms, and Extension", excerpt: "The Pakistan-mediated U.S.-Iran ceasefire: what it covers, what it doesn\u0027t, Trump\u0027s April 21 indefinite extension, and what markets expect next.", date: "Apr 21, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1300, title: "What Happens If the Strait of Hormuz Closes?", excerpt: "Hour-by-hour and week-by-week scenario analysis: oil prices, gasoline, shipping, and the countries most exposed if the world\u0027s most important chokepoint shuts.", date: "Apr 18, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1301, title: "What Is OPEC+ and How Does It Affect Oil Prices?", excerpt: "The 23-nation producer alliance that controls roughly 40% of global oil output. Who\u0027s in it, how it sets quotas, and why its decisions move prices within minutes.", date: "Apr 18, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1801, title: "Islamabad Talks Collapse After 21-Hour Marathon — No Deal Reached Between U.S. and Iran", excerpt: "The highest-level U.S.-Iran negotiations since 1979 ended without agreement. Vance blamed Iran for refusing nuclear commitments. Trump announces full naval blockade of Hormuz.", date: "Apr 17, 2026", author: "EnergyPricesToday Editorial", readTime: "8 min" },
      { id: 1802, title: "Trump Announces Full Naval Blockade of Strait of Hormuz", excerpt: "Following failed Islamabad talks, President Trump orders U.S. Navy to blockade the strait and interdict all vessels that paid transit tolls to Iran.", date: "Apr 17, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1803, title: "Ceasefire Expires April 22 With No Extension in Sight", excerpt: "The two-week truce brokered by Pakistan runs out in 10 days. Without a deal, the conflict could resume with even greater intensity.", date: "Apr 17, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1804, title: "Iran Nuclear Program Remains Central Sticking Point in U.S. Negotiations", excerpt: "Tehran refuses to commit to ending uranium enrichment — Washington calls it the core requirement for any deal.", date: "Apr 17, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1805, title: "Israel Struck 200+ Hezbollah Targets During Islamabad Peace Talks", excerpt: "Military operations in Lebanon continued unabated even as diplomats negotiated in Pakistan, complicating ceasefire prospects.", date: "Apr 17, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1806, title: "Pakistan Urges Continued Diplomacy After U.S.-Iran Talks End Without Deal", excerpt: "PM Sharif calls on both sides to uphold ceasefire commitments while keeping diplomatic channels open.", date: "Apr 17, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 1807, title: "Oil Markets Face Renewed Volatility as Islamabad Talks Fail", excerpt: "Crude prices expected to surge when markets open Monday as geopolitical risk premium rebuilds after diplomatic breakdown.", date: "Apr 17, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1808, title: "Strait of Hormuz: From Iranian Blockade to U.S. Naval Blockade", excerpt: "The world's most critical oil chokepoint faces competing closure threats from both sides of the conflict.", date: "Apr 17, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1809, title: "Israel-Lebanon Direct Negotiations Set for Tuesday in Washington", excerpt: "First official talks between the two countries in decades aim to address Hezbollah disarmament and border security.", date: "Apr 17, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1810, title: "Global Energy Crisis Deepens as Diplomatic Off-Ramp Narrows", excerpt: "IEA warns current crisis could exceed 1970s oil shocks. European gas prices remain elevated. U.S. consumers face $4+ gas.", date: "Apr 17, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
    ],
    stats: []
  },
  "company-news": {
    articles: [
      { id: 1900, title: "Saudi Aramco East-West Pipeline Continues at Full Capacity Through Blockade", excerpt: "Aramco's 5M bpd Hormuz bypass remains the global oil market's most critical piece of working infrastructure as the dual blockade enters its third month.", date: "Apr 24, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1901, title: "Energy Stocks Mixed as Ceasefire Extension Eases but Blockade Stays", excerpt: "Integrated majors traded mixed on the day of the ceasefire extension. Refiners held a more stable bid with crack spreads supported. LNG names benefited from continued Qatari disruption.", date: "Apr 22, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1902, title: "Maersk, Hapag-Lloyd Maintain Hormuz Transit Suspension Amid Continued Uncertainty", excerpt: "Both carriers cited continued threats to commercial shipping. Vessels continue routing around the Cape of Good Hope, adding 10-14 days per voyage and effectively reducing global container capacity.", date: "Apr 25, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 1903, title: "Cheniere Energy, Venture Global Ride LNG Premium as Qatar Flows Still Disrupted", excerpt: "U.S. LNG terminals operating near 14 Bcf/d combined export capacity. European buyers returning to premium bidding for U.S. cargoes. JKM trading premium to TTF for first time since early 2025.", date: "Apr 23, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 1904, title: "ExxonMobil Q1 Earnings Preview: Hormuz Disruption Hits Trading Timing", excerpt: "ExxonMobil's April 8 Q1 considerations supplement flagged $3.5-4.9B in negative timing effects from the Middle East conflict. Earnings call scheduled for April 30 will detail the full impact.", date: "Apr 22, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 1905, title: "OPEC+ April Output Increase Proceeding Despite Market Volatility", excerpt: "206,000 bpd April increase on schedule. Saudi Arabia holding current production. No emergency JMMC meeting called following ceasefire extension.", date: "Apr 22, 2026", author: "EnergyPricesToday Editorial", readTime: "8 min" },
    ],
    stats: []
  },
  "alternative-energy": {
    articles: [
      { id: 2001, title: "Global Renewable Investment Hits $1.8 Trillion in 2025, IRENA Reports", excerpt: "Solar, wind, and battery storage captured 80% of new power generation investment worldwide for the first time.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 2002, title: "Green Hydrogen Costs Fall 40% Since 2022 as Electrolyzer Scale Grows", excerpt: "Projects in Saudi Arabia, Australia, and Chile are proving that sub-$3/kg green hydrogen is achievable at scale.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 2003, title: "Battery Storage Deployments Triple Year-Over-Year in the U.S.", excerpt: "Grid-scale lithium-ion installations reached 18 GW in 2025 as utilities pair storage with solar to meet peak demand.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 2004, title: "EU Carbon Price Stabilizes at €85/Tonne, Supporting Clean Energy Economics", excerpt: "The Emissions Trading System continues to make fossil fuel power generation more expensive relative to renewables.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
    ],
    stats: [
      { label: "Renewable CapEx", value: "$1.8T", sub: "2025 global" },
      { label: "Solar Cost", value: "$24", sub: "/MWh avg" },
      { label: "EV Sales Share", value: "22%", sub: "global 2025" },
    ]
  },
  "nuclear": {
    articles: [
      { id: 2101, title: "NuScale Small Modular Reactor Receives Full NRC Design Certification", excerpt: "The 77 MWe module becomes the first SMR to complete the U.S. regulatory approval process, clearing the path for commercial deployment.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 2102, title: "France Commits €10B to Build Six New EPR2 Reactors by 2040", excerpt: "President Macron's nuclear renaissance plan aims to replace aging reactors while supporting European energy independence.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 2103, title: "Uranium Spot Price Surges to $92/lb as Utility Contracting Accelerates", excerpt: "After a decade of low prices, uranium has rallied 180% since 2023 on renewed nuclear ambitions from the U.S., China, and India.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 2104, title: "Microsoft Signs 20-Year Nuclear Power Purchase Agreement for Data Centers", excerpt: "The tech giant secures carbon-free baseload power from Constellation Energy's reactor fleet to support AI computing growth.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
    ],
    stats: [
      { label: "Uranium Price", value: "$92", sub: "/lb U₃O₈" },
      { label: "Global Reactors", value: "440", sub: "operational" },
      { label: "Under Constr.", value: "62", sub: "reactors" },
    ]
  },
  "solar": {
    articles: [
      { id: 2201, title: "Global Solar Installations Reach Record 420 GW in 2025", excerpt: "China alone accounted for 230 GW of new solar capacity as module prices fell below $0.10/watt for the first time.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 2202, title: "U.S. Utility-Scale Solar Pipeline Exceeds 300 GW as IRA Credits Flow", excerpt: "The Inflation Reduction Act's tax credits continue to drive a massive buildout of solar farms across the Sun Belt states.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 2203, title: "Perovskite-Silicon Tandem Cells Hit 33.9% Efficiency Record", excerpt: "Oxford PV's commercial-ready tandem cells promise to push rooftop solar economics further into mainstream territory.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 2204, title: "India's Solar Tariffs Drop to Record Low $0.029/kWh in Rajasthan Auction", excerpt: "The world's cheapest solar electricity bid underscores India's aggressive renewable deployment targets.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
    ],
    stats: [
      { label: "2025 Installed", value: "420 GW", sub: "global" },
      { label: "Module Price", value: "$0.09", sub: "/watt" },
      { label: "LCOE", value: "$24", sub: "/MWh avg" },
    ]
  },
  "wind": {
    articles: [
      { id: 2301, title: "Offshore Wind Capacity Surpasses 80 GW Globally as Costs Stabilize", excerpt: "After a period of cost inflation driven by supply chain bottlenecks, offshore wind developers report stabilizing turbine and installation costs.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
      { id: 2302, title: "Vineyard Wind Achieves Full 800 MW Output Off Massachusetts Coast", excerpt: "America's first utility-scale offshore wind farm is now operating at rated capacity, powering 400,000 homes.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 2303, title: "Vestas Unveils 17 MW Offshore Turbine, World's Most Powerful", excerpt: "The V236-17.0 MW platform can generate enough electricity for 20,000 households from a single installation.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
      { id: 2304, title: "Texas Wind Generation Sets New Record at 35 GW During March Storm", excerpt: "ERCOT's wind fleet produced more power than natural gas for a 48-hour period during sustained high wind conditions.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
    ],
    stats: [
      { label: "Offshore Global", value: "80 GW", sub: "installed" },
      { label: "U.S. Onshore", value: "155 GW", sub: "installed" },
      { label: "Largest Turbine", value: "17 MW", sub: "Vestas" },
    ]
  },
  "renewable-energy": {
    articles: [
      { id: 2401, title: "Renewables Provided 35% of Global Electricity in 2025, IEA Confirms", excerpt: "Wind, solar, hydro, and biomass generation surpassed coal for the first time on an annual basis worldwide.", date: "Apr 16, 2026", author: "EnergyPricesToday Editorial", readTime: "7 min" },
      { id: 2402, title: "Grid-Scale Battery Storage Hits 100 GW Global Milestone", excerpt: "Lithium-ion dominates the market but sodium-ion and iron-air chemistries are gaining ground for long-duration applications.", date: "Apr 15, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 2403, title: "Green Hydrogen Electrolyzer Orders Surge 300% in 2025", excerpt: "European and Middle Eastern projects drive demand for gigawatt-scale electrolysis systems from manufacturers like Plug Power and Nel.", date: "Apr 14, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
      { id: 2404, title: "U.S. Clean Energy Jobs Surpass 4 Million for First Time", excerpt: "Solar installation, EV manufacturing, and battery production drive employment growth outpacing fossil fuel sector hiring.", date: "Apr 13, 2026", author: "EnergyPricesToday Editorial", readTime: "4 min" },
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
  { state:"Alabama", abbr:"AL", regular:3.442, mid:3.925, premium:4.321, diesel:4.463 },
  { state:"Alaska", abbr:"AK", regular:4.735, mid:4.964, premium:5.199, diesel:5.264 },
  { state:"Arizona", abbr:"AZ", regular:3.917, mid:4.268, premium:4.594, diesel:4.875 },
  { state:"Arkansas", abbr:"AR", regular:3.425, mid:3.904, premium:4.285, diesel:4.305 },
  { state:"California", abbr:"CA", regular:5.371, mid:5.596, premium:5.797, diesel:6.473 },
  { state:"Colorado", abbr:"CO", regular:3.656, mid:4.043, premium:4.379, diesel:4.207 },
  { state:"Connecticut", abbr:"CT", regular:3.9, mid:4.506, premium:4.907, diesel:5.18 },
  { state:"Delaware", abbr:"DE", regular:3.638, mid:4.257, premium:4.541, diesel:4.697 },
  { state:"District of Columbia", abbr:"DC", regular:4.062, mid:4.689, premium:5.146, diesel:5.539 },
  { state:"Florida", abbr:"FL", regular:3.725, mid:4.19, premium:4.522, diesel:4.456 },
  { state:"Georgia", abbr:"GA", regular:3.548, mid:4.019, premium:4.44, diesel:4.612 },
  { state:"Hawaii", abbr:"HI", regular:5.464, mid:5.705, premium:5.953, diesel:6.955 },
  { state:"Idaho", abbr:"ID", regular:4.013, mid:4.317, premium:4.604, diesel:4.611 },
  { state:"Illinois", abbr:"IL", regular:3.975, mid:4.547, premium:5.07, diesel:4.902 },
  { state:"Indiana", abbr:"IN", regular:3.058, mid:3.637, premium:4.159, diesel:4.916 },
  { state:"Iowa", abbr:"IA", regular:3.492, mid:3.769, premium:4.35, diesel:4.318 },
  { state:"Kansas", abbr:"KS", regular:3.464, mid:3.822, premium:4.173, diesel:4.242 },
  { state:"Kentucky", abbr:"KY", regular:3.384, mid:3.914, premium:4.351, diesel:4.471 },
  { state:"Louisiana", abbr:"LA", regular:3.428, mid:3.877, premium:4.28, diesel:4.345 },
  { state:"Maine", abbr:"ME", regular:3.848, mid:4.407, premium:4.898, diesel:5.209 },
  { state:"Maryland", abbr:"MD", regular:3.698, mid:4.31, premium:4.61, diesel:4.733 },
  { state:"Massachusetts", abbr:"MA", regular:3.869, mid:4.512, premium:4.908, diesel:5.15 },
  { state:"Michigan", abbr:"MI", regular:3.913, mid:4.537, premium:5.136, diesel:4.939 },
  { state:"Minnesota", abbr:"MN", regular:3.589, mid:4.036, premium:4.525, diesel:4.536 },
  { state:"Mississippi", abbr:"MS", regular:3.424, mid:3.897, premium:4.274, diesel:4.327 },
  { state:"Missouri", abbr:"MO", regular:3.47, mid:3.863, premium:4.198, diesel:4.284 },
  { state:"Montana", abbr:"MT", regular:3.901, mid:4.244, premium:4.586, diesel:4.309 },
  { state:"Nebraska", abbr:"NE", regular:3.566, mid:3.781, premium:4.276, diesel:4.217 },
  { state:"Nevada", abbr:"NV", regular:4.541, mid:4.854, premium:5.156, diesel:5.282 },
  { state:"New Hampshire", abbr:"NH", regular:3.833, mid:4.433, premium:4.883, diesel:5.111 },
  { state:"New Jersey", abbr:"NJ", regular:3.838, mid:4.467, premium:4.74, diesel:4.878 },
  { state:"New Mexico", abbr:"NM", regular:3.785, mid:4.231, premium:4.55, diesel:4.636 },
  { state:"New York", abbr:"NY", regular:4.056, mid:4.593, premium:4.969, diesel:5.394 },
  { state:"North Carolina", abbr:"NC", regular:3.481, mid:3.945, premium:4.346, diesel:4.563 },
  { state:"North Dakota", abbr:"ND", regular:3.585, mid:3.952, premium:4.38, diesel:4.293 },
  { state:"Ohio", abbr:"OH", regular:3.559, mid:4.082, premium:4.604, diesel:4.796 },
  { state:"Oklahoma", abbr:"OK", regular:3.316, mid:3.728, premium:4.026, diesel:4.014 },
  { state:"Oregon", abbr:"OR", regular:4.557, mid:4.828, premium:5.111, diesel:5.361 },
  { state:"Pennsylvania", abbr:"PA", regular:3.97, mid:4.446, premium:4.828, diesel:5.346 },
  { state:"Rhode Island", abbr:"RI", regular:3.755, mid:4.49, premium:4.877, diesel:4.913 },
  { state:"South Carolina", abbr:"SC", regular:3.432, mid:3.912, premium:4.306, diesel:4.464 },
  { state:"South Dakota", abbr:"SD", regular:3.654, mid:3.907, premium:4.383, diesel:4.185 },
  { state:"Tennessee", abbr:"TN", regular:3.378, mid:3.855, premium:4.262, diesel:4.443 },
  { state:"Texas", abbr:"TX", regular:3.32, mid:3.819, premium:4.189, diesel:4.226 },
  { state:"Utah", abbr:"UT", regular:3.858, mid:4.135, premium:4.389, diesel:4.575 },
  { state:"Vermont", abbr:"VT", regular:3.966, mid:4.56, premium:5.0, diesel:5.147 },
  { state:"Virginia", abbr:"VA", regular:3.62, mid:4.121, premium:4.512, diesel:4.754 },
  { state:"Washington", abbr:"WA", regular:5.02, mid:5.311, premium:5.573, diesel:5.881 },
  { state:"West Virginia", abbr:"WV", regular:3.694, mid:4.08, premium:4.539, diesel:4.738 },
  { state:"Wisconsin", abbr:"WI", regular:3.554, mid:4.125, premium:4.707, diesel:4.571 },
  { state:"Wyoming", abbr:"WY", regular:3.824, mid:4.122, premium:4.409, diesel:4.522 }
];

const US_GAS_NATIONAL = {
  regular: 3.790,
  mid: 4.259,
  premium: 4.636,
  diesel: 4.790,
  source: "AAA Daily Fuel Gauge Report",
  updated: "As of July 7, 2026"
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

