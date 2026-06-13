/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Data Layer
   All mock data in one place for easy future API replacement
   ═══════════════════════════════════════════════════════════════════ */

const COMMODITIES = [
  { name: "WTI Crude", price: 84.88, change: -2.83, pct: -3.23, unit: "$/bbl", spark: [89.5,88.2,87.7,86.7,85.9,85.4,84.88], loading: false },
  { name: "Brent Crude", price: 87.33, change: -2.72, pct: -3.02, unit: "$/bbl", spark: [92.5,90.9,90.4,89.2,88.4,87.9,87.33], loading: false },
  { name: "Natural Gas", price: 3.41, change: -0.05, pct: -1.45, unit: "$/MMBtu", spark: [3.50,3.49,3.47,3.46,3.44,3.42,3.41], loading: false },
  { name: "Gasoline RBOB", price: 2.78, change: -0.09, pct: -3.14, unit: "$/gal", spark: [2.92,2.89,2.87,2.84,2.82,2.80,2.78], loading: false },
  { name: "Heating Oil", price: 3.02, change: -0.10, pct: -3.21, unit: "$/gal", spark: [3.18,3.14,3.11,3.08,3.06,3.04,3.02], loading: false },
  { name: "Murban Crude", price: 88.40, change: -2.70, pct: -2.96, unit: "$/bbl", spark: [93.5,91.9,91.4,90.2,89.4,88.9,88.4], loading: false },
  { name: "Diesel ULSD", price: 3.05, change: -0.10, pct: -3.17, unit: "$/gal", spark: [3.22,3.18,3.15,3.12,3.09,3.07,3.05], loading: false },
  { name: "Jet Fuel", price: 3.27, change: -0.11, pct: -3.25, unit: "$/gal", spark: [3.45,3.41,3.38,3.34,3.31,3.29,3.27], loading: false },
  { name: "Coal", price: 142.8, change: -0.4, pct: -0.28, unit: "$/ton", spark: [143.2,143.1,143.0,142.9,142.9,142.8,142.8], loading: false },
  { name: "Gold", price: 4928.50, change: 13.30, pct: 0.27, unit: "$/oz", spark: [], loading: false },
];

