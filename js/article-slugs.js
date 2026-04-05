// Article slug mapping for internal links
var ARTICLE_SLUGS = {
  'The New Oil Order: How OPEC+ Strategy Is Reshaping Global Crude Markets in 2026': 'the-new-oil-order-how-opec-strategy-is-reshaping-global-crude-markets-in-2026',
  'Permian Basin Output Hits Record 6.2M Barrels Per Day': 'permian-basin-output-hits-record-62m-barrels-per-day',
  'Why European Gas Storage Levels Matter More Than Ever': 'why-european-gas-storage-levels-matter-more-than-ever',
  'ExxonMobil vs. Chevron: Battle for Permian Supremacy': 'exxonmobil-vs-chevron-battle-for-permian-supremacy',
  'Nuclear Renaissance: Small Modular Reactors Enter Commercial Phase': 'nuclear-renaissance-small-modular-reactors-enter-commercial-phase',
  'WTI Crude Climbs Past 71 on U.S. Inventory Drawdown': 'wti-crude-climbs-past-71-on-us-inventory-drawdown',
  'Brent-WTI Spread Widens to 4.44 on Atlantic Basin Tightness': 'brent-wti-spread-widens-to-444-on-atlantic-basin-tightness',
  'Goldman Sachs Raises Brent Forecast to 82 by Year-End': 'goldman-sachs-raises-brent-forecast-to-82-by-year-end',
  'Global Energy Demand Growth Slows to 1.2 Percent in 2026': 'global-energy-demand-growth-slows-to-12-percent-in-2026',
  'U.S. Power Grid Faces Record Summer Demand From Data Centers': 'us-power-grid-faces-record-summer-demand-from-data-centers',
  'Red Sea Attacks Force 60 Percent of Tanker Traffic to Reroute': 'red-sea-attacks-force-60-percent-of-tanker-traffic-to-reroute',
  'U.S. Tightens Sanctions on Russian Oil Price Cap Violators': 'us-tightens-sanctions-on-russian-oil-price-cap-violators',
  'Venezuela Sanctions Relief Under Review After Election Delays': 'venezuela-sanctions-relief-under-review-after-election-delays',
  'ExxonMobil Reports 9.2 Billion Q1 Profit Raises Dividend': 'exxonmobil-reports-92-billion-q1-profit-raises-dividend',
  'Shell Accelerates North Sea Asset Sales Worth 4.5 Billion': 'shell-accelerates-north-sea-asset-sales-worth-45-billion',
  'Henry Hub Falls Below 3.50 as U.S. Storage Surplus Persists': 'henry-hub-falls-below-350-as-us-storage-surplus-persists',
  'European TTF Gas Rallies 12 Percent on Cold Weather Forecast': 'european-ttf-gas-rallies-12-percent-on-cold-weather-forecast',
  'Global Renewable Investment Hits 1.8 Trillion in 2025': 'global-renewable-investment-hits-18-trillion-in-2025',
  'NuScale Small Modular Reactor Receives Full NRC Certification': 'nuscale-small-modular-reactor-receives-full-nrc-certification',
  'Global Solar Installations Reach Record 420 GW in 2025': 'global-solar-installations-reach-record-420-gw-in-2025',
  'Offshore Wind Capacity Surpasses 80 GW Globally': 'offshore-wind-capacity-surpasses-80-gw-globally',
  'U.S. Rig Count Falls to 584 Down 5 From Prior Week': 'us-rig-count-falls-to-584-down-5-from-prior-week',
  'U.S. Average Gas Price Rises to 3.42 Per Gallon': 'us-average-gas-price-rises-to-342-per-gallon',
  'Heating Oil Futures Ease as Winter Demand Season Winds Down': 'heating-oil-futures-ease-as-winter-demand-season-winds-down',
  'Guyana Stabroek Block Delivers New 1.5 Billion Barrel Discovery': 'guyana-stabroek-block-delivers-new-15-billion-barrel-discovery',
  'Renewables Provided 35 Percent of Global Electricity in 2025': 'renewables-provided-35-percent-of-global-electricity-in-2025',
};

function articleUrl(title) {
  var slug = ARTICLE_SLUGS[title];
  if (!slug) {
    slug = title.toLowerCase().replace(/[^a-z0-9\s-]/g, '').replace(/[\s]+/g, '-').replace(/-+/g, '-').substring(0, 80);
  }
  var inSub = window.location.pathname.includes('/category/') || window.location.pathname.includes('/articles/');
  return (inSub ? '../' : '') + 'articles/' + slug + '.html';
}
