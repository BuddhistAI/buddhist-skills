# ☸📊 Community: shared skills and workflows

This is the place to share a skill, prompt or workflow that helps with Buddhist work: texts and translation, images and visual AI, or a personal AI setup (such as a Claude file) for study, teaching or practice, **before any benchmark exists for it**. No score, no git and no code are needed.

Everything here is listed in [SKILLS.md](../SKILLS.md) under *Community (not yet measured)*. It is not part of the installable plugins, because it has not been measured yet. That is the only difference: it is just as welcome.

## The ladder: Share → Measure → Ship

1. **Share** (here). Anyone can add a skill or workflow with a short card: what it does, which language, who made it, how to use it, one example.
2. **Measure.** When a benchmark exists for that task and language in [buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks), the entry is scored and appears on the [leaderboard](https://buddhistai.github.io/buddhist-benchmarks/). It then moves to `drafts/` as a challenger. If no benchmark exists yet, your entry shows us which one to build next.
3. **Ship.** The best measured skill for each task and language is promoted to `skills/` and installs with the language plugin (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

## How to share

**The easy way (no git):** open a [Share a skill or workflow](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=share.yml) issue and paste your prompt or describe your steps. A maintainer turns it into an entry here and credits you. You can also post in [Discussions](https://github.com/orgs/BuddhistAI/discussions).

**With a pull request:** copy the templates and fill them in.

```
community/<task>-<language>/<you>-<short-name>/
  CARD.md        what it is, who made it, how to use it (from templates/CARD.md)
  SKILL.md       the skill itself (from templates/skill/SKILL.md), or
  WORKFLOW.md    the steps of a workflow (from templates/workflow/WORKFLOW.md), or
  PROMPT.md      a plain prompt to paste into any chat assistant
  ...            any reference files the skill reads
```

- `<task>` is a short name for what it does, in lowercase with hyphens: `translation`, `text-cleanup`, `glossary-building`. Use a task ID from [tasks/index.json](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/tasks/index.json) when one fits, so it can be measured later; otherwise make up a clear one.
- `<language>` is the language of the source text, a full name from [languages.json](../languages.json) (for example `tibetan`, `pali`, `classical-chinese`). Tasks that produce another language add `-to-<language>`: `translation-pali-to-english`. One language per entry, as everywhere in this repo. A language that is missing can be added to `languages.json` in the same PR.
- Workflows (several steps, possibly several skills) use `<goal>-workflow-<language>`, for example `translation-workflow-tibetan`.
- `<you>` is your name or your organization's, for example `dharmachakra-glossary-first`.

Run `python3 scripts/build.py` and `python3 scripts/check.py` before opening the PR. If you cannot, say so in the PR and a maintainer will.

## What makes a good entry

- One clear job, for one language.
- An honest card: which models you used it with, what it does badly, and what you checked by hand.
- A short real example (input and output), so others can judge it quickly.
- Only material you may share: no texts with restricted transmission, and no copyrighted translations without permission. See the [code of conduct](../CODE_OF_CONDUCT.md).

## Using an entry

Copy its folder into your agent's skills folder (for Claude Code, `~/.claude/skills/<name>/`, renaming the folder to the `name` in its `SKILL.md`), or paste the prompt into any chat assistant. Tell the author how it went, in Discussions or an issue: that is how entries improve.
