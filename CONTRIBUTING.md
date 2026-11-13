# Contributing

BuddhistAI is open to every Buddhist organization and every specialist. You do not need to be part of WeBuddhist to propose a skill, a challenger, or a glossary entry.

## Where to send what

| You want to... | Go to |
| --- | --- |
| Improve a skill for your language | A challenger in `drafts/<task>-<language>/<your-variant>/` here (or in your own repo), then benchmark it |
| Add test data for your language, or a new task | [buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks) |
| Fix or add a glossary term, transliteration rule, or style rule | `shared/` in this repo |
| Add a new language | `languages.json` in this repo, then data in buddhist-benchmarks |

Promoted skills in `skills/` are only changed by promotion, so every shipped skill can be traced to a benchmark result.

## Naming

- `skills/<task>-<language>/`, for example `toc-extraction-tibetan`, `text-cleanup-classical-chinese`.
- Tasks that produce another language add `-to-<language>`: `translation-tibetan-to-english`, `text-translation-alignment-pali-to-english`.
- `<task>` is a task ID from [buddhist-benchmarks `tasks/index.json`](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/tasks/index.json).
- `<language>` is a full name from [`languages.json`](./languages.json). The ISO code goes in metadata, not the name.
- Language-neutral skills (like the router) have no language suffix.

## From challenger to promoted skill

1. Put your challenger in `drafts/<task>-<language>/<org>-<short-name>/SKILL.md` (or in your own repo). Its frontmatter `name` should already be the final skill name, for example `toc-extraction-tibetan`, and it needs `metadata.variant` and `metadata.version` (semver). Bump the version on every change.
2. Run it on the task's benchmark set for your language and add your row to the leaderboard in buddhist-benchmarks, citing the exact commit of your skill.
3. If it beats the current skill, open a PR here that copies it into `skills/<task>-<language>/` with this metadata:

   ```yaml
   ---
   name: toc-extraction-tibetan
   description: ...
   metadata:
     task: toc-extraction                 # task ID in buddhist-benchmarks
     language: tibetan                    # matches the folder suffix
     language-code: bo                    # from languages.json
     benchmark: toc-extraction/bo@1.0.0   # task / data code @ benchmark version (semver)
     score: "0.91 F1"                     # as on the leaderboard
     version: 1.0.0                       # this skill's version
     source: BuddhistAI/buddhist-skills@3f2a1c9:drafts/toc-extraction-tibetan/webuddhist-v1
     promoted: 2026-11-13
   ---
   ```

   Skills with `-to-<language>` also need `target-language`.

4. Run `python3 scripts/build.py` (regenerates `SKILLS.md` and the plugin marketplace) and `python3 scripts/check.py`.
5. Add an entry at the top of `CHANGELOG.md`. Update [ask-buddhistai](./skills/ask-buddhistai/SKILL.md) if this is a new task for any language.

Language owners in [`.github/CODEOWNERS`](./.github/CODEOWNERS) review promotions for their language.

## Shared resources

Refer to shared files by their path in this repo, for example `shared/glossaries/bo-en.tsv`. A skill that must work offline may bundle a copy if it records the commit it came from.

## Writing style

Plain English, for readers whose first language may not be English. Use Unicode for Tibetan, Sanskrit, Pali, and Chinese, and say which transliteration scheme you use (see `shared/transliteration/`).
