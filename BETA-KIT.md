# BETA-KIT.md — everything for putting TAKE 47 in front of new eyes

*The friends-and-family beta playbook. Two invite paths, the message to send, and the one thing that matters more than any of it: watching someone play.*

## The two invite paths (use whichever is ready)

**A · TestFlight (the real app).** Best experience — real haptics, the native icon, offline. Gated by Apple's **Beta App Review** of build 9 (the first external build of this version). Once it shows **"Ready to Test"** in App Store Connect → TestFlight → the "Friends & Family" group, the public link is live:
> **https://testflight.apple.com/join/C7Gx1gnb**
Testers install the free **TestFlight** app first, then tap the link. (Check the review state at: App Store Connect → TAKE 47 → TestFlight. "Waiting for Review" = not yet; "Ready to Test" = go.)

**B · The web build (always available, zero gatekeeper).** Same game, playable instantly in Safari, add-to-home-screen for fullscreen:
> **https://dmiceli.github.io/project-x/app/index.html**
Perfect for anyone who won't install TestFlight, or if review hasn't cleared by showtime. The share cards even carry this link baked into the image.

## The message to send

Short, warm, and it asks for the *two* things that actually help:

> You're one of the very first people to play TAKE 47 🎬 — a one-tap movie-stunt game I've been building.
>
> **Tap to jump, tap again to stop your spin, land upright.** That's the whole thing. Play however feels natural for a few minutes.
>
> Then tell me two things:
> 1. The first moment something **confused** you.
> 2. The first moment something made you **smile**.
>
> Brutal honesty is the gift here — "I didn't get X" is worth more than "it's great." Thank you for being on the crew. 🍿
>
> [TestFlight link OR web link]

## The thing that beats any feedback form: watch them play

Hand one or two people your phone and **say nothing.** Watch their thumbs, not their face. Note — don't correct — every moment they:
- hesitate before the first tap (is "ACTION!" clear?),
- tap at the wrong time (is the spin-stop timing learnable?),
- squint or re-read (which words don't land?),
- smile, laugh, or say "oh!" (what's working — protect it),
- try to tap something that isn't a button (unmet expectation = a feature request).

Ninety seconds of silent observation surfaces more than a page of written notes. Every hesitation is a design note; every laugh is a keeper. Log the findings in DEFECTS.md like any other tester's — cold-player data is the rarest thing this project can get.

## What to tell them it is (and isn't)

- Fully offline, no account, no sign-in, collects zero data.
- The "AD BREAK — PLACEHOLDER" screen is intentional (testing pacing; no real ads yet, and ads will never buy progress).
- It's a beta: the version line reads v0.9.0-beta, and there's a hidden QA panel (5 taps on that version line) that will be removed before the App Store — ignore it.

## After the session

- New defects → DEFECTS.md (the register is the source of truth, not the group chat).
- If it recurs across testers, it's a pattern — prioritize it.
- Genuine delight moments → note them too; they're the marketing copy writing itself.
