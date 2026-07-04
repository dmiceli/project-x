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

Bundle ID mismatch between Capacitor config, Xcode project, and App Store Connect record (keep it identical everywhere, set once). API key with insufficient role (use App Manager). Missing 1024×1024 app icon — TestFlight upload rejects without it (icon lands early in Phase 5, not last). First build always takes debugging — schedule the *hello-world TestFlight build* as its own session before the game is final. **Learned 2026-07-04, corrected after builds #1–#7 (final):** the yaml `environment.ios_signing` block only FETCHES signing files already stored in **Codemagic's Code signing identities vault** — an empty vault fails instantly with "No matching profiles found," and the script flow (`fetch-signing-files --create`) is no rescue because creating a certificate requires a `CERTIFICATE_PRIVATE_KEY` secret. **The right one-time fix is filling the vault in the UI (~5 min, no key material handled):** Codemagic → Team settings → Code signing identities → iOS certificates → *Generate certificate* (Apple Distribution, via the ASC integration) → developer.apple.com → Profiles → create an App Store profile for the bundle ID using that certificate → back in Codemagic → iOS provisioning profiles → *Fetch profiles*. Then the plain `ios_signing` block just works, forever.

## ✅ First-build session log (2026-07-04, "7 takes" — total ~12 build minutes)

| # | Failure | Lesson |
|---|---------|--------|
| 1–2 | "No matching profiles found" (instant) | Vault empty + integration then misnamed |
| 3 | Capacitor CLI: NodeJS >= 22 required | `node: 22` in yaml |
| 4 | Archive: "requires a provisioning profile"; log: "Cannot save Signing Certificates without certificate private key" | Script `--create` can't mint certs without a key secret |
| 5 | "No matching profiles found" (instant) | Proved `ios_signing` never creates — vault was still empty |
| 6 | Upload check 90474: portrait-only needs all orientations or fullscreen | `UIRequiresFullScreen=true` in Info.plist |
| 7 | **NONE — uploaded, processed, "Ready to Submit" in TestFlight** | Known noise: Codemagic's post-upload "App Store distribution" step showed red despite success — check log next build |

Vault contents (Codemagic → Code signing identities): certificate `take47_distribution` + profile `take47_appstore_profile` (both expire 2027-07-03 — renew both then). Internal group **Crew** (automatic distribution ON) + Dan invited. The per-release loop below is now LIVE (manual trigger for now; flip `triggering` to push events once stable).

## Dan-facing summary

Two setup sessions on your side (~25 min total, steps 2-4), then it's fully automatic. Nothing needs a Mac at any point ([Capawesome overview](https://capawesome.io/blog/how-to-build-and-deploy-ios-apps-without-a-mac/), [Capgo from-Windows guide](https://capgo.app/blog/build-ios-app-from-windows-capacitor-capgo-build/)).

## Phase 5 additions (approved big wins, 2026-07-04)
- Game Center leaderboard (daily gauntlet best + furthest scene) — Capacitor plugin, no backend, no privacy-label change.
- Local notification at midnight reset (opt-in, asked in-context after a completed daily; on-device only, no ATT).
- Wire existing haptic() calls to Capacitor Haptics + keep settings toggle.

## ✅ Step 1 complete (2026-07-04) — repo is Capacitor-ized

In the repo now: `package.json` + lockfile, `capacitor.config.json` (bundle ID `com.dmiceli.take47`, webDir `app`, set-black background), the generated `ios/` Xcode project (our real 1024px icon in the asset catalog, brand splash screens, portrait-locked, `ITSAppUsesNonExemptEncryption=false`), `codemagic.yaml` (manual-trigger TestFlight workflow), and the save write-through to Capacitor Preferences inside the game (browser no-op; restores + reloads once if iOS ever purges WebView storage). `node_modules/` is gitignored — Codemagic installs fresh via `npm ci`.

## ▶ Dan's setup checklist (~25 min, steps 2–4 of the runbook — do in this order)

**A · App Store Connect app record (~10 min)** — appstoreconnect.apple.com → My Apps → ➕ → New App → platform **iOS** · name **TAKE 47** *(this is the name-availability moment — if taken, stop and we regroup on naming)* · language English (U.S.) · bundle ID **com.dmiceli.take47** (register it at developer.apple.com → Identifiers if the dropdown doesn't offer it: ➕ → App IDs → App → explicit `com.dmiceli.take47`, no extra capabilities yet) · SKU `take47`.

**B · API key (~5 min)** — App Store Connect → Users and Access → Integrations → App Store Connect API → ➕ generate key, role **App Manager**. Download the `.p8` **once** and keep it somewhere safe on your PC; note the **Key ID** and **Issuer ID**. ⚠️ Never paste the key contents into chat or the repo.

**C · Codemagic (~10 min)** — codemagic.io → sign up with your GitHub login → grant access to `project-x` → Teams → Personal team → Integrations → **App Store Connect** → add the key from B (upload the .p8, enter Key ID + Issuer ID) and name the integration exactly **`take47-asc-key`** (codemagic.yaml references that name) → Applications → Add application → `project-x` → select **codemagic.yaml**.

**D · First build (with Claude, next session)** — press "Start new build" on the `ios-testflight` workflow and we debug whatever the first build throws (the runbook budgeted a session for this). When it's green: TestFlight → your iPhone.
