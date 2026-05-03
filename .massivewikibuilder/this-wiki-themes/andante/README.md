# andante

A MarkPub theme for substantive, long-form, interlinked material. *Italian: at a walking pace.* Patient, unhurried, dignified.

This theme is built for wikis where the writing matters more than the chrome — constitutions, guidebooks, pattern languages, personal knowledge bases, wisdom literature. It treats typography as architecture and aims to disappear into the reading.

## Design principles

1. **The theme should disappear into the reading.** Every pixel justifies itself by serving comprehension, contemplation, or trust. Beauty as a side effect of right proportions, right typography, right restraint.
2. **Calm by design.** No animations beyond gentle hovers, no carousels, no popups, no reading-time badges, no related-posts blocks, no flashing dark-mode toggles. The page just appears.
3. **Wiki-native.** Hover-previews on internal links, "Referenced by" backlinks at the bottom of every page, sidebar drawer navigation, and an integrated search page.
4. **Mobile-first, desktop-elegant.** Reads beautifully at every width.
5. **Print-ready.** Hit ⌘P and you get a clean, paginated PDF.
6. **Accessible.** WCAG AA contrast, focus-visible rings, reduced-motion support, semantic HTML.
7. **Honest performance.** ~30KB CSS, ~10KB JS, no required external CDNs at runtime (web fonts only). Lighthouse 100.

## What's included

- `page.html` — main page template with sidebar drawer, content column, and backlinks
- `all-pages.html` — index of all pages with client-side filter
- `recent-pages.html` — recent changes list
- `search.html` — Lunr-powered search with deep-linkable `?q=` queries
- `wiki.html` — minimal home (rarely used; `README.md` typically becomes the home)
- `_header.html`, `_navbar.html`, `_drawer.html`, `_footer.html`, `_javascript.html` — partials
- `static/andante-static/css/andante.css` — full stylesheet, custom-property tokens, dark mode, print
- `static/andante-static/js/andante.js` — drawer, hover-previews, heading anchors, index filter

## Typography

- **Body**: Source Serif 4 (variable, optical sizes 8–60), with system serif fallbacks
- **UI / labels**: Inter (400, 500, 600)
- **Code**: System monospace (`ui-monospace`, SF Mono, Menlo, JetBrains Mono…)

OpenType features enabled by default: kerning, ligatures, contextual alternates, and oldstyle proportional figures in body text. Tabular figures in tables.

## Color

Light mode is a warm parchment (`#fbfaf6`) with deep ink and a burnt-sienna accent. Dark mode uses the same palette inverted with a softer warm tan. Both follow `prefers-color-scheme` automatically — no toggle.

## Hover previews

Hovering an internal link for ~220ms fetches the target page, extracts the title and first paragraphs, and shows them in a small floating card. Cached in memory. Skipped on touch-primary devices. Hides on scroll, escape, or mouse-out.

## Sidebar drawer

The drawer is hidden by default at all widths and opens via the hamburger button. The current page is highlighted. Closes on scrim click, close button, or `Escape`.

## Browser support

Modern evergreen browsers (Chrome, Firefox, Safari, Edge — last 2 versions). Graceful degradation: with JS disabled, the site still reads cleanly — just no drawer toggle and no hover previews.

## License

MIT.

## Origin

Built for [superorganism.earth](https://superorganism.earth) by the (Currently Nameless) Superorganism interim launch team in 2026, then offered back to the MarkPub community in the spirit of mutual contribution.
