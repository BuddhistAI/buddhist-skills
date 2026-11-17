---
title: Two strategies for improving machine translation from Tibetan
kind: workflow
task: translation
language: tibetan
target-language: french
authors: Drupchen
contact: "@drupchen"
github: drupchen
license: CC-BY-4.0
version: 1.0.0
shared: 2026-11-17
---

# Two strategies for improving machine translation from Tibetan

**What it does:** a method for getting much better drafts from Claude (or another AI) when you translate spoken Tibetan teachings into French. It tells you what to put in the prompt, how to split the drafting into steps, which Tibetan features *not* to copy into the French, and which places the AI must always mark for a human check.

**Who it is for:** translators who already use an AI for transcription or first drafts, and people who want to build a Tibetan translation benchmark.

## How to use it

The full guide is in [WORKFLOW.md](./WORKFLOW.md). The author's PDF is kept as the source. In short:

1. **Answer five context questions first** (§1): pivot language, reader and register, how the source was delivered, target format, and who decides terminology. Put the answers in your standing instruction (for example a Claude project file).
2. **Draft in four steps** (§2): analyse the source; list the meaning units in French; **write the French in a separate turn or chat where the Tibetan is not visible**; then check that every meaning unit is present.
3. **Paste the "What not to preserve" paragraph** (§3) into your standing instruction, word for word.
4. **Add 5 to 10 correction triples** (§6.1): source segment, AI draft, your correction. The author says these help more than any list of rules. Use only pairs where the transcription did not change between the draft and the correction.
5. **Give the AI a closed list of things to flag** (§5.1), instead of "flag what you are unsure of". Use one rendering per term per file, and keep transliteration rules in the glossary.
6. **Ask for countable checks, not a critique** (§7). The AI is reliable for term consistency, repetition and missing meaning units. It is not reliable for "does this sound natural".

The transposition table (§4) lists, for each Tibetan device, the French operation to use and the common wrong one.

## Example

The guide has short worked examples, for example a flag for a particle whose reading changes the meaning (§5.1):

> དགྲ་འདིའི་བུ་ — read as genitive, "a child of this enemy"; if agentive, "this enemy, born as a child", which reverses which party is the parent.

## Limits

- The target-side rules (the transposition table) are written for **French**. For Spanish, Italian or Portuguese they are hypotheses, not results (§11). The source-side rules (how to read the Tibetan) work for any target language.
- The guide is based on spoken teaching in one genre. It has not been measured on a benchmark yet. Its §9 describes how such a benchmark could be built (meaning-unit coverage, countable checks, colophons as a first test set).
- The Markdown was converted from the author's PDF. The Tibetan was checked against the PDF text by script. If anything looks wrong, the PDF is the reference.

## Credits and sources

- Written by Drupchen ([@drupchen](https://github.com/drupchen)), 2026-11-17. License: CC BY 4.0. See [SOURCE.md](./SOURCE.md).
- Companion paper by the same author, with the evidence behind this guide: [Subtracting the Typological Baseline](https://buddhistai.github.io/knowledge-base/papers/subtracting-the-typological-baseline/) in the knowledge base.
