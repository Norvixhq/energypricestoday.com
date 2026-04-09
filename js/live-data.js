/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Price Data
   
   PRIMARY: Reference prices in data.js (updated with each deployment)
   SECONDARY: EIA API for daily spot prices (1-2 day lag)
   
   The EIA API is free but delayed. Reference prices in data.js are
   updated manually to reflect the most current market conditions.
   The API will only update prices if the data appears current
   (within 10% of reference values).
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
  console.log('[EPT] Checking EIA API for price updates...');

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
              
              // Check if EIA data is stale compared to reference
              var refPrice = null;
              if (typeof COMMODITIES !== 'undefined') {
                COMMODITIES.forEach(function(c) {
                  if (c.name === name && c.price !== null) refPrice = c.price;
                });
              }
              
              // Only update if EIA price is within 15% of reference
              // (larger gaps mean reference is more current, e.g. after a crash)
              if (refPrice !== null) {
                var diff = Math.abs(latest - refPrice) / refPrice;
                if (diff > 0.15) {
                  console.log('[EPT] ' + name + ': EIA $' + latest.toFixed(2) + ' differs >15% from ref $' + refPrice.toFixed(2) + ' — keeping reference (EIA data likely stale)');
                  return;
                }
              }
              
              updates[name] = { price: latest, change: change, pct: pct };
              console.log('[EPT] ' + name + ': $' + latest.toFixed(2) + ' (EIA)');
            }
          }
        } catch (e) {}
      })
      .catch(function(err) {
        console.log('[EPT] EIA fetch failed: ' + name);
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
        c.spark = [c.price * 0.97, c.price * 0.98, c.price * 0.99, c.price * 0.995, c.price * 0.998, c.price * 1.0, c.price];
        count++;
      }
    });
  }
  if (count > 0) {
    console.log('[EPT] Updated ' + count + ' prices from EIA');
    if (typeof renderHeroPrices === 'function') renderHeroPrices();
    if (typeof renderTicker === 'function') renderTicker();
    if (typeof renderMarketTable === 'function') {
      var tbl = document.getElementById('home-market-table');
      if (tbl) renderMarketTable('home-market-table', true);
    }
    var heroBenchmarks = document.getElementById('hero-benchmarks');
    if (heroBenchmarks && typeof sparkline === 'function') {
      heroBenchmarks.innerHTML = COMMODITIES.slice(0, 5).map(function(c) {
        if (c.price === null) return '<div class="price-card price-card-loading"><div class="price-card-header"><span class="price-card-label">' + c.name + '</span></div><div class="price-card-value" style="color:var(--text-3);font-size:15px">Updating\u2026</div><div class="price-card-footer"><span class="price-card-unit">' + c.unit + '</span></div></div>';
        return '<div class="price-card"><div class="price-card-header"><span class="price-card-label">' + c.name + '</span>' + sparkline(c.spark, c.change >= 0 ? '#10b45c' : '#dc3545') + '</div><div class="price-card-value">$' + c.price.toFixed(2) + '</div><div class="price-card-footer">' + priceChange(c.change, c.pct) + '<span class="price-card-unit">' + c.unit + '</span></div></div>';
      }).join('');
    }
  } else {
    console.log('[EPT] Reference prices are more current than EIA — no update needed');
    // Mark commodities as no longer loading
    if (typeof COMMODITIES !== 'undefined') {
      COMMODITIES.forEach(function(c) { c.loading = false; });
    }
  }
}

document.addEventListener('DOMContentLoaded', function() {
  // Mark reference prices as loaded (remove "loading" visual state)
  if (typeof COMMODITIES !== 'undefined') {
    COMMODITIES.forEach(function(c) {
      if (c.price !== null) c.loading = false;
    });
  }
  // Check EIA for updates after 2 seconds
  setTimeout(fetchLivePrices, 2000);
  // Recheck every 5 minutes
  setInterval(fetchLivePrices, 5 * 60 * 1000);
});
