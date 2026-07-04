# releases/ — one file per shipped build

Every build that reaches phones gets `X.Y-buildN.md` here, written when the build goes out. This is the release's permanent record; the App Store "What's New" text is copied FROM here at submission time, never written ad-hoc in the ASC form.

Each file contains, in order:

1. **Release notes (user-facing)** — the "What's New" text. Beta builds: written for Crew testers. App Store builds: player voice, brand copy rules per BRAND.md.
2. **QA report** — what was tested for THIS build, on what device/OS, verdicts. References QA-PLAN.md for method; records results here. Includes the defect IDs (DEFECTS.md) fixed and verified in this build.
3. **Known issues shipped** — what we knowingly shipped anyway, and why.
4. **Store metadata snapshot** *(App Store submissions only)* — the exact name/subtitle/description/keywords/screenshot set submitted, so review questions and ASO changes have a baseline.

Related docs: DEFECTS.md (defect register), CHANGELOG.md (engineering changelog), QA-PLAN.md (test method), PIPELINE.md (how a build ships), MARKETING.md (ASO source for store metadata).
