# CHANGELOG.md — developer changelog (technical, per shipped build)

One entry per build that reaches a phone (TestFlight or App Store). Newest first. Format loosely follows [Keep a Changelog](https://keepachangelog.com): Added / Changed / Fixed / Removed. User-facing release notes live in `releases/`; this file is the engineering truth.

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
