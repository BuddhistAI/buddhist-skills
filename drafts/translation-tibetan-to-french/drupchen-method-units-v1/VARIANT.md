# drupchen-method-units-v1 (version 0.1.0)

- **Made by:** BuddhistAI (written by Claude for NT, 2026-11-18), from the method of Drupchen ([@drupchen](https://github.com/drupchen)): *Two strategies for improving machine translation from Tibetan* and *Subtracting the Typological Baseline* (2026, CC BY 4.0, [knowledge base Papers](https://buddhistai.github.io/knowledge-base/papers/README.html)). Drupchen did not write this skill; it is our reading of his papers. The reference files quote and summarise them with credit.
- **What is different:** two stages. The French is written from a list of meaning units, with the Tibetan not in view (the papers' "sealed composition", which they say carries most of the gain). Fixed list of flags; audit by meaning units only.
- **Compared with:** `drupchen-method-onepass-v1` (same rules, one pass, Tibetan in view) and plain Claude with no skill. This comparison measures what the meaning-unit stage adds.
- **Tested with:** not yet. Benchmark `translation/bo-fr` is in preparation (Tibetan colophons, meaning-unit scorer).
- **Not included yet:** correction examples (source, AI draft, correction). The papers say they are the highest-leverage item. They must come from real corrections; a later variant will add them.
