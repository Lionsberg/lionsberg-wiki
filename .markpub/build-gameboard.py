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
COLORS = {"Spring":"#5E8639","Summer":"#D79417","Autumn":"#B4552D","Winter":"#28609E"}

def season_now():
    for (d1,s),(d2,_) in zip(TURNINGS, TURNINGS[1:]):
        if d1 <= TODAY < d2:
            frac = (TODAY-d1).days / (d2-d1).days
            return s, frac, (d2-TODAY).days, d2
    return "Summer", 0.5, 0, TURNINGS[3][0]

SEASON, FRAC, DAYS_TO_TURN, NEXT_TURN = season_now()

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
        for k in ("place","pledged","flame","sponsor","circle","gifts","state","formed","quest","commitment","season"):
            m=re.search(rf"^{k}::\s*(.+)$", s, re.M)
            if m: d[k]=re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", m.group(1)).strip()
        out.append(d)
    return out

players = cards("Players")
circles = cards("Circles")
quests  = cards("Quests")
stories = cards("Stories")

def esc(x): return html.escape(x or "")

# ---------- wheel SVG ----------
C, R = 330, 240
ARC_W = 58
GAP = 1.2  # degrees ≈ 2px surface gap at this radius
arcs=[]
labels=[]
for s,a0 in SEASON_START_ANGLE.items():
    dim = '' if s == SEASON else ' opacity="0.35"'
    arcs.append(f'<path d="{arc_path(C,C,R,a0+GAP,a0+90-GAP)}" stroke="{COLORS[s]}" stroke-width="{ARC_W}" fill="none" stroke-linecap="butt"{dim}/>')
    lx,ly = pol(C,C,R, a0+45)
    labels.append(f'<text x="{lx:.0f}" y="{ly:.0f}" class="season-label{" now" if s==SEASON else ""}" text-anchor="middle" dominant-baseline="middle">{s.upper()}</text>')
ticks=[]
for d,s in TURNINGS[:4]:
    a = SEASON_START_ANGLE[s]
    x1,y1=pol(C,C,R+ARC_W/2+4,a); x2,y2=pol(C,C,R-ARC_W/2-4,a)
    lx,ly = pol(C,C,R+ARC_W/2+26,a)
    ticks.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" class="tick"/>'
                 f'<text x="{lx:.0f}" y="{ly:.0f}" class="tick-label" text-anchor="middle" dominant-baseline="middle">{d.strftime("%b %-d")}</text>')
fx,fy = pol(C,C,R,NOW_ANGLE)
flame = (f'<circle cx="{fx:.0f}" cy="{fy:.0f}" r="21" fill="#FAF5EA" stroke="#B4552D" stroke-width="2"/>'
         f'<text x="{fx:.0f}" y="{fy+2:.0f}" text-anchor="middle" dominant-baseline="middle" font-size="24">🔥</text>')

WHEEL = f'''<svg viewBox="0 0 {2*C} {2*C}" role="img" aria-label="The wheel of the year. It is {SEASON} — {DAYS_TO_TURN} days until the turning on {NEXT_TURN.strftime("%B %-d")}.">
{''.join(arcs)}{''.join(ticks)}{''.join(labels)}
<text x="{C}" y="{C-74}" class="c-season">2026 · SEASON 1</text>
<text x="{C}" y="{C-46}" class="c-name">The Great Game Begins</text>
<text x="{C}" y="{C+14}" class="c-one">ØNE</text>
<text x="{C}" y="{C+58}" class="c-q">Does this make life</text>
<text x="{C}" y="{C+84}" class="c-q">a little more like Heaven?</text>
{flame}
</svg>'''

# ---------- sections ----------
def player_cards():
    out=[]
    for p in players:
        out.append(f'''<div class="card stand">
      <div class="flame-mark">🔥</div>
      <h3>{esc(p["name"])}</h3>
      <p class="meta">{esc(p.get("place",""))}</p>
      <p class="line">Flame passed by <strong>{esc(p.get("flame","—"))}</strong></p>
      <p class="line">Pledged · {esc(p.get("pledged","—"))}</p>
    </div>''')
    out.append('''<a class="card ghost" href="/The_Pledge.html">
      <div class="flame-mark dim">🔥</div>
      <h3>Your name belongs here</h3>
      <p class="line">Accept the Invitation · attend a gathering ·<br>make your Pledge — and stand with us.</p>
    </a>''')
    return "\n".join(out)

def simple_cards(items, kind):
    if not items:
        return ""
    out=[]
    for c in items:
        bits = " · ".join(esc(c[k]) for k in ("place","season","state") if c.get(k))
        out.append(f'<div class="card"><h3>{esc(c["name"])}</h3><p class="meta">{bits}</p></div>')
    return "\n".join(out)

