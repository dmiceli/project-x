# EXPLORATIONS.md — three design questions, researched + mocked (2026-07-04, overnight)

Dan's morning review queue. Mockups: `assets/mock-flip-variety.png`, `assets/mock-confirm-and-meter.png`. Nothing implemented — each ends with options and a recommendation.

---

## 1 · Flip variety (backflips / gymnastics / difficulty tie-in?)

**Research:** trick variety is core to the genre's biggest hit — Flip Diving builds its whole appeal on frontflips, backflips, pikes, twists, and per-character feel, while staying easy-to-learn/hard-to-master. Players read variety as depth even when it's cosmetic.

**Options:**
- **A · Cosmetic pose variety (recommended for MVP).** Pose auto-picked from what's already happening: fast spin = TUCK (current), medium = PIKE, slow spin & low-G wire work = LAYOUT, wind scenes = TWIST. Perfect landings announce it ("PIKE! PRINT!"). Zero new inputs, zero balance risk, ~1 session of work — the four poses are drawn in the mock.
- **B · Trick multiplier system.** Player *chooses* the pose (extra input) and stylish tricks multiply prints. Real depth, but new input + economy re-balance; overlaps the power-meter question below. Post-launch candidate.
- **C · Difficulty-curve integration.** Late scenes demand a called pose ("Director wants a PIKE"), judged like the landing. New challenge axis without new inputs — but adds copy, judging, FTUE burden. Cycle-2+ candidate.

**Recommendation:** ship A in MVP; park B/C in BACKLOG as the natural "more depth" levers post-launch.

## 2 · Confirmation on in-game (fake-currency) purchases

**Research:** genre practice is to keep soft-currency spending frictionless and reserve hard confirmation for real money (Apple's payment sheet always confirms real IAP regardless). But our prints are slow-earned (props cost 2–4, call sheet pays 6/day), so a misfire hurts.

**Options (both mocked):**
- **A · Modal confirm on every buy.** Safest, most friction; makes a 2-print purchase feel like a mortgage.
- **B · Instant buy + 4-second UNDO toast (recommended).** One tap keeps the shop joyful; the toast ("⚓ Boom Brake — 3 prints · UNDO") makes every misfire fully reversible. Cheap to build (toast system exists).
- **C · Hybrid threshold.** Confirm only when a purchase costs >⅓ of the wallet; instant otherwise. More rules to explain than it's worth at 6 SKUs.

**Recommendation:** B. Wardrobe colorways (up to 30 prints) could additionally get A — they're the only big-ticket spend.

## 3 · Hold-to-aim power meter (second touchpoint)

**Research:** hold-to-charge IS the proven second input of this genre — Flip Diving's core loop is literally *hold to charge, release to jump, then time the finish*, and it remained a one-thumb, easy-to-learn game. So the mechanic is neither alien nor inherently "too much."

**Analysis against our scenes:**
- *Makes it harder:* two timed decisions per take (release power + stop spin) roughly doubles early cognitive load; FTUE must teach both.
- *Makes it more strategic:* boom scenes (aim around the mic), wind scenes (compensate drift), big stunts (choose risk) all gain real agency.
- *Trivializes:* cart scenes — the cart's whole challenge is that the cart controls your launch; player-controlled power largely un-asks that question. The ramp and all six mechanics were tuned around fixed trajectories; a full switch means re-tuning everything two weeks from TestFlight.

**Options:**
- **A · No change.** One-tap purity; identity preserved; depth comes from mechanics/scenes.
- **B · Full power meter, always.** The Flip Diving model. Biggest identity upgrade, biggest cost: full re-tune + FTUE rework now.
- **C · Meter as difficulty-curve unlock.** Introduced like a mechanic ("SCENE 31+: you control the launch"), so early game keeps its simplicity and the meter becomes a taught skill mid-campaign.
- **D · Meter as a PROP first (recommended).** "Launch Rig" — a prop-department item: arm it, and that take gets the hold-to-aim meter. Fits the existing prop system exactly (scene-relevant, consumed per take, assisted = no PRINT), costs days not weeks, and gives us live signal on whether players *love* the input before we commit the game's identity to it. If it sings → promote via C. If not → it's still a fun prop.

**Recommendation:** D now, C as the promotion path, revisit B only post-launch with data. Other "playable element" levers worth noting: pose choice (1-B above) and a late-lock style bonus (BACKLOG: sub-frame timing) — both add expression without new touchpoints.

---
*Sources: Flip Diving mechanics coverage ([BestCrazyGames guide](https://www.bestcrazygames.com/blog/backflip-dive-3d-full-guide-how-to-play-tips-and-more), [BrightestGames](https://www.brightestgames.com/game/flip-diving-game), [Miniplay](https://www.miniplay.com/game/flip-diving)); hybrid-casual design layering ([Game Growth Advisor](https://gamegrowthadvisor.com/blog/2026-04-16-hybrid-casual-game-design-strategy-2026/)).*
