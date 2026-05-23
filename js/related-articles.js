/* EnergyPricesToday.com — Related Articles auto-injector
 *
 * On any article page (in /articles/) that does NOT already have a related/
 * continue-reading module, inject a "Continue Reading" section with 4 specific
 * article cards. Pulls from FEATURED_ARTICLES (data.js) and filters out the
 * current article + any unknown slugs. Skips hubs and the doubled-path artifact.
 */
(function(){
  'use strict';
  if (window.__eptRelatedLoaded) return;
  window.__eptRelatedLoaded = true;

  // Only run on article pages
  var path = location.pathname.toLowerCase();
  if (!/\/articles\//.test(path)) return;
  if (/\/articles\/articles\//.test(path)) return;  // doubled-path artifact — skip

  var currentSlug = path.split('/').pop().replace('.html','');

  // Hub pages: skip (they're already curated)
  var HUBS = ['iran','saudi-arabia','uae','opec-members','qatar','russia','brazil','nigeria',
              'venezuela','mexico','kazakhstan','suez-canal','china','india','united-kingdom',
              'united-states-other-states','european-union','japan','australia','south-korea',
              'red-sea-bab-el-mandeb'];
  if (HUBS.indexOf(currentSlug) !== -1) return;

  // Skip if a related module already exists on this page
  if (document.querySelector('.article-related, .related-coverage, .continue-reading, #article-related')) return;

  // We need FEATURED_ARTICLES and ARTICLE_SLUGS (both from data.js / article-slugs.js)
  if (typeof FEATURED_ARTICLES === 'undefined') return;
  if (typeof ARTICLE_SLUGS === 'undefined') return;

  // Find the slug for a given title (returns null if unknown — never slugifies)
  function knownSlug(title){
    return (ARTICLE_SLUGS && ARTICLE_SLUGS[title]) ? ARTICLE_SLUGS[title] : null;
  }

  // Build candidate list: FEATURED_ARTICLES, filtered for known slugs + not current page
  var candidates = [];
  for (var i = 0; i < FEATURED_ARTICLES.length; i++) {
    var a = FEATURED_ARTICLES[i];
    var slug = knownSlug(a.title);
    if (!slug) continue;
    if (slug === currentSlug) continue;
    candidates.push({
      title: a.title,
      slug: slug,
      date: a.date,
      excerpt: a.excerpt || '',
      cat: a.cat || 'Coverage'
    });
    if (candidates.length >= 4) break;
  }

  if (candidates.length === 0) return;

  // Find injection point — prefer before the last "Related Dashboards" / tags block
  // Fallback: append to the <article> element
  var anchor = null;
  var article = document.querySelector('article') || document.querySelector('main') || document.body;

  // Try to find the bottom tags/dashboards block to insert BEFORE it
  var tagsBlock = document.querySelector('.article-tags');
  var dashboardsBlock = null;
  // "Related Dashboards" h3 — find it
  var h3s = article.querySelectorAll('h3');
  for (var j = 0; j < h3s.length; j++) {
    if (/related dashboards/i.test(h3s[j].textContent)) {
      dashboardsBlock = h3s[j].parentNode;
      break;
    }
  }
  anchor = dashboardsBlock || tagsBlock;

  // Build HTML — uses inline styles to avoid depending on new CSS classes
  function escapeHtml(s){
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }
  function truncate(s, n){
    s = String(s);
    if (s.length <= n) return s;
    var cut = s.lastIndexOf(' ', n);
    return s.slice(0, cut > 100 ? cut : n) + '\u2026';
  }

  var cardsHtml = candidates.map(function(c){
    return (
      '<a href="' + escapeHtml(c.slug) + '.html" class="article-related-card" ' +
      'style="background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:18px;' +
      'display:block;text-decoration:none;transition:border-color .15s,transform .15s">' +
      '<div style="font-size:11px;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);margin-bottom:8px">' +
      escapeHtml(c.cat) + ' &middot; ' + escapeHtml(c.date || '') + '</div>' +
      '<h4 style="color:var(--text-1);font-size:15px;font-weight:600;line-height:1.35;margin:0 0 8px">' +
      escapeHtml(c.title) + '</h4>' +
      '<p style="color:var(--text-2);font-size:13px;line-height:1.5;margin:0">' +
      escapeHtml(truncate(c.excerpt, 140)) + '</p>' +
      '</a>'
    );
  }).join('');

  var sectionHtml =
    '<section class="article-related" aria-label="Continue Reading" ' +
    'style="margin:40px 0 8px;padding-top:28px;border-top:1px solid var(--border)">' +
    '<h2 style="font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);' +
    'font-weight:600;margin:0 0 18px">Continue Reading</h2>' +
    '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px">' +
    cardsHtml +
    '</div></section>';

  var wrapper = document.createElement('div');
  wrapper.innerHTML = sectionHtml;
  var section = wrapper.firstChild;

  if (anchor && anchor.parentNode) {
    anchor.parentNode.insertBefore(section, anchor);
  } else {
    article.appendChild(section);
  }

  // Mark for analytics — these clicks pick up the .article-related module classification automatically
})();