const FULL_PRICES = {
  "All Prices": [
    ...COMMODITIES,
    { name: "Dubai Fateh", price: 85.80, change: -2.65, pct: -3.00, unit: "$/bbl", spark: [90.6,89.0,88.5,87.3,86.5,86.0,85.8] },
    { name: "Louisiana Light", price: 87.80, change: -2.72, pct: -3.01, unit: "$/bbl", spark: [92.6,91.0,90.5,89.3,88.5,88.0,87.8] },
  ],
  "OPEC Blends": [
    { name: "OPEC Basket", price: 87.00, change: -2.60, pct: -2.90, unit: "$/bbl", spark: [92.1,90.5,90.0,88.8,88.0,87.5,87.0] },
    { name: "Arab Light", price: 88.20, change: -2.62, pct: -2.89, unit: "$/bbl", spark: [93.4,91.8,91.3,90.1,89.3,88.7,88.2] },
    { name: "Bonny Light", price: 88.90, change: -2.60, pct: -2.84, unit: "$/bbl", spark: [94.1,92.5,92.0,90.8,90.0,89.4,88.9] },
    { name: "Iran Heavy", price: 81.60, change: -2.45, pct: -2.92, unit: "$/bbl", spark: [86.5,84.9,84.4,83.2,82.4,82.0,81.6] },
    { name: "Kuwait Export", price: 86.10, change: -2.62, pct: -2.95, unit: "$/bbl", spark: [91.2,89.6,89.1,87.9,87.1,86.6,86.1] },
  ],
  "U.S. Blends": [
    { name: "WTI Crude", price: 84.88, change: -2.83, pct: -3.23, unit: "$/bbl", spark: [89.5,88.2,87.7,86.7,85.9,85.4,84.88] },
    { name: "Louisiana Light", price: 87.80, change: -2.72, pct: -3.01, unit: "$/bbl", spark: [92.6,91.0,90.5,89.3,88.5,88.0,87.8] },
    { name: "WTI Midland", price: 86.00, change: -2.80, pct: -3.15, unit: "$/bbl", spark: [90.7,89.1,88.6,87.4,86.6,86.2,86.0] },
    { name: "Mars Blend", price: 83.50, change: -2.70, pct: -3.13, unit: "$/bbl", spark: [88.4,86.8,86.3,85.1,84.3,83.9,83.5] },
    { name: "Eagle Ford", price: 85.00, change: -2.78, pct: -3.17, unit: "$/bbl", spark: [89.9,88.3,87.8,86.6,85.8,85.4,85.0] },
  ],
  "Canadian Blends": [
    { name: "Western Canadian Select", price: 73.00, change: -2.50, pct: -3.31, unit: "$/bbl", spark: [77.6,76.0,75.5,74.3,73.6,73.2,73.0] },
    { name: "Syncrude Sweet", price: 84.00, change: -2.72, pct: -3.14, unit: "$/bbl", spark: [88.9,87.3,86.8,85.6,84.8,84.3,84.0] },
    { name: "Cold Lake Blend", price: 72.30, change: -2.45, pct: -3.28, unit: "$/bbl", spark: [76.8,75.2,74.7,73.5,72.8,72.4,72.3] },
    { name: "Peace Sour", price: 77.70, change: -2.55, pct: -3.18, unit: "$/bbl", spark: [82.3,80.7,80.2,79.0,78.2,77.9,77.7] },
  ],
  "Refined Products": [
    { name: "Gasoline RBOB", price: 2.78, change: -0.09, pct: -3.14, unit: "$/gal", spark: [2.92,2.89,2.87,2.84,2.82,2.80,2.78] },
    { name: "Heating Oil", price: 3.02, change: -0.10, pct: -3.21, unit: "$/gal", spark: [3.18,3.14,3.11,3.08,3.06,3.04,3.02] },
    { name: "Diesel", price: 3.05, change: -0.10, pct: -3.17, unit: "$/gal", spark: [3.22,3.18,3.15,3.12,3.09,3.07,3.05] },
    { name: "Jet Fuel", price: 3.27, change: -0.11, pct: -3.25, unit: "$/gal", spark: [3.45,3.41,3.38,3.34,3.31,3.29,3.27] },
    { name: "Naphtha", price: 668.00, change: -19.40, pct: -2.82, unit: "$/mt", spark: [705,697,692,683,676,671,668] },
  ],
  "Natural Gas": [
    { name: "Henry Hub", price: 3.46, change: -0.04, pct: -1.14, unit: "$/MMBtu", spark: [3.55,3.52,3.50,3.49,3.48,3.47,3.46] },
    { name: "TTF Dutch", price: 52.40, change: -0.85, pct: -1.60, unit: "€/MWh", spark: [53.1,54.0,56.2,55.0,53.8,53.0,52.4] },
    { name: "UK NBP", price: 128.50, change: -2.10, pct: -1.61, unit: "p/therm", spark: [130.2,132.4,137.8,134.9,132.0,130.1,128.5] },
    { name: "JKM LNG", price: 27.80, change: -0.45, pct: -1.59, unit: "$/MMBtu", spark: [28.1,28.6,29.8,29.2,28.6,28.2,27.8] },
  ],
};

