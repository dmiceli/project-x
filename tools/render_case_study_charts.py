# tools/render_case_study_charts.py — regenerates CASE-STUDY.md's charts into
# assets/docs/. Update the DATA blocks when the weekly case-study task runs,
# then re-run: python3 tools/render_case_study_charts.py  (from repo root)
# Brand palette per BRAND.md; same aesthetic as render_docs_diagrams.py.
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
GOOD, RED = '#6ee7b7', '#f87171'

# ============ 1 · EIGHT TAKES (the first-build session) ============
# stage index each build reached before failing (or 5 = delivered)
STAGES = ['CI SIGNING', 'TOOLCHAIN', 'ARCHIVE + SIGN', 'APPLE UPLOAD CHECK', 'TESTFLIGHT']
DATA = [  # (take, stage_reached, verdict, lesson)
    (1, 0, 'CUT', 'signing vault empty (and integration misnamed)'),
    (2, 0, 'CUT', 'same — retake before diagnosing. lesson learned'),
    (3, 1, 'CUT', 'Capacitor CLI needs Node 22'),
    (4, 2, 'CUT', 'script --create can\'t mint certs w/o a key secret'),
    (5, 0, 'CUT', 'proved ios_signing only FETCHES — vault still empty'),
    (6, 3, 'CUT', 'portrait-only needs UIRequiresFullScreen (90474)'),
    (7, 4, 'PRINT', 'uploaded, processed, "Ready to Submit"'),
    (8, 4, 'PRINT', 'the fix batch — same pipeline, zero drama'),
]
W1, H1 = 960, 500
img = Image.new('RGB', (W1 * SS, H1 * SS), INK)
d = ImageDraw.Draw(img)
d.text(S(24, 16), 'EIGHT TAKES — GETTING TAKE 47 ONTO TESTFLIGHT (2026-07-04, one night)', font=font(16), fill=GOLD)
d.text(S(24, 42), 'each failure reached one stage further (mostly) · total cost: ~15 of 500 free build minutes', font=font(11, True), fill=DIM)
x0, xw = 150, 700
# stage columns
for i, st in enumerate(STAGES):
    x = x0 + xw * (i + 1) / 5
    d.line(S(x, 70) + S(x, 434), fill=EDGE, width=1 * SS)
    d.text(S(x - 8, 440), st, font=font(9), fill=DIM, anchor='ra' if i == 4 else 'ma')
for k, (take, stage, verdict, lesson) in enumerate(DATA):
    y = 78 + k * 44
    bar_w = xw * (stage + 1) / 5
    col = GOOD if verdict == 'PRINT' else RED
    d.text(S(24, y + 6), 'TAKE ' + str(take), font=font(13), fill=CREAM)
    d.rounded_rectangle(S(x0, y, x0 + bar_w, y + 20), radius=4 * SS, fill=PANEL, outline=col, width=2 * SS)
    d.text(S(x0 + bar_w - 10, y + 10), verdict, font=font(10), fill=col, anchor='rm')
    d.text(S(x0 + 10, y + 26), lesson, font=font(9, True), fill=DIM)
d.text(S(24, 470), 'The expensive failures were assertions, not code: takes 1–2 and 5 died on the same wrong theory, stated confidently twice.', font=font(10, True), fill=CREAM)
img = img.resize((W1, H1), Image.LANCZOS)
img.save(os.path.join(OUT, 'case-study-builds.png'))

# ============ 2 · WEEK-ONE PRODUCTION REPORT (call-sheet stat board) ============
NUMBERS = [  # (big number, label, sub)
    ('72 h',   'PROTOTYPE → TESTFLIGHT', 'repo created Jul 2, on Dan\'s iPhone Jul 4'),
    ('$99',    'TOTAL SPEND',            'Apple Developer fee. Everything else: free tiers'),
    ('54',     'COMMITS',                'every one written by Claude, pushed by Dan'),
    ('2,957',  'LINES, ONE FILE',        'the whole game: engine, art, audio, UI, save'),
    ('8',      'CLOUD BUILDS',           '6 outtakes, 2 delivered — no Mac involved'),
    ('59',     'DECISIONS LOGGED',       'each with its why (DECISIONS.md)'),
    ('24',     'LIVING DOCUMENTS',       'spec → brand → QA → pipeline → this case study'),
    ('11',     'BETA DEFECTS NIGHT 1',   'all triaged to a register; 10 fixed same night'),
]
W2, H2 = 960, 420
img = Image.new('RGB', (W2 * SS, H2 * SS), INK)
d = ImageDraw.Draw(img)
# clapper strip header (the brand's one indulgence)
for i in range(12):
    if i % 2 == 0:
        d.polygon(S(i * 80 + 6, 0, (i + 1) * 80 + 6, 0, (i + 1) * 80 - 6, 26, i * 80 - 6, 26), fill=GOLD)
d.text(S(24, 44), 'PRODUCTION REPORT — WEEK 1', font=font(20), fill=GOLD)
d.text(S(24, 74), 'TAKE 47 · a stunt double\'s life · shot entirely on a Windows PC by one PM and one AI', font=font(11, True), fill=DIM)
for k, (big, label, sub) in enumerate(NUMBERS):
    cx, cy = 24 + (k % 4) * 232, 110 + (k // 4) * 140
    d.rounded_rectangle(S(cx, cy, cx + 214, cy + 124), radius=8 * SS, fill=PANEL, outline=EDGE, width=2 * SS)
    d.text(S(cx + 107, cy + 34), big, font=font(30), fill=GOLD, anchor='mm')
    d.text(S(cx + 107, cy + 66), label, font=font(11), fill=CREAM, anchor='mm')
    d.text(S(cx + 107, cy + 88), sub, font=font(8, True), fill=DIM, anchor='ma', align='center')
d.text(S(24, 396), 'Sources: git history · Codemagic build log · DECISIONS.md · DEFECTS.md · releases/ — every number is checkable in the repo.', font=font(9, True), fill=DIM)
img = img.resize((W2, H2), Image.LANCZOS)
img.save(os.path.join(OUT, 'case-study-numbers.png'))

print('case-study charts rendered to assets/docs/')
