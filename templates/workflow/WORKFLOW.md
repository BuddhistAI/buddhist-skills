---
name: translation-workflow-tibetan
description: One sentence on the end result, e.g. "From a raw OCR'd Tibetan text to a reviewed English draft aligned to the source."
metadata:
  type: workflow
  language: tibetan
  language-code: bo
  version: 0.1.0
---

<!--
A workflow is a sequence of steps. A step can be a BuddhistAI skill (name it, with the
version you used), another tool, or a person's check. Delete these comments when done.
-->

# From raw Tibetan text to a reviewed English draft

## Steps

| # | Step | Done with | Output |
| --- | --- | --- | --- |
| 1 | Clean up OCR errors | `text-cleanup-tibetan` 1.0.0, or your own prompt | Clean text |
| 2 | Split into segments | ... | Segments |
| 3 | Draft translation | ... | Draft |
| 4 | Review by a translator | a person | Reviewed draft |

## Hand-offs

What each step passes to the next (file format, naming), and what to check before moving on.

## What it costs

Rough time and model cost for, say, 100 pages, if you know it.

## Example

A short before and after.