const BREAKING_NEWS = [
  { title: "Pakistan Says U.S. and Iran Reach a Final Text \u2014 the \u2018Islamabad Declaration\u2019; Signing Expected Within Hours", cat: "Geopolitics", slug: "geopolitics", time: "1h" },
  { title: "Iran\u2019s Team Calls the Geneva-Sunday Signing Claim \u2018Completely False\u2019", cat: "Geopolitics", slug: "geopolitics", time: "2h" },
  { title: "Trump: Leaked Deal Details Don\u2019t Match What\u2019s Agreed in Writing; Vance Warns of \u2018Fake Information\u2019", cat: "Geopolitics", slug: "geopolitics", time: "3h" },
  { title: "Crude Holds Near a Three-Month Low With Markets Closed; WTI $84.88, Brent $87.33", cat: "Oil Markets", slug: "oil-prices", time: "5h" },
  { title: "OPEC Lowers 2026 Oil Demand Growth Forecast to 970,000 BPD", cat: "Oil Markets", slug: "oil-prices", time: "8h" },
  { title: "Signing Ceremony Most Likely in Geneva, Attended by VP Vance, Near Next Week\u2019s G7", cat: "Geopolitics", slug: "geopolitics", time: "10h" },
  { title: "AAA: National Average Holds at $4.108 After a Third Straight Weekly Decline", cat: "Gas Prices", slug: "gas-prices", time: "12h" },
  { title: "Both Draft Texts Commit to Reopening Hormuz Within 30 Days of a Final Deal", cat: "Oil Markets", slug: "oil-prices", time: "1d" },
];

const MARKET_DRIVERS = [
  { cat: "Final Text Claimed", icon: "file-check", title: "Pakistan Says U.S. and Iran Reach a Final Text \u2014 the \u2018Islamabad Declaration\u2019; Signing Expected Within Hours", desc: "Pakistani Prime Minister Shehbaz Sharif said Friday that the United States and Iran had reached a final, agreed-upon text of a peace deal, declaring that \u201Cpeace has never been this close as it is now.\u201D Sources said the memorandum is being called the \u201CIslamabad declaration\u201D in recognition of Pakistan\u2019s mediating role. On Saturday, Sharif added that finalization was likely within 24 hours, with Pakistan preparing for an electronic signing followed by technical talks next week. A formal ceremony would most likely be held in Geneva, attended by U.S. Vice President JD Vance \u2014 near where Trump and a U.S. delegation will attend the G7 summit in France." },
  { cat: "Terms Disputed", icon: "alert-triangle", title: "Iran\u2019s Team Calls the Geneva-Sunday Claim \u2018Completely False\u2019 as Trump and Vance Push Back on Leaked Details", desc: "The claimed breakthrough is contested. A source close to Iran\u2019s negotiating team told the Fars news agency that reports of a finalized agreement set to be signed in Geneva on Sunday are \u201Ccompletely false.\u201D President Trump said leaked details circulating in the media do not represent what has been agreed to in writing, and Vice President Vance said he was seeing \u201Ca lot of fake information,\u201D stressing that Iran will not receive any cash and that no funds will be released simply for signing a deal or attending a meeting. A senior U.S. official said both sides had agreed on a text and that Washington expects to sign an initial deal in the coming days." },
  { cat: "Oil at Three-Month Lows", icon: "trending-down", title: "Crude Holds Near a Three-Month Low With Markets Closed; WTI $84.88, Brent $87.33 at Friday\u2019s Settle", desc: "Oil markets are closed for the weekend after crude fell to a three-month low Friday on the peace-deal optimism. WTI settled at $84.88 a barrel \u2014 its lowest since April 17 \u2014 and Brent at $87.33, its lowest since early March. Both lost about 6% on the week but remain up more than 20% since the war began February 28. The next moves hinge on whether a memorandum is actually signed over the weekend: a confirmed signing with a 30-day Hormuz reopening clause would extend the decline, while a breakdown over the disputed terms would risk a sharp reversal when trading resumes Monday." },
  { cat: "OPEC Cuts Demand View", icon: "bar-chart", title: "OPEC Lowers 2026 Oil Demand Growth Forecast to 970,000 BPD in Second Straight Downward Revision", desc: "OPEC on Thursday lowered its forecast for 2026 world oil demand growth to 970,000 barrels per day, down from a previous 1.17 million bpd \u2014 its second straight downward revision \u2014 while saying consumption would eventually rebound. The producer group expects oil demand in 2027 to rise by 1.73 million bpd, up 190,000 bpd from its previous forecast. The softer near-term demand view adds to the bearish backdrop as the market positions for a potential reopening of the Strait of Hormuz and the return of disrupted Gulf supply." },
  { cat: "Pump Relief Holds", icon: "fuel", title: "AAA National Average Holds at $4.108 After a Third Straight Weekly Decline", desc: "AAA\u2019s national average for regular gasoline stood at $4.108 over the weekend, holding the third straight weekly decline as crude trades near three-month lows on peace-deal optimism. Diesel is $5.259. Indiana remains the cheapest market at $3.39 and Texas among the lowest at $3.58, while California ($5.81) and Hawaii ($5.58) stay highest. A signed deal that reopens the Strait of Hormuz would accelerate the relief into the heart of the summer driving season; pump prices lag the futures market by one to two weeks, so more of the recent crude decline has yet to reach drivers." },
  { cat: "Reopening Watch", icon: "globe", title: "Both Draft Texts Commit to Reopening Hormuz Within 30 Days; Physical Obstacles Remain", desc: "Both the Iranian and U.S. draft frameworks commit to reopening the Strait of Hormuz within 30 days of a final deal taking effect, though the two versions diverge on sequencing, sanctions relief, and the fate of Iran\u2019s nuclear program. The U.S. military said commercial ships continued to transit the waterway even as tensions persisted. Analysts caution that clearing mines, restarting idled production fields, and repairing damaged energy facilities would delay full normalization even after a signing \u2014 and Fitch still sees a reopening around the end of July, with Brent averaging $87 for full-year 2026, a level already reached." },
];

