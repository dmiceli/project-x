# Status

**Phase:** 4 — Full build starts next session
**Last updated:** 2026-07-02 (end of day)

## Done
- Project plan reviewed and strengthened; foundation files created.
- Environment confirmed: Windows PC, iPhone for testing, no Mac (cloud build required), sprint pace.
- Apple Developer Program: Dan enrolled (2026-07-02).

- Phase 1 research done; concepts chosen: prototype both "Stick the Landing" and "Squeeze."
- Both prototypes built and playtested. **Winner: Stick the Landing** (ragdoll character theme). Squeeze parked as backup.
- STL v2 built: articulated character, ragdoll crashes, particles, hitstop, perfect-streak scoring, synth SFX.

- v2 playtested: loop validated (streaks work, ramp fair, crashes need comedy in build phase).
- DESIGN.md v1 written. Monetization, v1.0 scope, and tech stack decided (see DECISIONS.md). Name TBD.

- Git live: repo "project-x" on Dan's GitHub; GitHub Pages enabled; workflow: Claude edits → Dan commits/pushes in GitHub Desktop.
- iPhone feel-test passed (tap responsive, spin readable; sound = placeholder until themed).
- Theme + name decided: **TAKE 47** (movie stunt set). Theme confirmed in playtest; quips readable.
- Core restructured to **scenes-as-levels** (persisted progress, retry same scene, seeded scene design) in `prototypes/take-47.html`; includes first accessibility setting (reduce motion). Standing a11y/privacy rule added to CLAUDE.md.

- Scene progression refined: "Reshoot from Scene 1" restart (record preserved); monetization principle locked — ads never buy progress; daily challenge = ~3 attempts/day, rewarded ads for extra attempts.
- Working style: batch decisions via discussion, implement at logical stopping points (see CLAUDE.md).

- Phase 4 design batch settled: 6-character roster, 10 achievements, daily challenge (3 attempts + max 3 ad extras), settings scope, Apple-only analytics. DESIGN.md is now the complete build spec.
- Pre-build cleanup pass on take-47.html (2026-07-02): static set cached (per-frame cost ~45 canvas calls → 1), constants extracted, full comment pass, a11y additions (sound toggle, 44px touch targets, HUD split to ≥14px lines, keyboard S key), privacy audit documented in file header (fully offline, localStorage only). Old prototypes archived via prototypes/README.md. Logic regression-tested headlessly.

## Watch list (known risks, none blocking yet)
- **Phase 5 gate:** migrate save data to Capacitor Preferences (WebView localStorage can be purged by iOS). Must land before TestFlight.
- Codemagic signing/upload without a Mac is designed but unproven — de-risk with a build early in Phase 5, before the game is "done."
- Ad SDK choice (Phase 4/5) brings ATT prompt + privacy-label work; budget a session for it.
- "TAKE 47" name must be reserved in App Store Connect — verify availability when we first touch App Store Connect, not at submission.
- Apple review: rewarded-ad and IAP flows get scrutiny; keep DESIGN.md's caps/discipline implemented exactly.

