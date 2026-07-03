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
- Hybrid mute pass on remaining wardrobe: the other five cast members' Classic colorways (+ variants) should get the same muted-flat treatment as Stunt Guy during the art pass.
- In-game character face pass: bring the icon's terror-face (eyes/mouth/sweat) into the flight animation and share card — "one character, everywhere" (see DESIGN.md franchise-face note).
- Icon art: current version is polished programmatic art (MVP per Dan); optionally commission an artist pre-launch using icon-final.png as the exact brief.
- Sub-frame lock timing: use pointer-event timestamps to interpolate the lock angle between frames. At 700+°/s late-game spins, frame quantization (11°+/frame) makes the ±10° window partly luck; interpolation restores pure skill. Consider before beta if late scenes test as unfair.

## Deferred process items
- Third-party analytics: reconsider before public launch only if TestFlight feedback is insufficient (decided 2026-07-02: Apple built-in only for v1).
- Director reactions (leans in on ACTION, facepalm on crash, golf clap on perfect) — juice pass candidate
- Home poster-wall thumbnails could reflect actually wrapped sets (live data, not decorative)
- Per-set floor accents (scifi panel seams, noir wet sheen, western sand drifts) — fold into 5-set background rollout if cheap
