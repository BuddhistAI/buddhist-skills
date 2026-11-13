# BuddhistAI/<skill>

_Template for a BuddhistAI skill repo. Copy this folder into a new repo named after the task (for example `BuddhistAI/translation`, `BuddhistAI/toc-extraction`), then replace `<skill>` throughout._

This repo is where competing versions of the **<skill>** skill are built and compared. The current winner is published in [BuddhistAI/skills](https://github.com/BuddhistAI/skills).

## Layout

```
variants/          one folder per competing version of the skill
  <org>-v<N>/
    SKILL.md       the skill itself (same format as in BuddhistAI/skills)
    VARIANT.md     who made it, what is different, which model(s) it was tested on
benchmarks/
  <set-name>/      a test set: inputs, reference outputs, and a README describing it
  scoring/         the scripts that turn a variant's outputs into scores
results/
  LEADERBOARD.md   every variant's score on every benchmark set
  <variant>/<set>/ raw outputs and score files for each run
```

## Adding a variant

1. Copy an existing variant folder to `variants/<your-org>-v1/` and change it.
2. Fill in `VARIANT.md`.
3. Run the benchmark (see `benchmarks/scoring/README.md`) and commit the outputs under `results/<variant>/<set>/`.
4. Add a row to `results/LEADERBOARD.md` and open a PR.

Every variant is scored with the same benchmark sets, the same scoring scripts, and the model(s) named in the leaderboard. A score from a different setup goes in a separate table.

## Promoting a winner

When a variant tops the leaderboard and maintainers agree:

1. Tag the commit: `git tag <skill>@v<MAJOR>.<MINOR>.<PATCH>`.
2. Open a PR in [BuddhistAI/skills](https://github.com/BuddhistAI/skills) that copies the variant folder from that tag, following its `CONTRIBUTING.md`.

## Shared resources

Use glossaries, transliteration tables, and style guides from [`BuddhistAI/skills/shared`](https://github.com/BuddhistAI/skills/tree/main/shared). Do not keep a separate copy here. If a benchmark depends on a specific version, record the commit hash in the benchmark set's README.

## License

MIT. See [LICENSE](./LICENSE). Benchmark texts must be ones you are allowed to share under it; say where each text came from in its set's README.
