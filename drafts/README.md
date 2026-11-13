# Drafts

Challengers for a task and language, not shipped in any plugin.

Layout: `drafts/<task>-<language>/<org>-<short-name>/SKILL.md`, for example `drafts/toc-extraction-tibetan/webuddhist-v1/SKILL.md`.

Every draft's frontmatter has `metadata.variant` (the folder name) and `metadata.version` (semver, see [design decision 10](../docs/design.md)). Bump the version whenever you change the draft, and cite variant and version in benchmark runs.

Each draft should have a short `VARIANT.md` next to its `SKILL.md`: who made it, what is different from the current skill, and which model(s) it was tested with. Score it in [buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks) before proposing promotion (see `CONTRIBUTING.md`).
