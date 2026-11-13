# Contributing

BuddhistAI is open to every Buddhist organization. You do not need to be part of WeBuddhist to propose a skill, a variant, a benchmark item, or a glossary entry.

## Where to send what

| You want to... | Go to |
| --- | --- |
| Improve how a skill works | The skill's own repo, as a new folder under `variants/` |
| Add test cases or change how a skill is scored | The skill's own repo, under `benchmarks/` |
| Fix or add a glossary term, transliteration rule, or style rule | This repo, under `shared/` |
| Propose a brand new skill | An issue in this repo, then a new skill repo from `templates/skill-repo/` |
| Promote a benchmark winner | A PR in this repo (see below) |

Changes to a promoted skill go through its skill repo first, never straight into this repo. That keeps every promoted skill traceable to a benchmark result.

## Promoting a winner

A promotion PR must:

1. Copy the winning variant's folder, unchanged, from a **tag** in its skill repo into `skills/<workflow>/<skill-name>/`.
2. Fill in the `metadata` block in that `SKILL.md`:

   ```yaml
   ---
   name: translate-tibetan-english
   description: ...
   metadata:
     source: BuddhistAI/translation      # skill repo
     variant: webuddhist-v2              # folder under variants/
     version: translation@v1.2.0         # tag in the skill repo
     benchmark: tib-eng-core-v1          # benchmark set used
     score: "0.81 chrF / 4.3 human"      # headline result, as in results/
     promoted: 2026-11-13
   ---
   ```

3. List the skill in the top-level `README.md`, its workflow `README.md`, and `.claude-plugin/plugin.json`.
4. Update [ask-buddhistai](./skills/router/ask-buddhistai/SKILL.md) if the skill is new or its purpose changed.
5. Add an entry at the top of `CHANGELOG.md`.

`scripts/check.py` runs in CI and checks items 2 and 3.

## Skill folders

- `skills/translation/`, `skills/text-preparation/`, ... : promoted skills, grouped by workflow. Shipped in the plugin.
- `skills/router/`: the router skill. Shipped in the plugin.
- `skills/in-progress/`: public on purpose, feedback wanted, not shipped.
- `skills/deprecated/`: replaced or retired, kept for reference, not shipped.

A new workflow folder needs a `README.md` and a section in the top-level `README.md`.

## Shared resources

Skills reference shared files by their path in this repo, for example `shared/glossaries/tibetan-english.tsv`. If a skill must work offline after `npx skills add`, it may bundle a copy, but this repo's copy is the source of truth and the bundled copy must say which commit it came from.

## Writing style

Plain English. Write for a reader whose first language may not be English. Use Unicode for Tibetan, Sanskrit, Pali, and Chinese, and say which transliteration scheme you use (see `shared/transliteration/`).
