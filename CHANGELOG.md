# CHANGELOG.md — developer changelog (technical, per shipped build)

One entry per build that reaches a phone (TestFlight or App Store). Newest first. Format loosely follows [Keep a Changelog](https://keepachangelog.com): Added / Changed / Fixed / Removed. User-facing release notes live in `releases/`; this file is the engineering truth.

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
