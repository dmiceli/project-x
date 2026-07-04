# CHANGELOG.md — developer changelog (technical, per shipped build)

One entry per build that reaches a phone (TestFlight or App Store). Newest first. Format loosely follows [Keep a Changelog](https://keepachangelog.com): Added / Changed / Fixed / Removed. User-facing release notes live in `releases/`; this file is the engineering truth.

## [1.0 (build 11)] — 2026-07-04 · beta feedback batch 1 (auto-shipped, unattended)

Shipped by the `take47-ship-take11` scheduled task after Dan's approval and push (commit 2d8c7e7). Pipeline 3m 10s, App.ipa uploaded to ASC.

**Added**
- D-020: 📣 SHARE TODAY'S RESULT directly on the daily screen (visible once played today; forces the daily share variant); in-game prints chip redesigned as an unmistakable film-print ticket (dark ticket, sprocket hole columns, gold count, PRINTS caption) — no longer reads as a second iPhone battery.
- D-021: home-screen wallet stat is now a tappable shortcut to the Prop Department. In-gameplay HUD stays untappable BY DESIGN (canvas = one big button; ratified by Dan).
- D-022: home stats line reframed as the "production slip" — slim panel with film-sprocket rails, gold scene number, wallet link preserved.
- New home tagline: "the first 46 didn't land."

**Changed**
- D-016: cold open no longer auto-advances on a 2.3s timer — after the ACTION! beat the scene HOLDS with a pulsing "TAP TO ROLL" prompt (static under reduce-motion); the player's tap rolls the guided first take.
- D-018: daily-end canvas decluttered to CUT! + quip + "🎬 TAP FOR YOUR DAILIES REPORT"; stats live on the DAILIES REPORT card alone; miss-angle lesson suppressed on the final life.
- D-019: two-line CTA pattern (bold main line + small dim `.sub` detail line) on the EXTRA ATTEMPT ad button and START OVER — wraps are now intentional.

**Fixed**
- D-017: toast hidden state now translates by calc(-100% − sat − 24px) with opacity:0 + pointer-events:none — no more half-visible toasts stuck under the clock (or intercepting taps).
- D-023: in-game HUD prints chip now draws wallet() (earned − spent) like every other surface, instead of lifetime `S.prints`; all other displays audited clean.

**Notes**
- GitHub Pages was serving the previous build at ship time (deploy/CDN lag, up to ~10 min); the post-push runtime smoke was run by injecting the verified raw-main file into a live browser tab instead. Codemagic pulls the repo directly, so TestFlight is unaffected.
- The red post-upload "App Store distribution" step (open since build 7) is decoded for this build: upload succeeded (delivery bd6c2af4, ASC processing complete); the red is the workflow's auto-submit to TestFlight beta review failing with 422 "Another build is in review" (build 9 holds the version's review slot). Benign — internal Crew distribution is automatic and unaffected.

## [1.0 (build 10)] — 2026-07-04 · beta-night build (icons, copy, share grid, reminder)

