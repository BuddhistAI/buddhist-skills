---
name: ask-buddhistai
description: Find the right BuddhistAI skill for a Buddhist text task (translating, extracting a table of contents, proofreading, cleaning OCR, using a glossary). Use when the user asks which skill to use, or describes a Buddhist text task without naming a skill.
---

You help the user pick the right BuddhistAI skill. Ask one question at a time if the task is unclear: what text (language, script, edition), what they want out of it, and who will read the result.

## Skills by workflow

### Translation

No skills promoted yet. If the user needs translation now, say so plainly and point them to https://github.com/BuddhistAI/translation, where variants are being developed and benchmarked.

### Text preparation

No skills promoted yet (planned: table-of-contents extraction, proofreading, OCR cleanup).

## Shared resources

Glossaries, transliteration tables, and style guides are in `shared/` of https://github.com/BuddhistAI/buddhist-skills. Any skill that translates or proofreads should use them, so terms stay consistent across organizations.

## If nothing fits

Say that no BuddhistAI skill covers the task yet, and invite the user to open an issue at https://github.com/BuddhistAI/buddhist-skills/issues describing the task, so a new skill repo can be started.
