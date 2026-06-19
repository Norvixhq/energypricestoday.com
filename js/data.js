/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Data Layer
   All mock data in one place for easy future API replacement
   ═══════════════════════════════════════════════════════════════════ */

const COMMODITIES = [
  { name: "WTI Crude", price: 75.83, change: -0.96, pct: -1.25, unit: "$/bbl", spark: [84.9,82.5,80.2,79.2,77.6,76.5,75.83], loading: false },
  { name: "Brent Crude", price: 78.41, change: -1.11, pct: -1.40, unit: "$/bbl", spark: [87.3,85.0,82.7,81.7,80.1,79.2,78.41], loading: false },
  { name: "Natural Gas", price: 3.38, change: -0.03, pct: -0.88, unit: "$/MMBtu", spark: [3.46,3.44,3.42,3.41,3.40,3.39,3.38], loading: false },
  { name: "Gasoline RBOB", price: 2.48, change: -0.07, pct: -2.75, unit: "$/gal", spark: [2.78,2.70,2.62,2.58,2.54,2.51,2.48], loading: false },
  { name: "Heating Oil", price: 2.69, change: -0.07, pct: -2.54, unit: "$/gal", spark: [3.02,2.93,2.85,2.80,2.75,2.72,2.69], loading: false },
  { name: "Murban Crude", price: 79.20, change: -1.05, pct: -1.31, unit: "$/bbl", spark: [88.4,86.0,83.6,82.5,80.9,80.0,79.2], loading: false },
  { name: "Diesel ULSD", price: 2.72, change: -0.07, pct: -2.51, unit: "$/gal", spark: [3.05,2.96,2.88,2.83,2.78,2.75,2.72], loading: false },
  { name: "Jet Fuel", price: 2.91, change: -0.08, pct: -2.68, unit: "$/gal", spark: [3.27,3.17,3.08,3.03,2.98,2.94,2.91], loading: false },
  { name: "Coal", price: 141.5, change: -0.6, pct: -0.42, unit: "$/ton", spark: [142.8,142.5,142.2,142.0,141.8,141.6,141.5], loading: false },
  { name: "Gold", price: 4940.10, change: 11.60, pct: 0.24, unit: "$/oz", spark: [], loading: false },
];

