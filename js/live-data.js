/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Price Data (EIA API v2)
   
   Pulls real commodity prices from the U.S. Energy Information
   Administration. Free API, updates daily.
   ═══════════════════════════════════════════════════════════════════ */

var EIA_API_KEY = '7e5ThaUOS3zjIVzaCxJCXDrCRRH9Eg15ji0gch0x';

// EIA v2 API endpoints for major benchmarks
var EIA_QUERIES = [
  {
    name: 'WTI Crude',
    url: 'https://api.eia.gov/v2/petroleum/pri/spt/data/?api_key=' + EIA_API_KEY +
         '&frequency=daily&data[0]=value&facets[product][]=EPCWTI&sort[0][column]=period&sort[0][direction]=desc&length=2'
  },
  {
    name: 'Brent Crude',
    url: 'https://api.eia.gov/v2/petroleum/pri/spt/data/?api_key=' + EIA_API_KEY +
         '&frequency=daily&data[0]=value&facets[product][]=EPCBRENT&sort[0][column]=period&sort[0][direction]=desc&length=2'
  },
  {
    name: 'Natural Gas',
    url: 'https://api.eia.gov/v2/natural-gas/pri/fut/data/?api_key=' + EIA_API_KEY +
         '&frequency=daily&data[0]=value&facets[process][]=FRC&sort[0][column]=period&sort[0][direction]=desc&length=2'
  },
  {
    name: 'Heating Oil',
    url: 'https://api.eia.gov/v2/petroleum/pri/spt/data/?api_key=' + EIA_API_KEY +
         '&frequency=daily&data[0]=value&facets[product][]=EPC0&sort[0][column]=period&sort[0][direction]=desc&length=2'
  },
];

function fetchLivePrices() {
  if (!EIA_API_KEY) {
    console.log('[EPT] No EIA API key set');
    return;
  }

  console.log('[EPT] Fetching live prices from EIA v2 API...');

  var completed = 0;
  var updates = {};

  EIA_QUERIES.forEach(function(q) {
    fetch(q.url)
      .then(function(res) { return res.json(); })
      .then(function(data) {
        try {
          var rows = data.response.data;
          if (rows && rows.length >= 2) {
            var latest = parseFloat(rows[0].value);
            var prev = parseFloat(rows[1].value);
            if (!isNaN(latest) && !isNaN(prev) && prev > 0) {
              var change = latest - prev;
              var pct = (change / prev) * 100;
              updates[q.name] = { price: latest, change: change, pct: pct };
              console.log('[EPT] ' + q.name + ': $' + latest.toFixed(2) + ' (' + (change >= 0 ? '+' : '') + change.toFixed(2) + ')');
            }
          }
        } catch (e) {
          console.log('[EPT] Parse error for ' + q.name + ':', e.message);
        }
      })
      .catch(function(err) {
        console.log('[EPT] Fetch error for ' + q.name + ':', err.message);
      })
      .finally(function() {
        completed++;
        if (completed === EIA_QUERIES.length) {
          applyLiveUpdates(updates);
        }
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
        count++;
      }
    });
  }

  if (count > 0) {
    console.log('[EPT] Applied ' + count + ' live price updates');
    
    // Re-render hero prices if on homepage
    var heroEl = document.getElementById('hero-prices');
    if (heroEl) {
      heroEl.innerHTML = COMMODITIES.map(function(c) {
        var color = c.change >= 0 ? '#10b45c' : '#dc3545';
        return '<div class="price-card"><div class="price-card-header"><span class="price-card-label">' + c.name + '</span>' + sparkline(c.spark, color) + '</div><div class="price-card-value">$' + c.price.toFixed(2) + '</div><div class="price-card-footer">' + priceChange(c.change, c.pct) + '<span class="price-card-unit">' + c.unit + '</span></div></div>';
      }).join('');
    }
    
    // Re-render ticker
    if (typeof renderTicker === 'function') {
      renderTicker();
    }
  }
}

// Auto-fetch on load, refresh every 5 minutes
document.addEventListener('DOMContentLoaded', function() {
  setTimeout(fetchLivePrices, 2000);
  setInterval(fetchLivePrices, 5 * 60 * 1000);
});
