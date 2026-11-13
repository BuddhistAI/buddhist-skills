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
    CHANGELOG.md                    every benchmark version
    data/bo/v1/                     Tibetan test set, major version 1 (exact semver in its README)
    results/bo/LEADERBOARD.md       Tibetan leaderboard
    results/bo/runs/<run>/          outputs + scores for one run
```

Data folders use ISO codes. Data is versioned (decision 10): a leaderboard row always names the version, and scores from different versions are never compared.

### 6. Leaderboard rows cite an exact skill commit

A row is keyed by task × language × data version × skill reference (`owner/repo@commit:path`) × model. Because a skill reference can point at any repo, other organizations can compete from their own forks without a PR here first.

### 7. Promotion is a PR with metadata, checked by CI

A promoted `SKILL.md` records `task`, `language`, `language-code`, `benchmark`, `score`, `version`, `source`, and `promoted`. CI checks that the metadata matches the folder name and `languages.json`, that the task exists in buddhist-benchmarks, and that the generated catalog and marketplace are current.

### 8. Ownership per language

`CODEOWNERS` in both repos assigns language owners by glob: `skills/*-tibetan/` here, `tasks/*/data/bo/` there. Until language teams exist, NT owns everything.

### 9. Shared resources live in buddhist-skills `shared/`

Glossaries (`shared/glossaries/bo-en.tsv`), transliteration tables, and style guides have one copy. Skills use them at run time; benchmark data that depends on one records the commit.

### 10. Everything that is scored has a semantic version

**Skills.** Every skill, promoted or draft, has `metadata.version` (semver) in its frontmatter, and also `metadata.variant` for drafts. Reports and leaderboard rows cite variant and version next to the exact commit, so a reader can tell "gepa-v1 1.0.0" from "gepa-v1 1.1.0" without diffing. Patch: wording fixes that should not change behavior. Minor: new rules or examples. Major: a change to the output format or to what the skill is for.

**Benchmarks.** Benchmarks grow every time a new corner case is found, so each task's data set per language also has a semver version ([buddhist-benchmarks VERSIONING.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/VERSIONING.md)):

- **patch**: wrong reference answers fixed;
- **minor**: new items added, each with a short note on what it tests and where it came from;
- **major**: the scorer or the input/output format changed (new `v<major>/` folder).

Each task has a `CHANGELOG.md`, and releases are tagged `<task>/<code>@<version>`. A promoted skill's `metadata.benchmark` names the exact version (`toc-extraction/bo@1.0.0`). When the benchmark gets a new version, the promoted skill and the open challengers are re-run on it, and promotion is decided on the new version only.

**Why:** without versions, a score of "0.95" means nothing once the data has moved, and nobody can tell whether a skill got better or the test got easier.

### 11. Workflows (planned)

A pipeline of skills, such as cleanup → segmentation → translation → review, will be packaged as a skill of type `workflow` (e.g. `translation-workflow-tibetan`) that pins its stage skills' versions and ships in the same language plugin. It gets its own leaderboard with an end-to-end benchmark (raw input → finished output) showing total cost and time, next to the per-task stage leaderboards. Not built yet; details in [workflows.md](./workflows.md).

**Why:** the best skill per stage is not always the best workflow, because errors compound; stage scores then show where a workflow loses points.

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
