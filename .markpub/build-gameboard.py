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
        for k in ("place","region","open","pledged","flame","sponsor","circle","gifts","state","formed","quest","commitment","season"):
            m=re.search(rf"^{k}::\s*(.+)$", s, re.M)
            if m: d[k]=re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", m.group(1)).strip()
        out.append(d)
    return out

players = cards("Players")
circles = cards("Circles")
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
        arcs.append(f'<path class="{cls}" data-season="{sname}" d="{arc_path(C,C,R,a0+GAP,a0+90-GAP)}" stroke="{colors[sname]}" stroke-width="{ARC_W}" fill="none" stroke-linecap="butt"{dim}/>')
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
    flame = (f'<g class="flame-now" data-built-angle="{NOW_ANGLE:.2f}"><circle cx="{fx:.0f}" cy="{fy:.0f}" r="21" fill="{t["surface"]}" stroke="{t["rust"]}" stroke-width="2"/>'
             f'<text x="{fx:.0f}" y="{fy+2:.0f}" text-anchor="middle" dominant-baseline="middle" font-size="24">🔥</text></g>')
    return f"""<svg viewBox="0 0 {2*C} {2*C}" role="img" aria-label="The wheel of the year. It is {SEASON} — {DAYS_TO_TURN} days until the turning on {NEXT_TURN.strftime('%B %-d')}.">
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
body {{ background:var(--surface); color:var(--ink); font-family:"Source Serif 4", Georgia, serif;
  font-size:20px; line-height:1.55; }}
{stars}
{glow_css}
.wrap {{ max-width:880px; margin:0 auto; padding:28px 20px 60px; position:relative; }}
header {{ text-align:center; padding:26px 0 8px; }}
header .kicker {{ font-family:Inter,sans-serif; font-size:14px; letter-spacing:.22em; color:var(--ink-soft); text-transform:uppercase; }}
h1 {{ font-size:clamp(40px,7vw,58px); font-weight:700; letter-spacing:.01em; margin:6px 0 2px; }}
header .questions {{ font-style:italic; color:var(--ink-soft); font-size:19px; }}
.wheel {{ max-width:600px; margin:16px auto 0; }}
.wheel svg {{ width:100%; height:auto; display:block; }}
.season-label {{ font-family:Inter,sans-serif; font-size:19px; font-weight:600; letter-spacing:.14em; fill:{t["label_fill"]}; }}
.season-label.now {{ fill:#fff; }}
.tick {{ stroke:var(--surface); stroke-width:3; }}
.tick-label {{ font-family:Inter,sans-serif; font-size:14px; fill:var(--ink-soft); }}
.c-season {{ font-family:Inter,sans-serif; font-size:15px; letter-spacing:.2em; fill:var(--ink-soft); text-anchor:middle; }}
.c-name {{ font-size:21px; font-style:italic; fill:var(--ink-soft); text-anchor:middle; }}
.c-one {{ font-size:54px; font-weight:700; fill:var(--gold); text-anchor:middle; }}
.c-q {{ font-size:19px; font-style:italic; fill:var(--ink); text-anchor:middle; }}
.sky-line {{ text-align:center; font-style:italic; color:var(--ink-soft); font-size:18px; margin:10px 0 0; }}
.now-line {{ text-align:center; font-size:21px; margin:8px 0 4px; }}
.now-line strong {{ color:var(--rust); }}
.update-row {{ text-align:center; font-size:19px; margin:2px 0 0; }}
.update-row a {{ color:var(--gold); text-decoration:none; font-family:Inter,sans-serif; }}
.actions {{ display:flex; flex-wrap:wrap; gap:14px; justify-content:center; margin:30px 0 8px; }}
.btn {{ font-family:Inter,sans-serif; font-weight:600; font-size:19px; text-decoration:none;
  padding:16px 26px; border-radius:14px; min-height:44px; display:inline-flex; align-items:center; gap:10px; }}
.btn.primary {{ background:var(--gold); color:{t["gold_ink"]}; border:2px solid var(--gold-deep); }}
.btn.quiet {{ background:var(--card); color:var(--ink); border:2px solid var(--edge); }}
.btn:hover {{ filter:brightness(1.08); }}
section {{ margin-top:46px; }}
.h2link {{ text-decoration:none; color:inherit; }}
.h2link:hover h2 {{ color:var(--gold); }}
h2 {{ font-size:31px; border-bottom:3px solid var(--gold); display:inline-block; padding-bottom:4px; margin-bottom:6px; }}
.sub {{ color:var(--ink-soft); font-style:italic; margin-bottom:16px; }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:16px; }}
.card {{ background:var(--card); border:1.5px solid var(--edge); border-radius:16px; padding:20px 22px; display:block; text-decoration:none; color:inherit; }}\na.card:hover {{ border-color:var(--gold); filter:brightness(1.04); }}
.card h3 {{ font-size:24px; margin:4px 0 2px; }}
.card .meta {{ color:var(--ink-soft); font-size:17px; margin-bottom:8px; }}
.card .line {{ font-size:18px; margin-top:6px; }}
.card.stand {{ border-color:var(--gold); box-shadow:0 2px 14px rgba(232,177,75,.22); }}
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
.skin {{ font-family:Inter,sans-serif; font-size:15px; }}
@media print {{ .actions,.card.ghost,.skin {{ display:none; }} body {{ font-size:16px; background:#fff !important; color:#1C1710; }}
  body::before {{ display:none; }} .card,.tile {{ background:#fff; border-color:#bbb; color:#1C1710; }}
  .card .meta,.tile .lab,.sub,.young,footer {{ color:#555; }}
  .season-label {{ fill:#fff; }} .c-one {{ fill:#8A6A10; }} .c-q,.c-name,.c-season,.tick-label {{ fill:#333; }}
  .now-arc,.flame-now {{ filter:none; }} }}
</style></head><body>
<div class="wrap">
<header>
  <div class="kicker">The Great Game of LIØNSBERG</div>
  <h1>The Gameboard</h1>
  <p class="questions">Who We Are · How We Are Questing · Where We Are Going · Why</p>
</header>

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
  <a class="h2link" href="/players.html"><h2>Who Stands →</h2></a>
  <p class="sub">We stand together — openly, by name. {n_players} {"soul stands" if n_players==1 else "souls stand"} so far; the first, so that no one is asked to stand first.</p>
  <div class="cards">{player_cards(BOARD_CAP)}</div>
</section>

<section>
  <a class="h2link" href="/circles.html"><h2>The Circles →</h2></a>
  <p class="sub">Three to thirteen souls, sealed at the pace of trust.</p>
  <div class="cards">{circles_html}</div>
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
    <a class="card" href="/The_Decision_Log.html"><h3>📜 The Decision Log</h3><p class="line">What was decided, when, and why. <strong>Read before asking.</strong></p></a>
    <a class="card" href="/LIØNSBERG_Issue_Tracker.html"><h3>🪨 The Issue Tracker</h3><p class="line">What blocks the work. When something stops you that your Circle cannot resolve, log it — a named issue is half-solved.</p></a>
    <a class="card" href="/Request_For_Guidance.html"><h3>🧭 Requests For Guidance</h3><p class="line">What is unclear. <strong>Ask before assuming</strong> — every good question improves the plans.</p></a>
    <a class="card" href="/Submittals.html"><h3>📬 Submittals</h3><p class="line">What awaits review and approval — proposals, tools, resources, and improvements offered to the whole.</p></a>
  </div>
  <p class="young">To add to any ledger: send word through <a href="/Reaching_Us.html" style="color:var(--gold-deep)">Reaching Us</a> or the Server — the stewards tend the record.</p>
</section>

<footer>
  <p><a href="/About_the_Gameboard.html" style="color:var(--gold)">What is this? — About the Gameboard</a></p>
  <p>This Board is kept in plain text, in the open record, tended by hand —
     the ledger behind it lives at <a href="/The_Gameboard.html">The Gameboard</a>.</p>
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
body {{ background:var(--surface); color:var(--ink); font-family:"Source Serif 4",Georgia,serif; font-size:20px; line-height:1.55; }}
{starfield_css() if t["stars"] else ""}
.wrap {{ max-width:880px; margin:0 auto; padding:28px 20px 60px; position:relative; }}
.back {{ font-family:Inter,sans-serif; font-size:16px; }} .back a {{ color:var(--gold-deep); text-decoration:none; }}
h1 {{ font-size:clamp(34px,6vw,48px); margin:10px 0 4px; }}
.sub {{ color:var(--ink-soft); font-style:italic; margin-bottom:22px; }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:16px; }}
.card {{ background:var(--card); border:1.5px solid var(--edge); border-radius:16px; padding:20px 22px; display:block; text-decoration:none; color:inherit; }}
a.card:hover {{ border-color:var(--gold); filter:brightness(1.06); }}
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
render_field(_t, "The Quests", "Real work that makes one place measurably more like Heaven.", simple_cards(quests, "Quests") or GHOSTS["quests"], "quests.html")
render_field(_t, "The Stories", "Living proof, passed from hand to hand.", simple_cards(stories, "Stories") or GHOSTS["stories"], "stories.html")
print(f"{SEASON} frac {FRAC:.2f}, {DAYS_TO_TURN}d to turn; players={n_players} circles={n_circles}")
