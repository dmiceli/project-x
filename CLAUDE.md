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

## Operational notes for Claude (learned 2026-07-02)
- **Claude never commits.** Dan commits/pushes via GitHub Desktop after reviewing diffs — this review step is deliberate. Claude supplies the commit message.
- Claude's sandbox cannot run git on the shared folder (lock-file restrictions) and its mounted view may truncate larger files (~18KB seen) — the Write/Edit/Read file tools are authoritative; don't trust `wc`/`cat` on the mount for big files.
- **Verify before handing over:** test game-logic changes headlessly (logic mirror + simulated input driver lives in the session scratchpad under `test/`; recreate as needed). Visual changes still need Dan's eyes.

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
- **Code commenting standard (Dan, 2026-07-02):** every code file gets (a) a header block stating its purpose, architecture, and privacy/accessibility posture, and (b) succinct comments on non-obvious decisions — the *why*, not the *what* (e.g., why scenes are seeded, why audio unlocks on tap). Keep comments current when code changes; no comment noise on self-explanatory lines.
- Living docs in this folder: DESIGN.md (spec), DECISIONS.md (choices + why), STATUS.md (current state), BACKLOG.md (post-launch parking lot — new ideas go here, not into v1 scope).
- Update STATUS.md at the end of every working session; log every significant choice in DECISIONS.md with the "why."

## Session protocol (handoff)
**Start:** Claude reads STATUS.md, then opens with a 2-3 line brief — where we left off, what's planned today, anything needing Dan's decision up front (batched). Dan confirms or redirects; then work begins.
**During:** new scope ideas → BACKLOG.md by default (keeps v1 fixed); decisions → DECISIONS.md as they land.
**End:** Claude updates STATUS.md (done / next steps / open questions), supplies the commit note, and flags anything Dan must do before next session (e.g., push, play-test, account actions). Dan commits/pushes via GitHub Desktop — that push is what updates the phone-playable Pages build.
- "Viral" is a lottery — design for its ingredients (one-thumb play, instant restart, shareable score, "one more try" loop) and measure against concrete goals: App Store approval, 20+ TestFlight testers.
