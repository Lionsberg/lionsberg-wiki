#!/usr/bin/env python3
"""Build gameboard.html — the living Gameboard — from The Commons cards.
Run from repo root:  python3 .markpub/build-gameboard.py
Agent-optional: any human can run this, or hand-edit the output.
"""
import os, re, math, datetime, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today()

# ---------- season geometry (2026 turnings) ----------
TURNINGS = [  # (date, season starting)
    (datetime.date(2025,12,21), "Winter"),
    (datetime.date(2026, 3,20), "Spring"),
    (datetime.date(2026, 6,21), "Summer"),
    (datetime.date(2026, 9,22), "Autumn"),
    (datetime.date(2026,12,21), "Winter"),
]
THEMES = {
  "light": dict(out="gameboard.html",
    colors={"Spring":"#5E8639","Summer":"#D79417","Autumn":"#B4552D","Winter":"#28609E"},
    surface="#FAF5EA", card="#FFFDF6", edge="#E7DCC4", ink="#2B2419", soft="#6B6152",
    gold="#D79417", gold_deep="#A8720C", gold_ink="#241B08", rust="#B4552D",
    label_fill="#FAF5EA", glow="", stars="", body_extra=""),
  "cosmic": dict(out="gameboard.html",
    colors={"Spring":"#7EA260","Summer":"#935B00","Autumn":"#C98063","Winter":"#3C6BA1"},
    surface="#0D1424", card="#16203A", edge="#2A3A5E", ink="#EDE6D6", soft="#B8AE97",
    gold="#E8B14B", gold_deep="#B8841F", gold_ink="#1A1408", rust="#E09070",
    label_fill="#0D1424",
    glow="filter:drop-shadow(0 0 14px rgba(232,177,75,.55));",
    stars="STARFIELD", body_extra="text-shadow:none;"),
}
COLORS = THEMES["light"]["colors"]  # overridden per theme in render()

def season_now():
    for (d1,s),(d2,_) in zip(TURNINGS, TURNINGS[1:]):
        if d1 <= TODAY < d2:
            frac = (TODAY-d1).days / (d2-d1).days
            return s, frac, (d2-TODAY).days, d2
    return "Summer", 0.5, 0, TURNINGS[3][0]

SEASON, FRAC, DAYS_TO_TURN, NEXT_TURN = season_now()

import random
def starfield_css():
    rng = random.Random(369)
    shadows=[]
    for _ in range(140):
        x=rng.randint(0,1600); y=rng.randint(0,2400); r=rng.choice([1,1,1,2])
        o=rng.choice([".9",".7",".5",".35"])
        shadows.append(f"{x}px {y}px 0 {r}px rgba(237,230,214,{o})")
    return ("body::before{content:'';position:absolute;inset:0;pointer-events:none;"
            "width:1px;height:1px;border-radius:50%;box-shadow:" + ",".join(shadows) + ";}"
            "body{position:relative;overflow-x:hidden;}")

# wheel: 12 o'clock = Winter solstice; clockwise Winter, Spring, Summer, Autumn (90° each)
SEASON_START_ANGLE = {"Winter":0, "Spring":90, "Summer":180, "Autumn":270}
NOW_ANGLE = SEASON_START_ANGLE[SEASON] + FRAC*90

def pol(cx, cy, r, ang_deg):
    a = math.radians(ang_deg - 90)  # 0° at 12 o'clock, clockwise
    return cx + r*math.cos(a), cy + r*math.sin(a)

def arc_path(cx, cy, r, a1, a2):
    x1,y1 = pol(cx,cy,r,a1); x2,y2 = pol(cx,cy,r,a2)
    large = 1 if (a2-a1)%360 > 180 else 0
    return f"M {x1:.1f} {y1:.1f} A {r} {r} 0 {large} 1 {x2:.1f} {y2:.1f}"

# ---------- read The Commons ----------
def cards(folder):
    out=[]
    for p in sorted(glob.glob(os.path.join(ROOT,"The Commons",folder,"*.md"))):
        if "Template" in os.path.basename(p): continue
        s=open(p,encoding="utf-8").read()
        d={"name": os.path.basename(p)[:-3]}
        for k in ("place","region","open","kind","reach","purpose","members","pledged","flame","sponsor","circle","gifts","state","formed","quest","commitment","season"):
            m=re.search(rf"^{k}::\s*(.+)$", s, re.M)
            if m: d[k]=re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", m.group(1)).strip()
        out.append(d)
    return out

players = cards("Players")
circles = cards("Circles")
groups  = cards("Groups")
quests  = cards("Quests")
stories = cards("Stories")

def esc(x): return html.escape(x or "")

# ---------- render (both themes) ----------
C, R = 330, 240
ARC_W = 58
GAP = 1.2

