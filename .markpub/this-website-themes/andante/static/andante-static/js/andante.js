/*
 * andante — small, focused enhancements.
 * The site reads fine without JS; this layer adds polish.
 */

(function () {
  'use strict';

  // ---------- Drawer ----------

  function initDrawer() {
    var openBtn = document.querySelector('[data-drawer-open]');
    var closeBtn = document.querySelector('[data-drawer-close]');
    var drawer = document.querySelector('.drawer');
    var scrim = document.querySelector('.scrim');
    if (!openBtn || !drawer || !scrim) return;

    function open() {
      drawer.classList.add('is-open');
      scrim.classList.add('is-visible');
      document.body.classList.add('no-scroll');
      openBtn.setAttribute('aria-expanded', 'true');
      // focus the close button for keyboard users
      var c = drawer.querySelector('[data-drawer-close]');
      if (c) c.focus();
    }
    function close() {
      drawer.classList.remove('is-open');
      scrim.classList.remove('is-visible');
      document.body.classList.remove('no-scroll');
      openBtn.setAttribute('aria-expanded', 'false');
    }

    openBtn.addEventListener('click', open);
    if (closeBtn) closeBtn.addEventListener('click', close);
    scrim.addEventListener('click', close);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) close();
    });

    // Highlight current page in drawer
    var here = window.location.pathname.replace(/index\.html$/, '');
    var links = drawer.querySelectorAll('a[href]');
    links.forEach(function (a) {
      var href = a.getAttribute('href');
      if (!href) return;
      try {
        var url = new URL(href, window.location.origin);
        var path = url.pathname.replace(/index\.html$/, '');
        if (path === here) a.classList.add('is-current');
      } catch (e) { /* ignore */ }
    });
  }

  // ---------- Hover previews ----------
  // Fetches target HTML, extracts the first paragraphs of .prose, caches in-memory.

  var cache = new Map();
  var card = null;
  var hoverTimer = null;
  var hideTimer = null;
  var currentTarget = null;

  function makeCard() {
    if (card) return card;
    card = document.createElement('div');
    card.className = 'preview-card';
    card.setAttribute('role', 'tooltip');
    card.innerHTML = '<div class="preview-card__title"></div><div class="preview-card__excerpt"></div>';
    document.body.appendChild(card);
    return card;
  }

  function positionCard(target) {
    var rect = target.getBoundingClientRect();
    var scrollY = window.scrollY || window.pageYOffset;
    var scrollX = window.scrollX || window.pageXOffset;

    // Render off-screen first to measure
    card.style.left = '-9999px';
    card.style.top = '0';
    card.classList.add('is-visible');
    var cw = card.offsetWidth;
    var ch = card.offsetHeight;

    // Prefer below; flip above if not enough room
    var top = rect.bottom + scrollY + 8;
    var bottomRoom = (window.innerHeight - rect.bottom);
    if (bottomRoom < ch + 16 && rect.top > ch + 16) {
      top = rect.top + scrollY - ch - 8;
    }

    // Horizontal: align to left of target, clamp inside viewport
    var left = rect.left + scrollX;
    var maxLeft = window.innerWidth + scrollX - cw - 12;
    var minLeft = scrollX + 12;
    if (left > maxLeft) left = maxLeft;
    if (left < minLeft) left = minLeft;

    card.style.top = top + 'px';
    card.style.left = left + 'px';
  }

  function extractPreview(html) {
    // Parse HTML and find the prose body
    try {
      var doc = new DOMParser().parseFromString(html, 'text/html');
      var prose = doc.querySelector('.prose') || doc.querySelector('.markdown-body') || doc.body;
      var title = '';
      var titleEl = prose.querySelector('h1');
      if (titleEl) title = titleEl.textContent.trim();
      else if (doc.title) title = doc.title.split(' - ')[0].trim();

      // Walk siblings after the H1, gather paragraphs
      var node = titleEl ? titleEl.nextElementSibling : prose.firstElementChild;
      var pieces = [];
      var totalLen = 0;
      while (node && totalLen < 280) {
        if (node.tagName === 'P' || node.tagName === 'BLOCKQUOTE') {
          var text = node.textContent.trim();
          if (text) {
            pieces.push('<p>' + escapeHTML(text) + '</p>');
            totalLen += text.length;
          }
        } else if (/^H[1-6]$/.test(node.tagName)) {
          break;
        }
        node = node.nextElementSibling;
      }
      return { title: title, html: pieces.join('') };
    } catch (e) {
      return null;
    }
  }

  function escapeHTML(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function fetchPreview(href) {
    if (cache.has(href)) return Promise.resolve(cache.get(href));
    return fetch(href, { credentials: 'same-origin' })
      .then(function (r) { return r.ok ? r.text() : null; })
      .then(function (html) {
        if (!html) return null;
        var data = extractPreview(html);
        cache.set(href, data);
        return data;
      })
      .catch(function () { return null; });
  }

  function showPreview(target) {
    var href = target.getAttribute('href');
    if (!href) return;
    var url;
    try { url = new URL(href, window.location.href); } catch (e) { return; }
    if (url.origin !== window.location.origin) return;
    if (url.pathname === window.location.pathname) return;

    fetchPreview(url.pathname + url.search).then(function (data) {
      if (!data || target !== currentTarget) return;
      makeCard();
      card.querySelector('.preview-card__title').textContent = data.title || '';
      card.querySelector('.preview-card__excerpt').innerHTML = data.html || '';
      if (!data.html && !data.title) return;
      positionCard(target);
    });
  }

  function hidePreview() {
    if (card) card.classList.remove('is-visible');
    currentTarget = null;
  }

  function initHoverPreviews() {
    // Skip on touch-primary devices
    var isCoarse = window.matchMedia && window.matchMedia('(hover: none)').matches;
    if (isCoarse) return;

    var prose = document.querySelector('.prose');
    if (!prose) return;

    function isInternalPageLink(a) {
      var href = a.getAttribute('href');
      if (!href) return false;
      if (href.startsWith('#')) return false;
      if (href.startsWith('mailto:') || href.startsWith('tel:')) return false;
      try {
        var u = new URL(href, window.location.href);
        if (u.origin !== window.location.origin) return false;
        return /\.html?($|[?#])/.test(u.pathname) || u.pathname.endsWith('/');
      } catch (e) { return false; }
    }

    prose.addEventListener('mouseover', function (e) {
      var a = e.target.closest('a');
      if (!a || !prose.contains(a)) return;
      if (!isInternalPageLink(a)) return;
      currentTarget = a;
      clearTimeout(hideTimer);
      clearTimeout(hoverTimer);
      hoverTimer = setTimeout(function () { showPreview(a); }, 220);
    });

    prose.addEventListener('mouseout', function (e) {
      var a = e.target.closest('a');
      if (!a) return;
      clearTimeout(hoverTimer);
      hideTimer = setTimeout(hidePreview, 180);
    });

    // Don't hide while pointer is over the card
    document.addEventListener('mouseover', function (e) {
      if (card && card.contains(e.target)) clearTimeout(hideTimer);
    });
    document.addEventListener('mouseout', function (e) {
      if (card && card.contains(e.target) && !card.contains(e.relatedTarget)) {
        hideTimer = setTimeout(hidePreview, 120);
      }
    });

    // Hide on scroll
    window.addEventListener('scroll', hidePreview, { passive: true });
  }

  // ---------- Heading anchors ----------

  function initHeadingAnchors() {
    var prose = document.querySelector('.prose');
    if (!prose) return;
    var hs = prose.querySelectorAll('h2[id], h3[id], h4[id]');
    hs.forEach(function (h) {
      if (h.querySelector('.header-anchor')) return;
      var id = h.id;
      if (!id) return;
      var a = document.createElement('a');
      a.className = 'header-anchor';
      a.href = '#' + id;
      a.setAttribute('aria-label', 'Anchor link to this section');
      a.style.cssText = 'margin-left:.4em;font-size:.85em;color:var(--ink-faint);';
      a.textContent = '¶';
      h.appendChild(a);
    });
  }

  // ---------- Index filter ----------

  function initIndexFilter() {
    var input = document.querySelector('[data-index-filter]');
    var list = document.querySelector('[data-index-list]');
    if (!input || !list) return;
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      var rows = list.querySelectorAll('[data-index-row]');
      rows.forEach(function (r) {
        var t = (r.getAttribute('data-search-text') || r.textContent).toLowerCase();
        r.classList.toggle('is-hidden', q !== '' && t.indexOf(q) === -1);
      });
    });
  }

  // ---------- Boot ----------

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
  function boot() {
    initDrawer();
    initHeadingAnchors();
    initHoverPreviews();
    initIndexFilter();
  }
})();
