# ART-RESEARCH.md — Background imagery: market research + application plan

**Date:** 2026-07-03 · **Trigger:** Dan's defect report ("background imagery is not interesting at all") + decision to use open libraries as *influence* (not replace/augment).
**Sources:** industry art-trend reports (AAA Game Art Studio, VSQUAD, RetroStyle, Udonis, Pixune), background-craft guides (GameMaker, Game Developer, 300Mind, Wayline), competitor store pages, Kenney.nl CC0 catalog. Links in session chat.

---

## Part 1 — What the market says (2026)

**1. Premium minimalism is the winning register.** Pure hyper-casual visuals are fading; what converts now is the *same minimalist DNA executed with higher production quality* — stronger silhouettes, deliberate lighting, real composition. Our flat-deadpan style is on-trend; our *empty single-plane backdrops* are the part that reads "unfinished" rather than "minimal."

**2. Color is a brand system, not decoration.** Top games use a distinctive color signature that's recognizable at thumbnail size (store screenshots, share cards, ad frames). We already have this (BRAND.md palette + warm set-black world) — background work must stay inside each set's sky family, never introduce new hues.

**3. The 6-second test.** Hybrid-casual art succeeds when one screenshot/6-second clip communicates the game. Backgrounds contribute mood and depth to that frame but must never compete with the character arc — the flip IS the ad.

**4. Depth without cost.** The market trend (isometric, lightweight 3D) is really a demand for *perceived depth*. In 2D canvas we get the same effect free with layered silhouettes + atmospheric perspective — no engine, no performance cost (our sets are cached to an offscreen canvas; extra layers cost zero per-frame).

## Part 2 — Background craft rules (from the guides + Kenney composition study)

1. **2–3 layers, stop there.** Far (silhouettes, no detail) → mid (simple shapes, small detail) → near (our existing outlined props). More layers = clutter.
2. **Contrast separation is the law.** Playfield objects: solid outlines, brighter/higher contrast. Background layers: *no outlines ever* (outline = foreground language), lower contrast, values that step darker toward the viewer (far lighter/hazier, mid darker, near darkest + outlined).
3. **One focal point per scene**, placed off the flight corridor. Everything else stays quiet and desaturated.
4. **Atmospheric perspective:** a translucent warm haze band where far layers meet the ground line sells distance instantly.
5. **A storytelling silhouette** — one recognizable shape (windmill, sea serpent, water tower) does more for "interesting" than ten generic shapes. This is where our deadpan movie-set humor lives.
6. **Readability first:** the vertical flight corridor (roughly x 90–350, y 100–460) stays visually quiet — depth layers live below y≈460 and in the sky's outer thirds.

## Part 3 — TAKE 47 application (per set)

Universal: all colors derived from that set's existing `sky` triplet; far layer ≈ mid-sky value; mid layer distinctly darker; haze band at y 540–600; focal point in the left or right third; ZERO outlines on depth layers.

| Set | Focal point | Far layer | Mid layer | Deadpan silhouette |
|---|---|---|---|---|
| DUST GULCH ✅ pilot | low dull sun + glow | flat-top mesas L/R | scrub ridge | water windmill + 2 birds |
| THE BACKLOT | dim work-lamp glow, stage right | distant scaffold towers | sagging cable swags between them | a second, bored camera crane |
| THE HIGH SEAS | low moon + shimmer on the wave cloth | cloud bank | distant "sister ship" cutout | cardboard sea-serpent on a visible stick |
| SAUCER STAGE | existing ringed planet (keep) | faint nebula wash + tiny second moon | cratered moonscape ridge | cardboard rocket on a stick |
| RAIN STREET | existing neon HOTEL (keep) | city skyline w/ sparse lit windows | rooftop line + water tower | one blinking distant neon block |
| MINIATURE CITY | crossing searchlight beams | bigger "real city" skyline behind the miniature | tabletop edge / model-shop clutter line | a to-scale moon on a wire |

**Rollout:** Dust Gulch shipped as the pilot (`propsWestern`). Dan validates in-hand → remaining five applied in one batch, then re-verify + fresh brand-sheet screenshot for store-asset reuse.

**License posture:** nothing imported — every shape drawn by us; CC0 libraries (Kenney.nl, OpenGameArt CC0 filter) used strictly as composition reference. Zero attribution or App Store obligations. If we ever *do* embed third-party assets, only CC0, and log it here.
