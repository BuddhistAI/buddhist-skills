# BuddhistAI Skills

Agent skills for Buddhist text work: translation, table-of-contents extraction, proofreading, and more. Built in the open by WeBuddhist and any Buddhist organization that wants to take part.

This repo holds the **current best version** of each skill. Each skill is developed, compared, and benchmarked in its own repo (for example [`BuddhistAI/translation`](https://github.com/BuddhistAI/translation)). When a variant wins its benchmark, it is tagged there and promoted here.

## Install

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add BuddhistAI/buddhist-skills
claude plugin install buddhistai-skills@buddhistai
```

</details>

<details>
<summary><strong>Any agent (skills.sh)</strong></summary>

```bash
npx skills add BuddhistAI/buddhist-skills
```

This copies the skill files into your project. Update by running it again.

</details>

Not sure which skill you need? Ask your agent to use **[ask-buddhistai](./skills/router/ask-buddhistai/SKILL.md)**, which maps every skill and when to use it.

## Skills

Skills are grouped by workflow. Each entry shows where the skill came from and how it scored.

### Translation

_No skills promoted yet. See [skills/translation](./skills/translation/README.md)._

### Text preparation

_No skills promoted yet. See [skills/text-preparation](./skills/text-preparation/README.md)._

### Router

- **[ask-buddhistai](./skills/router/ask-buddhistai/SKILL.md)**: Find the right BuddhistAI skill for a task.

## Shared resources

Glossaries, transliteration tables, and style guides used by more than one skill live in [`shared/`](./shared/README.md). There is one copy of each, here, so every skill and every skill repo uses the same terms.

## How it works

```
BuddhistAI/translation          BuddhistAI/buddhist-skills (this repo)
  variants/                       skills/translation/<skill>/
    webuddhist-v1/   ─┐             SKILL.md  (source, version, score)
    other-org-v2/     ├─ benchmark ─►
  benchmarks/        ─┘   winner      CHANGELOG.md
  results/LEADERBOARD.md  tagged
```

1. Anyone proposes a variant in a skill repo under `variants/`.
2. The skill repo's benchmark scores every variant the same way. Scores go in `results/`.
3. The winner is tagged in the skill repo (for example `translation@v1.2.0`).
4. A PR here copies that tagged variant into `skills/<workflow>/<skill>/`, records its source, version, and score in the frontmatter, and adds a `CHANGELOG.md` entry.

The full process is in [CONTRIBUTING.md](./CONTRIBUTING.md). To start a new skill repo, copy [`templates/skill-repo/`](./templates/skill-repo/README.md).

## License

MIT, for code, skills, and shared resources alike. See [LICENSE](./LICENSE). By contributing you agree your contribution is released under the same license.
