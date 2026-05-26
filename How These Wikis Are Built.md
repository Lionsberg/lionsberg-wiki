# How These Wikis Are Built

A practical guide to how this wiki and its sibling, [superorganism.earth](https://superorganism.earth), are built, themed, and deployed. Written so future stewards can do this again — or do it differently with full understanding of what we learned.

---

## The shape of the commons

Two wikis. One look. Open-source themes shared between them.

| Wiki | Repo | Builder | Host | Theme |
|------|------|---------|------|-------|
| LIØNSBERG | `LIØNSBERG/LIØNSBERG-wiki` | Massive Wiki Builder (`mwb.py`) | Netlify | `andante` |
| superorganism.earth | `The-Currently-Nameless-Superorganism/superorganism.earth` | MarkPub (pinned to `0.4.5`) | Cloudflare Pages | `andante` |

Both wikis are Obsidian vaults checked into git. A static-site generator turns the markdown into HTML on each push. The HTML is served from the host's CDN. There is no database, no server, no Wordpress, no admin panel. Editing the wiki means editing markdown files in the repo.

This is the simplest possible architecture and it is intentional. **The text is the truth, the build is reproducible, and the hosting is incidental.**

---

## The theme: `andante`

`andante` is a typography-first theme built from first principles for substantive, long-form, interlinked material. Italian for *at a walking pace.*

**What's in it:**
- Source Serif 4 body type (variable font, optical sizes 8–60), Inter for UI labels
- Hamburger drawer sidebar, opens left, dismisses on Esc / scrim click
- Hover previews on internal wikilinks — fetches target page, shows title + first paragraphs in a floating card
- "Referenced by" backlinks at the bottom of every page (the lattice made visible)
- Lunr-powered search with deep-linkable `?q=` queries
- Automatic dark mode via `prefers-color-scheme` (no toggle, no flash)
- Print-ready stylesheet — `⌘P` produces a clean PDF
- WCAG-AA contrast, focus-visible rings, reduced-motion support
- ~23 KB CSS, ~9 KB JS, no runtime CDN dependencies beyond Google Fonts

**Design principle:** the theme should disappear into the reading. Beauty as a side effect of right proportions, right typography, right restraint. No carousels, no popups, no banners, no estimated-reading-time badges.

The theme lives in two places (same content, identical files):
- `LIØNSBERG-wiki/.massivewikibuilder/this-wiki-themes/andante/`
- `superorganism.earth/.markpub/this-website-themes/andante/`

When the theme is updated in one place, the same change should be copied to the other.

---

## How to apply `andante` to a new wiki

### For a Massive Wiki Builder wiki

1. Copy the `andante/` directory into `.massivewikibuilder/this-wiki-themes/andante/`
2. In `netlify.toml`, change the build command's `-t` flag to `../this-wiki-themes/andante`
3. Commit and push
4. Watch Netlify build — ~3–5 minutes for a medium-large wiki

### For a MarkPub wiki

1. Copy the `andante/` directory into `.markpub/this-website-themes/andante/`
2. **Pin `markpub==0.4.5` in `.markpub/requirements.txt`** — see "Why we pin" below
3. Update the build script to pass `--templates ./this-website-themes/andante`
4. Make sure pip-installed scripts are findable on PATH — see "PATH gotcha" below
5. Commit and push

---

## Why we pin `markpub==0.4.5`

`markpub` 2.x (current latest on PyPI) introduced a companion package `markpub-themes` and changed how theme statics are handled. In 0.4.5 (and the earlier `mwb.py`), the theme's `static/` directory contents are copied directly to the output root — so `theme/static/andante-static/css/andante.css` lands at `/andante-static/css/andante.css`, exactly where the rendered HTML expects it.

In 2.x, theme statics land under `output/markpub_static/`, which means our `/andante-static/...` references 404 and the page renders unstyled. Until `andante` is adapted to the 2.x convention, we pin to 0.4.5.

When future-us is ready to migrate, the work is:
1. Read 2.x source to understand the new convention
2. Restructure `andante/static/` accordingly
3. Update CSS/JS references in `_header.html`
4. Migrate both wikis together
5. Unpin

Estimated effort: one focused 2–3 hour session.

---

## The PATH gotcha (Cloudflare + Python 3.13)

Cloudflare Pages now defaults to Python 3.13. With 3.13, `pip install` puts script binaries (like `markpub`) into `~/.local/bin`, which is **not on `PATH`** by default in Cloudflare's build environment. The build fails at `markpub: command not found` — but the previous deploy stays live, so the symptom looks like "the site reverted to the old theme."

**Fix in `build.sh`:** after `pip install`, explicitly add Python's user-bin directory to PATH:

```bash
PYTHON_USER_BIN=$(python3 -c "import site; print(site.USER_BASE + '/bin')")
PYTHON_SYS_BIN=$(python3 -c "import sysconfig; print(sysconfig.get_path('scripts'))")
export PATH="$PYTHON_USER_BIN:$PYTHON_SYS_BIN:$HOME/.local/bin:$PATH"
```

This is invisible work — the kind that takes hours to debug if you don't know it exists. Now you do.

---

## Build hygiene we adopted

A few practices that paid for themselves the day we needed them:

1. **Pin major dependencies.** Don't trust `latest` for the engine of your wiki. The day a 2.x release breaks conventions, you'll wish you had pinned.

2. **Verify the build's own output.** Our `build.sh` checks that the andante CSS file actually landed in the output directory and that the rendered HTML actually references it. If either fails, the script exits with a clear error rather than silently shipping a broken site.

3. **Add a marker comment to the rendered HTML.** When something looks wrong on the live site, view-source for the marker (`<!-- ANDANTE THEME ACTIVE -->`) tells you instantly whether the deploy is what you think it is, or whether you're looking at an older cached version.

4. **Fail loudly, not silently.** When a build fails on a hosted CI, the previous successful deploy stays live. That's good — but it means you can spend an hour wondering why the site looks "old" when the real answer is "the new build hasn't deployed because it's been failing." Loud, descriptive errors save time.

5. **Build the same way locally and in CI.** If `markpub build -i .. -o ../output --templates ./this-website-themes/andante` works on your laptop, the same command should work on Cloudflare. When local and CI diverge, suspect the environment first (Python version, PATH, missing dependencies).

---

## How the wikis are connected

The two wikis are sibling commons, not duplicates. LIØNSBERG holds the broader pattern language and program; superorganism.earth holds the constitutional package and guidebook for emergence. They link to each other via web URLs, not wikilinks (since they're separate vaults).

Themes, however, are shared. The theme is part of the technical commons. If you improve `andante` in one repo, copy the change to the other so they stay visually identical.

Eventually, `andante` will be offered upstream to the MarkPub community as a contribution. At that point, both wikis can pull it as a normal theme dependency rather than vendoring the source. Until then, vendoring is fine.

---

## When something looks wrong

Run this checklist:

1. **View the rendered source** of the live page (`⌘⌥U` in Safari, `Ctrl+U` elsewhere). Look for the marker comment. If it's missing, the build failed and you're seeing a stale deploy.
2. **Check the build log.** Netlify Deploys tab or Cloudflare Pages Deployments tab. Read from the bottom up — the last error is the proximate cause.
3. **Hard refresh.** `⌘⇧R` (desktop) or close-and-reopen the tab on iOS. Edge caches can serve stale CSS for ~60 seconds after a fresh deploy.
4. **Build locally.** Clone, install deps, run the build command. If it works locally and not in CI, it's an environment issue (PATH, Python version, network).
5. **Check pinned versions.** Did `pip` upgrade `markpub` past `0.4.5`? Did the host's default Python version change?

---

## License

The `andante` theme is MIT-licensed. The wiki content carries its own license per repo (LIØNSBERG: CC-BY 4.0; superorganism.earth: CC-BY-SA 4.0).

---

*Written 2026-05-02 by the team that learned all of this the hard way, so the next team doesn't have to.*
