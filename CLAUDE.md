# Project X — iOS Game

## Goal
Dan (product owner) and Claude (lead developer) build a low-complexity iOS game and publish it to the Apple App Store. This is also a test of whether a non-developer can ship a real product with Claude.

## Who's who
- **Dan**: technically savvy, zero development experience. Makes all product decisions. Explain every technical concept in plain language — never assume coding knowledge.
- **Claude**: lead developer and translator. Always present tradeoffs with a clear recommendation. Ask before anything costly, irreversible, or account-related (Apple ID, payments, publishing actions).

## Environment (confirmed 2026-07-02)
- Windows PC only — **no Mac**. All iOS compilation/signing/upload goes through a cloud build service.
- iPhone available for on-device testing.
- Apple Developer Program ($99/yr): Dan will enroll early, during design phase.
- Pace: sprint mode (near-daily sessions). Target: TestFlight beta in ~2 weeks.

## Tech direction
Decide in Phase 0. Leading approach: build the game in web tech (HTML5 canvas, e.g. Phaser) so prototypes run instantly in the iPhone browser, then wrap with Capacitor and build/sign/submit via a cloud service (e.g. Codemagic). Alternative: Expo + EAS. Log the final choice in DECISIONS.md.

## Phases
0. Environment + stack decision; start Apple Developer enrollment
1. Idea generation (research viral hits; agree on concept)
2. Playable browser prototype — validate the core loop is fun *before* heavy documentation
3. Design doc (DESIGN.md) written around what proved fun
4. Full build: art, sound, juice, menus, scoring
5. Cloud build pipeline → TestFlight beta, user testing
6. App Store submission: metadata, screenshots, privacy policy, age rating, review

## Working rules
- Use git from day one; commit at every meaningful step.
- Living docs in this folder: DESIGN.md, DECISIONS.md, STATUS.md.
- Update STATUS.md at the end of every working session; log every significant choice in DECISIONS.md with the "why."
- "Viral" is a lottery — design for its ingredients (one-thumb play, instant restart, shareable score, "one more try" loop) and measure against concrete goals: App Store approval, 20+ TestFlight testers.
