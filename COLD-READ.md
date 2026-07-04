# COLD-READ.md — zero-context copy audit (Opus 4.8 agent, 2026-07-05 overnight)

*Method: a fresh AI agent with deliberately NO project context read every player-facing string in the shipped build as "a brand-new casual player" and reported comprehension failures. Value: it can't know what we know — the closest available proxy for tomorrow's first-time players. Triaged by Claude (lead dev) below; verdicts marked. Two agent claims were verified FALSE and are marked — a good calibration on cold-reader reports generally.*

## Triage summary (Dan verdicts needed on ⚑ items)

| # | Finding | Claude's triage | Action |
|---|---------|-----------------|--------|
| 1 | **"PRINT" does 3 jobs** (success verb, currency noun, poster flag) — agent's confidence in decoding: LOW | VALID, the biggest one. But the pun (a "print" of film = the currency you earn by "printing" scenes) is core brand voice. Full currency rename = big call | ⚑ Dan: keep the pun + introduce it explicitly (first-earn toast: "+1 PRINT — the studio's currency. Spend at the Prop Dept."), or rename the currency outright? Claude recommends KEEP + introduce |
| 2 | **Two "reshoots"**: Reel replay vs Settings full reset — agent "would not tap without dread" | VALID, cheap, no downside | Rename Settings button → "START OVER (back to Scene 1 — your record is kept)". Ship without ceremony |
| 3 | **Daily vocabulary sprawl**: DAILY CHALLENGE / gauntlet / "shoot" | VALID. But "gauntlet" carries flavor; full removal flattens voice | ⚑ Dan: unify on "daily" in buttons/instructions, keep "gauntlet" as flavor in body copy only? Claude recommends that split |
| 4 | **HIGHLIGHTS (achievements) vs REEL (replays) collision** — agent "would absolutely tap the wrong one" | VALID — we created this renaming BLOOPER REEL → HIGHLIGHT REEL (D-form of an old fix) | ⚑ Dan: 🏆 AWARDS for achievements? (agent suggestion; Claude concurs — trophy icon then matches) |
| 5 | **clean vs perfect never taught** (that only perfects PRINT) | VALID — the lesson currently hides in a post-failure parenthetical | Add one FTUE-style line on first clean-but-not-perfect landing: "CLEAN — but only PERFECT prints a scene." No verdict needed |
| 6 | **Golden takes invisible** — reward arrives unexplained | VALID and ironic (our "correct but unfelt" pattern, in copy form) | Add "✨ GOLDEN TAKE" popup + toast on trigger. No verdict needed |
| 7 | **Dev-speak leaks**: "placeholder in beta", "(App Store build)" | PARTIALLY VALID: honest-with-testers during beta (intentional); must not ship to store | Added to the pre-submission strip gate alongside the QA panel |
| 8 | "STAR THEM" ambiguous | Minor, valid | Change to "⭐ MAKE THEM THE STAR" — self-clarifying, same joke |
| 9 | Undo-toast tap target undiscoverable | Minor, valid | Already says "TAP HERE TO UNDO"; consider button styling post-beta. Parked |
| 10 | "in the can" reads as failure to non-insiders | Debatable — verdicts are color+tier coded (green=good) and the film voice IS the brand | No change; watch for confusion in live testing |
| — | ~~"No visible how-to-play text exists"~~ | **FALSE** — the agent missed the FTUE coaching pills ("TAP to jump." etc.), which are canvas-drawn for all new players | None; noted as cold-reader calibration |
| — | ~~"No share message text exists"~~ | **FALSE** — `shareText()` ships taunt copy + link | None; ditto |

## What the cold reader said works (protected list — don't "fix")
Director quips ("We'll fix it in post."), "Earned with prints — never with money," "Three crashes and it's a wrap," the character bios, "No attempts left today — back tomorrow!", concrete prop descriptions.

## Full agent report
Preserved verbatim below for the record.

---

(Original report as returned by the zero-context agent — see repo history for any edits.)

**1. JARGON WALL** — print/printed (LOW), take (MED), gauntlet (LOW-MED), golden take (LOW — invisible), reshoot ×2 (MED/LOW), clean vs perfect (LOW), in the can (LOW), BIG STUNT (MED), assisted take (LOW), the belt (MED), call sheet (MED), gild (MED), wrapped (MED), the lot (MED), your double (MED), mat/boom/arm sweep/wire work as hazards (LOW).

**2. MIXED SIGNALS** — daily/challenge/gauntlet triple-naming; two reshoots; "three lives" vs "three crashes"; prints noun/verb collision; perfect-vs-clean taught only in a parenthetical; HIGHLIGHTS vs REEL double-reel; trophy icon vs "HIGHLIGHTS" label mismatch.

**3. MOMENTS OF CONFUSION** — ACTION! (charming but undefined), shelf buttons cryptic, SHOOT TODAY'S GAUNTLET, ad placeholder dev-speak, RESHOOT FROM SCENE 1 dread, RESTORE PURCHASES greyed mystery, STAR THEM ambiguity, undo-toast timing, (and the two FALSE findings struck above).

**4. WHAT WORKED** — as listed in the protected list.

**5. TOP 5 FIXES** — visible control prompt (moot — exists); disambiguate print (⚑1); split reshoots (#2, shipping); unify daily vocab (⚑3); fix HIGHLIGHTS collision (⚑4). Runner-up: strip dev-facing strings before submission (adopted, #7).