const FULL_PRICES = {
  "All Prices": [
    ...COMMODITIES,
    { name: "Dubai Fateh", price: 76.70, change: -1.02, pct: -1.31, unit: "$/bbl", spark: [85.8,83.4,81.1,80.1,78.5,77.5,76.7] },
    { name: "Louisiana Light", price: 78.60, change: -1.08, pct: -1.36, unit: "$/bbl", spark: [87.8,85.4,83.1,82.0,80.4,79.4,78.6] },
  ],
  "OPEC Blends": [
    { name: "OPEC Basket", price: 77.90, change: -1.05, pct: -1.33, unit: "$/bbl", spark: [87.0,84.6,82.3,81.2,79.6,78.6,77.9] },
    { name: "Arab Light", price: 79.00, change: -1.06, pct: -1.32, unit: "$/bbl", spark: [88.2,85.8,83.5,82.4,80.8,79.8,79.0] },
    { name: "Bonny Light", price: 79.70, change: -1.05, pct: -1.30, unit: "$/bbl", spark: [88.9,86.5,84.2,83.1,81.5,80.5,79.7] },
    { name: "Iran Heavy", price: 72.80, change: -0.98, pct: -1.33, unit: "$/bbl", spark: [81.6,79.2,76.9,75.8,74.2,73.5,72.8] },
    { name: "Kuwait Export", price: 77.00, change: -1.04, pct: -1.33, unit: "$/bbl", spark: [86.1,83.7,81.4,80.3,78.7,77.7,77.0] },
  ],
  "U.S. Blends": [
    { name: "WTI Crude", price: 75.83, change: -0.96, pct: -1.25, unit: "$/bbl", spark: [84.9,82.5,80.2,79.2,77.6,76.5,75.83] },
    { name: "Louisiana Light", price: 78.60, change: -1.08, pct: -1.36, unit: "$/bbl", spark: [87.8,85.4,83.1,82.0,80.4,79.4,78.6] },
    { name: "WTI Midland", price: 76.90, change: -0.98, pct: -1.26, unit: "$/bbl", spark: [86.0,83.6,81.3,80.2,78.6,77.6,76.9] },
    { name: "Mars Blend", price: 74.60, change: -0.97, pct: -1.28, unit: "$/bbl", spark: [83.5,81.1,78.8,77.7,76.1,75.2,74.6] },
    { name: "Eagle Ford", price: 76.00, change: -0.99, pct: -1.29, unit: "$/bbl", spark: [85.0,82.6,80.3,79.2,77.6,76.6,76.0] },
  ],
  "Canadian Blends": [
    { name: "Western Canadian Select", price: 64.80, change: -0.85, pct: -1.29, unit: "$/bbl", spark: [73.0,70.8,68.6,67.6,66.2,65.4,64.8] },
    { name: "Syncrude Sweet", price: 75.10, change: -0.97, pct: -1.27, unit: "$/bbl", spark: [84.0,81.6,79.3,78.2,76.6,75.7,75.1] },
    { name: "Cold Lake Blend", price: 64.20, change: -0.84, pct: -1.29, unit: "$/bbl", spark: [72.3,70.1,67.9,66.9,65.5,64.7,64.2] },
    { name: "Peace Sour", price: 69.20, change: -0.91, pct: -1.30, unit: "$/bbl", spark: [77.7,75.3,73.0,71.9,70.3,69.6,69.2] },
  ],
  "Refined Products": [
    { name: "Gasoline RBOB", price: 2.48, change: -0.07, pct: -2.75, unit: "$/gal", spark: [2.78,2.70,2.62,2.58,2.54,2.51,2.48] },
    { name: "Heating Oil", price: 2.69, change: -0.07, pct: -2.54, unit: "$/gal", spark: [3.02,2.93,2.85,2.80,2.75,2.72,2.69] },
    { name: "Diesel", price: 2.72, change: -0.07, pct: -2.51, unit: "$/gal", spark: [3.05,2.96,2.88,2.83,2.78,2.75,2.72] },
    { name: "Jet Fuel", price: 2.91, change: -0.08, pct: -2.68, unit: "$/gal", spark: [3.27,3.17,3.08,3.03,2.98,2.94,2.91] },
    { name: "Naphtha", price: 600.00, change: -8.10, pct: -1.33, unit: "$/mt", spark: [668,650,632,621,610,604,600] },
  ],
  "Natural Gas": [
    { name: "Henry Hub", price: 3.46, change: -0.04, pct: -1.14, unit: "$/MMBtu", spark: [3.55,3.52,3.50,3.49,3.48,3.47,3.46] },
    { name: "TTF Dutch", price: 52.40, change: -0.85, pct: -1.60, unit: "€/MWh", spark: [53.1,54.0,56.2,55.0,53.8,53.0,52.4] },
    { name: "UK NBP", price: 128.50, change: -2.10, pct: -1.61, unit: "p/therm", spark: [130.2,132.4,137.8,134.9,132.0,130.1,128.5] },
    { name: "JKM LNG", price: 27.80, change: -0.45, pct: -1.59, unit: "$/MMBtu", spark: [28.1,28.6,29.8,29.2,28.6,28.2,27.8] },
  ],
};

