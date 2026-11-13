# Notes for agents working in this repo

- Skills are per language: `skills/<task>-<language>/` (or `<task>-<source>-to-<target>/`). Never mix languages in one skill. Language-neutral skills have no suffix. Names and codes come from `languages.json`; task IDs come from buddhist-benchmarks `tasks/index.json`.
- `skills/` only holds **promoted** skills. Do not edit a promoted `SKILL.md` directly; improvements start as a challenger in `drafts/` and come back through promotion (see `CONTRIBUTING.md`).
- Never hand-edit `.claude-plugin/marketplace.json` or `SKILLS.md`. Run `python3 scripts/build.py`, then `python3 scripts/check.py`.
- When a new task appears in `skills/`, or a skill is removed, update `skills/ask-buddhistai/SKILL.md` so the router never points at a skill that does not exist.
- Shared glossaries, transliteration tables, and style guides live only in `shared/`.
- Design rationale: `docs/design.md`.
