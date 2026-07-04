# Project X — iOS Game: TAKE 47

## Goal
Dan (product owner) and Claude (lead developer) build a low-complexity iOS game and publish it to the Apple App Store. This is also a test of whether a non-developer can ship a real product with Claude.

## The game
**TAKE 47** — one-tap stunt game, movie-set theme: every attempt is a "take," crashes are outtakes (director quips), levels are scenes with persistent progress. Full spec in DESIGN.md; every decision and its rationale in DECISIONS.md. Standing product principle (Dan): **ads never buy progress** — no scene skips, no pay-to-win; rewarded ads only for daily-challenge attempts and cosmetics.

## Who's who
- **Dan**: technically savvy, zero development experience. Makes all product decisions. Explain every technical concept in plain language — never assume coding knowledge.
- **Claude**: lead developer and translator. Always present tradeoffs with a clear recommendation. Ask before anything costly, irreversible, or account-related (Apple ID, payments, publishing actions).

## Environment (updated 2026-07-02)
- Windows PC only — **no Mac**. All iOS compilation/signing/upload goes through a cloud build service.
- iPhone available for on-device testing; feel-tests via GitHub Pages URL saved to home screen.
- Apple Developer Program: **enrolled** ✓
- GitHub: repo **project-x** (public), managed by Dan via GitHub Desktop; Pages enabled. GitHub connector available — reserved for CI status/issues/releases later, NOT for commits.
- Pace: sprint mode (near-daily sessions). Target: TestFlight beta in ~2 weeks.

## Tech stack (decided 2026-07-02)
Vanilla JS + HTML5 canvas, single-file during prototyping (no game engine — proven unnecessary at this scope) → Capacitor wrapper for iOS → Codemagic cloud build/sign/submit. Browser-playable at every stage.