**Added**
- D-014 icon system in-game: 10 runtime-drawn glyphs (director's-chair HOME, slate DAILY, masks CAST, crate PROPS, projector REEL, framed-star POSTERS, trophy-v2 AWARDS, megaphone SHARE, aperture SETTINGS, film-print ticket for prints) replacing the generic emoji tier; emoji retained as fallback; prints glyph on wallet chip + BUY buttons.
- Wordle-style daily share grid (NEXT-10 #2): 🟩 perfect / 🟨 clean / 🟥 crash per take, in shareText with date + gimmick.
- 🌙 Midnight call-sheet reminder (approved big win): local notification (fully on-device), offered once in-context on the DAILIES REPORT card, Settings toggle, web no-op.

**Changed (D-015 cold-read verdicts, all Dan-approved)**
- First print earn now introduces the currency explicitly; first clean landing teaches clean-vs-perfect.
- 🏆 AWARDS / THE AWARDS SHELF (was HIGHLIGHTS / HIGHLIGHT REEL — collided with THE REEL).
- "START OVER (back to Scene 1 — your record is kept)" (was RESHOOT FROM SCENE 1).
- PLAY TODAY'S CHALLENGE; "gauntlet" demoted to flavor copy; share text says "daily challenge".
- "⭐ MAKE THEM THE STAR" (was STAR THEM).

## [1.0 (build 9)] — 2026-07-04 · pre-beta polish (first 60 seconds)

**Added**
- One-time cold open on fresh saves: slate drop + clap, "ACTION!" bubble, straight into the guided first take — no menu before the first flip. Skippable; reduce-motion variant.
- First-ever-landing celebration card ("THAT'S A KEEPER") that also introduces the lot.
- DAILIES REPORT as a real interstitial card: gimmick kicker, record callout, 📣 SHARE on-card (keepOpen), exits to the daily screen (`after` route in the card engine).
- Real iOS haptics via the Taptic engine (light=lock, medium=landing, heavy×2=crash).
- New app icon ("A1 WHOA") in the asset catalog + web touch icons.

**Fixed**
- D-012: FOG OF WAR keeps the cart landing marker (fairness), hides only the arc.
- D-005 scale bugs: GALE WARNING now on the real wind scale (×1.6 / ±12 crosswind); BUDGET CUTS also tightens landing tolerance (×0.82, 10° floor) so it bites on non-cart steps. Sweep: 120 dates × 12 steps, all bounds hold.
- D-002 follow-up: env() confirmed dead in WKWebView on-device; inset fallback upgraded to an 11-class device-width table (16 Pro Max 62pt … SE 20pt).
- D-013: HTML overlay screens vertically centered on tall phones (auto-margin pseudo pair; long lists still scroll).
- Wardrobe: ALL unowned colorways are preview-first, buy-second (D-006 follow-up); preview persists while deciding.

**Notes**
- IPA 3.77→1.11 MB: old grain-heavy icon PNGs replaced by flat design.
- Pages deploy for this commit flaked GitHub-side ("try again later"); re-run triggered. TestFlight unaffected (Codemagic pulls the repo directly).

## [1.0 (build 8)] — 2026-07-04 · first-night fix batch

**Added**
- Daily modifier system "Today's Gimmick" (D-005): 7 seeded date-locked mutators (GALE WARNING, WIRE WORK, BUDGET CUTS, MIRROR MODE, FOG OF WAR, GOLDEN HOUR, UNDERCRANKED); slate on the daily screen, in-run HUD chip, DAILIES REPORT wrap screen, gimmick on the share taunt.
- Cast portraits rendered from the in-game rig; locked cast silhouettes; wardrobe colorway preview on chip tap (D-006).
- Poster wall thumbnails from real set art; COMING SOON dimmed tease (D-003).
- Hand-drawn prop card art ×7; prop belt hierarchy (hazard-counter ★ first, generics dimmed); persistent active-prop chip + slow-mo film-gate treatment (D-008/D-010).

**Fixed**
- Safe-area layout: canvas below the notch, symmetric cinematic letterbox, JS-measured insets with iOS fallback + QA diagnostics (D-002).
- Daily/call-sheet rollover now local midnight, not UTC (D-007).
- Ad cap enforced in-handler with visible "x/3 left today" counter (D-004 hardening; original report not reproduced).
- Prop Department wallet as headline chip (D-009).

**Changed**
- Iconography: prints 🎞️ (was 🖨), Reel 📽️, rewarded ad 🍿 (D-011).

**Known issues**
- FOG OF WAR can hide the cart aim preview — fairness regression on daily cart steps (D-012, fix queued build 9).
- App icon still the old design (new icon lands build 9).

## [1.0 (build 7)] — 2026-07-04 · first TestFlight build

**Added**
- Capacitor 8 iOS shell: portrait-locked, fullscreen-only (`UIRequiresFullScreen`), brand splash, real 1024px icon, `ITSAppUsesNonExemptEncryption=false`.
- Save durability: `persist()` write-through mirror to Capacitor Preferences; boot restore + single reload if iOS purges WebView storage (browser no-op). *Verified on-device: survives force-quit.*
- Codemagic CI: `ios-testflight` workflow (manual trigger) → build, sign from Code signing identities vault, upload to TestFlight; internal group "Crew" with automatic distribution.

**Game content** (identical to the final Pages build of 2026-07-04)
- Express-QA feel fixes: random flip pose per take; High Seas sea band + serpent eye; "TAP FOR TAKE n" copy; live poster wall; HIGHLIGHT REEL rename.
- Exploration batch: flip pose variety (tuck/pike/layout/twist), instant-buy + undo toast, Launch Rig hold-to-aim prop, sub-frame landing judgment ("RODE IT OUT!"), mercy prop at 7 wall-crashes.

**Known issues**
- Codemagic's post-upload "App Store distribution" step reports red despite successful delivery — cosmetic CI noise, under investigation.
- QA Test Mode panel present (intentional through beta; hard-gate strip before App Store submission).
