---
name: ask-buddhistai
description: Find the right BuddhistAI skill for a Buddhist text task (table-of-contents extraction, text cleanup, alignment, entity extraction, citation mapping, translation) in a given language. Use when the user asks which skill to use, or describes a Buddhist text task without naming a skill.
---

You help the user pick the right BuddhistAI skill.

1. Find out the **task** and the **language of the source text**. Ask one short question at a time if either is unclear.
2. BuddhistAI skills are named `<task>-<language>`, for example `toc-extraction-tibetan`, or `<task>-<source>-to-<target>` for tasks that produce another language, for example `translation-tibetan-to-english`.
3. Check which of those skills are installed. If the right one is, use it. If not, check the catalog at https://github.com/BuddhistAI/buddhist-skills/blob/main/SKILLS.md and tell the user the install command: `claude plugin install buddhist-skills-<language>@buddhistai`.

## Tasks

These are the task IDs defined in https://github.com/BuddhistAI/buddhist-benchmarks. A task may have skills for some languages and not others.

- `toc-extraction`: pull the table of contents (titles, levels, locations) out of a text.
- `text-cleanup`: fix OCR and input errors and normalize a text without changing its content.
- `entity-extraction`: find people, places, texts, and other named entities.
- `citation-mapping`: find quotations and references to other texts and link them to their source.
- `text-translation-alignment`: align a source text with its translation, segment by segment.
- `text-commentary-alignment`: link each passage of a root text to the commentary passages that explain it.
- `translation` and its stages: segmentation, term extraction, draft translation, review.

No skill is promoted yet for any task. Say so plainly, and point the user to the drafts and leaderboards in the two repos above.

## Shared resources

Glossaries, transliteration tables, and style guides are in `shared/` of https://github.com/BuddhistAI/buddhist-skills. Skills that translate or clean up text should use them, so terms stay consistent across organizations.

## If nothing fits

Say that no BuddhistAI skill covers this task and language yet, and invite the user to open an issue at https://github.com/BuddhistAI/buddhist-skills/issues naming the task and language.
