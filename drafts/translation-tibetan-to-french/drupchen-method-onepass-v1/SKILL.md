---
name: translation-tibetan-to-french
description: Translate Tibetan Buddhist texts and oral teachings into French in one pass, applying a list of Tibetan features not to copy, a French operations table and a fixed list of flags. Use when the user gives Tibetan (a transcript, a passage, a colophon) and asks for a French translation or draft.
metadata:
  task: translation
  language: tibetan
  language-code: bo
  target-language: french
  target-language-code: fr
  variant: drupchen-method-onepass-v1
  version: 0.1.0
  benchmark: translation/bo-fr (in preparation, not yet scored)
  authors: BuddhistAI, from the method of Drupchen (@drupchen)
  origin: "Drupchen, Two strategies for improving machine translation from Tibetan (2026) and Subtracting the Typological Baseline (2026), CC BY 4.0, https://buddhistai.github.io/knowledge-base/papers/"
  license: CC-BY-4.0
---

# Translate Tibetan into French in one pass, with the method's rules

This variant uses the rules from Drupchen's papers (see `metadata.origin`) in a single pass, with the Tibetan in view. It exists to measure what the separate meaning-unit stage of `drupchen-method-units-v1` adds.

Read `references/source-analysis-tibetan.md` and `references/french-operations.md` first.

## Steps

1. **Context sheet:** answer the five questions of `references/source-analysis-tibetan.md` §1 from the input. State any assumption.
2. **Sort the features** into the four bins (§2). Do not preserve typological defaults, and do not count their absence as loss.
3. **Translate** into French, applying `references/french-operations.md`. Name the target genre without reference to translation and write that. Keep who is speaking and with what authority. One rendering per term.
4. **Flag** every instance of the closed list (§4), whatever your confidence.

## Output format

```
## Traduction
<the French text>

## Signalements
1. <flag type>: <what you chose> — <the other reading>
```
