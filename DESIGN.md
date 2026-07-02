# DESIGN.md — "Stick the Landing" (working title)

*Status: v1 draft, 2026-07-02. Name TBD pending theme exploration. This document describes what we're building for v1.0; it was written after the core loop was validated in playtesting, not before.*

## The pitch

A one-tap stunt game. Your character launches into the air spinning; you tap once to stop the spin, then gravity decides the rest. Land on your feet and you score — chain perfect landings for multiplying streaks. Miss, and your character explodes into a flailing ragdoll. Runs last seconds, restart is instant, and the difficulty ramp makes every crash feel like *your* fault. The physical premise (landing something upright) needs zero explanation — everyone has flipped a bottle or played flip cup.

## Validated in playtesting (2026-07-02)

Playtesting the v2 prototype against Squeeze (parked backup concept) confirmed: the "one more try" pull is strong and failure motivates retry rather than quitting; perfect landings are satisfying and streaks are actively chased; the current difficulty ramp feels fair. The whimsical tone works but crashes are not yet *funny* — comedy is a build-phase goal (see Juice).

## Core loop: scenes as levels (updated 2026-07-02)

The movie is the progression. Each **scene** is one designed jump: the player taps ("ACTION!", clapperboard), the character arcs and spins per that scene's parameters, a second tap freezes the rotation, and the landing angle decides the outcome. Land within tolerance and the scene is **complete — forever**: progress persists and the next scene begins. A perfect landing "prints" the scene (PRINT IT!, confetti, persisted prints counter). Crash and the director yells CUT! with a randomized quip — you retry the *same* scene, with the take counters (per-scene and lifetime) climbing. The share hook is the scene number ("I'm stuck on Scene 137") plus the lifetime take count ("1,047 takes so far"). A **"Reshoot from Scene 1"** option (two-tap confirm) lets a frustrated or nostalgic player voluntarily restart; the furthest-scene record survives the reset, so restarting never destroys the bragging number.

Scene design is deterministic-procedural: a seeded PRNG derives each scene's spin speed/direction, airtime, and landing tolerance from the scene number, so every player faces the identical Scene 137. Every 10th scene is a marked "BIG STUNT SCENE" (faster spin).

Current tuning (prototype, subject to feel iteration):

| Parameter | Value |
|---|---|
| Airtime | 1.15–1.5 s (seeded per scene), gravity 1400 px/s² |
| Spin speed | 280 + 28×scene °/s + seeded 0–80, capped 880; ×1.15 on big-stunt scenes; direction seeded |
| Good window | 30 − 1.2×scene degrees, floor 15° |
| Perfect window | 10° |
| Perfect streak | session-scoped flair (popup ×n); prints counter persists |
| Hitstop on landing | 60 ms |
| Persistence | scene, lifetime takes, prints, reduce-motion setting (local storage) |

## Juice and feel

Already in: hitstop, screen shake, red flash, landing dust, perfect confetti, ragdoll crash with X-eyes, squash-and-stretch, synth SFX (jump sweep, lock click, land thud, perfect arpeggio, crash noise). Build-phase goals, in priority order: make crashes comedic (more exaggerated ragdoll physics, brief slow-mo on spectacular crashes, occasional absurd crash variations), character personality (idle animations, terrified face mid-spin), and real sound design to replace the synth placeholder.

## v1.0 features

**Scene progression (the levels system).** Described in Core loop above — the level number is the primary progression, retention, and share metric.

**Share button.** After a CUT! or a milestone, one tap generates a share-card image (scene number, take count, prints, character mid-crash or mid-triumph) and opens the iOS share sheet. This is the primary viral mechanism.

**Unlockable characters (6 at launch, locked 2026-07-02).** Stunt Guy (default), Stunt Gal, Crash-Test Dummy, Hot-Dog-Costume Guy, The Aging Legend, The Diva. All reskins of the same rig. Unlock at scene milestones (10/25/50/75/100); rewarded-ad early unlock. Robot Double and Grandma reserved for post-launch.

**Daily challenge (locked 2026-07-02).** Seeded from the date — everyone worldwide faces the same gauntlet of consecutive scenes, one life: a crash ends the attempt, score = scenes cleared. 3 free attempts per day; rewarded ads grant extras, capped at +3/day (6 total), keeping daily scores comparable. Shareable via the score card ("Today's shoot: 14 scenes. Beat me.").