- Overnight research sprint (2026-07-02, late): five new docs — PIPELINE.md (no-Mac build runbook; cuts watch-list risk #1 to two ~10-min Dan sessions), MARKETING.md (ASO + launch plan draft), TRENDS.md (hybrid-casual shift — our design is on-trend; retention targets adopted), THEME.md (stunt-lore/genre research + IP guardrails), PRIVACY.md (policy draft, ad section pre-written). BACKLOG.md updated with research-driven ideas.

- 2026-07-03: **v1 app built** at `app/index.html` — six genre sets (Dan: full v1), six characters with milestone unlocks, daily challenge (one life, 3 attempts + ad-stub extras), 10 achievements + trophy room, HTML settings/menus (VoiceOver-able), share card via Web Share API, versioned save blob with legacy migration. Full flow verified headlessly (campaign progression, reset-keeps-record, daily attempt limits, settings persistence).

- 2026-07-03 (later): feedback batch implemented — milestone interstitial cards (set changes + cast unlocks with STAR THEM choice), daily = 3 lives/attempt, share button prominent on CUT screen (+ home screen) with 0.6s lockout so it's seen. Bonus: headless testing caught a game-breaking exploit (instant-lock = free landing) — fixed with a 200° spin gate ("TOO SOON!"). All flows re-verified headlessly, including a skilled-play run to Scene 12.

- 2026-07-03 (later still): interstitial cards given context per Dan's feedback — set changes are now wrap parties with stats ("THE BACKLOT — WRAPPED. All ten scenes shot in 43 takes") + a flavor tease of the next set; cast unlocks carry character bios + what the player survived to earn them. Re-verified headlessly.

- 2026-07-03: playtest verdicts — milestone cards land ✓; 3-lives daily locked ✓; share rebuilt as a challenge ("BEAT THIS." card + taunt text + playable link via native share sheet; beta link = Pages URL, swaps to App Store at launch). "TOO SOON!" confirmed working (only shows on premature lock taps). **Open: GAME_URL needs Dan's GitHub username.**

- 2026-07-03: **Joy package shipped** after guided replayability session — near-miss tier, the Reel (reshoot/print), Poster Wall, Call Sheet dailies, golden takes, director approval, prints wallet + wardrobe (18 colorways). All flows verified headlessly (near-miss trigger, scene-21 run, reshoot isolation, wallet math, call-sheet payout, golden seeding).

- 2026-07-03: **Depth pass shipped** — economy baseline logged; "every set teaches a stunt" (cart/boom/gravity/wind/arm/double-bounce, full v1 per Dan); logarithmic ramp w/ brutal-but-fair ceiling (floor 12° @ ~scene 72); launch platforms everywhere; cycle-2 combos. Headless verification caught + fixed an untouchable-boom placement bug. Sub-frame lock timing noted in BACKLOG as pre-beta fairness candidate.

- 2026-07-03 (late): **Incentives batch shipped** — Prop Department (6 earned-only consumables w/ belt + shop, assisted-takes-don't-print, barred from daily), daily personal-best pay, visible call-sheet rewards, achievement progress + halfway toasts. All verified headlessly.

- 2026-07-03 (pre-polish audit): FTUE package (guided first takes + progressive home disclosure), miss-angle crash lessons, midnight-reset hook, interstitial placeholder on real caps. All verified headlessly. Save-durability gate added to watch list.

- 2026-07-03 (final quick wins): share card carries the play link ON the image; app icon (180 + 1024px placeholder) + iOS home-screen meta (standalone, status bar, title); take-counter milestone quips (100/250/1000/2000); version stamp in Settings + global error handler that saves progress. Regression green.

- 2026-07-03: cart fairness fix — live trajectory preview (dotted arc, green-ring-on-mat / red-X-off marker) so launch timing is aimed, not guessed. Verified headlessly.

- 2026-07-03: **Polish phase opened with the brand kit** — BRAND.md (research-grounded: single-focal icon data, gold-reward psychology, roles-not-vibes palette; full WCAG contrast audit — all pairings AA+, most AAA) + assets/brand-sheet.png. Kit codifies the shipped identity; all polish assets now build from it.

- 2026-07-03: **Icon finalized (MVP)** after 11 iterations — "clapperboard contains the scene": no-text container composition, screaming inverted flipper (now the franchise face, per DESIGN note), spotlight, stage, X mark. Production files in app/ (icon-1024/180); source assets/icon-final.png; iteration artifacts cleaned.

- 2026-07-03 (session end): **sanitization pass** — folder audited (prototypes/README updated: all prototypes archived, app/ is the game); a11y fixes (canvas aria-label, FTUE pulse respects reduce-motion); file header rewritten to current architecture; zero-gain refactors deliberately skipped (verified code > micro-churn); full headless regression green; CLAUDE.md operational lessons expanded (read-cap workaround, verification wins, visual workflow).

- 2026-07-03 (new session): **face pass shipped** — franchise face on the in-game character (terror scream in flight, relief on clean landings, grin on perfects, unchanged X-eyes/faceplant variants) and the star now appears mid-scream on the share card beside the number, wearing the player's selected costume. drawGuy/drawAccessory parameterized for reuse. Regression green.

- 2026-07-03: BRAND.md expanded — copy rules (4 registers: STAMPS / sentence case / Title Case / quips) + art direction reference (Tim-adjacent flat deadpan, inspiration-only). In-app capitalization violations fixed ("Wait for the spin…", home stats normalized). Regression green.

- 2026-07-03: **Flipper direction settled via 3-way study** (assets/flipper-direction-study.png): B-hybrid — anatomy + scream kept, flat/muted/mid-line treatment adopted. Icon re-rendered and deployed (same composition); Stunt Guy recolored in-app (ochre/sand/brick); Marquee Gold now exclusive to rewards/CTAs. Wardrobe mute pass for other characters → BACKLOG.

- 2026-07-03: **Sound pass v2 shipped** ("deadpan delivery, cartoon heart" — codified in BRAND art direction per Dan's kid-friendly note): filtered-noise foley (wood-crack clapper, whoosh, body thud, dry tumble), warm accents kept cartoonish-lite (perfect sting + sparkle, golden coin-glint, one honest boing on bounces, faint sad-trombone tail on crashes). New fnoise (bandpass) helper; golden takes and bounces got dedicated sounds. Regression green.

- 2026-07-03: sound approved MVP; **crash comedy pass shipped** — per-part ragdoll restitution + one "launcher" part that gets famous, brief slow-mo (0.35×, ~0.5s) on spectacular crashes (>92° miss or any hazard hit), and the 12% delayed falling-light gag: a stage lamp gives up half a beat after the crash, BONK., lens dies on impact. Regression green.

- 2026-07-03: **Comedy & Clarity batch shipped** (all four of Dan's points): crashes now prominent (launcher part rockets, wide scatter, slow-mo every wipeout, impact puffs, longer beat); the falling light is a proper 3-act gag (creak → lazy fall on a cable → BONK., lens dies) drawn above everything; game-wide art pass (outlined recognizable props — lamps/camera/mat/genre sets, kaiju arm has a zipper now); verdict stamps (rotating word pools on slate chips, tilt + pop, never clipped off-screen). Art code relocated to file tail (head stability). Full regression green.

- 2026-07-03: **Pace reset (Dan):** no rushing between phases; validation gets equal energy to construction. Rule added to CLAUDE.md; **BETA-READINESS.md created** — the no-stone-unturned checklist (8 sections, honest statuses) that now governs the path to TestFlight.

## Next steps
1. Dan: review/amend BETA-READINESS.md — add stones, challenge statuses, pick what we tackle first.
2. Work the checklist together, at whatever depth each item deserves. Screenshots and pipeline happen when the list says so, not before.
3. **App Store screenshot set** per BRAND.md ("the fail is the ad").
4. Then Phase 5: PIPELINE.md runbook → Capacitor wrap (save-durability gate) → hello-world TestFlight build.
2. Then: polish phase (real icon art, sound design, crash comedy pass) → PIPELINE.md → TestFlight.
2. Then: tuning/polish batch → icon + real sound design.
3. PIPELINE.md runbook → first hello-world TestFlight build.
4. Later: verify "TAKE 47" name in App Store Connect.