def build_wheel(t):
    colors = t["colors"]
    arcs, labels = [], []
    for sname, a0 in SEASON_START_ANGLE.items():
        now = sname == SEASON
        cls = "arc now-arc" if now else "arc"
        dim = "" if now else ' opacity="0.4"'
        order = ["Winter","Spring","Summer","Autumn"].index(sname)
        arcs.append(f'<path class="{cls}" data-season="{sname}" style="animation-delay:{0.15*order:.2f}s" pathLength="100" d="{arc_path(C,C,R,a0+GAP,a0+90-GAP)}" stroke="{colors[sname]}" stroke-width="{ARC_W}" fill="none" stroke-linecap="butt"{dim}/>')
        lx, ly = pol(C, C, R, a0+45)
        lcls = "season-label now" if now else "season-label"
        labels.append(f'<text x="{lx:.0f}" y="{ly:.0f}" class="{lcls}" data-season="{sname}" text-anchor="middle" dominant-baseline="middle">{sname.upper()}</text>')
    ticks = []
    for d, sname in TURNINGS[:4]:
        a = SEASON_START_ANGLE[sname]
        x1,y1 = pol(C,C,R+ARC_W/2+4,a); x2,y2 = pol(C,C,R-ARC_W/2-4,a)
        lx,ly = pol(C,C,R+ARC_W/2+26,a)
        ticks.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" class="tick"/>'
                     f'<text x="{lx:.0f}" y="{ly:.0f}" class="tick-label" text-anchor="middle" dominant-baseline="middle">{d.strftime("%b %-d")}</text>')
    fx, fy = pol(C, C, R, NOW_ANGLE)
    flame = (f'<g class="flame-now" data-built-angle="{NOW_ANGLE:.2f}">'
             f'<circle cx="{fx:.0f}" cy="{fy:.0f}" r="26" class="flame-halo"/>'
             f'<circle cx="{fx:.0f}" cy="{fy:.0f}" r="20" fill="{t["surface"]}" stroke="{t["gold_deep"]}" stroke-width="1.5"/>'
             f'<g class="flame-art" transform="translate({fx:.0f},{fy+9:.0f}) scale(0.62)"><g class="flick">'
             f'<path fill="url(#flameOuter)" d="M0,-30 C10,-16 15,-8 15,2 C15,13 8,20 0,20 C-8,20 -15,13 -15,2 C-15,-6 -9,-12 -6,-18 C-4,-12 2,-12 0,-30 Z"/>'
             f'<path fill="url(#flameInner)" d="M0,-14 C5,-7 8,-3 8,3 C8,10 4,14 0,14 C-4,14 -8,10 -8,3 C-8,-2 -4,-7 0,-14 Z"/>'
             f'</g></g></g>')
    return f"""<svg viewBox="0 0 {2*C} {2*C}" role="img" aria-label="The wheel of the year. It is {SEASON} — {DAYS_TO_TURN} days until the turning on {NEXT_TURN.strftime('%B %-d')}.">
<defs>
<radialGradient id="flameOuter" cx="50%" cy="70%" r="80%"><stop offset="0%" stop-color="#F7DE9A"/><stop offset="45%" stop-color="#E8A62B"/><stop offset="100%" stop-color="#B4552D"/></radialGradient>
<radialGradient id="flameInner" cx="50%" cy="75%" r="80%"><stop offset="0%" stop-color="#FFF6DC"/><stop offset="100%" stop-color="#F2C154"/></radialGradient>
<radialGradient id="oneGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="rgba(232,177,75,0.28)"/><stop offset="70%" stop-color="rgba(232,177,75,0.06)"/><stop offset="100%" stop-color="rgba(232,177,75,0)"/></radialGradient>
</defs>
<circle cx="{C}" cy="{C}" r="{R-ARC_W/2-6}" fill="url(#oneGlow)"/>
{''.join(arcs)}{''.join(ticks)}{''.join(labels)}
<text x="{C}" y="{C-74}" class="c-season">2026 · SEASON 1</text>
<text x="{C}" y="{C-46}" class="c-name">The Great Game Begins</text>
<text x="{C}" y="{C+14}" class="c-one">ØNE</text>
<text x="{C}" y="{C+58}" class="c-q">Does this make life</text>
<text x="{C}" y="{C+84}" class="c-q">a little more like Heaven?</text>
{flame}
</svg>"""

BOARD_CAP = 9

def player_cards(limit=None):
    out = []
    shown = players if limit is None else players[:limit]
    for pl in shown:
        url = "/The_Commons/Players/" + pl["name"].replace(" ", "_") + ".html"
        out.append(f"""<a class="card stand" href="{url}">
      <div class="flame-mark">🔥</div>
      <h3>{esc(pl["name"])}</h3>
      <p class="meta">{esc(pl.get("place",""))}{(" · " + esc(pl["region"])) if pl.get("region") else ""}{(" · " + esc(pl["state"])) if pl.get("state") else ""}</p>
      <p class="line" style="font-size:16px;color:var(--ink-soft)">{esc(pl.get("gifts",""))}</p>
      <p class="line">Flame passed by <strong>{esc(pl.get("flame","—"))}</strong></p>
      <p class="line">Pledged · {esc(pl.get("pledged","—"))}</p>
    </a>""")
    if limit is not None and len(players) > limit:
        out.append(f'<a class="card ghost" href="/players.html"><h3>… and {len(players)-limit} more</h3><p class="line">See the whole field of Players →</p></a>')
    out.append("""<a class="card ghost" href="/The_Pledge.html">
      <div class="flame-mark dim">🔥</div>
      <h3>Your name belongs here</h3>
      <p class="line">Accept the Invitation · attend a gathering ·<br>make your Pledge — and stand with us.</p>
    </a>""")
    return "\n".join(out)

