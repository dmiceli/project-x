# tools/render_docs_diagrams.py — regenerates the documentation diagrams into
# assets/docs/. Run after any architecture/doc-structure change (MAINTENANCE.md
# checks that the diagrams still match reality). Brand palette per BRAND.md.
# Usage: python3 tools/render_docs_diagrams.py   (from the repo root)
import os
from PIL import Image, ImageDraw, ImageFont

SS = 2
OUT = os.path.join(os.path.dirname(__file__), '..', 'assets', 'docs')
os.makedirs(OUT, exist_ok=True)
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FI = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def font(sz, plain=False): return ImageFont.truetype(FI if plain else F, sz * SS)
def S(*v): return [x * SS for x in v]

INK, PANEL, EDGE = '#191010', '#241515', '#3a2a22'
GOLD, CREAM, DIM = '#ffd166', '#e8d5b5', '#a08b72'
GOOD, BLUE, PURPLE, RED = '#6ee7b7', '#93c5fd', '#c084fc', '#f87171'

def sheet(w, h, title):
    img = Image.new('RGB', (w * SS, h * SS), INK)
    d = ImageDraw.Draw(img)
    d.text(S(24, 16), title, font=font(17), fill=GOLD)
    return img, d

def box(d, x, y, w, h, label, sub=None, edge=EDGE, fill=PANEL, tcol=CREAM, tsz=12):
    d.rounded_rectangle(S(x, y, x + w, y + h), radius=8 * SS, fill=fill, outline=edge, width=2 * SS)
    cy = y + (14 if sub else h / 2)
    d.text(S(x + w / 2, cy), label, font=font(tsz), fill=tcol, anchor='mm' if not sub else 'ma')
    if sub:
        d.text(S(x + w / 2, cy + 20), sub, font=font(9, True), fill=DIM, anchor='ma', align='center')

def arrow(d, x0, y0, x1, y1, col=DIM, w=2):
    d.line(S(x0, y0) + S(x1, y1), fill=col, width=w * SS)
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    for s in (-0.45, 0.45):
        d.line(S(x1, y1) + S(x1 - 9 * math.cos(a + s), y1 - 9 * math.sin(a + s)), fill=col, width=w * SS)

