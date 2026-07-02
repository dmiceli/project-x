# BRAND.md — TAKE 47 brand kit (v1, 2026-07-03)

*The single source of truth for every visual and verbal surface: app, icon, App Store page, share cards, social clips, landing page. Grounded in conversion research (sources at bottom) and in what the shipped game already established — consistency IS the strategy: same hexes, same type, same voice, everywhere.*

## Essence

**TAKE 47 is a film production that takes itself completely seriously while everything goes wrong.** The player is the stunt double; the brand is the crew. Every surface should feel like it was made by the fictional production's art department: functional, warm-lit, slightly weathered, quietly funny.

Personality in three words: **deadpan, earnest, cinematic.** Never: zany, neon, "epic."

## Voice

Defined in DESIGN.md (standing rule, Dan 2026-07-03): whimsy through specificity, deadpan crew energy, humor from taking absurd things seriously. No pun pile-ups, no fourth-wall mugging, no exclamation-point enthusiasm outside the director's yells. The cheese test: *if a line would fit a minion meme, cut it.* Applies to App Store copy, social captions, and update notes — release notes are written as production memos ("Week 3 on set: the boom now apologizes to no one").

## Color — roles, not vibes

Research: 4–8 core colors with assigned jobs, identical hex across all platforms; dark base + gold accent reads cinematic/premium, gold signals reward. Every pairing below is WCAG-audited (computed 2026-07-03):

| Color | Hex | Role | Contrast on Set Black |
|---|---|---|---|
| Set Black | `#191010` | base / backgrounds | — |
| Slate Panel | `#241515` | surfaces, cards | — |
| Marquee Gold | `#ffd166` | brand, CTAs, rewards, the "47" | 13.0:1 AAA |
| Screen Cream | `#e8d5b5` | primary text | 13.0:1 AAA |
| Dust | `#a08b72` | secondary text, captions | 5.7:1 AA |
| Cut Red | `#f87171` | failure, CUT!, alerts | 6.8:1 AA+ |
| Print Green | `#6ee7b7` | success, prints, go-signals | 12.3:1 AAA |
| Streak Purple | `#c084fc` | streaks, rare moments | 7.1:1 AAA |
| Prop Blue | `#93c5fd` | props, informational | 10.4:1 AAA |

Rules: gold is precious — one gold element per composition (it's the reward color; overuse debases it). Red and green always ship with a text label (accessibility standing rule: never color alone). No pure black, no pure white, anywhere.

## Typography

**Display:** bold serif (Georgia in-app; DejaVu Serif in generated assets) — slates, titles, verdicts (CUT!, BEAT THIS.). The serif is the "movie" in the brand. **UI/body:** system sans — everything functional. Never mix roles: a serif button or a sans-serif slate is off-brand. Minimum sizes: 14px equivalent in-app, nothing under 24px on marketing assets.

## Motifs (the recognizable furniture)

The **clapper stripe band** (45°-slanted alternating stripes, gold/black — our 0.5 rad slant) is the primary brand device: header of the icon, share cards, brand sheet, store screenshots. The **spotlight cone**, **warning tape**, and **crash mat blue** are set dressing for backgrounds. The **take counter** is the verbal motif — big numbers with deadpan captions are always on-brand.

## Icon (per conversion research: one focal element, readable at 60px)

Composition: clapper stripe band across the top, oversized gold **47** centered on Set Black, "TAKE" small in Dust. Nothing else — research shows single-focus icons lift conversion 22–30%, and if it doesn't read at 60px it fails. Current `app/icon-1024.png` implements this; the art pass may refine weight/texture but must not add elements. A/B candidates later may vary the character mid-flip as focal element instead — test, don't guess.

## Applications

**Share cards:** slate-format, serif verdict headline, one big number, quip sign-off, play-link printed on-image (already shipped — the card IS the brand's most-traveled asset). **App Store screenshots:** in-game captures on device frames, one message per shot in serif caption ("Land it. Or don't."), first two shots carry the whole pitch, a crash features prominently — the fail is the ad. **Store subtitle/description, social captions:** voice rules apply; captions read like production paperwork. **Landing (Pages):** dark set, wordmark, one CTA in gold.

## Don'ts

No gradients-for-drama, no lens flares, no neon cyberpunk drift, no stock Hollywood imagery (film reels/popcorn clichés beyond our own slate), no real-film references (IP guardrails in THEME.md), no gold on cream (2.2:1 — fails contrast), no color-only signaling ever.

---
*Research: [Storemaven — icon CVR +22.8% avg](https://www.storemaven.com/academy/app-icons-aso-guide/), [ASO World — icon optimization up to +30%](https://asoworld.com/blog/app-icon-optimization-a-practical-guide-to-boost-app-conversion-rate/), [AppTweak — single focal element, 60px test](https://www.apptweak.com/en/aso-blog/how-to-design-an-app-icon), [Design Your Way — gold = reward psychology](https://www.designyourway.net/blog/gaming-color-palettes/), [itch.io — roles-not-vibes palette discipline](https://itch.io/blog/1039646/picking-the-perfect-color-palette-for-your-game). WCAG ratios computed against WCAG 2.1 relative-luminance formula.*
