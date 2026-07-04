# Backlog — post-launch parking lot

Ideas deliberately kept OUT of v1.0 so scope stays fixed. Nothing here is forgotten; nothing here blocks launch.

## v1.1 candidates
- Characters 7–8: Robot Double, Grandma
- Slow-mo replay of spectacular crashes (crash-comedy amplifier)
- More director quips; quip packs per scene range

## From overnight research (2026-07-02, see TRENDS.md / THEME.md)
- Cosmetic character IAP (premium skins, no progression impact) — hybrid-casual data says IAP is where revenue lives if retention proves out.
- Quip packs per director archetype / genre block.
- Facade-fall homage scene ("The Nail") as a milestone BIG STUNT.

## Ideas worth revisiting
- Squeeze (the parked bake-off concept) — Dan saw real potential: movement variation, abilities (e.g., "air" mechanics), Dune-like feel with a twist. Could be game #2.
- Rank titles on top of scene progress (Extra → Stunt Legend) as extra flair on the share card.
- Take-counter milestones as celebrations (take #100, #1,000 get a director ceremony).

## Fairness / polish candidates (pre-launch review)
- Hybrid mute pass on remaining wardrobe: the other five cast members' Classic colorways (+ variants) should get the same muted-flat treatment as Stunt Guy during the art pass.
- Icon art: current version is polished programmatic art (MVP per Dan); optionally commission an artist pre-launch using icon-final.png as the exact brief.

## Deferred process items
- Third-party analytics: reconsider before public launch only if TestFlight feedback is insufficient (decided 2026-07-02: Apple built-in only for v1).

*(Removed as shipped/promoted, 2026-07-03 maintenance: Game Center leaderboard → Phase 5 via BIG-WINS; in-game face pass → shipped; per-set floor accents → shipped with the six-set background rollout.)*
*(Removed as shipped, 2026-07-04 maintenance: haptics polish pass → real Taptic haptics, build 9; scene-genre sets → shipped full in v1 (six sets, Dan 2026-07-03); live poster-wall career data → shipped in express-QA fixes + D-003 thumbnails.)*

- **Native safe-area inset plugin (post-beta hardening):** env(safe-area-inset-*) is confirmed dead in our WKWebView (build-8 on-device evidence, D-002). Take 9 ships a per-device-width inference table — correct for all current iPhones but a maintenance liability as new models appear. Adopt a native inset source (e.g. a Capacitor safe-area plugin) once the beta settles; drop the table then.

- **Wardrobe accessories (Dan, 2026-07-04):** beyond colorways — hats, capes, glasses, props-as-costume for the cast. The portrait renderer (D-006) makes previews free; the rig's acc slot (pony/bun/glasses/grayhair) is the natural attachment point. Post-v1: pairs well with earned-only economy and Golden Take rewards.
