# BETA-READINESS.md — the path to TestFlight (rigor: 5/10 by Dan's calibration)

*Statuses: ✅ validated by Dan · 🔶 built, awaiting validation · ⬜ open. Core items gate the beta; parked items only get pulled up if play or beta signals warrant.*

## Core validation (one good play session + short sweeps)

- 🔶 **Fresh-save FTUE run** (Dan, ~10 min, private tab) — coaching clear, home reveals paced right, first success fast
- 🔶 **The big feel session** (Dan, one sitting) — covers in one pass: crash spectacle + gag + verdicts + readable sets (Comedy & Clarity verdict), mechanic feel via normal progression + a few Reel revisits, difficulty ramp, sound dosage, prop/economy gut-check, ad-placeholder annoyance
- ⬜ **One cold playtest** (someone who isn't us, Dan observing silently) — the highest-value item on the list
- ⬜ **Combined a11y sweep** (Dan, ~15 min) — VoiceOver through menus, then a few scenes with reduce-motion on and sound off
- ⬜ **Full copy read** (Dan, ~15 min in-app) — every quip/bio/toast/setting against the voice; Claude fixes
- ⬜ **Standalone device check** (Dan, ~5 min) — home-screen app: icon, fullscreen, safe areas, audio unlocks; confirm current save intact
- ⬜ **Daily rollover observed** (passive) — next real midnight: gauntlet + call sheet reset correctly

## Hard gates (Claude, before TestFlight)

- ⬜ **Save migration to Capacitor Preferences** (iOS can purge WebView storage — non-negotiable)
- ⬜ **Privacy policy published at public URL** + contact-email decision
- ⬜ **"TAKE 47" name check** at first App Store Connect touch
- 🔶 **Headless regression green on every push** (standing practice)

## Launch checklist (quick items, sequenced at pipeline time)

- ⬜ Screenshot set + store copy (per BRAND/MARKETING) — after feel validation locks the look
- ⬜ Age-rating questionnaire dry-run
- ⬜ Beta success criteria + wave-1 tester names + simple feedback ask (TestFlight notes + 3 questions)
- ⬜ Version bump discipline (v0.9.x)

## Parked (10-rigor extras — pull up only on signal)

Interrupt/call handling test · 30-min soak test · error-handler fire drill · save-fixture export · economy earn/spend logging · formal feedback instrument · beta build cadence doc · device matrix beyond Dan's phone (beta testers cover this naturally)
