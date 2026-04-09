/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Price Engine
   OilPriceAPI.com — 5-minute CME/ICE data
   ═══════════════════════════════════════════════════════════════════ */

var OILPRICE_API_KEY = 'f719bf8a7ff3844d0a5436da144bc985db3acf2431ddf3095702b1c5f4926e5a';

var API_CODES = {
  'WTI Crude':     'WTI_USD',
  'Brent Crude':   'BRENT_CRUDE_USD',
  'Natural Gas':   'NATURAL_GAS_USD',
  'Gasoline RBOB': 'GASOLINE_USD',
  'Heating Oil':   'HEATING_OIL_USD',
  'Diesel ULSD':   'DIESEL_USD',
  'Jet Fuel':      'JET_FUEL_USD',
  'Coal':          'COAL_USD',
};

// Map API code back to display name for oil price table matching
var CODE_TO_TABLE = {
  'WTI_USD': 'WTI Crude',
  'BRENT_CRUDE_USD': 'Brent Crude',
  'NATURAL_GAS_USD': 'Natural Gas',
  'GASOLINE_USD': 'Gasoline RBOB',
  'HEATING_OIL_USD': 'Heating Oil',
  'DIESEL_USD': 'Diesel ULSD',
  'JET_FUEL_USD': 'Jet Fuel',
  'COAL_USD': 'Coal (Newcastle)',
};

function fetchLivePrices() {
  var names = Object.keys(API_CODES);
  var pending = names.length;
  var liveMap = {};

  names.forEach(function(name) {
    fetch('https://api.oilpriceapi.com/v1/prices/latest?by_code=' + API_CODES[name], {
      headers: { 'Authorization': 'Token ' + OILPRICE_API_KEY }
    })
    .then(function(r) { return r.json(); })
    .then(function(d) {
      if (d.status === 'success' && d.data && d.data.price) {
        liveMap[name] = parseFloat(d.data.price);
        // Also map by API code for oil table matching
        liveMap[API_CODES[name]] = parseFloat(d.data.price);
      }
    })
    .catch(function() {})
    .finally(function() {
      if (--pending === 0) applyAll(liveMap);
    });
  });
}

