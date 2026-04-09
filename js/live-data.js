/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Price Data
   
   PRIMARY: OilPriceAPI.com (5-min updates, real CME/ICE data)
   All 5 homepage commodities now use real-time data.
   Murban derived from Brent + $1.76 premium.
   ═══════════════════════════════════════════════════════════════════ */

var OILPRICE_API_KEY = 'f719bf8a7ff3844d0a5436da144bc985db3acf2431ddf3095702b1c5f4926e5a';

// All commodities via OilPriceAPI — 5-minute updates from CME/ICE
var API_CODES = {
  'WTI Crude':     'WTI_USD',
  'Brent Crude':   'BRENT_CRUDE_USD',
  'Natural Gas':   'NATURAL_GAS_USD',
  'Gasoline RBOB': 'GASOLINE_USD',
  'Heating Oil':   'HEATING_OIL_USD',
};

function fetchLivePrices() {
  console.log('[EPT] Fetching live prices from OilPriceAPI...');
  
  var names = Object.keys(API_CODES);
  var completed = 0;
  var updates = {};

  names.forEach(function(name) {
    var code = API_CODES[name];
    fetch('https://api.oilpriceapi.com/v1/prices/latest?by_code=' + code, {
      headers: { 'Authorization': 'Token ' + OILPRICE_API_KEY, 'Content-Type': 'application/json' }
    })
    .then(function(res) { return res.json(); })
    .then(function(data) {
      if (data.status === 'success' && data.data && data.data.price) {
        var price = parseFloat(data.data.price);
        if (!isNaN(price) && price > 0) {
          // Calculate change from reference price
          var refPrice = null;
          if (typeof COMMODITIES !== 'undefined') {
            COMMODITIES.forEach(function(c) {
              if (c.name === name && c.price !== null) refPrice = c.price;
            });
          }
          var change = refPrice ? +(price - refPrice).toFixed(3) : 0;
          var pct = refPrice ? +((price - refPrice) / refPrice * 100).toFixed(2) : 0;
          updates[name] = { price: price, change: change, pct: pct };
          console.log('[EPT] ' + name + ': $' + price.toFixed(2) + ' (live, ' + (data.data.created_at || '') + ')');
        }
      }
    })
    .catch(function(err) {
      console.log('[EPT] Failed: ' + name + ' — ' + err.message);
    })
    .finally(function() {
      completed++;
      if (completed === names.length) applyLiveUpdates(updates);
    });
  });
}

function applyLiveUpdates(updates) {
  var count = 0;
  if (typeof COMMODITIES !== 'undefined') {
    COMMODITIES.forEach(function(c) {
      if (updates[c.name]) {
        c.price = updates[c.name].price;
        c.change = updates[c.name].change;
        c.pct = updates[c.name].pct;
        c.loading = false;
        c.spark = [c.price*0.97,c.price*0.98,c.price*0.99,c.price*0.995,c.price*0.998,c.price,c.price];
        count++;
      }
      // Murban derived from Brent + $1.76
      if (c.name === 'Murban Crude' && updates['Brent Crude']) {
        c.price = +(updates['Brent Crude'].price + 1.76).toFixed(2);
        c.change = updates['Brent Crude'].change;
        c.pct = updates['Brent Crude'].pct;
        c.loading = false;
        c.spark = [c.price*0.97,c.price*0.98,c.price*0.99,c.price*0.995,c.price*0.998,c.price,c.price];
        count++;
      }
    });
  }

  console.log('[EPT] Applied ' + count + ' live price updates');
  
  // Re-render everything
  if (typeof renderHeroPrices === 'function') renderHeroPrices();
  if (typeof renderTicker === 'function') renderTicker();
  if (typeof renderMarketTable === 'function') {
    var tbl = document.getElementById('home-market-table');
    if (tbl) renderMarketTable('home-market-table', true);
  }
  // Re-render subpage hero cards (oil-prices, markets, rig-count)
  var heroBenchmarks = document.getElementById('hero-benchmarks');
  if (heroBenchmarks && typeof sparkline === 'function' && typeof priceChange === 'function') {
    heroBenchmarks.innerHTML = COMMODITIES.slice(0,5).map(function(c) {
      if (c.price === null) return '<div class="price-card price-card-loading"><div class="price-card-header"><span class="price-card-label">'+c.name+'</span></div><div class="price-card-value" style="color:var(--text-3);font-size:15px">Updating\u2026</div><div class="price-card-footer"><span class="price-card-unit">'+c.unit+'</span></div></div>';
      return '<div class="price-card"><div class="price-card-header"><span class="price-card-label">'+c.name+'</span>'+sparkline(c.spark,c.change>=0?'#10b45c':'#dc3545')+'</div><div class="price-card-value">$'+c.price.toFixed(2)+'</div><div class="price-card-footer">'+priceChange(c.change,c.pct)+'<span class="price-card-unit">'+c.unit+'</span></div></div>';
    }).join('');
  }
}

document.addEventListener('DOMContentLoaded', function() {
  // Show reference prices immediately (no loading state)
  if (typeof COMMODITIES !== 'undefined') {
    COMMODITIES.forEach(function(c) { if (c.price !== null) c.loading = false; });
  }
  // Fetch live prices after 1 second
  setTimeout(fetchLivePrices, 1000);
  // Refresh every 5 minutes
  setInterval(fetchLivePrices, 5 * 60 * 1000);
});
