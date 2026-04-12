/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Stock Prices via Finnhub
   Parallel batch loading with LIVE indicators
   ═══════════════════════════════════════════════════════════════════ */

var FINNHUB_KEY = 'd7dsf2pr01qmm59ebskgd7dsf2pr01qmm59ebsl0';

// U.S.-listed tickers that Finnhub supports
var US_TICKERS = ['XOM','CVX','COP','SHEL','TTE','BP','EOG','PXD','DVN','SLB','HAL','BKR','LNG','FANG','MPC','VLO','PSX','SU','EC','YPF'];

function fetchStockPrices() {
  var rows = document.querySelectorAll('.company-table tbody tr');
  if (!rows.length) return;

  // Separate rows into US-listed and international
  var usRows = [];
  var intlRows = [];

  rows.forEach(function(row) {
    var tickerCell = row.children[1];
    if (!tickerCell) return;
    var ticker = tickerCell.textContent.trim();
    if (US_TICKERS.indexOf(ticker) > -1) {
      usRows.push({ row: row, ticker: ticker });
    } else {
      intlRows.push({ row: row, ticker: ticker });
    }
  });

  // Add LIVE badge to header
  var thead = document.querySelector('.company-table thead tr');
  if (thead && !thead.querySelector('.stock-th')) {
    var th = document.createElement('th');
    th.className = 'stock-th';
    th.innerHTML = 'Stock Price <span style="color:#10b981;font-size:8px;font-weight:700;vertical-align:super">LIVE</span>';
    thead.insertBefore(th, thead.children[2]);
  }

  // Add placeholder cells to ALL rows immediately
  rows.forEach(function(row) {
    if (row.querySelector('.stock-td')) return;
    var td = document.createElement('td');
    td.className = 'stock-td';
    td.style.cssText = 'text-align:right;font-size:13px;min-width:110px';
    var ticker = row.children[1] ? row.children[1].textContent.trim() : '';
    if (US_TICKERS.indexOf(ticker) > -1) {
      td.innerHTML = '<span style="color:var(--text-3);font-size:11px">Loading...</span>';
    } else {
      td.innerHTML = '<span style="color:var(--text-3);font-size:11px">—</span>';
    }
    row.insertBefore(td, row.children[2]);
  });

  // Fetch ALL US tickers in parallel (not sequential)
  var fetched = 0;
  usRows.forEach(function(item, idx) {
    // Small stagger to avoid burst — 100ms apart instead of 200ms
    setTimeout(function() {
      fetch('https://finnhub.io/api/v1/quote?symbol=' + item.ticker + '&token=' + FINNHUB_KEY)
        .then(function(r) { return r.json(); })
        .then(function(data) {
          var td = item.row.querySelector('.stock-td');
          if (data && data.c && data.c > 0) {
            var price = data.c.toFixed(2);
            var pct = data.dp ? data.dp.toFixed(2) : '0.00';
            var color = parseFloat(pct) >= 0 ? '#10b981' : '#ef4444';
            var arrow = parseFloat(pct) >= 0 ? '▲' : '▼';
            td.innerHTML = '<strong style="color:var(--text-1)">$' + price + '</strong> <span style="color:' + color + ';font-size:10px;font-weight:600">' + arrow + pct + '%</span> <span style="display:inline-block;width:6px;height:6px;background:#10b981;border-radius:50%;margin-left:3px;animation:pulse-live 2s infinite"></span>';
            fetched++;
          } else {
            td.innerHTML = '<span style="color:var(--text-3)">—</span>';
          }
        })
        .catch(function() {
          var td = item.row.querySelector('.stock-td');
          if (td) td.innerHTML = '<span style="color:var(--text-3)">—</span>';
        });
    }, idx * 100);
  });
}

// Add pulse animation
var style = document.createElement('style');
style.textContent = '@keyframes pulse-live{0%,100%{opacity:1}50%{opacity:0.3}}';
document.head.appendChild(style);

document.addEventListener('DOMContentLoaded', function() {
  setTimeout(fetchStockPrices, 800);
});