function applyAll(liveMap) {
  // 1. UPDATE COMMODITIES (hero cards, ticker, market table)
  if (typeof COMMODITIES !== 'undefined') {
    COMMODITIES.forEach(function(c) {
      if (liveMap[c.name]) {
        c.price = liveMap[c.name];
        c.change = 0;
        c.pct = 0;
        c.loading = false;
        c.spark = [c.price*.97,c.price*.98,c.price*.99,c.price*.995,c.price*.998,c.price,c.price];
      }
      if (c.name === 'Murban Crude' && liveMap['Brent Crude']) {
        c.price = +(liveMap['Brent Crude'] + 1.76).toFixed(2);
        c.loading = false;
        c.spark = [c.price*.97,c.price*.98,c.price*.99,c.price*.995,c.price*.998,c.price,c.price];
      }
    });
  }

  // 2. UPDATE OIL_PRICE_SECTIONS Futures & Indexes
  if (typeof OIL_PRICE_SECTIONS !== 'undefined' && OIL_PRICE_SECTIONS[0]) {
    OIL_PRICE_SECTIONS[0].rows.forEach(function(row) {
      if (row.apiCode && liveMap[row.apiCode]) {
        var newPrice = liveMap[row.apiCode];
        row.change = +(newPrice - row.price).toFixed(2);
        row.pct = row.price > 0 ? +((newPrice - row.price) / row.price * 100).toFixed(2) : 0;
        row.price = newPrice;
        row.live = true;
      }
    });
    // Also update Murban in the table
    OIL_PRICE_SECTIONS[0].rows.forEach(function(row) {
      if (row.name === 'Murban Crude' && liveMap['Brent Crude']) {
        var newPrice = +(liveMap['Brent Crude'] + 1.76).toFixed(2);
        row.change = +(newPrice - row.price).toFixed(2);
        row.pct = row.price > 0 ? +((newPrice - row.price) / row.price * 100).toFixed(2) : 0;
        row.price = newPrice;
        row.live = true;
      }
    });
  }

  // 3. RE-RENDER EVERYTHING
  if (typeof renderHeroPrices === 'function') renderHeroPrices();
  if (typeof renderTicker === 'function') renderTicker();
  var mkt = document.getElementById('home-market-table');
  if (mkt && typeof renderMarketTable === 'function') renderMarketTable('home-market-table', true);

  // Hero benchmarks on subpages
  var hero = document.getElementById('hero-benchmarks');
  if (hero && typeof sparkline === 'function' && typeof priceChange === 'function') {
    hero.innerHTML = COMMODITIES.slice(0,5).map(function(c) {
      if (c.price === null) return '<div class="price-card price-card-loading"><div class="price-card-header"><span class="price-card-label">'+c.name+'</span></div><div class="price-card-value" style="color:var(--text-3);font-size:15px">Updating\u2026</div><div class="price-card-footer"><span class="price-card-unit">'+c.unit+'</span></div></div>';
      return '<div class="price-card"><div class="price-card-header"><span class="price-card-label">'+c.name+'</span>'+sparkline(c.spark,c.change>=0?'#10b45c':'#dc3545')+'</div><div class="price-card-value">$'+c.price.toFixed(2)+'</div><div class="price-card-footer">'+priceChange(c.change,c.pct)+'<span class="price-card-unit">'+c.unit+'</span></div></div>';
    }).join('');
  }

  // 4. RE-RENDER OIL PRICES TABLE — full re-render of ALL sections
  var sectionsEl = document.getElementById('price-sections');
  if (sectionsEl && typeof OIL_PRICE_SECTIONS !== 'undefined') {
    sectionsEl.innerHTML = OIL_PRICE_SECTIONS.map(function(s, i) {
      var header = '<div id="price-section-' + i + '" style="scroll-margin-top:100px;margin-bottom:32px">' +
        '<div style="display:flex;align-items:center;gap:8px;margin-bottom:12px">' +
        (s.flag ? '<span style="font-size:22px">' + s.flag + '</span>' : '') +
        '<h2 style="font-size:17px;margin:0">' + s.title + '</h2>' +
        (s.subtitle ? '<span style="color:var(--text-3);font-size:12px;font-weight:500">(' + s.subtitle + ')</span>' : '') +
        '</div>';

      var table = '<div class="market-table-wrap"><table class="market-table">' +
        '<thead><tr><th style="text-align:left">Blend / Index</th><th>Price</th><th>Change</th><th>% Change</th></tr></thead><tbody>';

      table += s.rows.map(function(r) {
        var cls = r.change >= 0 ? 'up' : 'down';
        var tag = r.live ? ' <span style="color:#10b981;font-size:9px;font-weight:700;vertical-align:super">LIVE</span>' : '';
        return '<tr><td>' + r.name + tag + '</td>' +
          '<td class="table-price">$' + r.price.toFixed(2) + '</td>' +
          '<td><span class="change ' + cls + '">' + (r.change >= 0 ? '+' : '') + r.change.toFixed(2) + '</span></td>' +
          '<td><span class="change ' + cls + '">' + (r.change >= 0 ? '+' : '') + r.pct.toFixed(2) + '%</span></td></tr>';
      }).join('');

      table += '</tbody></table></div></div>';
      return header + table;
    }).join('');
  }
}

document.addEventListener('DOMContentLoaded', function() {
  if (typeof COMMODITIES !== 'undefined') {
    COMMODITIES.forEach(function(c) { if (c.price !== null) c.loading = false; });
  }
  fetchLivePrices();
  setInterval(fetchLivePrices, 5 * 60 * 1000);
});
