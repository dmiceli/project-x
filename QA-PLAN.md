# QA-PLAN.md — morning session (2026-07-04) · ~75–90 min total

One pass, logical order: cheapest checks first, immersion last (so bugs found early don't taint the feel session). **Test Mode:** Settings → tap the version line 5× (backup your save before anything that mutates state). Log defects in the template at the bottom — screenshots beat descriptions.

## 0 · Prep (2 min)
- Push last night's commits if any are pending; confirm the Pages build updated (version line in Settings).
- Test Mode → **💾 Back up save**.

## 1 · Real midnight rollover (2 min) — do this FIRST, it's naturally armed
Open the game fresh this morning (no QA needed — actual midnight passed).
- [ ] Daily shows a NEW gauntlet, attempts back to 3, ad-extras reset.
- [ ] Call sheet card shows 3 new unchecked goals; yesterday's are gone.
- [ ] Home stats and record intact. **Pass:** all three, no weirdness.

## 2 · Fresh-save FTUE run (10 min — private/incognito tab, not your real save)
Open the Pages URL in a private tab (fresh localStorage).
- [ ] First take: both coaching pills fit on screen, above the character.
- [ ] First landing retires coaching; TOO SOON! only fires on premature taps.
- [ ] Zero-state home: ticket ACTION button, shelf shows LOCKED cards with 🔒 hints ("scene 3" etc.), call sheet card present with 3 goals, footer dimmed except Settings.
- [ ] Reach scene 3 → Daily unlock toast fires + card lights up.
- [ ] Earn a print → Props unlocks. **Pass:** a new player always knows what to do next and what's coming.

## 3 · Last night's features (10 min — your real save, Test Mode assists)
Setup: Test Mode → **+50 prints**, **+1 of every prop**.
- [ ] **Undo toast:** buy any prop → tap the toast → refunded (wallet + count restored). Let one expire (4s) → no refund.
- [ ] **Wardrobe confirm:** try a 15+ print colorway → first tap warns, second tap buys.
- [ ] **Launch Rig:** arm 🎯 on any scene → HOLD: meter sweeps on the left → release: launch power visibly varies (try min and max) → verdict says ASSISTED, no print.
- [ ] **Flip poses:** Test Mode → jump to scene 31, then 41, then 51 — watch TUCK vs PIKE vs LAYOUT vs TWIST across spin speeds; wind scenes = TWIST; low-G = LAYOUT. Land a perfect → pose name announced.
- [ ] **Ride it out:** don't tap a second time for ~5 takes — spins to the floor; if one lands upright → "RODE IT OUT!" clean verdict (it's luck — the fix is that it's POSSIBLE and judged fairly).
- [ ] **Mercy:** Test Mode → **🩹 Arm mercy** → crash once → "The insurance guy insists." + scene-relevant prop granted. **Pass:** all six behave; nothing feels mistimed.

## 4 · Combined a11y sweep (15 min — your phone's settings + in-game toggles)
- [ ] Settings → REDUCE MOTION: ON → crash a few times: no shake/flash, gag lamp falls without flicker, FTUE pulse calm (private tab), director poses still change (pose swaps are allowed).
- [ ] SOUND: OFF → play 3 takes: everything still readable/judgeable without audio.
- [ ] iOS VoiceOver ON → navigate home, settings, prop department: buttons announce sensibly, toggles report state, canvas announces its label.
- [ ] Squint test: HUD slate/ticket/tags readable at arm's length; hazards (mic, arm) pop on every set (the contrast audit says yes — confirm with eyes).
- [ ] Touch targets: nothing requires precision tapping. **Pass:** playable with motion reduced, sound off; menus VoiceOver-navigable.

## 5 · Full copy read (15 min — slow lap through every screen)
Home, all shelf screens, settings, prop dept, wardrobe, trophies, daily, CUT screen, share card, interstitial cards (Test Mode scene-jump to a wrap boundary like scene 10→11 to force one), quips (crash repeatedly), verdicts, toasts.
- [ ] No cutoffs, no typos, no placeholder text left.
- [ ] Register check per BRAND.md: STAMPS for stamps, sentence case for coaching, Title Case for named things, quips in quotes.
- [ ] Every number is right (prices, counts, scene numbers). **Pass:** you'd hand this text to a stranger.

## 6 · The big feel session (20–30 min — the one that matters)
Restore your save first if you QA'd on it (Test Mode → ⏪). Then just PLAY — no checklist, phone in hand, honest sitting. Afterwards, answer these five in one or two sentences each:
1. Where did you feel friction or boredom?
2. Did any scene feel unfair (vs hard-but-fair)?
3. Did the new backgrounds/poses/props make it feel richer or noisier?
4. When you crashed, did you want one more take — every time?
5. Would you show this to a friend today?

## 7 · Wrap-up (5 min)
- Test Mode → ⏪ **Restore save** (if not already), leave Test Mode.
- Paste defects + the five feel answers into chat. I'll triage into fix-now / beta-blocker / backlog.
- Still needed this week: a **cold playtest volunteer** (someone who's never seen it — 10 min, you watch silently).

## Defect template
```
[#] Screen/scene · what happened · what you expected · repro steps (if known) · screenshot?
```

**After this session:** BETA-READINESS core is complete → Phase 5 begins (PIPELINE.md runbook: Capacitor wrap, save migration, hello-world TestFlight build).
