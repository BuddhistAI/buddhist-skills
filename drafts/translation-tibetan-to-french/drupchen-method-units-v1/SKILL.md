---
name: translation-tibetan-to-french
description: Translate Tibetan Buddhist texts and oral teachings into French in two separate stages, first a flat list of meaning units from the Tibetan, then French written from that list without the Tibetan in view, with a fixed list of flags. Use when the user gives Tibetan (a transcript, a passage, a colophon) and asks for a French translation or draft.
metadata:
  task: translation
  language: tibetan
  language-code: bo
  target-language: french
  target-language-code: fr
  variant: drupchen-method-units-v1
  version: 0.1.0
  benchmark: translation/bo-fr (in preparation, not yet scored)
  authors: BuddhistAI, from the method of Drupchen (@drupchen)
  origin: "Drupchen, Two strategies for improving machine translation from Tibetan (2026) and Subtracting the Typological Baseline (2026), CC BY 4.0, https://buddhistai.github.io/knowledge-base/papers/"
  license: CC-BY-4.0
---

# Translate Tibetan into French: meaning units first, then French

This method comes from Drupchen's two papers (see `metadata.origin`). Its main idea: much of what a Tibetan passage looks like is the Tibetan language, not the author. Copy it into French and the French becomes worse, not more faithful. So first find what the passage **says**, then write French from that, **without the Tibetan in view**.

Read `references/source-analysis-tibetan.md` before stage 1 and `references/french-operations.md` before stage 2.

## Stage 0: context sheet

Answer the five context questions in `references/source-analysis-tibetan.md` §1 (pivot, reader and register, how the source was delivered, target format, who decides terms). Use what the user or the input gives you. If an answer is missing and changes the work (above all delivery and format), ask once. Otherwise state your assumption.

## Stage 1: read the Tibetan (source visible)

1. Segment the passage into periods. List the connectives (ནས་, སྟེ་/ཏེ་, ན་, པར་/བར་ ...) and the one finite verb of each period.
2. Sort every feature into the four bins of `references/source-analysis-tibetan.md` §2. Write down, for example: "the recitation is a temporal frame; the three descriptors are co-ranked recognition criteria". Without this step you will invent devices to preserve.
3. Write the **meaning units**: a flat numbered list in plain French, with no Tibetan syntax, each with its channel (`text`, `outside`, `absent`). For a colophon, also name each unit's slot (request, requester, place, date, author's epithet, aspiration, verb).
4. Write the **flags** from the closed list (§4). Every instance, whatever your confidence.

## Stage 2: write the French (source not visible)

Write the French **only from the stage 1 output and the context sheet**. The Tibetan word order must not be in view, or it becomes the template.

- **With subagents** (for example Claude Code's Agent tool): give a new subagent only the context sheet, the meaning units, the flags and `references/french-operations.md`, and ask it for the French. Do not pass the Tibetan.
- **Without subagents:** start the French in a new turn, after telling the user you are now working from the list only, and do not quote or reread the Tibetan.

Rules for the French:

- Name the target genre without reference to translation (for example "explanatory prose of a respected teacher, formal but spoken"). Write that, not "French translated from Tibetan".
- Apply the operations in `references/french-operations.md`. Keep who is speaking and with what authority: nested French with one or two oral markers, not flat juxtaposition.
- Use the correction examples, if the user has given any (source, AI draft, correction). They help more than any rule.
- One rendering per term per file. No alternatives inline.

## Stage 3: audit (both texts visible)

Check **only** that each meaning unit is present: delivered, shifted, thinned or absent. A unit can be anywhere in the sentence. Before you record an absence, say what the French construction at that point is doing in French; record a loss only if you cannot. Do not judge whether the French "sounds natural": the method says a model is not reliable there. Fix real losses in the French, then stop.

## Output format

```
## Traduction
<the French text>

## Signalements
1. <flag type>: <what you chose> — <the other reading>
...

## Unités de sens
u1 [slot; channel] <unit> — delivered
...
```

If the user asks only for the French, give the first section and keep the flags short.

## Example

Input (a synthetic colophon, for format only):

```
ཅེས་པ་འདི་ནི་དགེ་སློང་བློ་བཟང་གིས་ཡང་ཡང་བསྐུལ་བའི་ངོར། བཙུན་གཟུགས་ངག་དབང་གིས་དཔལ་ཆོས་སྡེར་སྦྱར་བ་དགེ་ལེགས་འཕེལ།
```

Stage 1 units: u1 [closing; outside] fin du texte · u2 [request; text] à la demande du moine Lobsang · u3 [request; text] demandé à plusieurs reprises · u4 [epithet; text] l'auteur se dit simple apparence de moine · u5 [verb; text] Ngawang l'a composé · u6 [place; text] à Pal Chöde · u7 [aspiration; text] que croissent vertu et bien.

Stage 2 French: *Ce texte a été composé à Pal Chöde par Ngawang, qui n'a du moine que l'apparence, à la demande instante du moine Lobsang. Que vertu et bien s'accroissent !*

(The main verb comes first; the slots follow French order; the epithet stays a phrase; no *ainsi* or *donc* is added.)