circles_html = simple_cards(circles,"circle") or '''<div class="card ghost still"><h3>The first Circles are forming now</h3>
  <p class="line">Yours will appear here as it seals — visible to All,<br>so the Game can see itself grow.</p></div>'''
quests_html = simple_cards(quests,"quest") or '''<div class="card ghost still"><h3>The first Quests await their Circles</h3>
  <p class="line">One tangible act of goodwill, each season —<br>real, achievable, meaningful, together.</p></div>'''
stories_html = simple_cards(stories,"story") or '''<div class="card ghost still"><h3>The first harvest comes at the Equinox</h3>
  <p class="line">Every Quest becomes a Story; every Story becomes<br>a Prophesy of even greater things to come.</p></div>'''

n_players=len(players); n_circles=len(circles)

HTML = f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Gameboard — The Great Game of LIØNSBERG</title>
<meta name="description" content="The living Gameboard of The Great Game of LIØNSBERG — who stands, the Circles, the Quests, the Stories, the season, and the Score.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root {{ --surface:#FAF5EA; --ink:#2B2419; --ink-soft:#6B6152; --gold:#D79417; --gold-deep:#A8720C;
  --rust:#B4552D; --card:#FFFDF6; --edge:#E7DCC4; }}
* {{ box-sizing:border-box; margin:0; }}
body {{ background:var(--surface); color:var(--ink); font-family:"Source Serif 4", Georgia, serif;
  font-size:20px; line-height:1.55; }}