const FEATURED_ARTICLES = [
  { id: 101, title: "Pakistan Says U.S. and Iran Reach a Final Text \u2014 the \u2018Islamabad Declaration\u2019; Signing Expected Within Hours", excerpt: "Pakistani PM Sharif said the U.S. and Iran reached a final, agreed-upon text \u2014 the \u201CIslamabad declaration\u201D \u2014 with electronic signing likely within 24 hours and a formal ceremony expected in Geneva, attended by VP Vance. \u201CPeace has never been this close,\u201D Sharif said, near where Trump attends next week\u2019s G7 in France.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "June 13, 2026", readTime: "6 min", featured: true },
  { id: 102, title: "Iran\u2019s Team Calls the Geneva-Sunday Claim \u2018Completely False\u2019 as Trump and Vance Push Back", excerpt: "The breakthrough is contested. A source close to Iran\u2019s team told Fars that reports of a Sunday Geneva signing are \u201Ccompletely false.\u201D Trump said leaked details don\u2019t match what\u2019s agreed in writing; Vance warned of \u201Cfake information,\u201D stressing Iran gets no cash for signing. A senior U.S. official said both sides agreed on a text and expect to sign in the coming days.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "June 13, 2026", readTime: "5 min" },
  { id: 103, title: "Crude Holds Near a Three-Month Low With Markets Closed; WTI $84.88, Brent $87.33 at Friday\u2019s Settle", excerpt: "Oil markets are closed for the weekend after crude fell to a three-month low Friday. WTI settled at $84.88, its lowest since April 17, and Brent at $87.33. Both lost ~6% on the week but remain up 20%+ since the war began. Monday\u2019s open hinges on whether a memorandum is actually signed.", cat: "Oil Markets", slug: "oil-prices", author: "EnergyPricesToday Editorial", date: "June 13, 2026", readTime: "5 min" },
  { id: 104, title: "OPEC Lowers 2026 Oil Demand Growth Forecast to 970,000 BPD in Second Straight Cut", excerpt: "OPEC lowered its 2026 world oil demand growth forecast to 970,000 bpd from 1.17 million, its second straight downward revision, while expecting a 2027 rebound of 1.73 million bpd. The softer demand view adds to the bearish backdrop as the market positions for a potential Hormuz reopening.", cat: "Oil Markets", slug: "oil-prices", author: "EnergyPricesToday Editorial", date: "June 12, 2026", readTime: "4 min" },
  { id: 105, title: "U.S. and Iran Near a Peace Deal; Trump Says It Could Be Signed This Weekend in Europe", excerpt: "Trump said an agreement to end the war could be signed as soon as this weekend in Europe, and a senior official said Washington is 85% confident \u2014 the momentum that has now produced a claimed final text and a planned Geneva signing.", cat: "Geopolitics", slug: "geopolitics", author: "EnergyPricesToday Editorial", date: "June 12, 2026", readTime: "6 min" },
  { id: 106, title: "What a Signed Deal Would Mean for Gas Prices: A 30-Day Hormuz Reopening and the Pump Lag", excerpt: "Both draft texts commit to reopening the Strait of Hormuz within 30 days of a final deal. With pump prices lagging crude by one to two weeks, a confirmed signing would extend the decline well into summer \u2014 though mine-clearing and facility repairs would slow full normalization.", cat: "Gas Prices", slug: "gas-prices", author: "EnergyPricesToday Editorial", date: "June 13, 2026", readTime: "5 min" },
];

const COMPANY_NEWS = [
  { id: 201, title: "Pakistan Says U.S. and Iran Reach a Final Text \u2014 the \u2018Islamabad Declaration\u2019; Signing Expected Within Hours", date: "June 13, 2026" },
  { id: 202, title: "Iran\u2019s Team Calls the Geneva-Sunday Claim \u2018Completely False\u2019 as Trump and Vance Push Back", date: "June 13, 2026" },
  { id: 203, title: "Crude Holds Near a Three-Month Low With Markets Closed; WTI $84.88, Brent $87.33", date: "June 13, 2026" },
  { id: 204, title: "OPEC Lowers 2026 Oil Demand Growth Forecast to 970,000 BPD in Second Straight Cut", date: "June 12, 2026" },
  { id: 205, title: "U.S. and Iran Near a Peace Deal; Trump Says It Could Be Signed This Weekend in Europe", date: "June 12, 2026" },
  { id: 206, title: "Crude Falls to a Three-Month Low: WTI Settles $84.88, Brent $87.33 on Deal Optimism", date: "June 12, 2026" },
];

const GEO_ITEMS = [
  { id: 301, region: "Pakistan (Mediator)", title: "Sharif: U.S. and Iran Reach a Final Text \u2014 the \u2018Islamabad Declaration\u2019", desc: "Pakistani Prime Minister Shehbaz Sharif said Friday that the U.S. and Iran had reached a final, agreed-upon text of a peace deal, calling it the moment \u201Cpeace has never been this close.\u201D Sources said the memorandum is being called the \u201CIslamabad declaration\u201D for Pakistan\u2019s mediating role. On Saturday Sharif said finalization was likely within 24 hours, with Pakistan preparing for an electronic signing followed by technical talks next week." },
  { id: 302, region: "United States", title: "Trump and Vance Dispute Leaked Terms; Geneva Signing Expected, Vance to Attend", desc: "A formal signing ceremony would most likely be held in Geneva, attended by Vice President JD Vance, near where Trump and a U.S. delegation will attend the G7 summit in France next week. But Trump said leaked details do not represent what has been agreed to in writing, and Vance warned of \u201Cfake information,\u201D stressing Iran will receive no cash and no funds will be released merely for signing or attending. A senior official said the U.S. expects to sign an initial deal in the coming days." },
  { id: 303, region: "Iran", title: "Negotiating Team Calls the Sunday-Geneva Signing Claim \u2018Completely False\u2019", desc: "A source close to Iran\u2019s negotiating team told the Fars news agency that reports of a finalized agreement set to be signed in Geneva on Sunday are \u201Ccompletely false.\u201D Foreign Minister Araghchi had earlier said a memorandum \u201Chas never been closer\u201D but urged the media to refrain from speculating on its content pending finalization. The competing signals underscore that no text has been publicly confirmed as signed by both sides." },
  { id: 304, region: "Strait of Hormuz", title: "Both Drafts Commit to a 30-Day Reopening; Ships Still Transiting", desc: "Both the Iranian and U.S. draft frameworks commit to reopening the Strait of Hormuz within 30 days of a final deal taking effect, though they diverge on sequencing and sanctions relief. The U.S. military said commercial ships continued to transit the waterway even as tensions persisted. Analysts caution that mine-clearing, restarting idled production fields, and repairing damaged facilities would delay full normalization even after a signing." },
  { id: 305, region: "Global Markets", title: "Crude Holds Near Three-Month Lows With Markets Closed for the Weekend", desc: "Oil markets are closed Saturday after crude fell to a three-month low Friday: WTI settled at $84.88 (its lowest since April 17) and Brent at $87.33. Both lost about 6% on the week but remain up more than 20% since the war began. OPEC cut its 2026 demand-growth forecast to 970,000 bpd. Monday\u2019s reopening will turn on whether a memorandum is actually signed over the weekend." },
  { id: 306, region: "U.S. Consumers", title: "AAA National Average Holds at $4.108 After a Third Straight Weekly Decline", desc: "AAA\u2019s national average for regular gasoline held at $4.108 over the weekend, maintaining a third straight weekly decline as crude trades near three-month lows. Diesel is $5.259. Indiana is the cheapest market at $3.39 and Texas among the lowest at $3.58, while California ($5.81) and Hawaii ($5.58) stay highest. A signed deal reopening Hormuz would accelerate the relief; the pump lags crude by one to two weeks." },
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
  { id: 420, title: "Pakistan Says U.S. and Iran Reach a Final Text \u2014 the Islamabad Declaration; Signing Expected Within Hours", excerpt: "PM Sharif said the two sides reached a final, agreed-upon text, with electronic signing likely within 24 hours and a Geneva ceremony to follow \u2014 though Iran\u2019s team and Vance disputed leaked details.", date: "Jun 13, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
  { id: 421, title: "Crude Holds Near a Three-Month Low With Markets Closed; WTI $84.88, Brent $87.33", excerpt: "Oil markets are closed for the weekend after crude fell to a three-month low Friday. Monday\u2019s open hinges on whether a memorandum is actually signed over the weekend.", date: "Jun 13, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
  { id: 410, title: "U.S. and Iran Near a Peace Deal; Trump Says It Could Be Signed This Weekend in Europe", excerpt: "A senior administration official said Washington is 85% confident it will sign; Araghchi said an MOU has never been closer. The framework would reopen Hormuz, lift the naval blockade, and suspend oil sanctions.", date: "Jun 12, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
  { id: 411, title: "Crude Falls to a Three-Month Low: WTI Settles $84.88, Brent $87.33 on Deal Optimism", excerpt: "WTI settled down 3.2% and Brent lost 3.4% to its lowest since early March as the U.S. and Iran neared a deal to reopen the Strait of Hormuz. Both lost about 6% on the week.", date: "Jun 12, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" },
  { id: 401, title: "Iran and Israel Agree to Halt Attacks After Weekend Exchange; Trump Says New Ceasefire Is Close", excerpt: "The de-escalation capped a volatile seventy-two hours that began with Israel\u2019s strike on southern Beirut and ended with both militaries standing down.", date: "Jun 9, 2026", author: "EnergyPricesToday Editorial", readTime: "6 min" },
  { id: 402, title: "Oil Falls Below $90 After Touching $95; Crude Surrenders the Escalation Spike", excerpt: "The retreat completed a round-trip that began with the weekend\u2019s exchange of strikes and ended with the de-escalation traders had been waiting for.", date: "Jun 9, 2026", author: "EnergyPricesToday Editorial", readTime: "5 min" }
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
  us_total: 563, us_total_change: 1, us_oil: 431, us_oil_change: 2, us_gas: 124, us_gas_change: -1, us_misc: 8, us_misc_change: 0,
  us_land: 549, us_offshore: 10, us_inland: 4,
  us_directional: 64, us_horizontal: 481, us_vertical: 13,
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
  source: "Baker Hughes", updated: "U.S./Canada: June 5, 2026 | International: April 2026"
};

const OIL_FUTURES_DATA = [
  { contract: "WTI Jul 2026", price: 84.88, change: -2.83, pct: -3.23 },
  { contract: "WTI Aug 2026", price: 84.30, change: -2.75, pct: -3.16 },
  { contract: "WTI Sep 2026", price: 83.70, change: -2.66, pct: -3.08 },
  { contract: "WTI Oct 2026", price: 83.10, change: -2.55, pct: -2.98 },
  { contract: "WTI Dec 2026", price: 81.90, change: -2.34, pct: -2.78 },
  { contract: "WTI Dec 2027", price: 78.20, change: -1.70, pct: -2.13 },
  { contract: "Brent Aug 2026", price: 87.33, change: -2.72, pct: -3.02 },
  { contract: "Brent Sep 2026", price: 86.70, change: -2.63, pct: -2.94 },
  { contract: "Brent Oct 2026", price: 86.05, change: -2.52, pct: -2.85 },
  { contract: "Brent Dec 2026", price: 84.80, change: -2.30, pct: -2.64 },
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
      { label: "WTI Crude", value: "$84.88", sub: "-3.23%" },
      { label: "Brent Crude", value: "$87.33", sub: "-3.02%" },
      { label: "OPEC Basket", value: "$87.00", sub: "-2.90%" },
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
      { label: "WTI Front Month", value: "$84.88", sub: "Jul 2026" },
      { label: "Brent Front Month", value: "$87.33", sub: "Aug 2026" },
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
      { label: "U.S. Total", value: "563", sub: "+1 w/w" },
      { label: "U.S. Oil Rigs", value: "431", sub: "+2 w/w" },
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
      { label: "U.S. National Avg", value: "$4.108", sub: "/gallon (AAA 6/13)" },
      { label: "RBOB Futures", value: "$2.78", sub: "/gallon" },
      { label: "Crack Spread", value: "$35.10", sub: "3-2-1" },
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
  { state:"Alabama", abbr:"AL", regular:3.739, mid:4.215, premium:4.593, diesel:4.894 },
  { state:"Alaska", abbr:"AK", regular:5.153, mid:5.387, premium:5.605, diesel:5.701 },
  { state:"Arizona", abbr:"AZ", regular:4.484, mid:4.852, premium:5.164, diesel:5.585 },
  { state:"Arkansas", abbr:"AR", regular:3.745, mid:4.232, premium:4.601, diesel:4.794 },
  { state:"California", abbr:"CA", regular:5.809, mid:6.048, premium:6.23, diesel:7.098 },
  { state:"Colorado", abbr:"CO", regular:4.206, mid:4.597, premium:4.928, diesel:4.974 },
  { state:"Connecticut", abbr:"CT", regular:4.293, mid:4.882, premium:5.282, diesel:5.562 },
  { state:"Delaware", abbr:"DE", regular:3.884, mid:4.484, premium:4.789, diesel:5.012 },
  { state:"District of Columbia", abbr:"DC", regular:4.401, mid:5.008, premium:5.412, diesel:5.707 },
  { state:"Florida", abbr:"FL", regular:3.936, mid:4.411, premium:4.747, diesel:4.993 },
  { state:"Georgia", abbr:"GA", regular:3.793, mid:4.257, premium:4.674, diesel:4.944 },
  { state:"Hawaii", abbr:"HI", regular:5.583, mid:5.829, premium:6.082, diesel:7.107 },
  { state:"Idaho", abbr:"ID", regular:4.463, mid:4.746, premium:5.024, diesel:5.301 },
  { state:"Illinois", abbr:"IL", regular:4.448, mid:5.04, premium:5.52, diesel:5.58 },
  { state:"Indiana", abbr:"IN", regular:3.394, mid:3.962, premium:4.477, diesel:5.579 },
  { state:"Iowa", abbr:"IA", regular:3.756, mid:4.087, premium:4.586, diesel:4.85 },
  { state:"Kansas", abbr:"KS", regular:3.769, mid:4.126, premium:4.452, diesel:4.758 },
  { state:"Kentucky", abbr:"KY", regular:3.694, mid:4.252, premium:4.686, diesel:4.898 },
  { state:"Louisiana", abbr:"LA", regular:3.69, mid:4.142, premium:4.54, diesel:4.754 },
  { state:"Maine", abbr:"ME", regular:4.206, mid:4.818, premium:5.283, diesel:5.592 },
  { state:"Maryland", abbr:"MD", regular:3.901, mid:4.515, premium:4.814, diesel:5.069 },
  { state:"Massachusetts", abbr:"MA", regular:4.235, mid:4.856, premium:5.247, diesel:5.521 },
  { state:"Michigan", abbr:"MI", regular:4.253, mid:4.891, premium:5.469, diesel:5.647 },
  { state:"Minnesota", abbr:"MN", regular:3.916, mid:4.358, premium:4.846, diesel:5.013 },
  { state:"Mississippi", abbr:"MS", regular:3.713, mid:4.173, premium:4.546, diesel:4.786 },
  { state:"Missouri", abbr:"MO", regular:3.795, mid:4.201, premium:4.524, diesel:4.845 },
  { state:"Montana", abbr:"MT", regular:4.289, mid:4.636, premium:4.973, diesel:5.079 },
  { state:"Nebraska", abbr:"NE", regular:3.938, mid:4.156, premium:4.629, diesel:4.821 },
  { state:"Nevada", abbr:"NV", regular:4.965, mid:5.287, premium:5.574, diesel:5.84 },
  { state:"New Hampshire", abbr:"NH", regular:4.214, mid:4.798, premium:5.248, diesel:5.521 },
  { state:"New Jersey", abbr:"NJ", regular:4.175, mid:4.76, premium:5.035, diesel:5.272 },
  { state:"New Mexico", abbr:"NM", regular:3.973, mid:4.381, premium:4.694, diesel:5.113 },
  { state:"New York", abbr:"NY", regular:4.404, mid:4.919, premium:5.304, diesel:5.766 },
  { state:"North Carolina", abbr:"NC", regular:3.757, mid:4.232, premium:4.63, diesel:4.938 },
  { state:"North Dakota", abbr:"ND", regular:3.88, mid:4.257, premium:4.673, diesel:4.822 },
  { state:"Ohio", abbr:"OH", regular:4.156, mid:4.712, premium:5.23, diesel:5.505 },
  { state:"Oklahoma", abbr:"OK", regular:3.619, mid:4.028, premium:4.333, diesel:4.581 },
  { state:"Oregon", abbr:"OR", regular:5.048, mid:5.322, premium:5.596, diesel:5.914 },
  { state:"Pennsylvania", abbr:"PA", regular:4.267, mid:4.725, premium:5.116, diesel:5.663 },
  { state:"Rhode Island", abbr:"RI", regular:4.112, mid:4.837, premium:5.238, diesel:5.287 },
  { state:"South Carolina", abbr:"SC", regular:3.73, mid:4.212, premium:4.606, diesel:4.868 },
  { state:"South Dakota", abbr:"SD", regular:4.011, mid:4.225, premium:4.692, diesel:4.736 },
  { state:"Tennessee", abbr:"TN", regular:3.681, mid:4.154, premium:4.56, diesel:4.887 },
  { state:"Texas", abbr:"TX", regular:3.584, mid:4.071, premium:4.44, diesel:4.687 },
  { state:"Utah", abbr:"UT", regular:4.367, mid:4.656, premium:4.903, diesel:5.223 },
  { state:"Vermont", abbr:"VT", regular:4.347, mid:4.901, premium:5.35, diesel:5.573 },
  { state:"Virginia", abbr:"VA", regular:3.883, mid:4.391, premium:4.768, diesel:5.115 },
  { state:"Washington", abbr:"WA", regular:5.567, mid:5.853, premium:6.102, diesel:6.533 },
  { state:"West Virginia", abbr:"WV", regular:4.092, mid:4.49, premium:4.937, diesel:5.237 },
  { state:"Wisconsin", abbr:"WI", regular:3.911, mid:4.485, premium:5.058, diesel:5.202 },
  { state:"Wyoming", abbr:"WY", regular:4.26, mid:4.538, premium:4.834, diesel:5.167 }
];

const US_GAS_NATIONAL = {
  regular: 4.108,
  mid: 4.618,
  premium: 4.994,
  diesel: 5.259,
  source: "AAA Daily Fuel Gauge Report",
  updated: "As of June 13, 2026"
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

