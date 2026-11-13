# Scoring

Scripts that compare a variant's outputs with the references and write a score file.

Each script should:

- take `--outputs <dir>` and `--references <dir>`,
- write `scores.json` with one score per item plus the overall score,
- be deterministic, so anyone can reproduce a leaderboard row.

Where automatic metrics are not enough (for example translation quality), document the human review rubric here and record reviewer scores in the same `scores.json` format.
