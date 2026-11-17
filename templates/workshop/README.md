# <task>-<language>

<!-- Template for a workshop repo (one per skill): copy this folder into a new repo named after the skill,
     for example translation-tibetan-to-english. Delete these comments when you are done. -->

The workshop for the BuddhistAI skill `<task>-<language>`: every variant we tried, the runs, the provenance records and the ranking report. It does not hold the test data: that is in [buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks), pinned in `benchmark/benchmark.json`.

## Layout

```
benchmark/
  benchmark.json      the buddhist-benchmarks release used (repo, tag, path), never a copy of the data
  <run script>        runs a variant on the benchmark; saves the exact command and library versions per run
variants/<name>/      SKILL.md (with metadata.version) + VARIANT.md (who made it, what is different)
results/              one output file + log (+ meta) per model and run
provenance/           one provenance record per leaderboard row: provenance/<run-id>.json
scripts/              summarize, to_result_json (leaderboard rows), provenance (records)
REPORT.md             the ranking and what we learned
```

## Provenance

Every leaderboard row has a record in [`provenance/`](./provenance/) in the standard format [buddhistai/provenance@1](https://buddhistai.github.io/knowledge-base/handbook/provenance.html): skill files with hashes, model and settings, prompt, benchmark tag and data hash, harness, libraries, command, run files and logs with hashes, tokens, cost and scores. buddhist-benchmarks keeps only the short `result.json`. Working example: [toc-extraction-tibetan](https://github.com/BuddhistAI/toc-extraction-tibetan/tree/main/provenance) (its `scripts/provenance.py` can be adapted).

## Run it

```bash
python benchmark/<run script> --model <model> --variant variants/<name> --out results/<date>-<model>-run1.json
python scripts/to_result_json.py ... --benchmarks ../buddhist-benchmarks
python scripts/provenance.py --benchmarks ../buddhist-benchmarks && python scripts/provenance.py --check
```

Run each variant at least 3 times. Never tune on the test set.

## License

MIT, unless a variant says otherwise.
