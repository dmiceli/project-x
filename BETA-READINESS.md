# BETA-READINESS.md — the no-stone-unturned checklist

*Created 2026-07-03 at Dan's direction. This document governs the path to TestFlight. Statuses: ✅ validated (Dan has confirmed it in his hands) · 🔶 built, not yet validated by Dan · ⬜ open. Nothing ships while a blocking ⬜/🔶 remains in sections 1–7. We work through this together; either of us can add stones.*

## 1. Gameplay & feel (owner: Dan, structured playtests)

- 🔶 **Fresh-save FTUE run** — private tab, zero context: coaching clear? Home reveal pacing right? First success within a minute?
- 🔶 **Comedy & Clarity batch verdict** — crash spectacle, gag visibility, verdict variety, sets readable (the current build's headline changes)
- 🔶 **Mechanic-by-mechanic tour** — cart (with preview), boom, gravity, wind, arm, double-bounce: each fair, readable, fun? (The Reel makes revisiting each set easy)
- 🔶 **Long-session difficulty** — play deep in one sitting: does the ramp hold interest? Where does frustration first appear, and is it the good kind?
- 🔶 **Daily challenge week** — play the gauntlet several real days: attempt economy right? PB pay motivating?
- 🔶 **Prop economy in practice** — do props feel like clever production choices? Prices right against real earning?
- 🔶 **Sound pass verdict** — clapper/crash/boing dosage (approved as MVP concept; validate in extended play)
- ⬜ **Second-opinion playtest** — at least one person who isn't us plays the FTUE cold while Dan watches silently (the single highest-value test on this list)

## 2. Technical QA (owner: Claude builds tests/fixes; Dan verifies on device)

- 🔶 **Full-flow headless regression** — green as of latest build (rerun before every push)
- ⬜ **Device matrix** — Dan's iPhone (Safari + home-screen standalone) verified deliberately: safe areas, notch, no scroll-bounce, audio unlock, orientation behavior
- ⬜ **Interrupt handling** — incoming call / app-switch mid-flight: game state sane on return? Audio resumes?
- ⬜ **Midnight rollover** — daily + call sheet reset correctly across a real midnight (not just code review)
- ⬜ **Save integrity** — old-save upgrade path (Dan's live save has survived every schema change so far — confirm after latest); export a copy of Dan's save as a test fixture
- ⬜ **Long-session soak** — 30+ min continuous play: memory/heat/frame-rate on device
- ⬜ **Error handler fire drill** — deliberately trigger an error; confirm save persists and reload hint shows

## 3. Accessibility on-device (owner: both)

- ⬜ **VoiceOver walkthrough** — every menu screen navigable and sensibly labeled (canvas gameplay exempt by design, documented)
- ⬜ **Reduce-motion full session** — all effects respect it (shake, flash, pulses, wobble, stamps); game still feels alive
- ⬜ **Sound-off full session** — nothing depends on audio
- ⬜ **Small-device text audit** — all text ≥ readable at Dan's phone size; check the longest strings (call-sheet rows, home stats)

## 4. Content & copy (owner: Dan reads, Claude fixes)

- ⬜ **Full in-app copy read** — every quip, bio, achievement, toast, setting, card against BRAND copy rules + voice (whimsy, never cheesy)
- ⬜ **Share card + share text final review** — the most-traveled asset; wording, layout, link
- 🔶 **Capitalization audit** — rules codified, one pass done; re-sweep after all recent additions (BONK., verdict pools, prop toasts)

## 5. Economy calibration (owner: both, data from Dan's play)

- ⬜ **Real earn/spend log** — after Dan's next few sessions: prints earned/hr, first wardrobe buy timing, prop usage rate vs baseline intent in DESIGN.md
- ⬜ **Adjustment pass if needed** — prices first, earn rates second (per baseline rule)

## 6. Pre-pipeline gates (owner: Claude)

- ⬜ **Save migration to Capacitor Preferences** — HARD GATE before TestFlight (iOS can purge WebView storage)
- 🔶 **Ad pacing placeholder** — wired to real caps; validate the annoyance level in Dan's long session
- ⬜ **Remove-ads IAP stub** — decide beta presentation (hidden vs visible-disabled)
- ⬜ **Version/versioning scheme** — bump discipline for beta builds (v0.9.x)

## 7. Store & legal (owner: both)

- ⬜ **Privacy policy published at a public URL** — required before submission; PRIVACY.md drafted, needs publish + contact-email decision (dedicated address?)
- ⬜ **App Store name reservation** — "TAKE 47" availability check in App Store Connect (watch-list item; do at first ASC touch)
- ⬜ **Age rating questionnaire dry-run** — walk Apple's questions before submission day
- ⬜ **Screenshot set + preview video** — per BRAND ("the fail is the ad"); AFTER feel validation locks the look
- ⬜ **Store copy** — title/subtitle/description per MARKETING.md ASO draft + copy rules

## 8. Beta program design (owner: both)

- ⬜ **Success criteria** — what must be true to exit beta? (e.g., 20+ testers, D1 signal, no save-loss reports, crash-free sessions)
- ⬜ **Tester recruitment plan** — wave 1 list (names!), wave 2 communities per MARKETING.md
- ⬜ **Feedback instrument** — structured form (difficulty, favorite/least-favorite mechanic, economy, one-word feel) + TestFlight notes
- ⬜ **Beta build cadence** — how often we ship, what a beta changelog looks like (production-memo voice)
