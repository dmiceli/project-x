# DESIGN.md — "Stick the Landing" (working title)

*Status: v1 draft, 2026-07-02. Name TBD pending theme exploration. This document describes what we're building for v1.0; it was written after the core loop was validated in playtesting, not before.*

## The pitch

A one-tap stunt game. Your character launches into the air spinning; you tap once to stop the spin, then gravity decides the rest. Land on your feet and you score — chain perfect landings for multiplying streaks. Miss, and your character explodes into a flailing ragdoll. Runs last seconds, restart is instant, and the difficulty ramp makes every crash feel like *your* fault. The physical premise (landing something upright) needs zero explanation — everyone has flipped a bottle or played flip cup.

## Validated in playtesting (2026-07-02)

Playtesting the v2 prototype against Squeeze (parked backup concept) confirmed: the "one more try" pull is strong and failure motivates retry rather than quitting; perfect landings are satisfying and streaks are actively chased; the current difficulty ramp feels fair. The whimsical tone works but crashes are not yet *funny* — comedy is a build-phase goal (see Juice).

## Core loop: scenes as levels (updated 2026-07-02)

The movie is the progression. Each **scene** is one designed jump: the player taps ("ACTION!", clapperboard), the character arcs and spins per that scene's parameters, a second tap freezes the rotation, and the landing angle decides the outcome. Land within tolerance and the scene is **complete — forever**: progress persists and the next scene begins. A perfect landing "prints" the scene (PRINT IT!, confetti, persisted prints counter). Crash and the director yells CUT! with a randomized quip — you retry the *same* scene, with the take counters (per-scene and lifetime) climbing. The share hook is the scene number ("I'm stuck on Scene 137") plus the lifetime take count ("1,047 takes so far"). A **"Reshoot from Scene 1"** option (two-tap confirm) lets a frustrated or nostalgic player voluntarily restart; the furthest-scene record survives the reset, so restarting never destroys the bragging number.

Scene design is deterministic-procedural: a seeded PRNG derives each scene's spin speed/direction, airtime, and landing tolerance from the scene number, so every player faces the identical Scene 137. Every 10th scene is a marked "BIG STUNT SCENE" (faster spin).

**Every set teaches a stunt (depth architecture, 2026-07-03).** Difficulty comes from mechanics layering, not raw speed. Each genre introduces its signature mechanic when the production arrives: THE BACKLOT teaches the basics; DUST GULCH adds the **rolling launch cart** (first-tap timing + a mandatory crash mat); THE HIGH SEAS swings a **boom** through the descent corridor; SAUCER STAGE runs **wire-work gravity** (low-G/high-G arcs); RAIN STREET's **wind machine** drifts your spin mid-air; MINIATURE CITY's **arm sweeps** the landing zone on a rhythm. Cycle 2 (scene 61+) mixes a seeded second mechanic into scenes and upgrades BIG STUNTS to **double-bounce** format (two spin phases, two locks). Launch platforms (0/60/120px, seeded) vary every scene's arc everywhere. All hazards telegraph via constant visible motion + text badges; input stays strictly one-thumb.

Current tuning ("brutal but fair" ceiling, subject to feel iteration):

| Parameter | Value |
|---|---|
| Airtime | 1.15–1.5 s (seeded), gravity 1400 px/s² × wire-work factor (0.55/1.45) |
| Spin speed | 280 + 150·ln(1+n/12) °/s + seeded 0–40, soft cap 950; ×1.12 big stunts |
| Good window | 30 − 0.25×scene degrees, floor 12° (big stunts −2°, floor 10°) |
| Breathers | ~10% of scenes seeded easier (spin ×0.85, window +6°) |
| Perfect window | 10° |
| Hitstop on landing | 60 ms |
| Persistence | full save blob (scene, printed map, wallet, wardrobe, call sheet, settings) |

## Juice and feel

Already in: hitstop, screen shake, red flash, landing dust, perfect confetti, ragdoll crash with X-eyes, squash-and-stretch, synth SFX (jump sweep, lock click, land thud, perfect arpeggio, crash noise). Build-phase goals, in priority order: make crashes comedic (more exaggerated ragdoll physics, brief slow-mo on spectacular crashes, occasional absurd crash variations), character personality (idle animations, terrified face mid-spin), and real sound design to replace the synth placeholder.

## v1.0 features

**Scene progression (the levels system).** Described in Core loop above — the level number is the primary progression, retention, and share metric.

**Share button.** After a CUT! or a milestone, one tap generates a share-card image (scene number, take count, prints, character mid-crash or mid-triumph) and opens the iOS share sheet. This is the primary viral mechanism.

**Unlockable characters (6 at launch, locked 2026-07-02).** Stunt Guy (default), Stunt Gal, Crash-Test Dummy, Hot-Dog-Costume Guy, The Aging Legend, The Diva. All reskins of the same rig. Unlock at scene milestones (10/25/50/75/100); rewarded-ad early unlock. Robot Double and Grandma reserved for post-launch.

