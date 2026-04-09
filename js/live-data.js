/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Price Data (EIA API)
   ═══════════════════════════════════════════════════════════════════ */

var EIA_API_KEY = '7e5ThaUOS3zjIVzaCxJCXDrCRRH9Eg15ji0gch0x';

var EIA_SERIES = {
  'WTI Crude':     'PET.RWTC.D',
  'Brent Crude':   'PET.RBRTE.D',
  'Natural Gas':   'NG.RNGWHHD.D',
  'Gasoline RBOB': 'PET.EER_EPMRU_PF4_RGC_DPG.D',
  'Heating Oil':   'PET.EER_EPD2DXL0_PF4_RGC_DPG.D',
  'Murban Crude':   'PET.RBRTE.D',  // Derived from Brent + premium
};

function fetchLivePrices() {
  if (!EIA_API_KEY) return;
  console.log('[EPT] Fetching live prices...');

  var entries = Object.entries(EIA_SERIES);
  var completed = 0;
  var updates = {};

  entries.forEach(function(entry) {
    var name = entry[0], seriesId = entry[1];
    var url = 'https://api.eia.gov/v2/seriesid/' + seriesId + '?api_key=' + EIA_API_KEY + '&num=2';

    fetch(url)
      .then(function(res) { return res.json(); })
      .then(function(data) {
        try {
          var rows = data.response && data.response.data;
          if (rows && rows.length >= 2) {
            var latest = parseFloat(rows[0].value);
            var prev = parseFloat(rows[1].value);
            if (!isNaN(latest) && !isNaN(prev) && prev > 0) {
              var change = +(latest - prev).toFixed(2);
              var pct = +((latest - prev) / prev * 100).toFixed(2);

              // Murban trades at ~$1.76 premium to Brent
              if (name === 'Murban Crude') {
                latest = +(latest + 1.76).toFixed(2);
              }
              updates[name] = { price: latest, change: change, pct: pct };
              console.log('[EPT] ' + name + ': $' + latest.toFixed(2));
            }
          }
        } catch (e) {}
      })
      .catch(function(err) {
        console.log('[EPT] Failed: ' + name);
      })
      .finally(function() {
        completed++;
        if (completed === entries.length) applyLiveUpdates(updates);
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
        c.spark = c.spark.length > 0 ? c.spark : [c.price * 0.97, c.price * 0.98, c.price * 0.99, c.price * 0.995, c.price * 0.998, c.price * 1.0, c.price];
        count++;
      }
    });
  }
  if (count > 0) {
    console.log('[EPT] Applied ' + count + ' live prices');
    // Re-render homepage hero
    if (typeof renderHeroPrices === 'function') renderHeroPrices();
    // Re-render ticker
    if (typeof renderTicker === 'function') renderTicker();
    // Re-render market table
    if (typeof renderMarketTable === 'function') {
      var tbl = document.getElementById('home-market-table');
      if (tbl) renderMarketTable('home-market-table', true);
    }
    // Re-render any page-specific hero cards (oil-prices, markets, rig-count)
    var heroBenchmarks = document.getElementById('hero-benchmarks');
    if (heroBenchmarks) {
      heroBenchmarks.innerHTML = COMMODITIES.slice(0, 5).map(function(c) {
        if (c.price === null) return '<div class="price-card price-card-loading"><div class="price-card-header"><span class="price-card-label">' + c.name + '</span></div><div class="price-card-value" style="color:var(--text-3);font-size:15px">Updating\u2026</div><div class="price-card-footer"><span class="price-card-unit">' + c.unit + '</span></div></div>';
        return '<div class="price-card"><div class="price-card-header"><span class="price-card-label">' + c.name + '</span>' + sparkline(c.spark, c.change >= 0 ? '#10b45c' : '#dc3545') + '</div><div class="price-card-value">$' + c.price.toFixed(2) + '</div><div class="price-card-footer">' + priceChange(c.change, c.pct) + '<span class="price-card-unit">' + c.unit + '</span></div></div>';
      }).join('');
    }
  }
}

document.addEventListener('DOMContentLoaded', function() {
  setTimeout(fetchLivePrices, 800);
  setInterval(fetchLivePrices, 5 * 60 * 1000);
});