const BREAKING_NEWS = [
  { title: "U.S. and Iran Sign Peace Deal; Interim Agreement Takes Effect, Ending the War", cat: "Geopolitics", slug: "geopolitics", time: "1h" },
  { title: "Crude Falls to Multi-Month Lows as Supply Returns: WTI Near $75.83, Brent $78.41", cat: "Oil Markets", slug: "oil-prices", time: "2h" },
  { title: "AAA National Average Falls Below $4 for the First Time Since the War to $3.999", cat: "Gas Prices", slug: "gas-prices", time: "3h" },
  { title: "Strait of Hormuz to Reopen With 60 Days of Free Passage; Mine-Clearing Could Take Weeks", cat: "Geopolitics", slug: "geopolitics", time: "5h" },
  { title: "Araghchi Warns an Israeli Move on Lebanon Would Violate the Deal", cat: "Geopolitics", slug: "geopolitics", time: "7h" },
  { title: "IEA Sees Possible 2027 Supply Surplus as Gulf Barrels Prepare to Return", cat: "Oil Markets", slug: "oil-prices", time: "9h" },
  { title: "Baker Hughes: U.S. Oil Rigs Rise to 433 in the Week Ended June 12", cat: "Oil Markets", slug: "oil-prices", time: "11h" },
  { title: "Geneva Signing Ceremony for the U.S.-Iran Agreement Set for June 19", cat: "Geopolitics", slug: "geopolitics", time: "13h" },
];

const MARKET_DRIVERS = [
  { cat: "Deal Signed", icon: "check-circle", title: "U.S. and Iran Sign Peace Deal; Interim Agreement Takes Effect, Ending the War", desc: "The United States and Iran have signed an interim peace agreement that took effect Thursday, June 18, formally ending the three-month war that closed the Strait of Hormuz and sent oil above $100. Presidents Trump and Pezeshkian, with Vice President Vance and Iran\u2019s parliament speaker Qalibaf, electronically signed the memorandum of understanding on June 15; Trump signed on the sidelines of the G7 summit in France. A formal signing ceremony is set for Geneva on June 19. Under the 14-point accord, Iran agreed not to produce or acquire nuclear weapons and to dilute its enriched uranium, which the IAEA is preparing to verify; the U.S. agreed to release $25 billion in frozen Iranian assets, though officials say no cash has changed hands." },
  { cat: "Hormuz Reopening", icon: "anchor", title: "Strait of Hormuz to Reopen With 60 Days of Free Passage; Mine-Clearing Could Take Weeks", desc: "Under Article 5 of the agreement, Iran will use its best efforts to ensure safe passage of commercial vessels free of charge for 60 days from the Gulf to the Sea of Oman and back, reopening the strait through which roughly a fifth of the world\u2019s oil transits. Nearly 600 ships and 20,000 seafarers had been stranded in Gulf waters during the closure. President Trump says the waterway will be fully open following the signing, but maritime and security experts warn that clearing naval mines and restoring insurer confidence could take weeks. IEA Executive Director Fatih Birol welcomed the deal and urged that the strait be reopened \u201Cwithout conditions\u201D to restore confidence in global supply." },
  { cat: "Oil Tumbles to Mid-$70s", icon: "trending-down", title: "Crude Falls to Multi-Month Lows as Supply Returns: WTI Near $75.83, Brent $78.41", desc: "Oil prices fell again Thursday as the interim U.S.-Iran peace deal took effect, easing the supply fears that have driven the market since February. U.S. WTI crude dropped about 1.25% to $75.83 a barrel and Brent fell about 1.4% to $78.41, extending a slide that has taken Brent from above $107 at the peak to the high $70s. The International Energy Agency said the market could move into a significant supply surplus by 2027 once Hormuz reopens and disrupted Gulf production returns. Cushing inventories have fallen to about 20 million barrels, the lowest in years, a tightness that may slow the decline even as the structural premium unwinds." },
  { cat: "Gas Below $4", icon: "fuel", title: "AAA National Average Falls Below $4 for the First Time Since the War to $3.999", desc: "AAA\u2019s national average for regular gasoline fell to $3.999 on Thursday, dropping below $4 a gallon for the first time since the war began in late February as crude tumbles on the peace deal. Diesel eased to $5.129. The decline reflects the sharp drop in crude working through the one-to-two-week wholesale-to-retail lag, and more relief is likely as the Strait of Hormuz reopens. Texas ($3.49) and Oklahoma ($3.51) are among the cheapest markets and Indiana the lowest at $3.40, while California ($5.64) and Washington ($5.44) remain the most expensive." },
  { cat: "Lebanon Risk Remains", icon: "alert-triangle", title: "Araghchi Warns an Israeli Move on Lebanon Would Violate the Deal as Israel Holds Seized Territory", desc: "The agreement\u2019s durability faces an immediate test. Iranian Foreign Minister Abbas Araghchi warned that any Israeli attack on Lebanon, or occupation of Lebanese territory, would violate the U.S.-Iran agreement. Israel has said it will not withdraw from territory it seized in Lebanon during the conflict despite the peace deal. The unresolved Lebanon front is the most visible fault line in an accord that has otherwise moved quickly from signature to implementation, and a flare-up there remains the clearest path to a renewed risk premium in oil." },
  { cat: "Supply Surplus Ahead", icon: "bar-chart", title: "IEA Sees Possible 2027 Supply Surplus; OPEC Had Already Cut Its 2026 Demand View", desc: "With the strait reopening, the International Energy Agency said the oil market could move into a significant supply surplus by 2027 as disrupted Gulf barrels return alongside strong non-OPEC growth. OPEC last week cut its own 2026 world oil demand-growth forecast to 970,000 bpd, a second straight downward revision, while projecting a 2027 rebound. Fitch had projected Brent averaging $87 for full-year 2026; prices have now fallen well below that, and the debate is shifting from scarcity to how quickly a glut could form once Gulf production fully normalizes." },
];