**Daily challenge (locked 2026-07-02).** Seeded from the date — everyone worldwide faces the same gauntlet of consecutive scenes, one life: a crash ends the attempt, score = scenes cleared. 3 free attempts per day; rewarded ads grant extras, capped at +3/day (6 total), keeping daily scores comparable. Shareable via the score card ("Today's shoot: 14 scenes. Beat me.").

**Initial achievements (10, locked 2026-07-02).** First Print (first perfect); Hat Trick (streak ×3); On Fire (streak ×5); Director's Cut (big-stunt scene on the first take); One-Take Wonder (5 consecutive scenes, first take each); Frequent Flyer (100 lifetime crashes); Method Actor (500 lifetime takes); The Long Haul (Scene 50); Franchise Material (Scene 100); Full Cast (all characters). Client-side, no Game Center dependency; trophy-room screen; each feeds the share card.

**Settings.** Sound effects, haptics, reduce motion, Reshoot from Scene 1, restore purchases, privacy policy link — all real labeled buttons (VoiceOver-navigable).

**The joy package (added 2026-07-03 after Dan's replayability session).** Six interlocking systems: (1) **Near-miss tier** — landing within 8° outside tolerance is "SO CLOSE!": no ragdoll, a dignified faceplant, pained director quips; the strongest retry-driver in the genre. (2) **The Reel** — reshoot any completed scene; perfect it to *print* it. The mastery loop: forward-only becomes beat-your-own-history. (3) **Poster Wall** — one poster per wrapped set; printing all ten of its scenes gilds it to a Director's Cut. (4) **Call Sheet** — three seeded daily goals (+2 prints each, +5 for the sweep); gives sessions a finish line. (5) **Golden takes** — ~1 in 20 scenes (seeded, never big stunts) pays +3 prints. (6) **Rare director approval** — 2% of perfects, he has no notes. Prints economy: perfects earn prints (+call sheet+goldens); prints spend on **wardrobe** — three colorways per character (0/15/30) — cosmetic only, never progression (the no-pay-to-win principle extends to earned currency).

**The Prop Department (added 2026-07-03, Dan's utility-items layer).** Six consumables, one per take, each answering a mechanic: Slow-Mo Rig (spin ×0.7, 3🖨), Wheel Chock (cart holds, 2🖨), Wind Break (2🖨), Grip Tape (window +5°, 4🖨), Boom Brake (3🖨), Trap Door (arm skipped, 3🖨). **Earned only** — prints, golden-take drops, call-sheet-sweep drops; never money or ads. Assisted takes complete scenes but never PRINT them (perfects stay earned-raw; protects the Poster Wall). Props are barred from the daily gauntlet (fair fight). Armed via a prop belt on the ready screen.

**Daily/incentive economy (updated 2026-07-03):** call-sheet goals display their +2🖨 rewards; the daily gauntlet pays +1 print per scene of personal-best improvement (un-farmable); achievements show live progress in the trophy room and fire a one-time halfway toast.

**Economy baseline (2026-07-03, for calibration — Dan: evaluate usage over time).** Earn rates: +1/perfect, +3/golden scene (~1 in 20), +2/call-sheet goal (max 3/day), +5/call-sheet sweep = a skilled day ≈ 15-25 prints; casual ≈ 5-10. Sink: 15/30 per colorway, 270 to buy everything. Baseline intent: first purchase within ~2 days casual, full wardrobe ≈ 2-3 weeks. Calibration checkpoints: Dan's own play now, TestFlight feedback later (no analytics SDK — self-report + direct questions to testers). Adjust prices, not earn rates, first.

**Scene genres (added 2026-07-03, Dan: full v1).** The set changes genre every 10 scenes, cycling: The Backlot → Dust Gulch (western) → The High Seas (swashbuckler) → Saucer Stage (50s sci-fi) → Rain Street (noir) → Miniature City (kaiju). All trope-level per THEME.md IP guardrails; every set keeps the film-set framing (rig, spotlight, camera, crash mat). Genre transitions announced with a toast; each genre's 10th scene is its BIG STUNT finale.

Explicitly out of v1.0: Game Center leaderboard (revisit for 1.1), cloud saves, multiplayer, level/world structure.

## Monetization

Free download. **Principle (Dan, 2026-07-02): ads never buy progress.** No scene skips, no pay-to-win — main-mode scene progression cannot be advanced by watching or paying for anything. Rewarded ads (opt-in only) live where they don't touch progression: extra attempts in the daily challenge (base allowance ~3 attempts/day, which also makes the daily score meaningful), and early cosmetic character unlocks. Interstitials: full-screen ad between takes, at most one per 3 crashes and never less than 90 seconds apart, never mid-jump. No banners — they earn little and clutter the screen. "Remove Ads" IAP at $1.99–2.99 removes interstitials but keeps opt-in rewarded ads available. Ad SDK choice (AdMob vs. alternatives) is a build-phase decision; whichever we pick brings Apple's App Tracking Transparency prompt and privacy-label requirements — accounted for in the App Store phase.

## The flipper is the face of the franchise (Dan, 2026-07-03)

Like Flappy's bird and the Angry Birds, the character IS the brand. The icon established his identity: inverted mid-flip, wide terror eyes, open "AAAAH" mouth, sweat drops, red shoes. This face must propagate: into the in-game character during flight (art pass), the share card, App Store screenshots, and any future marketing. One character, everywhere.

## Voice (Dan, 2026-07-03): whimsical, never cheesy

All game copy — quips, cards, bios, achievements, share cards — aims for deadpan film-industry humor. The joke is always that the crew takes absurd things completely seriously ("one nervous insurance guy," "a city of shoeboxes," "files no complaints"). Whimsy comes from *specificity*, not wackiness. Guardrails: no pun pile-ups, no fourth-wall mugging, no exclamation-point enthusiasm outside the director's yells, no random-lol humor. If a line would fit a minion meme, cut it.

## Theme and name: TAKE 47 (decided 2026-07-02)

**Theme: movie stunt set.** You're a stunt double; every attempt is a take. Crashes aren't failures — they're outtakes: the director yells "CUT!" and delivers a randomized quip; restart is "one more take." The lifetime take counter (persisted) is the running joke — it climbs forever and headlines the share card ("Scored 23. Only took 1,047 takes."). Landings: "CLEAN TAKE +1"; perfects: "PRINT IT!". Rewarded-ad continue = "reshoot the scene." Daily challenge = "today's scene." Achievements = the blooper reel. Visual language: warm studio lighting, spotlight on the landing zone, camera silhouette, crash mat, warning-tape floor edge, film-slate UI cards. Sound language: clapperboard on action, director's bullhorn on cuts.

**Name: TAKE 47** — no App Store collision found (verify in App Store Connect before reserving). Icon direction: film slate.

Research notes: the generic flip niche is saturated (Flip Master, Flip Trickster, Backflip Madness, Flip Jump Stickman); "Stick the Landing" collided with a Steam/Switch title; "Take Two" blocked by Take-Two Interactive; "Stunt Guy" taken. The movie-set framing is the differentiator — personality over mechanic novelty.

## Tech

Plain HTML5 canvas + vanilla JS (prototype v2 proved we don't need a game engine at this scope), wrapped with Capacitor for iOS, built/signed/submitted through a cloud build service (leading: Codemagic) since there is no Mac. Prototypes remain browser-playable throughout development — the iPhone browser (via GitHub Pages) is the primary feel-testing surface before TestFlight.

## First-time experience (added 2026-07-03 after pre-polish audit)

Research: onboarding loses half of a game's audience; nine buttons on first launch is cognitive overload. So: the home screen starts with ACTION + Settings only and **reveals itself as the player earns it** (Daily at Scene 3, Call Sheet at 5, Reel/Posters at the first wrap, Props at first print, Cast at first unlock, Blooper Reel at first trophy — each announced with a toast). First-session coaching: plain two-line instruction on the ready screen and a pulsing "TAP NOW!" cue near upright, both retiring permanently after the first completed scene. Crash legibility: angle-crashes show "missed upright by N°" on the CUT screen — every failure teaches. The home screen notes that the gauntlet and call sheet reset at midnight. Interstitial pacing ships in beta as a clearly-labeled placeholder card wired to the real caps (1 per 3 crashes, ≥90s), so testers tune the annoyance level before real ads exist. **Pre-beta gate (Phase 5): migrate saves from WebView localStorage to Capacitor Preferences** — iOS can purge WebView storage, and a tester losing Scene 87 is an uninstall.

## Accessibility (standing rule — checked on every change)

Every color signal is paired with text or shape (CUT!/PRINT IT! labels carry meaning, never color alone) and the palette gets a color-blind pass before launch. One-tap input is motor-friendly; the game is fully playable without sound. Reduce-motion setting (already in the prototype) disables screen shake and the red flash — also the photosensitivity mitigation; no strobing effects anywhere. Text sizes audited at phone scale; director quips persist through the retry screen rather than flashing briefly. Menus, settings, and share UI in the shipped app use real labeled buttons (VoiceOver-navigable); canvas gameplay itself is acknowledged as not screen-reader playable.

## Success metrics

Concrete goals: App Store approval; 20+ TestFlight testers; instant restart under 1 second; a share card people actually post (qualitative). Measurement: Apple's built-in App Analytics only (downloads, retention, crashes) — no third-party analytics SDK in v1 (decided 2026-07-02; keeps privacy surface minimal). Per-scene difficulty tuning comes from TestFlight feedback.
