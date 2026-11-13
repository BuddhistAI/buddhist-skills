# Notes for agents working in this repo

- This repo only holds **promoted** skills. Do not edit a promoted `SKILL.md` directly: changes go to its skill repo (named in `metadata.source`) and come back through promotion. See `CONTRIBUTING.md`.
- Every skill in a workflow folder (anything under `skills/` except `in-progress/` and `deprecated/`) must be listed in `README.md`, its folder `README.md`, and `.claude-plugin/plugin.json`. Skills in `in-progress/` and `deprecated/` must not be.
- When a skill is added, renamed, removed, or changes purpose, update `skills/router/ask-buddhistai/SKILL.md` so the router never points at a skill that does not exist.
- Shared glossaries, transliteration tables, and style guides live only in `shared/`. Do not copy them into a skill without noting the source commit.
- Run `python3 scripts/check.py` before opening a PR.
