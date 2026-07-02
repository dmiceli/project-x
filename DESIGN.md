# DESIGN.md — "Stick the Landing" (working title)

*Status: v1 draft, 2026-07-02. Name TBD pending theme exploration. This document describes what we're building for v1.0; it was written after the core loop was validated in playtesting, not before.*

## The pitch

A one-tap stunt game. Your character launches into the air spinning; you tap once to stop the spin, then gravity decides the rest. Land on your feet and you score — chain perfect landings for multiplying streaks. Miss, and your character explodes into a flailing ragdoll. Runs last seconds, restart is instant, and the difficulty ramp makes every crash feel like *your* fault. The physical premise (landing something upright) needs zero explanation — everyone has flipped a bottle or played flip cup.

## Validated in playtesting (2026-07-02)

Playtesting the v2 prototype against Squeeze (parked backup concept) confirmed: the "one more try" pull is strong and failure motivates retry rather than quitting; perfect landings are satisfying and streaks are actively chased; the current difficulty ramp feels fair. The whimsical tone works but crashes are not yet *funny* — comedy is a build-phase goal (see Juice).

## Core loop

The player taps to jump. The character arcs across the screen (airtime ~1.35s) while rotating at a fixed angular speed. A second tap freezes the rotation at its current angle. On touching the ground, the landing angle is measured against upright: within the perfect window it's a PERFECT (+3 × current perfect-streak count, confetti, arms-up pose); within the good window it's STUCK IT (+1, streak resets); outside it's a crash — the character breaks into six ragdoll pieces, the score is banked to best-if-higher, and a tap restarts immediately.

Current tuning (from prototype v2, subject to feel iteration):

| Parameter | Value |
|---|---|
| Airtime | 1.35 s, gravity 1400 px/s² |
| Spin speed | 300 + 45×round °/s, capped 720, direction alternates each round |
| Good window | 30 − 1.5×round degrees, floor 16° |
| Perfect window | 10° |
| Perfect streak | consecutive perfects; score +3×streak; good landing keeps the run but resets streak |
| Hitstop on landing | 60 ms |

## Juice and feel

Already in: hitstop, screen shake, red flash, landing dust, perfect confetti, ragdoll crash with X-eyes, squash-and-stretch, synth SFX (jump sweep, lock click, land thud, perfect arpeggio, crash noise). Build-phase goals, in priority order: make crashes comedic (more exaggerated ragdoll physics, brief slow-mo on spectacular crashes, occasional absurd crash variations), character personality (idle animations, terrified face mid-spin), and real sound design to replace the synth placeholder.

## v1.0 features

**Share button.** After each run, one tap generates a score-card image (score, best, streak, character mid-crash or mid-triumph) and opens the iOS share sheet. This is the primary viral mechanism.

**Unlockable characters.** New stunt characters unlock at score milestones. Each is a reskin of the same rig (art cost stays contained). Rewarded-ad integration: watch an ad to unlock the next character early.

**Daily challenge.** One fixed seed per day — same jump sequence for everyone. Separate daily score, shareable via the same score-card ("Today's run: 14. Beat me."). Social competition happens through shared images rather than a server.

**Initial achievements.** A starter set of in-game badges (no server, no Game Center dependency): first perfect, streak ×3, streak ×5, survive round 10, 100 total crashes ("Frequent Flyer"), unlock all characters. Achievements surface in a simple trophy screen and feed the share card.

Explicitly out of v1.0: Game Center leaderboard (revisit for 1.1), cloud saves, multiplayer, level/world structure.

## Monetization

Free download. Rewarded ads (opt-in only): continue a crashed run once per run by watching an ad; unlock characters early. Interstitials: full-screen ad between runs, at most one per 3 crashes and never less than 90 seconds apart, never mid-run. No banners — they earn little and clutter the screen. "Remove Ads" IAP at $1.99–2.99 removes interstitials but keeps opt-in rewarded ads available. Ad SDK choice (AdMob vs. alternatives) is a build-phase decision; whichever we pick brings Apple's App Tracking Transparency prompt and privacy-label requirements — accounted for in the App Store phase.

## Theme and name (OPEN)

The name must grow out of the visual theme, which needs research. Candidate directions to explore with mockups and App Store crowding checks: Olympic/gymnast, rooftop stunt performer, trampoline park, clumsy animal (cat), daredevil movie-stunt set. Current placeholder art is an abstract stunt figure on a night background. Working title remains "Stick the Landing"; naming decision gates icon and branding work, not the build.

## Tech

Plain HTML5 canvas + vanilla JS (prototype v2 proved we don't need a game engine at this scope), wrapped with Capacitor for iOS, built/signed/submitted through a cloud build service (leading: Codemagic) since there is no Mac. Prototypes remain browser-playable throughout development — the iPhone browser (via GitHub Pages) is the primary feel-testing surface before TestFlight.

## Success metrics

Concrete goals: App Store approval; 20+ TestFlight testers; instant restart under 1 second; a share card people actually post (qualitative). Stretch: measurable D1 retention once analytics exist (build-phase decision on whether/what to add).