## Operational notes for Claude (learned 2026-07-02/03)
- **Claude never commits.** Dan commits/pushes via GitHub Desktop after reviewing diffs — this review step is deliberate. Claude supplies the commit message.
- Claude's sandbox cannot run git on the shared folder (lock-file restrictions) and its mounted READ view truncates larger files (caps observed anywhere from ~18KB to ~46KB, and the boundary shifts as the file grows) — the Write/Edit/Read file tools are authoritative; never trust `wc`/`cat`/`node fs` on the mount for app/index.html.
- **Headless testing of the app despite the read cap:** stitch a test copy in the scratchpad from [mounted head] + [bridge] anchored on unique code lines, then run the input-simulation driver (recreate under scratchpad `test/`; drivers 1-7 pattern: DOM stubs, vm sandbox, __t47 hook widened per test). When the cap boundary swallows an anchor, bridge one section higher. Sandbox `bash` CAN WRITE to the mount (icons were written that way) — only reads are capped. **Mirror-drift lesson (2026-07-03): incrementally-patched bridge segments silently drift (one failed assert aborted sibling patches once; a whole feature went missing from the mirror). Rebuild the bridge fresh from `Read` of the real file after heavy edit sessions; sync scripts must apply patches independently and report per-patch status. The real file is always the truth — verify it by direct Read inspection when in doubt.**
- **Verification pays:** headless drivers caught a game-breaking exploit (instant-lock), an untouchable hazard (boom placed above all flight paths), and multiple driver-side false alarms — always distinguish game bug vs test bug before patching the game.
- **Visual asset workflow:** PIL in the sandbox, written directly to the mount; supersample 4× + LANCZOS downscale, soft light via GaussianBlur, grain/vignette to escape flat "programmer art." Render → Read (view) → self-critique honestly → iterate with Dan in short loops. Keep a 60px test strip for icons.
- **Skip zero-gain refactors:** micro-optimizations that add churn risk to verified code are declined deliberately (noted in session log) — cleanup passes target real waste, a11y, comments, docs.
- **Test with REAL state sequences (2026-07-03):** a headless pose test passed with synthetic inputs the game never produces (crash without a quote) and hid an unreachable branch Dan caught on device. Drive verification with the sequences actual play generates.
- **Visual coherence rules (2026-07-03, also in the code header):** outlines mark foreground only; an active prop must visibly change the scene, not just the physics; a hitbox is exactly what's drawn (a 10px draw-vs-hitbox offset on the boom caused "inconsistent" collisions).
- **Search-output display quirk:** grep-style results can render `//` as `\` on lines containing em-dashes — display artifact, not corruption. Read is the authority; don't fix phantom syntax errors.
- **Mount staleness is worse than truncation (2026-07-04):** shortly after Edit-tool writes, the sandbox mount can serve a stale/PARTIAL hybrid of app/index.html (some edits visible, others not; frozen byte size) — never rebuild a test mirror from it mid-session. **The post-push verification gate that replaced it:** after Dan pushes, fetch the raw GitHub file in his Chrome tab (`javascript_tool`: fetch + `new Function(scriptBody)` = full-file parse in a real JS engine + marker-count integrity check), then run a runtime smoke on the live Pages build in the same tab (back up/restore localStorage around it). This gate is mandatory before firing a TestFlight build.
- **Routine maintenance is codified:** MAINTENANCE.md holds the checklist; scheduled task `take47-maintenance` runs it daily 6:38 AM (or on next app launch). Manual run at session end after big batches.
- **Verification prerequisites (Dan, 2026-07-04):** every on-device verification request must include exact QA-panel setup steps (Settings → tap version line 5× → Test Mode: scene jump, prints, props, mercy arm, FTUE reset, rollover force, save backup/restore). Always tell Dan to back up his save first when a step mutates state. Panel is a Phase 5 strip-before-submission hard gate.
- **PIL study harness:** per-set study scripts live in the session scratchpad (dustgulch_study.py = importable base). Scratchpad clears between sessions — rebuild from ART-RESEARCH.md's pattern when needed; approved sheets persist in assets/.

## Phases
0. Environment + stack decision; start Apple Developer enrollment
1. Idea generation (research viral hits; agree on concept)
2. Playable browser prototype — validate the core loop is fun *before* heavy documentation
3. Design doc (DESIGN.md) written around what proved fun
4. Full build: art, sound, juice, menus, scoring
5. Cloud build pipeline → TestFlight beta, user testing
6. App Store submission: metadata, screenshots, privacy policy, age rating, review

## Working rules
- **Accessibility & privacy by design (standing rule, added 2026-07-02):** every feature/change gets checked against accessibility (color-blind-safe signaling paired with text/shapes, readable text sizes/durations, reduce-motion & flash options, no strobing, sound-optional play) and privacy (data minimization, ATT/privacy-label impact of any SDK, privacy policy kept current). Flag concerns to Dan when they involve tradeoffs.
- Use git from day one; commit at every meaningful step. Claude provides a brief commit message at the end of every working session (and at any mid-session point worth committing); Dan pastes it into GitHub Desktop.
- **Batch before building (Dan, 2026-07-02):** don't update the prototype/code after every individual decision. Discuss and settle open questions first, then implement accumulated changes at logical stopping points.
- **Pace discipline (Dan, 2026-07-03, calibrated same day):** don't rush toward the next phase — work isn't "done" until Dan validates it in his hands, and responses close with verification prompts rather than next-step momentum. But rigor target is a **5/10**: meaningful validation without exhaustive ceremony (Dan explicitly dialed back from a 10-rigor checklist). BETA-READINESS.md holds the calibrated list; parked extras only get pulled up on real signals.
- **Code commenting standard (Dan, 2026-07-02):** every code file gets (a) a header block stating its purpose, architecture, and privacy/accessibility posture, and (b) succinct comments on non-obvious decisions — the *why*, not the *what* (e.g., why scenes are seeded, why audio unlocks on tap). Keep comments current when code changes; no comment noise on self-explanatory lines.
- Living docs in this folder: DESIGN.md (spec), DECISIONS.md (choices + why), STATUS.md (current state), BACKLOG.md (post-launch parking lot — new ideas go here, not into v1 scope).
- **Release records (standing rule, Dan 2026-07-04, from TestFlight beta on):** every reported defect gets a DEFECTS.md row immediately (never chat-only) and is tracked to on-device verification; every shipped build gets a CHANGELOG.md entry (engineering) + `releases/X.Y-buildN.md` (user-facing release notes, QA report, known issues, and — for App Store submissions — the exact store-metadata snapshot).
- Update STATUS.md at the end of every working session; log every significant choice in DECISIONS.md with the "why."

## Session protocol (handoff)
**Start:** Claude reads STATUS.md, then opens with a 2-3 line brief — where we left off, what's planned today, anything needing Dan's decision up front (batched). Dan confirms or redirects; then work begins.
**During:** new scope ideas → BACKLOG.md by default (keeps v1 fixed); decisions → DECISIONS.md as they land.
**End:** Claude updates STATUS.md (done / next steps / open questions), supplies the commit note, and flags anything Dan must do before next session (e.g., push, play-test, account actions). Dan commits/pushes via GitHub Desktop — that push is what updates the phone-playable Pages build.
- "Viral" is a lottery — design for its ingredients (one-thumb play, instant restart, shareable score, "one more try" loop) and measure against concrete goals: App Store approval, 20+ TestFlight testers.