# ============ 1 · SYSTEM ARCHITECTURE ============
img, d = sheet(960, 640, 'TAKE 47 — SYSTEM ARCHITECTURE (v0.9 beta)')
# the single file
d.rounded_rectangle(S(24, 52, 620, 600), radius=10 * SS, outline=GOLD, width=2 * SS)
d.text(S(40, 62), 'app/index.html — THE ENTIRE GAME (single file, ~2500 lines)', font=font(12), fill=GOLD)
box(d, 44, 90, 264, 64, 'HTML OVERLAY SCREENS', 'menus · settings · cards · shop\n(real buttons = VoiceOver-able)', edge=BLUE)
box(d, 328, 90, 264, 64, 'CANVAS RENDER', 'set cache + depth layers → director\n→ mechanics → player → HUD chips', edge=BLUE)
box(d, 44, 178, 264, 64, 'GAME ENGINE', 'state machine · physics ·\nsub-frame landing judgment', edge=GOOD)
box(d, 328, 178, 264, 64, 'SEEDED SCENE DESIGN', 'mulberry32(scene#) — everyone\'s\nScene N is identical · 6 mechanics', edge=GOOD)
box(d, 44, 266, 264, 64, 'ECONOMY & SYSTEMS', 'prints · props · wardrobe · call\nsheet · achievements · mercy', edge=PURPLE)
box(d, 328, 266, 264, 64, 'WEBAUDIO SYNTH', 'tone/noise/fnoise — deadpan foley,\ncartoon heart · no audio files', edge=PURPLE)
box(d, 44, 354, 548, 58, 'VERSIONED SAVE (t47_save_v1, one localStorage key)', 'scene · prints · items · unlocks · settings · daily/call-sheet dates', edge=RED)
box(d, 44, 436, 548, 52, 'QA TEST MODE (5-tap version line)', 'scene jump · prints · props · mercy · rollover · save backup — STRIPPED AT PHASE 5', edge=RED, tcol=RED)
d.text(S(44, 508), 'STANDING RULES: outlines = foreground only · a hitbox is exactly what\'s drawn ·', font=font(10, True), fill=DIM)
d.text(S(44, 526), 'active props visibly change the scene · ads never buy progress · fully offline (no', font=font(10, True), fill=DIM)
d.text(S(44, 544), 'network, no analytics, no third-party code) · flicker < 3Hz · decorative ≤ 2:1 contrast', font=font(10, True), fill=DIM)
# right column: where it runs
box(d, 672, 90, 264, 70, 'GITHUB PAGES', 'browser-playable at every stage\n(phone home-screen standalone)', edge=GOLD)
box(d, 672, 216, 264, 96, 'PHASE 5: CAPACITOR SHELL', 'Preferences (save) · Haptics ·\nGame Center · Local Notifications\nbuilt via Codemagic cloud (no Mac)', edge=GOLD)
box(d, 672, 368, 264, 70, 'iOS APP', 'TestFlight beta → App Store', edge=GOLD, tcol=GOLD)
arrow(d, 620, 125, 672, 125)
arrow(d, 620, 264, 672, 264)
arrow(d, 804, 312, 804, 368)
d.text(S(672, 460), 'Dan commits/pushes via GitHub Desktop;', font=font(10, True), fill=DIM)
d.text(S(672, 478), 'the push updates the playable build.', font=font(10, True), fill=DIM)
img = img.resize((960, 640), Image.LANCZOS)
img.save(os.path.join(OUT, 'architecture.png'))

# ============ 2 · GAME STATE MACHINE ============
img, d = sheet(960, 400, 'TAKE 47 — GAME LOOP (one take)')
box(d, 40, 90, 130, 56, 'HOME', 'HTML menus', edge=BLUE)
box(d, 230, 90, 150, 56, 'READY', 'tap = jump · hold =\nLaunch Rig aim', edge=GOOD)
box(d, 440, 90, 150, 56, 'AIR', 'tap = lock the spin\n(or ride it out)', edge=GOOD)
box(d, 650, 34, 150, 64, 'LANDED', 'angle ≤ tol at exact\ncontact instant', edge=GOOD)
box(d, 650, 150, 150, 64, 'CRASH → CUT', 'ragdoll · quip ·\nmercy at 7', edge=RED)
box(d, 40, 230, 150, 64, 'CARD', 'wrap parties ·\ncast unlocks', edge=PURPLE)
arrow(d, 170, 118, 230, 118); d.text(S(178, 104), 'ACTION!', font=font(9), fill=DIM)
arrow(d, 380, 118, 440, 118); d.text(S(392, 104), 'tap/release', font=font(9), fill=DIM)
arrow(d, 590, 104, 650, 72); d.text(S(596, 78), 'feet-down', font=font(9), fill=DIM)
arrow(d, 590, 132, 650, 168); d.text(S(566, 178), 'anything\nelse', font=font(9), fill=DIM)
arrow(d, 650, 60, 305, 60); arrow(d, 305, 60, 305, 90)
d.text(S(370, 44), 'next scene (or CARD at set boundaries)', font=font(9), fill=DIM)
arrow(d, 700, 214, 490, 268); arrow(d, 490, 268, 320, 150)
d.text(S(455, 282), 'retry same scene (takes += 1)', font=font(9), fill=DIM)
arrow(d, 115, 230, 115, 146); arrow(d, 115, 146, 170, 130)
d.text(S(30, 196), 'unlocks &\nwrap parties', font=font(8), fill=DIM)
d.text(S(40, 330), 'MODES: campaign (persistent scenes) · daily gauntlet (3 lives, same seed worldwide, no props) · reshoot (the Reel).', font=font(10, True), fill=DIM)
d.text(S(40, 350), 'Perfect landing = PRINT (never with a prop assist). Mechanics by set: cart · boom · gravity · wind · arm · double-bounce.', font=font(10, True), fill=DIM)
img = img.resize((960, 400), Image.LANCZOS)
img.save(os.path.join(OUT, 'game-loop.png'))