**Initial achievements (10, locked 2026-07-02).** First Print (first perfect); Hat Trick (streak ×3); On Fire (streak ×5); Director's Cut (big-stunt scene on the first take); One-Take Wonder (5 consecutive scenes, first take each); Frequent Flyer (100 lifetime crashes); Method Actor (500 lifetime takes); The Long Haul (Scene 50); Franchise Material (Scene 100); Full Cast (all characters). Client-side, no Game Center dependency; trophy-room screen; each feeds the share card.

**Settings.** Sound effects, haptics, reduce motion, Reshoot from Scene 1, restore purchases, privacy policy link — all real labeled buttons (VoiceOver-navigable).

**Scene genres (added 2026-07-03, Dan: full v1).** The set changes genre every 10 scenes, cycling: The Backlot → Dust Gulch (western) → The High Seas (swashbuckler) → Saucer Stage (50s sci-fi) → Rain Street (noir) → Miniature City (kaiju). All trope-level per THEME.md IP guardrails; every set keeps the film-set framing (rig, spotlight, camera, crash mat). Genre transitions announced with a toast; each genre's 10th scene is its BIG STUNT finale.

Explicitly out of v1.0: Game Center leaderboard (revisit for 1.1), cloud saves, multiplayer, level/world structure.

## Monetization

Free download. **Principle (Dan, 2026-07-02): ads never buy progress.** No scene skips, no pay-to-win — main-mode scene progression cannot be advanced by watching or paying for anything. Rewarded ads (opt-in only) live where they don't touch progression: extra attempts in the daily challenge (base allowance ~3 attempts/day, which also makes the daily score meaningful), and early cosmetic character unlocks. Interstitials: full-screen ad between takes, at most one per 3 crashes and never less than 90 seconds apart, never mid-jump. No banners — they earn little and clutter the screen. "Remove Ads" IAP at $1.99–2.99 removes interstitials but keeps opt-in rewarded ads available. Ad SDK choice (AdMob vs. alternatives) is a build-phase decision; whichever we pick brings Apple's App Tracking Transparency prompt and privacy-label requirements — accounted for in the App Store phase.

## Theme and name: TAKE 47 (decided 2026-07-02)

**Theme: movie stunt set.** You're a stunt double; every attempt is a take. Crashes aren't failures — they're outtakes: the director yells "CUT!" and delivers a randomized quip; restart is "one more take." The lifetime take counter (persisted) is the running joke — it climbs forever and headlines the share card ("Scored 23. Only took 1,047 takes."). Landings: "CLEAN TAKE +1"; perfects: "PRINT IT!". Rewarded-ad continue = "reshoot the scene." Daily challenge = "today's scene." Achievements = the blooper reel. Visual language: warm studio lighting, spotlight on the landing zone, camera silhouette, crash mat, warning-tape floor edge, film-slate UI cards. Sound language: clapperboard on action, director's bullhorn on cuts.

**Name: TAKE 47** — no App Store collision found (verify in App Store Connect before reserving). Icon direction: film slate.

Research notes: the generic flip niche is saturated (Flip Master, Flip Trickster, Backflip Madness, Flip Jump Stickman); "Stick the Landing" collided with a Steam/Switch title; "Take Two" blocked by Take-Two Interactive; "Stunt Guy" taken. The movie-set framing is the differentiator — personality over mechanic novelty.

## Tech

Plain HTML5 canvas + vanilla JS (prototype v2 proved we don't need a game engine at this scope), wrapped with Capacitor for iOS, built/signed/submitted through a cloud build service (leading: Codemagic) since there is no Mac. Prototypes remain browser-playable throughout development — the iPhone browser (via GitHub Pages) is the primary feel-testing surface before TestFlight.

## Accessibility (standing rule — checked on every change)

Every color signal is paired with text or shape (CUT!/PRINT IT! labels carry meaning, never color alone) and the palette gets a color-blind pass before launch. One-tap input is motor-friendly; the game is fully playable without sound. Reduce-motion setting (already in the prototype) disables screen shake and the red flash — also the photosensitivity mitigation; no strobing effects anywhere. Text sizes audited at phone scale; director quips persist through the retry screen rather than flashing briefly. Menus, settings, and share UI in the shipped app use real labeled buttons (VoiceOver-navigable); canvas gameplay itself is acknowledged as not screen-reader playable.

## Success metrics

Concrete goals: App Store approval; 20+ TestFlight testers; instant restart under 1 second; a share card people actually post (qualitative). Measurement: Apple's built-in App Analytics only (downloads, retention, crashes) — no third-party analytics SDK in v1 (decided 2026-07-02; keeps privacy surface minimal). Per-scene difficulty tuning comes from TestFlight feedback.
