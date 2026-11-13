# webuddhist-gepa-v1 (version 1.0.0)

- **Made by:** WeBuddhist (NT), 2026-11-02, with DSPy GEPA (task model Claude Haiku 4.5, reflection model Sonnet 4.5), from a one-paragraph seed prompt. Lab copy: [toc-extraction-tibetan `variants/gepa-v1`](https://github.com/BuddhistAI/toc-extraction-tibetan/tree/main/variants/gepa-v1).
- **Different from the promoted skill:** a self-contained prompt of numbered rules learned from benchmark feedback, instead of the sabcad-outliner method. Shorter, and it does not need the reference files.
- **Tested with:** Claude Haiku 5.5 and Sonnet 5.5 on `toc-extraction/bo@1.0.0`, 3 runs each: structure_f1 0.824 and 0.949. That is a near-tie with the promoted skill (0.823 and 0.962). It is better on the held-out book and on the per-passage score. Re-run it after the benchmark's held-out references are fixed (1.0.1).