def simple_cards(items, folder, limit=None):
    out = []
    shown = items if limit is None else items[:limit]
    for c in shown:
        bits = " · ".join(esc(c[k]) for k in ("place","region","season","state") if c.get(k))
        if c.get("open","").lower().startswith("y"): bits += " · open to new members"
        url = f"/The_Commons/{folder}/" + c["name"].replace(" ", "_") + ".html"
        out.append(f'<a class="card" href="{url}"><h3>{esc(c["name"])}</h3><p class="meta">{bits}</p></a>')
    if limit is not None and len(items) > limit:
        out.append(f'<a class="card ghost" href="/{folder.lower()}.html"><h3>… and {len(items)-limit} more</h3><p class="line">See them all →</p></a>')
    return "\n".join(out)

GHOSTS = {
 "circles": """<div class="card ghost still"><h3>The first Circles are forming now</h3>
  <p class="line">Yours will appear here as it seals — visible to All,<br>so the Game can see itself grow.</p></div>""",
 "groups": """<div class="card ghost still"><h3>The Groups will weave here</h3>
  <p class="line">Networks, councils, and guilds — aggregations beyond<br>three-to-thirteen — joined by mutual consent, written on both cards.</p></div>""",
 "quests": """<div class="card ghost still"><h3>The first Quests await their Circles</h3>
  <p class="line">One tangible act of goodwill, each season —<br>real, achievable, meaningful, together.</p></div>""",
 "stories": """<div class="card ghost still"><h3>The first harvest comes at the Equinox</h3>
  <p class="line">Every Quest becomes a Story; every Story becomes<br>a Prophesy of even greater things to come.</p></div>""",
}

n_players, n_circles = len(players), len(circles)

def render(t, other_link=None, other_name=None):
    wheel = build_wheel(t)
    stars = starfield_css() if t["stars"] else ""
    glow_css = f'.now-arc,.flame-now {{ {t["glow"]} }}' if t["glow"] else ""
    skin_line = f'  <p class="skin"><a href="{other_link}">{other_name}</a></p>\n' if other_link else ""
    circles_html = simple_cards(circles, "Circles", BOARD_CAP) or GHOSTS["circles"]
    groups_html = simple_cards(groups, "Groups", BOARD_CAP) or GHOSTS["groups"]
    quests_html  = simple_cards(quests, "Quests", BOARD_CAP) or GHOSTS["quests"]
    stories_html = simple_cards(stories, "Stories", BOARD_CAP) or GHOSTS["stories"]
    HTML = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Gameboard — The Great Game of LIØNSBERG</title>
<meta name="description" content="The living Gameboard of The Great Game of LIØNSBERG — who stands, the Circles, the Quests, the Stories, the season, and the Score.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root {{ --surface:{t["surface"]}; --ink:{t["ink"]}; --ink-soft:{t["soft"]}; --gold:{t["gold"]}; --gold-deep:{t["gold_deep"]};
  --rust:{t["rust"]}; --card:{t["card"]}; --edge:{t["edge"]}; }}
