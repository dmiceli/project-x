# BIG-WINS.md — five MVP additions to maximize launch success (2026-07-04, overnight audit)

Full-game audit + market research. Benchmarks to beat: hybrid-casual D1 retention 30–35% (leaders 35–40%), D7 15–18%. What correlates with hitting them: competitive/social features, daily reward loops, habit anchors, and polish that survives the first 6 seconds. Ranked by impact-per-effort, all compatible with our privacy posture and "ads never buy progress."

## 1 · Game Center leaderboard for the Daily Gauntlet
The daily is already "the same gauntlet for everyone" — but today nobody can SEE everyone. A Game Center leaderboard (daily best + lifetime furthest scene) turns our strongest hook into real competition. Apple-native: no backend, no accounts of ours, no privacy-label change (Apple operates it), free. Competitive leaderboards are the single most consistent retention correlate in the research. **When:** Phase 5 (Capacitor Game Center plugin) — decide now so the wrapper includes it. **Effort:** ~1 session in the wrapper phase.

## 2 · Local notification at gauntlet reset (opt-in)
"New gauntlet & call sheet 🌙" already exists as a *hope*; a local notification makes it a *habit anchor* — the #1 pattern behind daily-loop retention. Fully on-device (no push server, no ATT, no data), permission asked in-context ("Want a heads-up when tomorrow's gauntlet opens?") after a completed daily — never at first launch. **When:** Phase 5 (Capacitor LocalNotifications). **Effort:** small.

## 3 · Make the haptics real
`haptic()` calls are already threaded through the game (jump, lock, crash, perfect) but do nothing in the browser. Wiring them to Capacitor Haptics in the wrapper gives every landing a physical thud — feel is disproportionately what one-thumb games get judged on, and it's effectively free since the call sites exist. Include a settings toggle (already built). **When:** Phase 5, first wrapper build. **Effort:** tiny.

## 4 · Mercy system at the difficulty wall ("The director takes pity")
Audit finding: our logarithmic ramp is brutal-but-fair, but D1 churn concentrates where players hit their first wall with no relief valve. Proposal: after ~7 consecutive crashes on one scene, the prop department sends a free scene-relevant prop with a dry quip ("The insurance guy insists."). No progress skipped, no ads, perfects still earned raw — pure churn softener aligned with every standing principle. **When:** pre-beta (pure JS). **Effort:** small — grantItem + counter exist.

## 5 · Store-conversion kit: screenshots + 15s preview from the brand
Retention is moot if nobody installs: the store page is the funnel's top. We uniquely have "the fail is the ad" (MARKETING.md) — outtakes, verdict stamps, the director facepalming. Produce the 6-screenshot set + a 15-second preview video (screen-record the browser build, cut on crashes) + subtitle/keyword pass before TestFlight, so beta testers land on a real page and launch day isn't blocked on assets. **When:** parallel with beta. **Effort:** ~1 session with existing brand kit.

**Not chosen (and why):** ghost replays (strong but medium-heavy; post-launch), seasonal events (needs live-ops muscle we don't have yet), cloud saves (Game Center covers the visible part; iCloud KV store is a Phase 5 stretch), more characters/sets (content ≠ retention at this stage).

*Sources: [GameAnalytics — hybrid-casual retention](https://www.gameanalytics.com/blog/hybrid-casual-higher-retention-better-engagement), [Game Growth Advisor — retention strategies 2026](https://gamegrowthadvisor.com/blog/2026-03-17-mobile-game-retention-strategies-2026/), [StudioKrew — 2026 strategy guide](https://studiokrew.com/blog/hybrid-casual-games-vs-traditional-mobile-games/), [CrazyLabs — retention tips](https://www.crazylabs.com/blog/5-tips-for-improving-retention-in-hybrid-casual-games/).*
