var FINNHUB_KEY = 'd7dsf2pr01qmm59ebskgd7dsf2pr01qmm59ebsl0';
var US_TICKERS = ['XOM','CVX','COP','SHEL','TTE','BP','EOG','DVN','SLB','HAL','BKR','LNG','FANG','MPC','VLO','PSX','SU','EC','YPF'];

function fetchStockPrices() {
  var tables = document.querySelectorAll('.company-table');
  if (!tables.length) return;

  tables.forEach(function(table) {
    var thead = table.querySelector('thead tr');
    if (thead && !thead.querySelector('.stock-th')) {
      var th = document.createElement('th');
      th.className = 'stock-th';
      th.innerHTML = 'Stock Price <span style="color:#10b981;font-size:8px;font-weight:700;vertical-align:super">LIVE</span>';
      thead.insertBefore(th, thead.children[2]);
    }

    var rows = table.querySelectorAll('tbody tr');
    rows.forEach(function(row) {
      if (row.querySelector('.stock-td')) return;
      var td = document.createElement('td');
      td.className = 'stock-td';
      td.style.cssText = 'text-align:right;font-size:13px;min-width:120px';
      var ticker = row.children[1] ? row.children[1].textContent.trim() : '';
      if (US_TICKERS.indexOf(ticker) > -1) {
        td.innerHTML = '<span style="color:var(--text-3);font-size:11px">Loading...</span>';
      } else {
        td.innerHTML = '<span style="color:var(--text-3);font-size:11px">Not Available</span>';
      }
      row.insertBefore(td, row.children[2]);
    });
  });

  // Fetch all US tickers in parallel
  US_TICKERS.forEach(function(ticker, idx) {
    setTimeout(function() {
      fetch('https://finnhub.io/api/v1/quote?symbol=' + ticker + '&token=' + FINNHUB_KEY)
        .then(function(r) { return r.json(); })
        .then(function(data) {
          // Find ALL rows with this ticker across all tables
          document.querySelectorAll('.company-table tbody tr').forEach(function(row) {
            var t = row.children[1] ? row.children[1].textContent.trim() : '';
            if (t !== ticker) return;
            var td = row.querySelector('.stock-td');
            if (!td) return;
            if (data && data.c && data.c > 0) {
              var pct = data.dp ? data.dp.toFixed(2) : '0.00';
              var color = parseFloat(pct) >= 0 ? '#10b981' : '#ef4444';
              var arrow = parseFloat(pct) >= 0 ? '▲' : '▼';
              td.innerHTML = '<strong style="color:var(--text-1)">$' + data.c.toFixed(2) + '</strong> <span style="color:' + color + ';font-size:10px;font-weight:600">' + arrow + pct + '%</span> <span style="display:inline-block;width:6px;height:6px;background:#10b981;border-radius:50%;margin-left:2px;animation:pulse-live 2s infinite"></span>';
            } else {
              td.innerHTML = '<span style="color:var(--text-3)">N/A</span>';
            }
          });
        }).catch(function() {});
    }, idx * 100);
  });
}

var s = document.createElement('style');
s.textContent = '@keyframes pulse-live{0%,100%{opacity:1}50%{opacity:0.3}}';
document.head.appendChild(s);
document.addEventListener('DOMContentLoaded', function() { setTimeout(fetchStockPrices, 800); });