# ============ 3 · DOCUMENTATION TAXONOMY ============
img, d = sheet(960, 880, 'TAKE 47 — DOCUMENTATION TAXONOMY (README.md is the front door)')
groups = [
    ('GOVERNANCE — how we work', GOLD, 60, [
        ('CLAUDE.md', 'rules, roles, lessons'),
        ('STATUS.md', 'session log + next steps'),
        ('DECISIONS.md', 'every choice + its WHY'),
        ('MAINTENANCE.md', 'daily routine checklist')]),
    ('PRODUCT — what we\'re building', GOOD, 60, [
        ('DESIGN.md', 'the full game spec'),
        ('BACKLOG.md', 'post-v1 parking lot'),
        ('EXPLORATIONS.md', 'design studies + verdicts'),
        ('BIG-WINS.md', 'MVP success levers')]),
    ('BRAND & ART — how it looks/sounds', PURPLE, 356, [
        ('BRAND.md', 'palette · copy · a11y rules'),
        ('THEME.md', 'movie-set lore + IP guards'),
        ('ART-RESEARCH.md', 'background pattern'),
        ('assets/', 'icons · sheets · diagrams')]),
    ('QUALITY — how we verify', BLUE, 356, [
        ('BETA-READINESS.md', 'the 5/10-rigor gate list'),
        ('QA-PLAN.md', 'structured test sessions'),
        ('ARCHITECTURE.md', 'code map + diagrams'),
        ('tools/', 'diagram generator etc.')]),
    ('LAUNCH — how it ships', RED, 652, [
        ('PIPELINE.md', 'no-Mac build runbook'),
        ('MARKETING.md', 'ASO + launch plan'),
        ('TRENDS.md', 'market research'),
        ('PRIVACY.md', 'policy (offline-first)')]),
]
yb = 64
for title, col, xx, docs in groups:
    yy = 64 if xx != groups[2][2] or True else 64
for i, (title, col, xx, docs) in enumerate(groups):
    yy = 64 + (0 if i in (0, 1) else 0)
# manual layout: two rows of two + one centered
POS = [(40, 70), (520, 70), (40, 330), (520, 330), (280, 590)]
for (title, col, _, docs), (xx, yy) in zip(groups, POS):
    d.rounded_rectangle(S(xx, yy, xx + 400, yy + 218 if len(docs) > 3 else yy + 218), radius=10 * SS, outline=col, width=2 * SS)
    d.text(S(xx + 16, yy + 12), title, font=font(12), fill=col)
    for j, (name, desc) in enumerate(docs):
        ry = yy + 44 + j * 42
        d.rounded_rectangle(S(xx + 16, ry, xx + 384, ry + 34), radius=6 * SS, fill=PANEL)
        d.text(S(xx + 28, ry + 9), name, font=font(11), fill=CREAM)
        d.text(S(xx + 180, ry + 11), desc, font=font(9, True), fill=DIM)
d.text(S(40, 830), 'CADENCE — living (every session): STATUS · DECISIONS · BACKLOG   |   on-change: DESIGN · BRAND · ARCHITECTURE ·', font=font(10, True), fill=DIM)
d.text(S(40, 850), 'PIPELINE · PRIVACY · diagrams   |   stable references: THEME · TRENDS · ART-RESEARCH · EXPLORATIONS · BIG-WINS', font=font(10, True), fill=DIM)
img = img.resize((960, 880), Image.LANCZOS)
img.save(os.path.join(OUT, 'doc-taxonomy.png'))
print('rendered 3 diagrams to assets/docs/')
