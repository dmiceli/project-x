# DEFECTS.md — defect register (living doc)

Every defect from TestFlight beta onward gets a row the moment it's reported — no defect exists only in chat. Lifecycle: **OPEN → DIAGNOSED → FIXED (build n) → VERIFIED (build n, by Dan on-device) → CLOSED**. Fixes ship in batches (batch-before-building rule); the "Fixed in" build is the batch that carried the fix. Severity: **S1** blocks play/loses data · **S2** feature wrong/unfair · **S3** feel/polish · **S4** cosmetic/copy.

Pre-TestFlight defects (prototype/QA phases) are already recorded in STATUS.md/DECISIONS.md and are not back-filled here.

## Register

| ID | Reported | Build | Sev | Symptom (as reported) | Root cause | Fix | Fixed in | Status |
|----|----------|-------|-----|----------------------|-----------|-----|----------|--------|
| — | — | — | — | *(no open defects — register opened 2026-07-04 during the build-7 live session)* | | | | |

## Verification notes (on-device passes that aren't defects)

| Date | Build | Check | Result |
|------|-------|-------|--------|
| 2026-07-04 | 7 | Save persists through force-quit (Capacitor Preferences mirror — Phase 5 hard gate) | ✅ PASS (Dan, iPhone) |