const FEATURED_ARTICLES = [
  { id: 101, title: "U.S. and Iran Sign Peace Deal; Interim Agreement Takes Effect, Ending the War", excerpt: "An interim U.S.-Iran peace agreement took effect Thursday, formally ending the three-month war that closed the Strait of Hormuz. Trump and Pezeshkian signed the MOU electronically on June 15; Trump signed at the G7 in France, with a Geneva ceremony set for June 19. Iran agreed to forgo nuclear weapons and dilute enriched uranium; the U.S. agreed to release $25 billion in frozen assets.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "June 18, 2026", readTime: "6 min", featured: true },
  { id: 102, title: "Crude Falls to Multi-Month Lows as Supply Returns: WTI Near $75.83, Brent $78.41", excerpt: "Oil fell again Thursday as the interim peace deal took effect. WTI dropped about 1.25% to $75.83 and Brent 1.4% to $78.41, extending a slide from above $107 at the peak. The IEA said the market could move into a significant supply surplus by 2027 once Hormuz reopens, though Cushing inventories near multi-year lows may slow the decline.", cat: "Oil Markets", slug: "oil-prices", author: "EnergyPricesToday Editorial", date: "June 18, 2026", readTime: "5 min" },
  { id: 103, title: "AAA National Average Falls Below $4 for the First Time Since the War to $3.999", excerpt: "AAA\u2019s national average for regular gasoline fell to $3.999 Thursday, below $4 for the first time since the war began, as crude tumbles on the peace deal. Diesel eased to $5.129. Texas ($3.49) and Indiana ($3.40) are among the cheapest; California ($5.64) and Washington ($5.44) stay highest. More relief is likely as the strait reopens.", cat: "Gas Prices", slug: "gas-prices", author: "EnergyPricesToday Editorial", date: "June 18, 2026", readTime: "5 min" },
  { id: 104, title: "Strait of Hormuz to Reopen With 60 Days of Free Passage; Mine-Clearing Could Take Weeks", excerpt: "Under Article 5, Iran will ensure free safe passage for commercial vessels for 60 days, reopening the strait through which a fifth of the world\u2019s oil transits. Nearly 600 ships had been stranded. Trump says it will be fully open, but experts warn mine-clearing and restoring insurer confidence could take weeks.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "June 18, 2026", readTime: "5 min" },
  { id: 105, title: "Araghchi Warns an Israeli Move on Lebanon Would Violate the Deal as Israel Holds Seized Territory", excerpt: "The agreement\u2019s durability faces an immediate test. Araghchi warned any Israeli attack on Lebanon or occupation of Lebanese territory would violate the U.S.-Iran deal; Israel says it will not withdraw from territory it seized. The unresolved Lebanon front is the clearest path to a renewed risk premium.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "June 18, 2026", readTime: "4 min" },
  { id: 106, title: "IEA Sees Possible 2027 Supply Surplus as Gulf Barrels Prepare to Return", excerpt: "With the strait reopening, the IEA said the oil market could move into a significant supply surplus by 2027 as disrupted Gulf barrels return alongside non-OPEC growth. OPEC last week cut its 2026 demand-growth forecast to 970,000 bpd. The debate is shifting from scarcity to how quickly a glut could form.", cat: "Oil Markets", slug: "oil-prices", author: "EnergyPricesToday Editorial", date: "June 18, 2026", readTime: "5 min" },
];

const COMPANY_NEWS = [
  { id: 201, title: "U.S. and Iran Sign Peace Deal; Interim Agreement Takes Effect, Ending the War", date: "June 18, 2026" },
  { id: 202, title: "Crude Falls to Multi-Month Lows as Supply Returns: WTI Near $75.83, Brent $78.41", date: "June 18, 2026" },
  { id: 203, title: "AAA National Average Falls Below $4 for the First Time Since the War to $3.999", date: "June 18, 2026" },
  { id: 204, title: "Strait of Hormuz to Reopen With 60 Days of Free Passage; Mine-Clearing Could Take Weeks", date: "June 18, 2026" },
  { id: 205, title: "Araghchi Warns an Israeli Move on Lebanon Would Violate the Deal", date: "June 18, 2026" },
  { id: 206, title: "U.S. and Iran Digitally Sign Framework Deal to Reopen the Strait of Hormuz", date: "June 15, 2026" },
];

const GEO_ITEMS = [
  { id: 301, region: "United States & Iran", title: "Peace Deal Signed and in Effect; Geneva Ceremony Set for June 19", desc: "The U.S. and Iran signed an interim peace agreement that took effect Thursday, June 18, ending the three-month war. Presidents Trump and Pezeshkian, with VP Vance and parliament speaker Qalibaf, electronically signed the MOU on June 15; Trump signed at the G7 in France, with a formal ceremony set for Geneva on June 19. Iran agreed not to produce or acquire nuclear weapons and to dilute its enriched uranium, verified by the IAEA; the U.S. agreed to release $25 billion in frozen Iranian assets, though officials say no cash has changed hands." },
  { id: 302, region: "Strait of Hormuz", title: "Reopening With 60 Days of Free Passage; Mine-Clearing Could Take Weeks", desc: "Under Article 5 of the accord, Iran will use its best efforts to ensure safe passage of commercial vessels free of charge for 60 days, reopening the chokepoint for roughly a fifth of the world\u2019s oil. Nearly 600 ships and 20,000 seafarers had been stranded during the closure. Trump says the strait will be fully open following the signing; maritime and security experts warn clearing naval mines and restoring insurer confidence could take weeks. IEA chief Birol urged a reopening \u201Cwithout conditions.\u201D" },
  { id: 303, region: "Lebanon (Risk)", title: "Araghchi: An Israeli Move on Lebanon Would Violate the Deal; Israel Holds Seized Territory", desc: "The agreement\u2019s durability faces an immediate test on the Lebanon front. Iranian Foreign Minister Araghchi warned that any Israeli attack on Lebanon, or occupation of Lebanese territory, would violate the U.S.-Iran agreement. Israel has said it will not withdraw from territory it seized in Lebanon during the conflict. The unresolved front is the most visible fault line in the accord and the clearest path to a renewed oil risk premium." },
  { id: 304, region: "Global Markets", title: "Crude Tumbles to Mid-$70s; IEA Sees Possible 2027 Supply Surplus", desc: "Oil fell again Thursday as the deal took effect: WTI dropped about 1.25% to $75.83 and Brent 1.4% to $78.41, extending a slide from above $107 at the peak. The IEA said the market could move into a significant supply surplus by 2027 as Gulf barrels return alongside strong non-OPEC growth. OPEC last week cut its 2026 demand-growth forecast to 970,000 bpd. Cushing inventories near multi-year lows may slow the decline even as the structural premium unwinds." },
  { id: 305, region: "Rig Count", title: "Baker Hughes: U.S. Oil Rigs Rise to 433 in the Week Ended June 12 (Released June 18)", desc: "Baker Hughes reported the U.S. oil rig count rose to 433 in the week ended June 12, up two from 431, with the release shifted to Thursday, June 18 because of the Juneteenth holiday. Rising oil rigs translate to higher production six to twelve months out, though with crude now in the mid-$70s and the Hormuz reopening set to return shut-in Gulf barrels, the economics of further additions tighten. The total U.S. count stands near 565." },
  { id: 306, region: "U.S. Consumers", title: "AAA National Average Falls Below $4 for the First Time Since the War to $3.999", desc: "AAA\u2019s national average for regular gasoline fell to $3.999 Thursday, below $4 for the first time since the war began, as crude tumbles on the peace deal. Diesel eased to $5.129. Indiana is the cheapest market at $3.40, with Texas ($3.49) and Oklahoma ($3.51) close behind; California ($5.64) and Washington ($5.44) remain the most expensive. More relief is likely as the strait reopens and the crude decline works through the pump lag." },
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
  { id: 430, title: "U.S. and Iran Sign Peace Deal; Interim Agreement Takes Effect, Ending the War", excerpt: "The interim accord took effect June 18, formally ending the three-month war. Trump and Pezeshkian signed electronically June 15; a Geneva ceremony is set for June 19. Iran will forgo nuclear weapons and dilute enriched uranium; the U.S. will release $25 billion in frozen assets.", date: "Jun 18, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
  { id: 431, title: "Crude Falls to Multi-Month Lows as Supply Returns: WTI Near $75.83, Brent $78.41", excerpt: "Oil fell again as the deal took effect; the IEA said the market could move into a significant supply surplus by 2027 once Hormuz reopens. Cushing inventories near multi-year lows may slow the decline.", date: "Jun 18, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
  { id: 420, title: "Pakistan Says U.S. and Iran Reach a Final Text \u2014 the Islamabad Declaration; Signing Expected Within Hours", excerpt: "PM Sharif said the two sides reached a final, agreed-upon text, with electronic signing likely within 24 hours and a Geneva ceremony to follow \u2014 though Iran\u2019s team and Vance disputed leaked details.", date: "Jun 13, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
  { id: 421, title: "Crude Holds Near a Three-Month Low With Markets Closed; WTI $84.88, Brent $87.33", excerpt: "Oil markets are closed for the weekend after crude fell to a three-month low Friday. Monday\u2019s open hinges on whether a memorandum is actually signed over the weekend.", date: "Jun 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
  { id: 410, title: "U.S. and Iran Near a Peace Deal; Trump Says It Could Be Signed This Weekend in Europe", excerpt: "A senior administration official said Washington is 85% confident it will sign; Araghchi said an MOU has never been closer. The framework would reopen Hormuz, lift the naval blockade, and suspend oil sanctions.", date: "Jun 12, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
  { id: 411, title: "Crude Falls to a Three-Month Low: WTI Settles $84.88, Brent $87.33 on Deal Optimism", excerpt: "WTI settled down 3.2% and Brent lost 3.4% to its lowest since early March as the U.S. and Iran neared a deal to reopen the Strait of Hormuz. Both lost about 6% on the week.", date: "Jun 12, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" }
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
  // U.S. — Baker Hughes North America Rig Count, June 5, 2026 (via Rigzone)
  us_total: 565, us_total_change: 2, us_oil: 433, us_oil_change: 2, us_gas: 124, us_gas_change: 0, us_misc: 8, us_misc_change: 0,
  us_land: 551, us_offshore: 10, us_inland: 4,
  us_directional: 64, us_horizontal: 483, us_vertical: 13,
  us_yoy: -13, us_yoy_total: 576,
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
  { contract: "WTI Jul 2026", price: 75.83, change: -0.96, pct: -1.25 },
  { contract: "WTI Aug 2026", price: 75.40, change: -0.92, pct: -1.21 },
  { contract: "WTI Sep 2026", price: 74.95, change: -0.88, pct: -1.16 },
  { contract: "WTI Oct 2026", price: 74.50, change: -0.83, pct: -1.10 },
  { contract: "WTI Dec 2026", price: 73.70, change: -0.74, pct: -0.99 },
  { contract: "WTI Dec 2027", price: 71.20, change: -0.50, pct: -0.70 },
  { contract: "Brent Aug 2026", price: 78.41, change: -1.11, pct: -1.40 },
  { contract: "Brent Sep 2026", price: 77.95, change: -1.05, pct: -1.33 },
  { contract: "Brent Oct 2026", price: 77.50, change: -0.99, pct: -1.26 },
  { contract: "Brent Dec 2026", price: 76.60, change: -0.88, pct: -1.13 },
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
      { label: "WTI Crude", value: "$75.83", sub: "-1.25%" },
      { label: "Brent Crude", value: "$78.41", sub: "-1.40%" },
      { label: "OPEC Basket", value: "$77.90", sub: "-1.33%" },
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
      { label: "WTI Front Month", value: "$75.83", sub: "Jul 2026" },
      { label: "Brent Front Month", value: "$78.41", sub: "Aug 2026" },
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
      { label: "U.S. National Avg", value: "$3.999", sub: "/gallon (AAA 6/18)" },
      { label: "RBOB Futures", value: "$2.48", sub: "/gallon" },
      { label: "Crack Spread", value: "$32.40", sub: "3-2-1" },
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
  { state:"Alabama", abbr:"AL", regular:3.618, mid:4.092, premium:4.499, diesel:4.76 },
  { state:"Alaska", abbr:"AK", regular:5.042, mid:5.293, premium:5.517, diesel:5.597 },
  { state:"Arizona", abbr:"AZ", regular:4.296, mid:4.664, premium:4.983, diesel:5.386 },
  { state:"Arkansas", abbr:"AR", regular:3.619, mid:4.105, premium:4.468, diesel:4.65 },
  { state:"California", abbr:"CA", regular:5.642, mid:5.882, premium:6.068, diesel:6.877 },
  { state:"Colorado", abbr:"CO", regular:3.979, mid:4.367, premium:4.703, diesel:4.76 },
  { state:"Connecticut", abbr:"CT", regular:4.136, mid:4.75, premium:5.151, diesel:5.448 },
  { state:"Delaware", abbr:"DE", regular:3.8, mid:4.375, premium:4.678, diesel:4.916 },
  { state:"District of Columbia", abbr:"DC", regular:4.27, mid:4.92, premium:5.311, diesel:5.73 },
  { state:"Florida", abbr:"FL", regular:3.705, mid:4.17, premium:4.511, diesel:4.79 },
  { state:"Georgia", abbr:"GA", regular:3.706, mid:4.176, premium:4.591, diesel:4.854 },
  { state:"Hawaii", abbr:"HI", regular:5.57, mid:5.782, premium:6.013, diesel:7.058 },
  { state:"Idaho", abbr:"ID", regular:4.323, mid:4.625, premium:4.896, diesel:5.093 },
  { state:"Illinois", abbr:"IL", regular:4.283, mid:4.855, premium:5.365, diesel:5.396 },
  { state:"Indiana", abbr:"IN", regular:3.399, mid:3.976, premium:4.492, diesel:5.406 },
  { state:"Iowa", abbr:"IA", regular:3.631, mid:3.967, premium:4.469, diesel:4.693 },
  { state:"Kansas", abbr:"KS", regular:3.679, mid:4.027, premium:4.374, diesel:4.636 },
  { state:"Kentucky", abbr:"KY", regular:3.657, mid:4.219, premium:4.659, diesel:4.802 },
  { state:"Louisiana", abbr:"LA", regular:3.591, mid:4.051, premium:4.44, diesel:4.639 },
  { state:"Maine", abbr:"ME", regular:4.088, mid:4.676, premium:5.127, diesel:5.486 },
  { state:"Maryland", abbr:"MD", regular:3.829, mid:4.425, premium:4.729, diesel:4.952 },
  { state:"Massachusetts", abbr:"MA", regular:4.113, mid:4.751, premium:5.145, diesel:5.423 },
  { state:"Michigan", abbr:"MI", regular:4.076, mid:4.711, premium:5.3, diesel:5.481 },
  { state:"Minnesota", abbr:"MN", regular:3.792, mid:4.238, premium:4.731, diesel:4.876 },
  { state:"Mississippi", abbr:"MS", regular:3.612, mid:4.077, premium:4.474, diesel:4.662 },
  { state:"Missouri", abbr:"MO", regular:3.68, mid:4.082, premium:4.414, diesel:4.699 },
  { state:"Montana", abbr:"MT", regular:4.17, mid:4.5, premium:4.836, diesel:4.848 },
  { state:"Nebraska", abbr:"NE", regular:3.794, mid:4.035, premium:4.475, diesel:4.649 },
  { state:"Nevada", abbr:"NV", regular:4.844, mid:5.176, premium:5.462, diesel:5.647 },
  { state:"New Hampshire", abbr:"NH", regular:4.074, mid:4.652, premium:5.103, diesel:5.388 },
  { state:"New Jersey", abbr:"NJ", regular:4.029, mid:4.644, premium:4.908, diesel:5.119 },
  { state:"New Mexico", abbr:"NM", regular:4.011, mid:4.444, premium:4.755, diesel:5.042 },
  { state:"New York", abbr:"NY", regular:4.293, mid:4.82, premium:5.205, diesel:5.677 },
  { state:"North Carolina", abbr:"NC", regular:3.607, mid:4.079, premium:4.481, diesel:4.795 },
  { state:"North Dakota", abbr:"ND", regular:3.808, mid:4.195, premium:4.61, diesel:4.686 },
  { state:"Ohio", abbr:"OH", regular:3.939, mid:4.478, premium:4.989, diesel:5.33 },
  { state:"Oklahoma", abbr:"OK", regular:3.508, mid:3.931, premium:4.229, diesel:4.435 },
  { state:"Oregon", abbr:"OR", regular:4.922, mid:5.189, premium:5.49, diesel:5.777 },
  { state:"Pennsylvania", abbr:"PA", regular:4.143, mid:4.612, premium:4.993, diesel:5.562 },
  { state:"Rhode Island", abbr:"RI", regular:3.968, mid:4.693, premium:5.093, diesel:5.138 },
  { state:"South Carolina", abbr:"SC", regular:3.582, mid:4.057, premium:4.454, diesel:4.761 },
  { state:"South Dakota", abbr:"SD", regular:3.919, mid:4.139, premium:4.616, diesel:4.612 },
  { state:"Tennessee", abbr:"TN", regular:3.588, mid:4.076, premium:4.474, diesel:4.757 },
  { state:"Texas", abbr:"TX", regular:3.493, mid:3.988, premium:4.353, diesel:4.54 },
  { state:"Utah", abbr:"UT", regular:4.14, mid:4.423, premium:4.669, diesel:5.014 },
  { state:"Vermont", abbr:"VT", regular:4.22, mid:4.82, premium:5.253, diesel:5.447 },
  { state:"Virginia", abbr:"VA", regular:3.742, mid:4.258, premium:4.638, diesel:4.984 },
  { state:"Washington", abbr:"WA", regular:5.436, mid:5.736, premium:5.985, diesel:6.368 },
  { state:"West Virginia", abbr:"WV", regular:3.966, mid:4.368, premium:4.804, diesel:5.091 },
  { state:"Wisconsin", abbr:"WI", regular:3.801, mid:4.37, premium:4.939, diesel:5.004 },
  { state:"Wyoming", abbr:"WY", regular:4.177, mid:4.471, premium:4.744, diesel:5.045 }
];

const US_GAS_NATIONAL = {
  regular: 3.999,
  mid: 4.509,
  premium: 4.886,
  diesel: 5.129,
  source: "AAA Daily Fuel Gauge Report",
  updated: "As of June 18, 2026"
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

