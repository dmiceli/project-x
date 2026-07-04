# MAINTENANCE.md — routine sanitization checklist

**Cadence:** automated daily (scheduled task `take47-maintenance`, 6:38 AM) + on-demand at session end when a big batch landed. **Rigor: 5/10** — meaningful checks, no ceremony. Claude never commits; findings end with a suggested commit note for Dan.

## The checklist

**1. Docs current & consistent** *(the package map lives in README.md; keep its index true)*
- README.md index matches the actual files (new doc → new row + taxonomy group).
- ARCHITECTURE.md still describes reality; if systems/docs changed structurally, rerun `python3 tools/render_docs_diagrams.py` and confirm the three diagrams in assets/docs/ match.
- STATUS.md latest entry reflects the most recent work; "Next steps" list is clean, ordered, and duplicate-free.
- Every significant change in STATUS has a DECISIONS.md row with the *why*.
- CLAUDE.md operational lessons updated when a new lesson was learned (not per-session noise).
- BACKLOG.md: new ideas landed there, shipped items removed.
- **Release records** (from TestFlight beta on): every reported defect has a DEFECTS.md row with current status; every shipped build has its CHANGELOG.md entry and `releases/X.Y-buildN.md` file (notes + QA report + known issues; store metadata snapshot on App Store submissions).

**2. Codebase health (app/index.html — use Read/Edit tools, never shell reads: mount READ-cap)**
- File header block still true (architecture, privacy posture, a11y posture).
- Comments current where code changed; no dead code; no zero-gain refactors (deliberate rule).
- New/changed visuals checked against the coherence rules: outlines = foreground only; hitboxes match what's drawn; active props visibly change the scene.

**3. Accessibility sweep (standing rule)**
- No color-only signaling (pair with text/shape).
- Readable sizes/durations; canvas text ≥ 11px bold w/ backing; HTML touch targets ≥ 44px.
- No strobing/flash above ~3Hz anywhere (photosensitivity — also an App Store review risk); reduce-motion honored by any new motion.
- Sound remains optional.

**4. Privacy & App Store posture**
- Still fully offline: no network calls, no new SDKs, no data collection. localStorage only (Capacitor Preferences at Phase 5).
- Ads/IAP stubs remain stubs; "ads never buy progress" untouched.
- PRIVACY.md still accurate.

**5. Verification**
- Any code change this pass: headless smoke test with REAL state sequences (lesson: synthetic states hid an unreachable pose).
- Never trust the scratchpad mirror over the real file — Read is the authority.

**6. Close-out**
- Append a dated line to the Maintenance log below.
- Surface anything needing Dan's judgment at the top of the reply + a commit note.

## Maintenance log
- 2026-07-03 (session-end run, manual): full pass — see STATUS.md entry of same date.
- 2026-07-03 (scheduled run, 6:38 AM): docs-only pass — STATUS next-steps de-duplicated (stale pre-consolidation items removed); BACKLOG cleared of shipped/promoted items (Game Center → Phase 5, face pass + floor accents shipped); DECISIONS row added for `.nojekyll`/Pages-CI; index.html header now lists the QA Test Mode panel + its strip gate. Sweeps clean: fully offline confirmed (only URL = GAME_URL share constant, now resolved to dmiceli.github.io), flash/flicker rules hold, README index matches files, ARCHITECTURE current. No code-logic changes → no headless run needed.
