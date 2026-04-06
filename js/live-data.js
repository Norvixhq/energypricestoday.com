/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Price Data (EIA API)
   Pulls real commodity prices from U.S. Energy Information Administration
   ═══════════════════════════════════════════════════════════════════ */

var EIA_API_KEY = '7e5ThaUOS3zjIVzaCxJCXDrCRRH9Eg15ji0gch0x';

var EIA_SERIES = {
  'WTI Crude':     'PET.RWTC.D',
  'Brent Crude':   'PET.RBRTE.D',
  'Natural Gas':   'NG.RNGWHHD.D',
  'Gasoline RBOB': 'PET.EER_EPMRU_PF4_RGC_DPG.D',
  'Heating Oil':   'PET.EER_EPD2DXL0_PF4_RGC_DPG.D',
};

function fetchLivePrices() {
  if (!EIA_API_KEY) return;
  console.log('[EPT] Fetching live prices from EIA API...');

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
              updates[name] = { price: latest, change: +(latest - prev).toFixed(2), pct: +((latest - prev) / prev * 100).toFixed(2) };
              console.log('[EPT] ' + name + ': $' + latest.toFixed(2) + ' (' + (latest >= prev ? '+' : '') + (latest - prev).toFixed(2) + ')');
            }
          }
        } catch (e) {
          console.log('[EPT] Parse error for ' + name);
        }
      })
      .catch(function(err) {
        console.log('[EPT] Failed: ' + name + ' — ' + err.message);
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
        count++;
      }
    });
  }
  if (count > 0) {
    console.log('[EPT] Applied ' + count + ' live price updates');
    // Re-render homepage hero
    var hero = document.getElementById('hero-prices');
    if (hero && typeof sparkline === 'function') {
      hero.innerHTML = COMMODITIES.map(function(c) {
        var color = c.change >= 0 ? '#10b45c' : '#dc3545';
        return '<div class="price-card"><div class="price-card-header"><span class="price-card-label">' + c.name + '</span>' + sparkline(c.spark, color) + '</div><div class="price-card-value">$' + c.price.toFixed(2) + '</div><div class="price-card-footer">' + priceChange(c.change, c.pct) + '<span class="price-card-unit">' + c.unit + '</span></div></div>';
      }).join('');
    }
    if (typeof renderTicker === 'function') renderTicker();
  }
}

document.addEventListener('DOMContentLoaded', function() {
  setTimeout(fetchLivePrices, 2000);
  setInterval(fetchLivePrices, 5 * 60 * 1000);
});
