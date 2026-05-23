/* EnergyPricesToday.com — unified analytics tracker
 * Fires both GA4 and Meta Pixel events with consistent params.
 * Auto-instruments: internal link clicks, scroll depth, engagement time,
 * outbound clicks, email clicks. Survives dynamic content via event delegation.
 *
 * Loaded sitewide AFTER gtag init and fbq init. Idempotent — safe to load twice.
 */
(function(){
  'use strict';
  if (window.__eptAnalyticsLoaded) return;
  window.__eptAnalyticsLoaded = true;

  // ─── Core helpers ────────────────────────────────────────────────────────
  function hasGtag(){ return typeof window.gtag === 'function'; }
  function hasFbq(){ return typeof window.fbq === 'function'; }

  /**
   * Unified event tracker.
   *   name:   GA4 event name (snake_case)
   *   params: object passed to GA4
   *   pixel:  optional Pixel event override { event: 'EventName', custom: true, params: {...} }
   *           default: skips Pixel unless explicitly opted-in (avoids spammy events)
   */
  function track(name, params, pixel) {
    params = params || {};
    try {
      if (hasGtag()) window.gtag('event', name, params);
    } catch(e){ /* swallow */ }
    try {
      if (pixel && hasFbq()) {
        var pp = pixel.params || params;
        if (pixel.custom) window.fbq('trackCustom', pixel.event, pp);
        else window.fbq('track', pixel.event, pp);
      }
    } catch(e){ /* swallow */ }
  }
  window.eptTrack = track;

  // ─── Page-type classifier ────────────────────────────────────────────────
  function pageType() {
    var p = location.pathname.toLowerCase();
    if (p === '/' || p.endsWith('/index.html')) return 'homepage';
    if (/\/articles\//.test(p)) {
      // Country hubs are specific articles by name
      var slug = p.split('/').pop().replace('.html','');
      var hubs = ['iran','saudi-arabia','uae','opec-members','qatar','russia','brazil','nigeria',
                  'venezuela','mexico','kazakhstan','suez-canal','china','india','united-kingdom',
                  'united-states-other-states','european-union','japan','australia','south-korea',
                  'red-sea-bab-el-mandeb'];
      if (hubs.indexOf(slug) !== -1) return 'hub';
      return 'article';
    }
    if (/\/category\//.test(p)) return 'category';
    if (/oil-prices|gas-prices|markets|rig-count|oil-futures/.test(p)) return 'pillar';
    if (/about|contact|editorial|corrections|disclaimer|privacy|terms/.test(p)) return 'support';
    return 'other';
  }
  window.eptPageType = pageType;

  function articleSlug() {
    if (pageType() !== 'article' && pageType() !== 'hub') return null;
    return location.pathname.split('/').pop().replace('.html','');
  }

  // ─── Meta Pixel: ViewContent for article pages ───────────────────────────
  (function pixelViewContent(){
    if (!hasFbq()) return;
    var pt = pageType();
    if (pt !== 'article' && pt !== 'hub') return;
    var slug = articleSlug();
    try {
      window.fbq('track', 'ViewContent', {
        content_type: pt,
        content_ids: [slug],
        content_name: document.title.replace(/\s*\|.*$/,'').trim()
      });
    } catch(e){}
  })();

  // ─── Click tracking via event delegation ─────────────────────────────────
  function classifyLink(a) {
    if (!a || !a.href) return null;
    var url;
    try { url = new URL(a.href); } catch(e) { return null; }

    // External link?
    if (url.host && url.host !== location.host) {
      // mailto/tel handled separately below
      if (url.protocol === 'mailto:') return { kind: 'email', target: url.pathname };
      if (url.protocol === 'tel:')    return { kind: 'phone', target: url.pathname };
      return { kind: 'outbound', target: url.host + url.pathname };
    }

    // Internal — classify by path and ancestor module
    var path = url.pathname.toLowerCase();

    // Module detection: walk up to nearest interesting ancestor
    var module = 'unknown';
    var node = a;
    for (var i = 0; i < 8 && node && node !== document.body; i++) {
      var cls = (node.className && typeof node.className === 'string') ? node.className : '';
      var id = node.id || '';
      if (/hub-article-row/.test(cls))           { module = 'hub_row'; break; }
      if (/article-card|article-related|related-coverage/.test(cls)) { module = 'related'; break; }
      if (/featured-card|featured-article/.test(cls)) { module = 'featured'; break; }
      if (/breaking-link|breaking-banner|breaking-ticker/.test(cls)) { module = 'breaking'; break; }
      if (/site-header|main-nav|primary-nav|mobile-nav/.test(cls)) { module = 'nav'; break; }
      if (/site-footer|footer/.test(cls))        { module = 'footer'; break; }
      if (/editor-note|prose/.test(cls))         { module = 'editorial_prose'; break; }
      if (/geo-card|geo-item/.test(cls))         { module = 'geo_card'; break; }
      if (/glance-item|glance-strip/.test(cls))  { module = 'glance'; break; }
      if (/ticker-card|news-ticker/.test(cls))   { module = 'ticker'; break; }
      if (/source-line/.test(cls))               { module = 'source_line'; break; }
      if (id === 'rig-articles')                 { module = 'rig_articles'; break; }
      node = node.parentNode;
    }

    // Path-based destination type
    var destType = 'page';
    if (/\/articles\//.test(path)) destType = 'article';
    else if (/\/category\//.test(path)) destType = 'category';
    else if (/oil-prices|gas-prices|markets|rig-count|oil-futures/.test(path)) destType = 'pillar';
    else if (/index\.html$|^\/$/.test(path)) destType = 'home';

    return {
      kind: 'internal',
      target: path,
      module: module,
      destType: destType,
      text: (a.textContent || '').trim().slice(0, 120)
    };
  }

  function onClick(e) {
    var a = e.target.closest && e.target.closest('a');
    if (!a) return;
    var info = classifyLink(a);
    if (!info) return;

    if (info.kind === 'outbound') {
      track('outbound_click', {
        link_url: info.target,
        link_domain: info.target.split('/')[0],
        page_type: pageType()
      });
      return;
    }
    if (info.kind === 'email') {
      track('email_click', {
        link_email: info.target,
        page_type: pageType()
      }, { event: 'Contact' });  // Meta standard Contact event
      return;
    }
    if (info.kind === 'phone') {
      track('phone_click', { page_type: pageType() }, { event: 'Contact' });
      return;
    }

    // Internal click — fire select_content (GA4 recommended) + InternalNav (Pixel custom)
    var slug = info.destType === 'article'
      ? info.target.split('/').pop().replace('.html','')
      : info.target;

    track('select_content', {
      content_type: info.destType,
      item_id: slug,
      link_module: info.module,
      link_text: info.text,
      page_type: pageType(),
      page_location: location.pathname
    }, {
      event: 'InternalNavigation',
      custom: true,
      params: {
        content_type: info.destType,
        link_module: info.module,
        from_page_type: pageType()
      }
    });
  }
  document.addEventListener('click', onClick, true);

  // ─── Scroll depth tracking (25/50/75/100%) ───────────────────────────────
  (function scrollDepth(){
    var hit = {25:false, 50:false, 75:false, 100:false};
    var pt = pageType();

    function check(){
      var doc = document.documentElement;
      var scrollTop = doc.scrollTop || document.body.scrollTop;
      var docHeight = (doc.scrollHeight || document.body.scrollHeight) - doc.clientHeight;
      if (docHeight <= 0) return;
      var pct = (scrollTop / docHeight) * 100;
      [25,50,75,100].forEach(function(milestone){
        if (!hit[milestone] && pct >= milestone) {
          hit[milestone] = true;
          track('scroll_depth', {
            percent_scrolled: milestone,
            page_type: pt,
            page_location: location.pathname
          });
          // Meta Pixel: DeepRead at 90%+
          if (milestone >= 75 && pt === 'article' && hasFbq() && !hit._deepRead) {
            hit._deepRead = true;
            try {
              window.fbq('trackCustom', 'DeepRead', {
                content_ids: [articleSlug()],
                content_type: 'article',
                percent_scrolled: milestone
              });
            } catch(e){}
          }
        }
      });
    }

    var ticking = false;
    window.addEventListener('scroll', function(){
      if (!ticking) {
        window.requestAnimationFrame(function(){ check(); ticking = false; });
        ticking = true;
      }
    }, { passive: true });
  })();

  // ─── Engagement time milestones (30/60/180/300s) ─────────────────────────
  (function engagementTime(){
    var pt = pageType();
    var fired = {};
    var milestones = [
      { sec: 30,  name: 'engagement_30s' },
      { sec: 60,  name: 'engagement_60s', pixelArticle: 'ArticleEngaged' },
      { sec: 180, name: 'engagement_180s' },
      { sec: 300, name: 'engagement_300s' }
    ];
    var visibleSince = Date.now();
    var accumulated = 0;

    document.addEventListener('visibilitychange', function(){
      if (document.hidden) {
        accumulated += (Date.now() - visibleSince) / 1000;
      } else {
        visibleSince = Date.now();
      }
    });

    function tick(){
      var elapsed = accumulated + (document.hidden ? 0 : (Date.now() - visibleSince) / 1000);
      milestones.forEach(function(m){
        if (fired[m.sec]) return;
        if (elapsed >= m.sec) {
          fired[m.sec] = true;
          track(m.name, { seconds: m.sec, page_type: pt });
          if (m.pixelArticle && pt === 'article' && hasFbq()) {
            try {
              window.fbq('trackCustom', m.pixelArticle, {
                content_ids: [articleSlug()],
                content_type: 'article',
                seconds: m.sec
              });
            } catch(e){}
          }
        }
      });
    }
    setInterval(tick, 10000);  // every 10s — cheap, accurate enough for engagement
  })();

  // ─── Form submission tracking (newsletter, contact) ──────────────────────
  document.addEventListener('submit', function(e){
    var form = e.target;
    if (!form || form.tagName !== 'FORM') return;
    var id = form.id || '';
    var action = (form.action || '').toLowerCase();
    var name = id || (action.indexOf('formspree') !== -1 ? 'formspree_form' : 'form');
    track('form_submit', { form_id: name, page_type: pageType() }, {
      event: 'Lead',
      params: { form_id: name }
    });
  }, true);

})();
