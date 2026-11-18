# ☸📊 Buddhist Skills

> BuddhistAI helps people who work on Buddhist projects find the best AI solution for each task: the one with the best results, and the one with the best results for its cost. It also helps people who build AI solutions share them and have them tested. This repo holds only the released skills: for each task and language, the **top performance** and the **best value** skill. Shared files and skills with no score yet are in the [prompt library](https://github.com/BuddhistAI/buddhist-prompt-library).

Open AI skills for Buddhist tasks: text work (table-of-contents extraction, cleanup, alignment, entity extraction, citation mapping, translation), images and visual AI, and personal AI setups (such as Claude files) for Buddhist study, teaching and practice. Built together by Buddhist organizations, translators, scholars and developers. Anyone can take part, and you can [share a skill or any file you give to AI](https://github.com/BuddhistAI/buddhist-prompt-library) today, with no benchmark score needed.

What each task is (definition, examples, hard cases) and the real workflows it comes from are in the [BuddhistAI knowledge base](https://buddhistai.github.io/knowledge-base/), together with our experiment reports. Anyone can edit it.

- **Need AI for a task that nothing here covers?** [Request an AI solution](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=request.yml). No technical knowledge needed.
- **See what is requested, shared and being measured:** the [Skills board](https://github.com/orgs/BuddhistAI/projects/1).

Every skill is **for one language**, written and maintained by people who know that language. Each one is the current winner on its task in [BuddhistAI/buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks).

## Install

Pick your language. You only get the skills for it, plus a few language-neutral ones.

<details open>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add BuddhistAI/buddhist-skills
claude plugin install buddhist-skills-tibetan@buddhistai     # or -pali, -sanskrit, -classical-chinese, ...
```

`buddhist-skills@buddhistai` installs every language.

</details>

<details>
<summary><strong>Any agent (skills.sh)</strong></summary>

```bash
npx skills add BuddhistAI/buddhist-skills
```

Then keep the skills ending in your language and drop the rest.

</details>

The full list, with each skill's benchmark score, is in **[SKILLS.md](./SKILLS.md)**. Not sure which skill you need? Ask your agent to use **[ask-buddhistai](./skills/ask-buddhistai/SKILL.md)**.

## How it fits together

```
BuddhistAI/buddhist-benchmarks            BuddhistAI/buddhist-skills (this repo)
  tasks/toc-extraction/                     skills/toc-extraction-tibetan/
    TASK.md      what the task is              SKILL.md   task, language, score
    scorer/      one scorer, all languages     ...
    data/bo/     Tibetan test set
    results/bo/  leaderboard  ◄──scored──   BuddhistAI/toc-extraction-tibetan (workshop repo)
                              ───winner──►    variants/<variant>/  challengers, not shipped
```

- A **task** (for example `toc-extraction`) is defined once, in the benchmarks repo, with one input/output format and one scorer for every language.
- A **skill** is a task for one language: `skills/<task>-<language>/`, for example `toc-extraction-tibetan`. Translation-type skills name both sides: `translation-tibetan-to-english`.
- **Shared files and unmeasured skills** live in the [prompt library](https://github.com/BuddhistAI/buddhist-prompt-library): Claude files, project instructions, style guides, glossaries, prompts, and skills before a benchmark exists for them. Not in the plugins.
- **Challengers** live in their task's workshop repo (one repo per skill, for example [toc-extraction-tibetan](https://github.com/BuddhistAI/toc-extraction-tibetan)), or in any fork or other organization's repo. They are scored on the benchmark; the winners are copied into `skills/`.

The reasoning behind this layout is in [docs/design.md](./docs/design.md). How to contribute (Share → Measure → Release) is in [CONTRIBUTING.md](./CONTRIBUTING.md).

## Shared resources

Glossaries, transliteration tables, and style guides live in [`shared/`](./shared/README.md), one copy each, so every skill uses the same terms.

## License

MIT, for code, skills, and shared resources alike. See [LICENSE](./LICENSE). By contributing you agree your contribution is released under the same license.