.wrap {{ max-width:880px; margin:0 auto; padding:28px 20px 60px; }}
header {{ text-align:center; padding:26px 0 8px; }}
header .kicker {{ font-family:Inter,sans-serif; font-size:14px; letter-spacing:.22em; color:var(--ink-soft); text-transform:uppercase; }}
h1 {{ font-size:clamp(40px,7vw,58px); font-weight:700; letter-spacing:.01em; margin:6px 0 2px; }}
header .questions {{ font-style:italic; color:var(--ink-soft); font-size:19px; }}
.wheel {{ max-width:600px; margin:16px auto 0; }}
.wheel svg {{ width:100%; height:auto; display:block; }}
.season-label {{ font-family:Inter,sans-serif; font-size:19px; font-weight:600; letter-spacing:.14em; fill:#FAF5EA; }}
.season-label.now {{ fill:#fff; }}
.tick {{ stroke:var(--surface); stroke-width:3; }}
.tick-label {{ font-family:Inter,sans-serif; font-size:14px; fill:var(--ink-soft); }}
.c-season {{ font-family:Inter,sans-serif; font-size:15px; letter-spacing:.2em; fill:var(--ink-soft); text-anchor:middle; }}
.c-name {{ font-size:21px; font-style:italic; fill:var(--ink-soft); text-anchor:middle; }}
.c-one {{ font-size:54px; font-weight:700; fill:var(--ink); text-anchor:middle; }}
.c-q {{ font-size:19px; font-style:italic; fill:var(--ink); text-anchor:middle; }}
.now-line {{ text-align:center; font-size:21px; margin:14px 0 4px; }}
.now-line strong {{ color:var(--rust); }}
.actions {{ display:flex; flex-wrap:wrap; gap:14px; justify-content:center; margin:30px 0 8px; }}
.btn {{ font-family:Inter,sans-serif; font-weight:600; font-size:19px; text-decoration:none;
  padding:16px 26px; border-radius:14px; min-height:44px; display:inline-flex; align-items:center; gap:10px; }}
.btn.primary {{ background:var(--gold); color:#241B08; border:2px solid var(--gold-deep); }}
.btn.quiet {{ background:var(--card); color:var(--ink); border:2px solid var(--edge); }}
.btn:hover {{ filter:brightness(1.05); }}
section {{ margin-top:46px; }}
h2 {{ font-size:31px; border-bottom:3px solid var(--gold); display:inline-block; padding-bottom:4px; margin-bottom:6px; }}
.sub {{ color:var(--ink-soft); font-style:italic; margin-bottom:16px; }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:16px; }}
.card {{ background:var(--card); border:1.5px solid var(--edge); border-radius:16px; padding:20px 22px; }}
.card h3 {{ font-size:24px; margin:4px 0 2px; }}
.card .meta {{ color:var(--ink-soft); font-size:17px; margin-bottom:8px; }}
.card .line {{ font-size:18px; margin-top:6px; }}
.card.stand {{ border-color:var(--gold); box-shadow:0 2px 10px rgba(215,148,23,.15); }}
.flame-mark {{ font-size:26px; }}
.flame-mark.dim {{ filter:grayscale(.6) opacity(.6); }}
.card.ghost {{ border-style:dashed; text-decoration:none; color:inherit; background:transparent; }}
a.card.ghost:hover {{ border-color:var(--gold); }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(140px,1fr)); gap:14px; }}
.tile {{ background:var(--card); border:1.5px solid var(--edge); border-radius:16px; padding:18px 14px; text-align:center; }}
.tile .num {{ font-size:40px; font-weight:700; line-height:1.1; }}
.tile .lab {{ font-family:Inter,sans-serif; font-size:14.5px; color:var(--ink-soft); margin-top:4px; }}
.young {{ color:var(--ink-soft); font-style:italic; font-size:18px; margin-top:12px; }}
footer {{ margin-top:60px; border-top:1.5px solid var(--edge); padding-top:22px; color:var(--ink-soft); font-size:17px; text-align:center; }}
footer a {{ color:var(--gold-deep); }}
.doors {{ margin-top:8px; }}
@media print {{ .actions,.card.ghost {{ display:none; }} body {{ font-size:16px; }} }}
</style></head><body>
<div class="wrap">
<header>
  <div class="kicker">The Great Game of LIØNSBERG</div>
  <h1>The Gameboard</h1>
  <p class="questions">Who We Are · How We Are Questing · Where We Are Going · Why</p>
</header>

<div class="wheel">{WHEEL}</div>
<p class="now-line">🔥 <strong>You are here</strong> — {SEASON} of Season&nbsp;1 · <strong>{DAYS_TO_TURN}&nbsp;days</strong> to the Harvest &amp; Equinox Celebration, {NEXT_TURN.strftime("%B %-d")}.</p>

<div class="actions">
  <a class="btn quiet" href="/LIØNSBERG_Wiki_Books/The_Story_of_LIØNSBERG/The_Story_of_LIØNSBERG.html">📖 Read the Story</a>
  <a class="btn quiet" href="/LIØNSBERG_Wiki_Books/The_Great_Game_of_LIØNSBERG/The_Great_Game_of_LIØNSBERG.html">🧭 Play the Game</a>
  <a class="btn quiet" href="/The_Invitation.html">🔥 Pass the Flame</a>
  <a class="btn primary" href="/The_Pledge.html">✍️ Make Your Pledge</a>
  <a class="btn quiet" href="/Reaching_Us.html">🤝 Get Help · Send Word</a>
</div>

<section>
  <h2>Who Stands</h2>
  <p class="sub">We stand together — openly, by name. {n_players} {"soul stands" if n_players==1 else "souls stand"} so far; the first, so that no one is asked to stand first.</p>
  <div class="cards">{player_cards()}</div>
</section>

<section>
  <h2>The Circles</h2>
  <p class="sub">Three to thirteen souls, sealed at the pace of trust.</p>
  <div class="cards">{circles_html}</div>
</section>

<section>
  <h2>The Quests &amp; The Stories</h2>
  <p class="sub">Real work that makes one place measurably more like Heaven — then told, as living proof.</p>
  <div class="cards">{quests_html}
{stories_html}</div>
</section>

<section>
  <h2>The Pledges &amp; The Score</h2>
  <p class="sub">The Pledges tell what is coming; the Score tells what has flowed.</p>
  <div class="tiles">
    <div class="tile"><div class="num">{n_players}</div><div class="lab">standing</div></div>
    <div class="tile"><div class="num">{n_circles or "—"}</div><div class="lab">Circles</div></div>
    <div class="tile"><div class="num">—</div><div class="lab">TEA pledged (hrs/wk)</div></div>
    <div class="tile"><div class="num">—</div><div class="lab">commitments kept</div></div>
    <div class="tile"><div class="num">{len(stories) or "—"}</div><div class="lab">Stories shared</div></div>
    <div class="tile"><div class="num">—</div><div class="lab">flames passed</div></div>
  </div>
  <p class="young">The first season is young. Every number here fills as the Turns flow — and the first moves are yours to make.</p>
</section>

<footer>
  <p>This Board is kept in plain text, in the open record, tended by hand —
     the ledger behind it lives at <a href="/The_Gameboard.html">The Gameboard</a>.</p>
  <p class="doors">Gatherings &amp; turnings announced via <a href="https://cocreatingheaven.substack.com/">the Substack</a> ·
     New here? Begin with <a href="/The_Invitation.html">The Invitation</a> and
     <a href="/LIØNSBERG_Wiki_Books/AURELLIØN's_Guide_to_LIØNSBERG/AURELLIØN's_Guide_to_LIØNSBERG.html">the Guide</a>.</p>
  <p>Made with love, for All · CC BY-SA 4.0 · regenerated {TODAY.strftime("%B %-d, %Y")}</p>
</footer>
</div></body></html>'''

out = os.path.join(ROOT, "gameboard.html")
open(out, "w", encoding="utf-8").write(HTML)
print(f"built {out}: {SEASON} frac {FRAC:.2f}, {DAYS_TO_TURN}d to turn; players={n_players} circles={n_circles} quests={len(quests)} stories={len(stories)}")
