# Design: BuddhistAI skills and benchmarks

_Status: adopted 2026-11-13. Covers [buddhist-skills](https://github.com/BuddhistAI/buddhist-skills) and [buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks)._

## Goal

Many Buddhist organizations need the same kinds of work done on texts in many languages: table-of-contents extraction, text cleanup, aligning a text with its translation or its commentary, entity extraction, citation mapping, and every stage of translation. We want one open place where they can share agent skills for that work, compare them fairly, and always ship the best one.

## Decisions

### 1. Two hub repos, not one repo per skill

- **buddhist-benchmarks** defines each task once and holds test data, scorers, and leaderboards.
- **buddhist-skills** holds the skills: the promoted winners in `skills/` and challengers in `drafts/`.

One repo per skill would mean dozens of repos with duplicated scoring code, and no single place to compare languages on the same task. Two hubs keep the task definition and the scorer shared across languages, while skills and data stay separate so a benchmark cannot quietly change to fit a skill.

### 2. A skill is one task in one language

Specialists contribute to the language they know. Mixing languages in one skill would make a Tibetan expert review Pali instructions, and a change for one language could lower another's score. So each skill covers exactly one source language, and each language can move at its own pace.

What is shared across languages is the **task**: its definition, input and output format, and scorer. That lives in buddhist-benchmarks.

### 3. Names: `<task>-<language>`, full language name as a suffix

- `toc-extraction-tibetan`, `text-cleanup-classical-chinese`, `entity-extraction-pali`.
- Tasks that produce another language: `translation-tibetan-to-english`.
- Language-neutral skills (the router) have no suffix.

**Suffix, not prefix**, so that typing the task (`toc-...`) lists that task's skill, and so skills sort by task in a catalog. A Tibetan translator doesn't see other languages' skills at all, because they install the Tibetan plugin only (decision 4).

**Full name, not ISO code**, because `tibetan` is readable to every contributor and `bo` is not. The extra length is small. ISO / BCP 47 codes (`bo`, `lzh`, `pi`, `sa`, ...) are used where machines need them: skill metadata, and data folder names in buddhist-benchmarks. [`languages.json`](../languages.json) maps one to the other.

### 4. One plugin per language

`scripts/build.py` generates the plugin marketplace from the folder names: `buddhist-skills-tibetan` contains every `*-tibetan` skill plus the language-neutral ones, and `buddhist-skills` contains everything. Nobody edits the marketplace by hand, so a new skill can't be forgotten in a manifest.

### 5. Tasks and data are organized by task, then language

```
buddhist-benchmarks/
  tasks/index.json                  every task ID, active or planned
  tasks/toc-extraction/
    TASK.md                         definition, I/O format, metric
    scorer/score.py                 one scorer, every language
    data/bo/v1/                     Tibetan test set, versioned
    results/bo/LEADERBOARD.md       Tibetan leaderboard
    results/bo/runs/<run>/          outputs + scores for one run
```

Data folders use ISO codes. Data is versioned (`v1`, `v2`): a leaderboard row always names the version, and scores from different versions are never compared.

### 6. Leaderboard rows cite an exact skill commit

A row is keyed by task × language × data version × skill reference (`owner/repo@commit:path`) × model. Because a skill reference can point at any repo, other organizations can compete from their own forks without a PR here first.

### 7. Promotion is a PR with metadata, checked by CI

A promoted `SKILL.md` records `task`, `language`, `language-code`, `benchmark`, `score`, `version`, `source`, and `promoted`. CI checks that the metadata matches the folder name and `languages.json`, that the task exists in buddhist-benchmarks, and that the generated catalog and marketplace are current.

### 8. Ownership per language

`CODEOWNERS` in both repos assigns language owners by glob: `skills/*-tibetan/` here, `tasks/*/data/bo/` there. Until language teams exist, NT owns everything.

### 9. Shared resources live in buddhist-skills `shared/`

Glossaries (`shared/glossaries/bo-en.tsv`), transliteration tables, and style guides have one copy. Skills use them at run time; benchmark data that depends on one records the commit.

## Tasks anticipated

| Task ID | What it does |
| --- | --- |
| `toc-extraction` | Titles, levels, and locations of a text's table of contents. Worked example. |
| `text-cleanup` | Fix OCR and input errors, normalize, without changing content. |
| `segmentation` | Split a text into sentences or translation units. |
| `entity-extraction` | People, places, texts, and other named entities. |
| `citation-mapping` | Quotations and references, linked to their sources. |
| `text-translation-alignment` | Source and translation aligned segment by segment. |
| `text-commentary-alignment` | Root text passages linked to the commentary that explains them. |
| `term-extraction` | Candidate glossary terms and their renderings. |
| `translation` | Draft translation. |
| `translation-review` | Check a translation against source, glossary, and style guide. |

The list lives in `tasks/index.json`; this table is a snapshot.

## Not decided yet

- How to run skills reproducibly across models (a shared runner script, or each contributor's harness plus a recorded run file). For now each run records its model and harness in `run.json`.
- Human evaluation for tasks where automatic metrics fall short, such as translation.
- Whether a language's leaderboard needs a minimum data size before a promotion counts.
