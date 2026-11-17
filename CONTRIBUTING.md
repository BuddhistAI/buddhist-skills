# ☸📊 Contributing to BuddhistAI

BuddhistAI is open to everyone: Buddhist organizations, translators, teachers, scholars and developers. You do not need to know git or code to take part.

## Three steps: Share → Measure → Release

1. **Share.** Have a prompt, skill or workflow that helps you? Share it in [`community/`](./community/README.md), with no benchmark score needed. The easiest way is the [Share a skill](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=share.yml) form: paste a link to your GitHub repo or drag in your files, and a maintainer adds it and credits you. Your name and picture are optional.
2. **Measure.** Once a benchmark exists for its task and language, it is scored on the [leaderboard](https://buddhistai.github.io/buddhist-benchmarks/). See [how to submit](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).
3. **Release.** The best measured skill for each task and language is promoted to `skills/` and installs with the plugin (below).

## Where to send what

| You want to... | Go to |
| --- | --- |
| Share a prompt, skill or workflow you use | [`community/`](./community/README.md), or the [Share form](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=share.yml): a link or your files, no git needed |
| Need AI for a task that nothing here covers | The [Request an AI solution form](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=request.yml) |
| Check texts or outputs in a language you read | The [Volunteer as a language reader](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=reader.yml) form |
| Improve a skill for your language | A challenger in `drafts/<task>-<language>/<your-variant>/` here (or in your own repo), then benchmark it |
| Review a benchmark's answers as an expert | The [Review a benchmark form](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=expert-review.yml) |
| Pay for evaluations with compute or API credits | The [Donate compute or API credits form](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=donate-compute.yml) |
| Add test data for your language, or a new task | [buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks) |
| Fix or add a glossary term, transliteration rule, or style rule | `shared/` in this repo |
| Add a new language | `languages.json` in this repo, then data in buddhist-benchmarks |

Promoted skills in `skills/` are only changed by promotion, so every shipped skill can be traced to a benchmark result.

Everything shared or requested is tracked on the [Skills board](https://github.com/orgs/BuddhistAI/projects/1). New benchmarks are tracked on the [Benchmarks board](https://github.com/orgs/BuddhistAI/projects/2).

## First time?

- You do not need to know git. The issue forms above, or a post in [Discussions](https://github.com/orgs/BuddhistAI/discussions), are enough; a maintainer does the rest.
- If you do open a pull request, a small or unfinished one is fine. Say what you are unsure about and we will help.
- Templates to copy: [`templates/CARD.md`](./templates/CARD.md), [`templates/skill/SKILL.md`](./templates/skill/SKILL.md), [`templates/workflow/WORKFLOW.md`](./templates/workflow/WORKFLOW.md), and for a workshop repo (all variants, runs and [provenance records](https://buddhistai.github.io/knowledge-base/handbook/provenance.html) of one skill) [`templates/workshop/`](./templates/workshop/).
- Step-by-step tutorials: [Learn by building](https://buddhistai.github.io/knowledge-base/learn/). Who decides what, and how organizations get their own team: [Governance](https://buddhistai.github.io/knowledge-base/governance.html).
- Everyone who contributes is credited by name: in the card or skill metadata, on the leaderboard, and in the changelog. Reviewers and language readers too.
- Please read the [code of conduct](./CODE_OF_CONDUCT.md).

## Naming

- `skills/<task>-<language>/`, for example `toc-extraction-tibetan`, `text-cleanup-classical-chinese`.
- Tasks that produce another language add `-to-<language>`: `translation-tibetan-to-english`, `text-translation-alignment-pali-to-english`.
- `<task>` is a task ID from [buddhist-benchmarks `tasks/index.json`](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/tasks/index.json).
- `<language>` is a full name from [`languages.json`](./languages.json). The ISO code goes in metadata, not the name.
- Language-neutral skills (like the router) have no language suffix.

## From challenger to promoted skill

1. Put your challenger in `drafts/<task>-<language>/<org>-<short-name>/SKILL.md` (or in your own repo). Its frontmatter `name` should already be the final skill name, for example `toc-extraction-tibetan`, and it needs `metadata.variant` and `metadata.version` (semver). Bump the version on every change.
2. Run it on the task's benchmark set for your language and add your row to the leaderboard in buddhist-benchmarks, citing the exact commit of your skill. Keep a [provenance record](https://buddhistai.github.io/knowledge-base/handbook/provenance.html) of each run in the repo where the skill is built (not in buddhist-benchmarks).
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

## Credit

Put every author in the frontmatter: `authors` in a community `CARD.md`, `metadata.authors` in a draft or promoted `SKILL.md` (for example `Jane Doe (Example Sangha); Tashi (Example Institute)`). Name the people and organizations whose work a skill builds on in its card or `VARIANT.md`, with their license.

## Writing style

Plain English, for readers whose first language may not be English. Use Unicode for Tibetan, Sanskrit, Pali, and Chinese, and say which transliteration scheme you use (see `shared/transliteration/`).
