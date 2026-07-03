# PIPELINE.md — no-Mac build & release runbook

*Researched 2026-07-02. Purpose: de-risk Phase 5 before we need it. Primary: Codemagic. Fallbacks exist (Capgo Build, Ionic Appflow, Capawesome Cloud) if Codemagic disappoints.*

## How it works (plain language)

We never compile iOS code on the PC. The repo holds our web game plus a Capacitor "wrapper" project. Codemagic rents us a Mac in the cloud: on each trigger it pulls the repo from GitHub, builds the iOS app, signs it with credentials it manages for us, and uploads straight to TestFlight. Signing without a Mac is possible because Codemagic talks to Apple through an **App Store Connect API key** — it creates and manages the certificates/provisioning profiles on our behalf ([Codemagic docs](https://docs.codemagic.io/yaml-code-signing/signing-ios/), [automatic signing](https://docs.codemagic.io/partials/alternative-code-signing-methods-ios/)).

## One-time setup (in order)

1. **Capacitor-ize the repo (Claude, on PC).** Add `package.json`, install Capacitor, `npx cap add ios` — this generates the `ios/` native project folder that cloud Macs will build. Set the bundle ID (e.g., `com.dmiceli.take47`) — must match everywhere.
2. **App Store Connect: create the app record (Dan, ~10 min).** appstoreconnect.apple.com → My Apps → "+" → New App: platform iOS, name **TAKE 47** (this is when we learn if the name is free — watch-list item), bundle ID as above, SKU anything. 
3. **App Store Connect API key (Dan, ~5 min).** Users and Access → Integrations → App Store Connect API → generate key with **App Manager** role. Download the `.p8` file (one-time download — keep it safe), note Key ID + Issuer ID. ⚠️ Treat like a password: never goes in the repo or chat; it gets pasted directly into Codemagic's UI.
4. **Codemagic account (Dan, ~10 min).** Sign up with GitHub login → grant access to `project-x` repo → Teams/Integrations → connect App Store Connect with the API key from step 3. Free tier: 500 macOS build minutes/month — plenty (each build ≈ 10-15 min).
5. **codemagic.yaml (Claude).** Workflow file in repo root: install deps → copy web build into wrapper (`npx cap sync ios`) → `xcode-project build-ipa` with automatic signing → publish to TestFlight. Sample basis: [Codemagic Ionic/Capacitor guide](https://docs.codemagic.io/yaml-quick-start/building-an-ionic-app/), [capgo walkthrough](https://capgo.app/blog/automatic-capacitor-ios-build-codemagic/).

## Per-release loop (after setup)

Dan pushes → Codemagic builds/signs → TestFlight processes (~15-30 min) → testers get the update notification. Effectively: **push to GitHub = new beta on phones.**

## Known failure points (and pre-answers)

Bundle ID mismatch between Capacitor config, Xcode project, and App Store Connect record (keep it identical everywhere, set once). API key with insufficient role (use App Manager). Missing 1024×1024 app icon — TestFlight upload rejects without it (icon lands early in Phase 5, not last). First build always takes debugging — schedule the *hello-world TestFlight build* as its own session before the game is final ([common issues](https://docs.codemagic.io/troubleshooting/common-ios-issues/)).

## Dan-facing summary

Two setup sessions on your side (~25 min total, steps 2-4), then it's fully automatic. Nothing needs a Mac at any point ([Capawesome overview](https://capawesome.io/blog/how-to-build-and-deploy-ios-apps-without-a-mac/), [Capgo from-Windows guide](https://capgo.app/blog/build-ios-app-from-windows-capacitor-capgo-build/)).

## Phase 5 additions (approved big wins, 2026-07-04)
- Game Center leaderboard (daily gauntlet best + furthest scene) — Capacitor plugin, no backend, no privacy-label change.
- Local notification at midnight reset (opt-in, asked in-context after a completed daily; on-device only, no ATT).
- Wire existing haptic() calls to Capacitor Haptics + keep settings toggle.
