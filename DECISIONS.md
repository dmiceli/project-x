# Decisions Log

| Date | Decision | Why |
|------|----------|-----|
| 2026-07-02 | No-Mac workflow: cloud build service for iOS compile/sign/submit | Dan is Windows-only; modern cloud services (Codemagic, EAS) make a Mac unnecessary |
| 2026-07-02 | Enroll in Apple Developer Program early ($99/yr) | Enrollment takes days; required for TestFlight and App Store |
| 2026-07-02 | Prototype before full design doc | For simple/hyper-casual games, core-loop feel matters more than specs; document what proves fun |
| 2026-07-02 | Sprint pace; target TestFlight beta in ~2 weeks | Dan's availability supports near-daily sessions |
| 2026-07-02 | Prototype two concepts: "Stick the Landing" (tap to land flipping character; ragdoll fails) and "Squeeze" (hold to grow / release to shrink through gaps) | Both scored well on the viral-ingredient checklist; picking by feel after playing both |
| 2026-07-02 | Git runs on Dan's PC via GitHub Desktop, not in Claude's sandbox | Sandbox can't manage git lock files on the shared folder; GitHub hosting is needed anyway for cloud builds, and GitHub Pages gives us iPhone-testable URLs |
| 2026-07-02 | All-in on "Stick the Landing"; Squeeze parked as backup | STL had the stronger "one more try" pull in playtesting; flip-cup/bottle-flip familiarity is a proven hook |
| 2026-07-02 | Ragdoll stunt character (not cup/bottle or animal) | Funnier fails = second share loop; room for unlockable characters; avoids bottle-flip clone space and drinking-game rating concerns |
| 2026-07-02 | Core loop validated; DESIGN.md written | Streak-chasing + retry pull confirmed in playtesting; crash comedy deferred to build phase |
| 2026-07-02 | Monetization: rewarded ads + capped interstitials + remove-ads IAP ($1.99-2.99), no banners | Genre-standard model; revenue goal from day one; placement discipline prevents player churn |
| 2026-07-02 | v1.0 scope: share button, unlockable characters, daily challenge, initial achievements. Game Center leaderboard deferred to 1.1 | Dan's picks; social competition via shared score-card images instead of server/GC |
| 2026-07-02 | Name deferred until theme exploration | Name must grow from visual theme; research App Store crowding first |
| 2026-07-02 | Tech stack: vanilla JS + canvas (no engine), Capacitor wrapper, Codemagic cloud build | v2 prototype proved engine unnecessary at this scope; browser-first keeps iteration instant on Windows/iPhone |
| 2026-07-02 | Theme: movie stunt set. Name: **TAKE 47** | Generic flip niche saturated; stunt-set framing turns failure into the joke (takes/outtakes/director) and the niche is open. Name has no collision; "Take Two"/"Stunt Guy"/"Stick the Landing" all blocked |
| 2026-07-02 | Lifetime take counter as core joke + share hook | Failure count becomes content: "Only took 1,047 takes" writes the share card itself |
| 2026-07-02 | Levels = scene progression: crash retries the SAME scene, progress persists; seeded so every player's Scene N is identical; endless score-run becomes the daily challenge mode | Dan wanted levels for accomplishment + sharing ("Scene 137"); fits the movie theme natively |
| 2026-07-02 | Standing rule: accessibility & privacy checked on every change (added to CLAUDE.md) | Dan's directive; cheaper as a habit than a retrofit |
