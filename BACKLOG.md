# Backlog — post-launch parking lot

Ideas deliberately kept OUT of v1.0 so scope stays fixed. Nothing here is forgotten; nothing here blocks launch.

## v1.1 candidates
- Game Center leaderboard (deferred from v1 scope discussion)
- Characters 7–8: Robot Double, Grandma
- Slow-mo replay of spectacular crashes (crash-comedy amplifier)
- More director quips; quip packs per scene range
- Haptics polish pass (light tap on lock, thud on crash)

## From overnight research (2026-07-02, see TRENDS.md / THEME.md)
- Cosmetic character IAP (premium skins, no progression impact) — hybrid-casual data says IAP is where revenue lives if retention proves out.
- Scene genres (sets change genre every ~10-15 scenes: western, sci-fi, noir...) — **Dan decision pending: v1 art scope vs flagship 1.1 update.** See THEME.md.
- Quip packs per director archetype / genre block.
- Facade-fall homage scene ("The Nail") as a milestone BIG STUNT.

## Ideas worth revisiting
- Squeeze (the parked bake-off concept) — Dan saw real potential: movement variation, abilities (e.g., "air" mechanics), Dune-like feel with a twist. Could be game #2.
- Rank titles on top of scene progress (Extra → Stunt Legend) as extra flair on the share card.
- Take-counter milestones as celebrations (take #100, #1,000 get a director ceremony).

## Fairness / polish candidates (pre-launch review)
- Sub-frame lock timing: use pointer-event timestamps to interpolate the lock angle between frames. At 700+°/s late-game spins, frame quantization (11°+/frame) makes the ±10° window partly luck; interpolation restores pure skill. Consider before beta if late scenes test as unfair.

## Deferred process items
- Third-party analytics: reconsider before public launch only if TestFlight feedback is insufficient (decided 2026-07-02: Apple built-in only for v1).
