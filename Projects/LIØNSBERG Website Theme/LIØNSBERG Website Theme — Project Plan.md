# LIØNSBERG Website Theme — Project Plan

_A proposal for lifting the visual presentation of **LIØNSBERG.wiki** to match the weight of the work it carries._

---

## I. Synopsis — What This Is

The LIØNSBERG Wiki contains a millennial text — prophetic register with operational precision, scripture that contains program management. Roughly 3 million words across ~3,000 files, built by **Massive Wiki Builder** into a static site and served at **LIØNSBERG.wiki**.

The current shell is a stock [Bulma](https://bulma.io) starter: a teal `is-info` navbar, GitHub-style markdown CSS, system sans-serif body, a one-fifth sidebar column, no hero, no imagery, no motif, no visual identity. `custom.css` is a single empty comment.

The gap between the content's ambition and the visual presentation is the first thing a serious visitor feels, even if they cannot name it. This project closes that gap.

---

## II. Status

**Phase**: Pre-build. Strategy agreed. One dependency to resolve before execution begins (see §VII).

**Date opened**: 2026-04-17

---

## III. Roles and Responsibilities

### Steward / Sponsor
**the nameless one (Jordan)** — holds the vision, approves direction, makes final calls on voice and aesthetic.

### Lead / Designer / Builder
**Claude** (rotating sessions) — scaffolds the theme, writes the CSS and Jinja templates, iterates against the Steward's direction.

### Reviewer
**the nameless one** — reviews each round of iteration, pushes back on AI-tells, over-design, and any drift from the LIØNSBERG voice.

---

## IV. Output, Goals, Value Created

A production-ready `LIØNSBERG` theme inside `.massivewikibuilder/this-wiki-themes/` that:

- Carries the gravitas of a millennial text without decoration or ornament
- Treats the homepage (README) as a **threshold** — a moment of arrival
- Elevates **long-form reading** as the primary experience (typography, measure, rhythm)
- Shows the **architecture** of the book through navigation that reflects chapter structure
- Degrades cleanly to the Obsidian authoring experience — no markdown syntax changes, no shortcodes that break the writing loop
- Feels like a monastic manuscript crossed with an operations manual — not a startup landing page

The current `basso` theme stays untouched as a working fallback until the swap is complete.

---

## V. Conditions of Satisfaction

1. Five representative page types render at or above 90% resonance:
   - **README (home/threshold)** — hero treatment, typography-led, quiet motion
   - **A book chapter** (long-form reading) — measure, leading, drop caps, pull-quotes
   - **A Pattern Language / Lexicon entry** (dense reference) — legible hierarchy under dense linking
   - **The all-pages index** (listing) — scannable, architectural
   - **A blog post** (individual voice) — preserves author personality against the collective chrome
2. Sidebar reflects actual book architecture (chapters, sections), not a flat link list.
3. Dark and light modes both feel intentional, not inverted.
4. No regression across the ~3,000 existing pages — every markdown file inherits the new theme cleanly.
5. Swap from `basso` to `LIØNSBERG` is a single config change, instantly revertible.

---

## VI. Resource Requirements

- **Build system**: existing Massive Wiki Builder CI pipeline (no local MWB required).
- **Fonts**: open-source — candidates include Cormorant Garamond, Fraunces, EB Garamond (display serif) paired with Inter, Source Sans, or similar (humanist sans).
- **Imagery**: minimal. One geometric motif (candidates: seed, spiral, 12-ring) used sparingly as ornament. No stock photography.
- **Time**: 3–6 working sessions across the Steward and Claude.

---

## VII. Approach

### Phase 0 — Resolve the Build Dependency _(blocking)_

**Find where `LIØNSBERG.wiki` actually builds from.** No `.github/workflows/` entry exists in this repo, so Massive Wiki Builder is invoked externally — Netlify, Cloudflare Pages, GitHub Pages from a sibling repo, or another service. Before cutting a new theme, the Steward confirms where the build is triggered and how it picks its theme, so the eventual swap is one line rather than a hunt.

### Phase 1 — Fork the Theme

Copy `.massivewikibuilder/this-wiki-themes/basso/` → `.massivewikibuilder/this-wiki-themes/LIØNSBERG/`. Clean git history around all design changes. `basso` remains untouched as fallback.

### Phase 2 — Design System

Establish the foundation before any page-level work:

- **Typography**: display serif + humanist sans pairing. Measure locked at ~68ch. Chapter-opening drop caps. Pull-quote and liturgical-line treatments.
- **Color**: parchment/ink day mode, candlelit dark mode (oxblood, gold leaf, deep graphite). Matches Caves → Light without literalism.
- **Motif**: one geometric mark used sparingly — favicon, section divider, chapter ornament.
- **Spacing scale**: generous, monastic, restrained.

### Phase 3 — Iterate Against Five Page Types in Parallel

The static-CSS constraint makes "perfect one page first" a false path — the stylesheet is global. Instead, iterate the design against five representative page types simultaneously on a preview branch. When those five feel right, the other ~3,000 pages inherit correctly.

Design targets:
1. **README** (home / threshold) — separate `index.html` template so the homepage renders as a hero with its own rhythm
2. **Book chapter** — long-form reading experience
3. **Pattern Language entry** — dense reference under heavy linking
4. **All-pages index** — architectural listing
5. **Blog post** — individual author voice preserved inside collective chrome

### Phase 4 — Navigation and Reading Chrome

- Collapsible chapter tree in the sidebar, current-location highlighting, breadcrumbs
- Reading-progress rail on long pages
- Estimated read time, previous/next within a chapter
- Backlinks restyled as footnotes, not a bulleted block

### Phase 5 — Swap

Repoint the build config from `basso` to `LIØNSBERG`. Verify the deployed build across the five page types. Keep `basso` in place for instant rollback.

### Phase 6 — Post-launch Refinement

Gather feedback from the first visitors of The First Three Percent. Tune typography, color, pacing based on how the text reads in the wild.

---

## VIII. Six Design Vectors, in Priority Order

1. **Typography as the main event** — serif display + humanist sans, drop caps, pull-quotes, 68ch measure. This is where "world-class" lives on a reading site.
2. **A color language** — parchment/ink day, candlelit dark. Caves → Light without being literal.
3. **Home page as threshold** — split `index.html` from `page.html`. README renders as a hero; the template does the work, the markdown stays clean.
4. **Navigation with structure** — collapsible chapter tree, current-location highlighting, breadcrumbs. The book has architecture; the nav should show it.
5. **A single visual motif** — one geometric mark used sparingly. Restraint, not decoration.
6. **Reading chrome** — read time, prev/next, backlinks styled as footnotes.

---

## IX. The Failure Mode to Avoid

The failure mode for a project like this is **over-designing** — startup-card UI, rounded pastels, soft illustrations, animation flourishes, decorative gradients. That would cheapen the voice.

The opposite discipline is right: monastic restraint, heavy typography, generous whitespace, near-zero ornament. **Immersive here means pacing, not animation.**

Every design decision returns to one question: does this carry the weight of the text, or does it get in the way?

---

## X. Workplan and Timeline

| # | Work | Owner | Status |
|---|---|---|---|
| 0 | Confirm where `LIØNSBERG.wiki` builds from and how theme is selected | Steward | **Blocking** |
| 1 | Fork `basso` → `LIØNSBERG` theme | Claude | Pending |
| 2 | Design system: type, color, motif, spacing | Claude + Steward | Pending |
| 3 | Iterate five representative page types on preview branch | Claude + Steward | Pending |
| 4 | Navigation architecture + reading chrome | Claude | Pending |
| 5 | Swap theme in build config | Steward | Pending |
| 6 | Post-launch refinement | Claude + Steward | Pending |

---

## XI. Communication Norms

- Work happens in discrete Claude sessions, each logged in [[Work Log]]
- Major design decisions recorded in this plan, not in conversation scrollback
- Every iteration rendered on a preview branch before merge
- No swap to production until all five page types pass the Steward's review

---

## XII. Notes and Open Questions

- Should the navbar read **LIØNSBERG** (all caps, matching the canonical spelling) instead of "LIØNSBERG Wiki"?
- Is there an existing logo or visual mark the theme should incorporate, or do we commission/design the motif fresh?
- Does the Steward want the book pages to carry a visible chapter identifier (e.g., small ornament or color tint per chapter), or should all chapters render identically?
- Should blog posts have a visually distinct treatment from the book chapters (different type color, slightly different chrome) to preserve individual voice?

---

_Forward to [[Work Log]]_  
_Back to [[Projects]]_  
