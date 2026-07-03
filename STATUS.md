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
- **Phase 5 hard gate: strip the QA Test Mode panel** (Settings, revealed by 5 taps on the version line) before the App Store build — hidden state-manipulation menus invite review questions and player exploits.
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

- 2026-07-03: **Dan's screenshot defect report fixed** (all three): HUD gets a cinematic top scrim + prompts on pill backings (text never fights lighting; rig lamps moved clear of the HUD zone); launch platform is now stacked APPLE BOXES (real film gear) and all launch spots/cart path moved clear of a more compact camera; backlot flats are now an obvious painted-sky backdrop + raw flat with braces; full-width floor tape (the "checkerboard") replaced by hazard tabs at the mat ends. Verified by full line-by-line inspection of the real file; mirror chain retired after drift (lesson in CLAUDE.md).

- 2026-07-03: **Defect round 2 fixed** (Dan's screenshots): prompt pills + verdict chips now MEASURE their text (shrink-to-fit + on-screen clamp — the old length-estimate math caused every cutoff); FTUE coaching split into two shorter lines and all ready-prompts moved above the platform zone (no more pill-over-character); Dust Gulch cactus relocated mid-stage clear of the camera; apple boxes redrawn as staggered crates with oval grab slots (the centered square slot read as drawer knobs); floor is now planked stage decking; hazard tabs (the last "checkerboard remnants") removed; crash mat got corner ties. Background direction decided: **influence** (Dan).

- 2026-07-03 (Dan away, per his ask): **background art research + Dust Gulch depth pilot.** Market research on 2026 hybrid-casual art + background craft distilled into **ART-RESEARCH.md** (layer rules, contrast law, per-set plans for all six backgrounds). Dust Gulch pilot SHIPPED in-game (low sun focal point, hazed mesas, birds, scrub ridge, windmill silhouette — no outlines at distance); before/after sheet at assets/dustgulch-before-after.png, iterated once via render-critique loop. Remaining five sets await Dan's pilot verdict, then land as one batch. Also resolved Dan's usage question: the long-running "complex response" was a scheduled task session (daily 7am briefing/LinkedIn post), not this project.

- 2026-07-03: **HUD v2 shipped** — Dan flagged persistent mid-field text; 3 icon+counter mockups rendered over the Dust Gulch pilot (assets/hud-options.png); Dan chose **C: mini clapperboard**. Scene/take now live on a small diegetic slate top-left (daily shows hearts + count, a11y intact), prints on a ticket chip top-right, stunt conditions as compact tags top-center; big scrim removed, playing field is now empty. Lifetime/furthest/set-name dropped from the persistent HUD (still on home + CUT screens). New block smoke-tested headlessly (both modes, all badge types).

- 2026-07-03 (late session): **Round-3 defects + two enhancements shipped.** Quips now word-wrap (shared wrapLines helper — last of the raw-fillText cutoff family); stunt tags moved to a left rail under the slate; the rig got ONE hero spotlight whose cone pours from a visible lit lens (fixed HUD/lamp collision AND "light with no source"); floor de-bricked to 3 long boards w/ sparse joints + front-edge shadow; **THE DIRECTOR now sits on every set** (tall chair, beret, megaphone, behind the camera — quips have a body). **Home menu rebuilt as option B** (Dan pick of 3 mockups, assets/menu-options.png): poster-wall backdrop, marquee title, ticket-shaped ACTION button, ON THE LOT shelf cards, quiet footer row — all button IDs/handlers unchanged. New code smoke-tested headlessly. Backlot depth draft ready in harness (assets/backlot-before-after.png); floor per-set accents + director reactions + live poster wall → BACKLOG/rollout.

- 2026-07-03 (round 4): quotes/spotlight/floor/director all validated by Dan ✓. **Menu zero-state fixed** — locked features now visible-but-dimmed with 🔒 unlock hints (scene 3 / scene 5 / scene 11 / earn a print / first trophy) instead of hidden; **call sheet is an always-on card** (header + right-aligned payout chips, seeded day one). **Director reactions shipped to MVP** (Dan promotion): watches, leans in during flight, facepalms crashes, raises the megaphone while his quote shows, hands up on perfects — moved out of the set cache to animate, reduce-motion safe (pose swaps, no motion loops). Poses + call-sheet seeding verified headlessly.

- 2026-07-03: director pose fix (Dan: only megaphone showed) — facepalm was unreachable (gated on "crash without quote"; every crash has a quote). Now: crash = facepalm, CUT screen = megaphone quote, lean enlarged + visor hand, clap held 2.2s. Every pose verified reachable via real state sequences. Test lesson: drive headless checks with states the game actually produces, not synthetic ones.

- 2026-07-03: **Background rollout COMPLETE — all six sets** (Dan approved the Dust Gulch pattern). Shipped: BACKLOT (scaffold towers, string lights on cable swags, parked crane, work-lamp glow), HIGH SEAS (low moon + sea shimmer, moonlit clouds, sister ship, cardboard sea serpent on a stick), SAUCER STAGE (nebula washes, second moon, cratered moonscape, cardboard rocket on a stick), RAIN STREET (lit-window skyline, water tower, distant neon, fire-escape rooftop), MINIATURE CITY (premiere searchlights, "real city" backdrop behind the miniature, to-scale moon on a wire). Per-set floor accents added (noir wet sheen, scifi panel glints, western sand drifts). All drafts iterated in the render harness first (assets/foursets-depth.png, backlot-before-after.png); every ported block smoke-tested. Task #33 closed.

- 2026-07-03: **Boom rebuilt + prop coherence batch** (Dan defects). Boom now hangs from the rig (strut + pivot mount) and ends in a gray windscreen-blimp mic with fuzz — reads as sound gear, hitbox unchanged. New rule (DECISIONS): an active prop must visibly change the scene — Boom Brake ties the boom up to the rig, Trap Door removes the arm and opens a hatch in the floor, Wheel Chock parks the cart with a visible wedge, Wind Break stops the wind streaks; all revert on the next take's ready screen. Prop Dept copy now states the lifecycle (stack, saved with the game, spent per take win-or-lose, barred from daily). All visual gates verified headlessly with real state sequences.

- 2026-07-03: **Prop relevance + mic-only boom.** Belt now offers only props that counter THIS scene's mechanic (Dan armed a Trap Door on a boom scene — silent no-op, prop wasted; belt gating + a consume guard make that impossible), arming fires a confirmation toast. Boom collision reduced to the mic only (r28 at tip) — the pole and handle are jumpable, per Dan; matches the new windscreen visual. Verified headlessly (relevance across boom/cart/combo scenes; midpoint no longer deadly).

- 2026-07-03: one-time Trap Door refund shipped (make-good for the pre-gating no-op consume) — flag-guarded in S.reveals, existing saves only (takes > 0), toast on grant. Remove or keep harmlessly post-beta.

- 2026-07-03: boom hitbox aligned to the drawn windscreen (center +10 along pole, r26) — v1 centered it on the bare tip, killing pole-grazes below the mic and forgiving the fuzz's far end (Dan: inconsistent collisions). Verified across the full sweep: pole ≥45px clear, windscreen always deadly.

- 2026-07-04 (overnight, per Dan's work order): **maintenance run + explorations + big wins.** Maintenance: MAINTENANCE.md codified + scheduled task `take47-maintenance` (daily 6:38 AM); CLAUDE.md ops lessons updated (real-state testing, visual coherence rules, grep display quirk, harness rebuild note); STATUS next-steps de-duplicated; code fixes — dead drawSetLamp removed, gag-lens flicker cut from ~7Hz to <3Hz + reduce-motion gated (photosensitivity/App Store), file header refreshed (depth backgrounds decorative, hitbox=visual rule). **EXPLORATIONS.md** (flip variety / purchase confirms / power meter — 2 mockup sheets in assets/) and **BIG-WINS.md** (Game Center daily leaderboard, reset notification, real haptics, mercy system, store-conversion kit) await Dan's morning review.

- 2026-07-04 (Dan still up): **all 5 big wins approved** — mercy system SHIPPED (7 straight crashes → scene-relevant prop, "The insurance guy insists.", campaign only, verified headlessly); Game Center + reset notification + haptics logged in PIPELINE.md Phase 5 additions; store kit queued beta-parallel. **Imagery contrast audit** (Dan follow-up on missed a11y check): programmatic WCAG pass over all six sets — depth layers correctly quiet (1.03–1.15:1), HUD text all passes (6.8–18.8:1), but three real fixes: kaiju arm was 1.06:1 against its own sky (lethal + near-invisible) → lifted to ≥3.2:1; boom windscreen → ≥4.1:1; wind streaks α .35→.55. Set palettes + audit rules codified in BRAND.md ("hazards trade mutedness for legibility; decorative stays ≤2:1"). Art-direction verdict: palette holds — dusk-muted sets + one warm accent each = deadpan-with-heart; Marquee Gold exclusivity intact.

- 2026-07-04: **QA Test Mode panel shipped** (Dan: set game state to test prerequisites) — Settings → tap version line 5×: save backup/restore, scene jump, +50 prints, +1 every prop, mercy arm, FTUE+reveals reset, forced rollover. Logic verified headlessly. Verification protocol updated in CLAUDE.md (all future verify steps reference the panel; backup first). Phase 5 hard gate added to watch list: strip before submission.

- 2026-07-04: **Exploration batch SHIPPED** (Dan approved all three recommendations): cosmetic flip poses (TUCK/PIKE/LAYOUT/TWIST by spin speed + scene, wind=twist, low-G=layout, announced on perfects); prop purchases now instant + 4s tap-toast UNDO, wardrobe ≥15 prints gets a second-tap confirm; **Launch Rig prop** (4🖨, hold-to-aim power meter 0.75–1.25×, canvas meter + release prompt) as the power-meter trial balloon. **Plus Dan's ride-it-out defect fixed:** landing angle now judged at exact sub-frame ground contact (was one frame late), unlocked clean landings earn "RODE IT OUT!" — sub-frame fairness item retired from BACKLOG. All five changes verified headlessly with real sequences.

## Next steps
1. **Tomorrow morning: run QA-PLAN.md** (~75–90 min, one pass) — consolidates ALL remaining BETA-READINESS core items + last night's feature verifications: rollover check, fresh-save FTUE, feature smoke, a11y sweep, copy read, big feel session. Paste defects + the five feel answers into chat for triage.
2. Schedule the **cold playtest volunteer** this week.
3. Then **Phase 5 begins**: PIPELINE.md runbook — Capacitor wrap, Preferences save migration (hard gate), QA-panel strip (hard gate), Game Center + notifications + haptics (approved wins), hello-world TestFlight build; "TAKE 47" name check at first ASC touch.
4. Beta-parallel: store-conversion kit (screenshots + 15s preview per BRAND/MARKETING).
2. **Fresh-save FTUE run** (~10 min, private tab).
3. **Combined a11y sweep** (~15 min).
4. **Full copy read** (~15 min).
5. **Daily rollover check** (passive — first open after midnight: fresh gauntlet, 3 attempts, 3 new call-sheet goals).
6. **The big feel session** (one sitting).
7. **Cold playtest** (needs a volunteer — schedule when you can).

Then: App Store screenshot set per BRAND.md ("the fail is the ad") → Phase 5: PIPELINE.md runbook → Capacitor wrap (save-durability hard gate) → hello-world TestFlight build → verify "TAKE 47" name at first App Store Connect touch.
(Standalone device check: retired — covered by tonight's many on-device rounds.)