* {{ box-sizing:border-box; margin:0; }}
html {{ scroll-behavior:smooth; }}
body {{ color:var(--ink); font-family:"Source Serif 4", Georgia, serif; font-size:20px; line-height:1.6;
  background:#090E1B;
  background-image:radial-gradient(1400px 900px at 50% -12%, #22345C 0%, #131E38 38%, #0D1424 62%, #090E1B 100%);
  background-repeat:no-repeat; background-color:#090E1B; }}
{stars}
body::after {{ content:''; position:absolute; inset:0; pointer-events:none; width:2px; height:2px; border-radius:50%;
  box-shadow: 240px 180px 0 1px rgba(245,233,200,.9), 1210px 340px 0 2px rgba(245,233,200,.8), 620px 90px 0 1px rgba(245,233,200,.85),
   940px 700px 0 2px rgba(245,233,200,.75), 150px 900px 0 1px rgba(245,233,200,.8), 1420px 1180px 0 1px rgba(245,233,200,.9),
   420px 1500px 0 2px rgba(245,233,200,.7), 1080px 1740px 0 1px rgba(245,233,200,.85), 760px 2100px 0 2px rgba(245,233,200,.75);
  animation: twinkle 5.5s ease-in-out infinite alternate; }}
@keyframes twinkle {{ from {{ opacity:.55; }} to {{ opacity:1; }} }}
{glow_css}
.flame-halo {{ fill:rgba(232,177,75,.16); }}
.flick {{ animation: flick 2.4s ease-in-out infinite alternate; transform-box:fill-box; transform-origin:50% 85%; }}
@keyframes flick {{ from {{ transform:scale(1); }} to {{ transform:scale(1.07) rotate(1.5deg); }} }}
.arc {{ stroke-dasharray:100; stroke-dashoffset:100; animation: draw 1.4s cubic-bezier(.6,0,.3,1) forwards; }}
@keyframes draw {{ to {{ stroke-dashoffset:0; }} }}
.wrap {{ max-width:920px; margin:0 auto; padding:34px 22px 70px; position:relative; }}
header {{ text-align:center; padding:36px 0 6px; }}
header .kicker {{ font-family:Inter,sans-serif; font-size:13.5px; letter-spacing:.34em; color:var(--gold); text-transform:uppercase; opacity:.9; }}
h1 {{ font-size:clamp(52px,9vw,88px); font-weight:700; letter-spacing:.005em; margin:10px 0 4px; line-height:1.05;
  background:linear-gradient(180deg,#F7EED6 20%, #E8B14B 85%); -webkit-background-clip:text; background-clip:text; color:transparent;
  text-shadow:0 0 60px rgba(232,177,75,.18); }}
header .questions {{ font-style:italic; color:var(--ink-soft); font-size:19px; letter-spacing:.02em; }}
.welcome-line {{ text-align:center; font-style:italic; font-size:19.5px; color:var(--ink-soft); max-width:640px; margin:18px auto 0; line-height:1.7; }}
.welcome-line a {{ color:var(--gold); text-decoration:none; border-bottom:1px solid rgba(232,177,75,.45); transition:border-color .25s; }}
.welcome-line a:hover {{ border-color:var(--gold); }}
.wheel {{ max-width:640px; margin:26px auto 0; position:relative; }}
.wheel::before {{ content:''; position:absolute; inset:-12%; border-radius:50%; pointer-events:none;
  background:radial-gradient(circle, rgba(232,177,75,.13) 0%, rgba(60,107,161,.10) 45%, rgba(0,0,0,0) 70%); filter:blur(24px); }}
.wheel svg {{ width:100%; height:auto; display:block; position:relative; }}
.season-label {{ font-family:Inter,sans-serif; font-size:18px; font-weight:600; letter-spacing:.22em; fill:{t["ink"]}; opacity:.85; }}
.season-label.now {{ fill:#FFF8E6; }}
.tick {{ stroke:#0D1424; stroke-width:3; }}
.tick-label {{ font-family:Inter,sans-serif; font-size:13.5px; letter-spacing:.06em; fill:var(--ink-soft); }}
.c-season {{ font-family:Inter,sans-serif; font-size:14.5px; letter-spacing:.3em; fill:var(--gold); text-anchor:middle; }}
.c-name {{ font-size:21px; font-style:italic; fill:var(--ink-soft); text-anchor:middle; }}
.c-one {{ font-size:58px; font-weight:700; fill:var(--gold); text-anchor:middle; }}
.c-q {{ font-size:19px; font-style:italic; fill:var(--ink); text-anchor:middle; }}
.sky-line {{ text-align:center; font-style:italic; color:var(--ink-soft); font-size:17.5px; margin:14px 0 0; opacity:.85; }}
.now-line {{ text-align:center; font-size:21.5px; margin:10px 0 4px; }}
.now-line strong {{ color:var(--rust); }}
.actions {{ display:flex; flex-wrap:wrap; gap:13px; justify-content:center; margin:34px 0 8px; }}
.btn {{ font-family:Inter,sans-serif; font-weight:600; font-size:18.5px; text-decoration:none;
  padding:15px 25px; border-radius:15px; min-height:44px; display:inline-flex; align-items:center; gap:10px;
  transition:transform .22s ease, box-shadow .22s ease, border-color .22s ease; }}
.btn.primary {{ background:linear-gradient(135deg,#F2C86B 0%, #D79417 70%); color:{t["gold_ink"]};
  border:1px solid rgba(255,230,170,.6); box-shadow:0 4px 26px rgba(232,177,75,.35); }}
.btn.quiet {{ background:rgba(22,32,58,.55); color:var(--ink); border:1px solid rgba(232,177,75,.18);
  backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px); }}
.btn:hover {{ transform:translateY(-2px); box-shadow:0 8px 32px rgba(232,177,75,.30); border-color:rgba(232,177,75,.55); }}
.update-row {{ text-align:center; font-size:19px; margin:4px 0 0; }}
.update-row a {{ color:var(--gold); text-decoration:none; font-family:Inter,sans-serif; }}
section {{ margin-top:66px; opacity:0; transform:translateY(22px); transition:opacity .8s ease, transform .8s ease; }}
section.in {{ opacity:1; transform:none; }}
h2 {{ font-size:30px; letter-spacing:.015em; display:inline-block; padding-bottom:7px; margin-bottom:6px; position:relative; }}
h2::after {{ content:''; position:absolute; left:0; bottom:0; height:2px; width:100%;
  background:linear-gradient(90deg, var(--gold), rgba(232,177,75,0)); }}
.h2link {{ text-decoration:none; color:inherit; }}
.h2link:hover h2 {{ color:var(--gold); }}
.sub {{ color:var(--ink-soft); font-style:italic; margin-bottom:18px; max-width:66ch; }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(255px,1fr)); gap:17px; }}
.card {{ background:rgba(22,32,58,.55); border:1px solid rgba(232,177,75,.13); border-radius:18px; padding:22px 24px;
  display:block; text-decoration:none; color:inherit; backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px);
  box-shadow:0 12px 34px rgba(0,0,0,.35); transition:transform .25s ease, border-color .25s ease, box-shadow .25s ease; }}
a.card:hover {{ transform:translateY(-4px); border-color:rgba(232,177,75,.5); box-shadow:0 16px 44px rgba(232,177,75,.14); }}
.card h3 {{ font-size:23.5px; margin:4px 0 2px; }}
.card .meta {{ color:var(--ink-soft); font-size:17px; }}
.card .line {{ font-size:17.5px; margin-top:7px; line-height:1.55; }}
.card.stand {{ border-color:rgba(232,177,75,.55); box-shadow:0 0 0 1px rgba(232,177,75,.25), 0 10px 40px rgba(232,177,75,.16); }}
.flame-mark {{ font-size:26px; }}
.flame-mark.dim {{ filter:grayscale(.6) opacity(.6); }}
.card.ghost {{ border-style:dashed; background:rgba(22,32,58,.25); }}
a.card.ghost:hover {{ border-color:var(--gold); }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(145px,1fr)); gap:15px; }}
.tile {{ background:rgba(22,32,58,.55); border:1px solid rgba(232,177,75,.13); border-radius:18px; padding:20px 14px; text-align:center;
  backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px); }}
.tile .num {{ font-size:42px; font-weight:700; line-height:1.1;
  background:linear-gradient(180deg,#F7EED6, #E8B14B); -webkit-background-clip:text; background-clip:text; color:transparent; }}
.tile .lab {{ font-family:Inter,sans-serif; font-size:14px; letter-spacing:.04em; color:var(--ink-soft); margin-top:5px; }}
.young {{ color:var(--ink-soft); font-style:italic; font-size:18px; margin-top:14px; }}
footer {{ margin-top:80px; border-top:1px solid rgba(232,177,75,.16); padding-top:26px; color:var(--ink-soft); font-size:17px; text-align:center; }}
footer a {{ color:var(--gold-deep); }}
.doors {{ margin-top:8px; }}
.skin {{ font-family:Inter,sans-serif; font-size:15px; }}
@media (prefers-reduced-motion: reduce) {{ *,*::before,*::after {{ animation:none !important; transition:none !important; }}
  section {{ opacity:1; transform:none; }} }}
@media print {{ .actions,.card.ghost,.skin {{ display:none; }} body {{ font-size:16px; background:#fff !important; color:#1C1710; }}
  body::before,body::after {{ display:none; }} .card,.tile {{ background:#fff; border-color:#bbb; color:#1C1710; box-shadow:none; }}
  .card .meta,.tile .lab,.sub,.young,footer {{ color:#555; }} .tile .num {{ color:#1C1710; -webkit-text-fill-color:#1C1710; }}
  .season-label {{ fill:#fff; }} .c-one {{ fill:#8A6A10; }} .c-q,.c-name,.c-season,.tick-label {{ fill:#333; }}
  .now-arc,.flame-now {{ filter:none; }} section {{ opacity:1; transform:none; }} h1 {{ color:#1C1710; -webkit-text-fill-color:#1C1710; text-shadow:none; }} }}
</style></head><body>
<div class="wrap">
<header>
  <div class="kicker">The Great Game of LIØNSBERG</div>
  <h1>The Gameboard</h1>
  <p class="questions">Who We Are · How We Are Questing · Where We Are Going · Why</p>
</header>

<p class="welcome-line">Welcome. The territory you are entering is vast, new, mythic, and unknown.<br>If you are just arriving, please enter through <a href="/README.html">The&nbsp;Gates</a> and walk with <a href="/LIØNSBERG_Wiki_Books/AURELLIØN's_Guide_to_LIØNSBERG/AURELLIØN's_Guide_to_LIØNSBERG.html">a&nbsp;Guide</a>.</p>

<div class="wheel">{wheel}</div>
<p class="sky-line" id="gb-sky">It is Summer in the northern sky, Winter in the southern — the turning is shared by All.</p>
<p class="now-line">🔥 <strong>You are here</strong> — <span id="gb-season">{SEASON}</span> of Season&nbsp;1 · <strong><span id="gb-days">{DAYS_TO_TURN}</span>&nbsp;days</strong> to <span id="gb-turnname">the Equinox Celebration &amp; Review</span>, <span id="gb-turndate">{NEXT_TURN.strftime("%B %-d")}</span>.</p>

<div class="actions">
  <a class="btn quiet" href="/LIØNSBERG_Wiki_Books/The_Story_of_LIØNSBERG/The_Story_of_LIØNSBERG.html">📖 Read the Story</a>
  <a class="btn quiet" href="/LIØNSBERG_Wiki_Books/The_Great_Game_of_LIØNSBERG/The_Great_Game_of_LIØNSBERG.html">🧭 Play the Game</a>
  <a class="btn quiet" href="/The_Invitation.html">🔥 Pass the Flame</a>
  <a class="btn primary" href="/The_Pledge.html">✍️ Make Your Pledge</a>
  <a class="btn quiet" href="/Reaching_Us.html">🤝 Get Help · Send Word</a>
</div>
<p class="update-row">Already playing? <a href="/Update_the_Board.html">🗓️ <strong>Update the Board</strong></a> — the two-minute weekly Turn.</p>

<section>
  <h2>The Gatherings</h2>
  <p class="sub">Where the Game meets face to face — invitations arrive by email via <a href="https://cocreatingheaven.substack.com/" style="color:var(--gold-deep)">the Substack</a>.</p>
  <div class="cards">
    <div class="card"><h3>🌅 Orientation Gatherings</h3><p class="line">Weekly, as the Game grows — hear the Story and the Game live, meet the others, ask everything.</p></div>
    <div class="card"><h3>🕊️ Sacred Spaces</h3><p class="line">Weekly gatherings for those playing the Game — held in trust, opened after orientation and the Pledge.</p></div>
    <div class="card"><h3>🍂 The Equinox Celebration &amp; Review</h3><p class="line">September 22 — the season's harvest: first Stories told, the OmniSpection, Season 2 begins.</p></div>
  </div>
</section>

<section>
  <a class="h2link" href="/players.html"><h2>Who Stands →</h2></a>
  <p class="sub">We stand together — openly, by name. {n_players} {"soul stands" if n_players==1 else "souls stand"} so far; the first, so that no one is asked to stand first. Every card carries its flame-line — the family tree of the Game, growing from ØNE outward.</p>
  <div class="cards">{player_cards(BOARD_CAP)}</div>
</section>

<section>
  <a class="h2link" href="/circles.html"><h2>The Circles →</h2></a>
  <p class="sub">Three to thirteen souls, sealed at the pace of trust.</p>
  <div class="cards">{circles_html}</div>
</section>

<section>
  <a class="h2link" href="/groups.html"><h2>The Groups →</h2></a>
  <p class="sub">Networks, councils, and guilds — weaving beyond the Circle, joined by mutual consent.</p>
  <div class="cards">{groups_html}</div>
</section>

<section>
  <a class="h2link" href="/quests.html"><h2>The Quests →</h2></a>
  <p class="sub">The work in play now — real, achievable, meaningful, together.</p>
  <div class="cards">{quests_html}</div>
</section>

<section>
  <a class="h2link" href="/stories.html"><h2>The Stories →</h2></a>
  <p class="sub">The living proof, harvested and told — every Story a Prophesy of greater things to come.</p>
  <div class="cards">{stories_html}</div>
</section>

<section>
  <a class="h2link" href="/The_Pledge.html"><h2>The Pledges →</h2></a>
  <p class="sub">What is coming — every Player's first Commitment, freshly chosen each season.</p>
  <div class="tiles">
    <a class="tile" style="text-decoration:none;color:inherit" href="/players.html"><div class="num">{n_players}</div><div class="lab">standing</div></a>
    <div class="tile"><div class="num">—</div><div class="lab">TEA pledged (hrs/wk)</div></div>
    <div class="tile"><div class="num">—</div><div class="lab">resources pledged</div></div>
    <div class="tile"><div class="num">—</div><div class="lab">gifts offered</div></div>
  </div>
</section>

<section>
  <a class="h2link" href="/The_Gameboard.html"><h2>The Score</h2></a>
  <p class="sub">What has flowed — the season's living record.</p>
  <div class="tiles">
    <div class="tile"><div class="num">{n_circles or "—"}</div><div class="lab">Circles sealed</div></div>
    <div class="tile"><div class="num">—</div><div class="lab">commitments kept</div></div>
    <div class="tile"><div class="num">—</div><div class="lab">value created</div></div>
    <div class="tile"><div class="num">{len(stories) or "—"}</div><div class="lab">Stories shared</div></div>
    <div class="tile"><div class="num">—</div><div class="lab">flames passed</div></div>
  </div>
  <p class="young">The first season is young. Every number here fills as the Turns flow — and the first moves are yours to make.</p>
</section>

<section>
  <h2>Program Management Basics</h2>
  <p class="sub">How the Game remembers — the ledgers behind the Board.</p>
  <div class="cards">
    <a class="card" href="/ØNE_Vision_and_Intent.html"><h3>🌟 ØNE Vision and Intent</h3><p class="line">The invariant above every plan: ØNE · Creator's Intent · Heaven for All, forever. Every how below may change; this line does not.</p></a>
    <a class="card" href="/Planning.html"><h3>🗺️ Planning</h3><p class="line">From the season to this week's promise — pull, don't push. Milestones and the Lookahead live here.</p></a>
    <a class="card" href="/The_Decision_Log.html"><h3>📜 Decision Log</h3><p class="line">What was decided, when, and why. <strong>Read before asking.</strong></p></a>
    <a class="card" href="/LIØNSBERG_Issue_Tracker.html"><h3>🪨 Issue Tracker</h3><p class="line">What blocks now, and what looms ahead. When your Circle cannot resolve it, log it — a named worry is a surprise unscheduled.</p></a>
    <a class="card" href="/Request_For_Guidance.html"><h3>🧭 Requests For Guidance</h3><p class="line">What is unclear. <strong>Ask before assuming</strong> — every good question improves the plans.</p></a>
    <a class="card" href="/Submittals.html"><h3>📬 Submittals</h3><p class="line">What awaits review and approval — proposals, tools, resources, and improvements offered to the whole.</p></a>
  </div>
  <p class="young">To add to any ledger: send word through <a href="/Reaching_Us.html" style="color:var(--gold-deep)">Reaching Us</a> or the Server — the stewards tend the record.</p>
</section>

<section>
  <h2>The Armory</h2>
  <p class="sub">What every Player carries — the aids of the Game.</p>
  <div class="cards">
    <a class="card" href="/LIØNSBERG_Wiki_Books/AURELLIØN's_Guide_to_LIØNSBERG/AURELLIØN's_Guide_to_LIØNSBERG.html"><h3>🕯️ The Guide</h3><p class="line">The one guide at the door — the whole territory, walked beside you.</p></a>
    <a class="card" href="/LIØNSBERG_Wiki_Books/The_LIØNSBERG_Playbook/The_LIØNSBERG_Playbook.html"><h3>🎼 The Playbook</h3><p class="line">The Plays — small choreography for every recurring moment in a Circle's life.</p></a>
    <a class="card" href="/LIØNSBERG_Wiki_Books/The_LIØNSBERG_System_Toolkit/The_LIØNSBERG_Toolkit.html"><h3>🛠️ The Toolkit</h3><p class="line">The instruments in hand — and the Forge, where what is missing gets made.</p></a>
    <a class="card" href="/The_LIØNSBERG_Resource_Library.html"><h3>📚 The Resource Library</h3><p class="line">The commons of provisions — open to all travelers, growing as each contributes.</p></a>
    <a class="card" href="/The_LIØNSBERG_Map_of_Maps.html"><h3>🌍 The Map of Maps</h3><p class="line">Who else is already awake and at work across the Earth — the fields where they gather.</p></a>
  </div>
</section>

<footer>
  <p><a href="/About_the_Gameboard.html" style="color:var(--gold)">What is this? — About the Gameboard</a></p>
  <p>This Board is kept in plain text, in the open record, tended by hand —
     the ledger behind it lives at <a href="/The_Gameboard.html">The Gameboard</a>.</p>
  <p class="doors"><a href="/search.html">🔍 Search the whole territory</a> · this season's chronicle: <a href="/2026_-_Season_1_-_The_Great_Game_Begins.html">2026 · Season 1</a></p>
  <p class="doors">Gatherings &amp; turnings announced via <a href="https://cocreatingheaven.substack.com/">the Substack</a> ·
     New here? Begin with <a href="/The_Invitation.html">The Invitation</a> and
     <a href="/LIØNSBERG_Wiki_Books/AURELLIØN's_Guide_to_LIØNSBERG/AURELLIØN's_Guide_to_LIØNSBERG.html">the Guide</a>.</p>
{skin_line}  <p>Made with love, for All · CC BY-SA 4.0 · board data tended {TODAY.strftime("%B %-d, %Y")} · the clock keeps itself</p>
</footer>
</div><script>
(function(){{
  var T=[["2025-12-21","Winter"],["2026-03-20","Spring"],["2026-06-21","Summer"],["2026-09-22","Autumn"],
         ["2026-12-21","Winter"],["2027-03-20","Spring"],["2027-06-21","Summer"],["2027-09-23","Autumn"],
         ["2027-12-21","Winter"],["2028-03-19","Spring"],["2028-06-20","Summer"],["2028-09-22","Autumn"],
         ["2028-12-21","Winter"],["2029-03-20","Spring"],["2029-06-21","Summer"],["2029-09-22","Autumn"],
         ["2029-12-21","Winter"],["2030-03-20","Spring"],["2030-06-21","Summer"],["2030-09-22","Autumn"]];
  var OPP={{Summer:"Winter",Winter:"Summer",Spring:"Autumn",Autumn:"Spring"}};
  var start={{Winter:0,Spring:90,Summer:180,Autumn:270}};
  function south(){{
    try{{var tz=Intl.DateTimeFormat().resolvedOptions().timeZone||"";
      return /Australia|Auckland|Fiji|Antarctica|Santiago|Buenos_Aires|Sao_Paulo|Montevideo|Asuncion|La_Paz|Lima|Johannesburg|Maputo|Harare|Windhoek|Gaborone|Maseru|Mbabane|Port_Moresby|Noumea|Pacific\/(Apia|Tongatapu|Rarotonga|Tahiti)/.test(tz);
    }}catch(e){{return false;}}
  }}
  var isSouth=south();
  var now=new Date(); var today=new Date(now.getFullYear(),now.getMonth(),now.getDate());
  for(var i=0;i<T.length-1;i++){{
    var d1=new Date(T[i][0]+"T00:00:00"), d2=new Date(T[i+1][0]+"T00:00:00");
    if(today>=d1&&today<d2){{
      var canon=T[i][1];                      // northern-canonical key
      var local=isSouth?OPP[canon]:canon;     // the viewer's sky
      var frac=(today-d1)/(d2-d1), days=Math.round((d2-today)/864e5);
      var m=d2.getMonth();
      var turn=(m===8)?"the Equinox Celebration & Review":(m===2)?"the March Equinox turning":(m===5)?"the June Solstice turning":"the December Solstice turning";
      var el=function(id){{return document.getElementById(id);}};
      if(el("gb-season"))el("gb-season").textContent=local;
      if(el("gb-days"))el("gb-days").textContent=days;
      if(el("gb-turnname"))el("gb-turnname").textContent=turn;
      if(el("gb-turndate"))el("gb-turndate").textContent=d2.toLocaleDateString("en-US",{{month:"long",day:"numeric"}});
      if(el("gb-sky"))el("gb-sky").textContent="It is "+canon+" in the northern sky, "+OPP[canon]+" in the southern — the turning is shared by All.";
      var angle=start[canon]+frac*90;
      var g=document.querySelector(".flame-now");
      if(g){{var built=parseFloat(g.getAttribute("data-built-angle")||angle);
        g.setAttribute("transform","rotate("+(angle-built)+" 330 330)");}}
      document.querySelectorAll(".arc").forEach(function(a){{
        var isNow=a.getAttribute("data-season")===canon;
        a.setAttribute("opacity",isNow?"1":"0.4");
        a.classList.toggle("now-arc",isNow);}});
      document.querySelectorAll(".season-label").forEach(function(l){{
        var key=l.getAttribute("data-season")||l.textContent;
        if(isSouth)l.textContent=OPP[key].toUpperCase();
        l.classList.toggle("now",key===canon);}});
      break;
    }}
  }}
}})();
(function(){{
  if(!('IntersectionObserver' in window))return;
  var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}});}},{{threshold:.12}});
  document.querySelectorAll('section').forEach(function(x){{io.observe(x);}});
  document.querySelectorAll('.tile .num').forEach(function(n){{
    var v=parseInt(n.textContent,10); if(isNaN(v)||v<1)return;
    var t0=null; var dur=900;
    function step(ts){{ if(!t0)t0=ts; var p=Math.min(1,(ts-t0)/dur);
      n.textContent=Math.round(v*(0.5-0.5*Math.cos(Math.PI*p))); if(p<1)requestAnimationFrame(step); }}
    n.textContent='0'; requestAnimationFrame(step);
  }});
}})();
</script></body></html>"""
    out = os.path.join(ROOT, t["out"])
    open(out, "w", encoding="utf-8").write(HTML)
    print(f"built {t['out']}")

def render_field(t, title, sub, body_html, out_name):
    HTML = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — The Gameboard — LIØNSBERG</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root {{ --surface:{t["surface"]}; --ink:{t["ink"]}; --ink-soft:{t["soft"]}; --gold:{t["gold"]}; --gold-deep:{t["gold_deep"]}; --rust:{t["rust"]}; --card:{t["card"]}; --edge:{t["edge"]}; }}
* {{ box-sizing:border-box; margin:0; }}
body {{ color:var(--ink); font-family:"Source Serif 4",Georgia,serif; font-size:20px; line-height:1.6;
  background:#090E1B; background-image:radial-gradient(1200px 700px at 50% -12%, #22345C 0%, #131E38 40%, #090E1B 100%); background-repeat:no-repeat; }}
{starfield_css() if t["stars"] else ""}
.wrap {{ max-width:880px; margin:0 auto; padding:28px 20px 60px; position:relative; }}
.back {{ font-family:Inter,sans-serif; font-size:16px; }} .back a {{ color:var(--gold-deep); text-decoration:none; }}
h1 {{ font-size:clamp(38px,6.5vw,56px); margin:10px 0 4px;
  background:linear-gradient(180deg,#F7EED6 20%, #E8B14B 85%); -webkit-background-clip:text; background-clip:text; color:transparent; }}
.sub {{ color:var(--ink-soft); font-style:italic; margin-bottom:22px; }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:16px; }}
.card {{ background:rgba(22,32,58,.55); border:1px solid rgba(232,177,75,.13); border-radius:18px; padding:20px 22px; display:block; text-decoration:none; color:inherit;
  backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px); box-shadow:0 12px 34px rgba(0,0,0,.35); transition:transform .25s ease, border-color .25s ease; }}
a.card:hover {{ transform:translateY(-3px); border-color:rgba(232,177,75,.5); }}
.card h3 {{ font-size:24px; margin:4px 0 2px; }} .card .meta {{ color:var(--ink-soft); font-size:17px; }}
.card .line {{ font-size:18px; margin-top:6px; }} .flame-mark {{ font-size:26px; }} .flame-mark.dim {{ filter:grayscale(.6) opacity(.6); }}
.card.stand {{ border-color:var(--gold); box-shadow:0 2px 14px rgba(232,177,75,.22); }}
.card.ghost {{ border-style:dashed; background:transparent; }}
</style></head><body><div class="wrap">
<p class="back"><a href="/gameboard">← back to the Gameboard</a></p>
<h1>{title}</h1><p class="sub">{sub}</p>
<input id="gb-filter" type="search" placeholder="Filter by name, place, or gift…" aria-label="Filter cards"
  style="width:100%;max-width:480px;font:inherit;font-size:18px;padding:12px 16px;border-radius:12px;border:1.5px solid var(--edge);background:var(--card);color:var(--ink);margin-bottom:18px;">
<div class="cards" id="gb-cards">{body_html}</div>
<p class="sub" style="margin-top:22px">To connect with anyone here, send word through any door on <a href="/Reaching_Us.html" style="color:var(--gold-deep)">Reaching Us</a> — contact details are never published; the membrane opens by consent. New to the Board? <a href="/About_the_Gameboard.html" style="color:var(--gold-deep)">About the Gameboard</a>.</p>
<script>
(function(){{var f=document.getElementById("gb-filter");if(!f)return;
f.addEventListener("input",function(){{var q=f.value.toLowerCase();
document.querySelectorAll("#gb-cards .card").forEach(function(c){{
c.style.display=(!q||c.textContent.toLowerCase().indexOf(q)>-1)?"":"none";}});}});}})();
</script>
</div></body></html>"""
    open(os.path.join(ROOT, out_name), "w", encoding="utf-8").write(HTML)
    print(f"built {out_name}")

render(THEMES["cosmic"], None, None)
_t = THEMES["cosmic"]
render_field(_t, "Who Stands", f"The whole field — {n_players} {'soul' if n_players==1 else 'souls'} standing openly, by name.", player_cards(None), "players.html")
render_field(_t, "The Circles", "Three to thirteen souls, sealed at the pace of trust.", simple_cards(circles, "Circles") or GHOSTS["circles"], "circles.html")
render_field(_t, "The Groups", "Networks, councils, and guilds — click any Group to see the Players and Circles who belong.", simple_cards(groups, "Groups") or GHOSTS["groups"], "groups.html")
render_field(_t, "The Quests", "Real work that makes one place measurably more like Heaven.", simple_cards(quests, "Quests") or GHOSTS["quests"], "quests.html")
render_field(_t, "The Stories", "Living proof, passed from hand to hand.", simple_cards(stories, "Stories") or GHOSTS["stories"], "stories.html")
print(f"{SEASON} frac {FRAC:.2f}, {DAYS_TO_TURN}d to turn; players={n_players} circles={n_circles}")
