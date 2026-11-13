# Workflows: skills that chain other skills (planned)

Status: **planned, not built.** Implement this when the first workflow skill exists. Tracking issue: [#2](https://github.com/BuddhistAI/buddhist-skills/issues/2).

A translator rarely wants one step. They want a pipeline, for example cleanup → segmentation → translation → review. This page records how such pipelines will be packaged and ranked, so the first one fits without redesign.

## A workflow is a skill

- It lives in `skills/` like any skill, named `<goal>-workflow-<language>`, e.g. `translation-workflow-tibetan`, and is still one language only.
- Its frontmatter marks it as a workflow (`metadata.type: workflow`) and lists the stage skills it calls, each at a pinned version:

  ```yaml
  metadata:
    type: workflow
    version: 1.0.0
    stages:
      - text-cleanup-tibetan@1.2.0
      - segmentation-tibetan@1.0.0
      - translation-tibetan-to-english@2.1.0
      - translation-review-tibetan-to-english@1.0.0
  ```

- It ships in the same language plugin as its stages, so installing the plugin gives a translator the workflow and every stage it needs. `scripts/check.py` will fail if a pinned stage is missing or at another version.
- Promoting a new stage version does not change a workflow: the workflow gets a new version that pins it, and is re-run.

## Two levels of leaderboard

1. **Stage leaderboards** (what exists now): one per task and language, such as TOC extraction or alignment. Each ranks single skills on that task's benchmark.
2. **Workflow leaderboards**: one per workflow goal and language, with its own **end-to-end benchmark** in buddhist-benchmarks. The input is the raw material (e.g. an unedited Tibetan text) and the target is the finished product (e.g. a reviewed translation aligned to the source). Each row is one workflow version on one model (or a model per stage), and shows:
   - the end-to-end score;
   - **total cost** (sum over stages, per 100 pages, as on stage leaderboards) and **total time**;
   - links to every component skill at the tested version;
   - optionally each stage's own score on that run, to show where points are lost.

## Why both levels

- The best skill at each stage does not guarantee the best workflow: errors compound, and some stages matter more than others. A cheaper, slightly worse cleanup can be fine if segmentation absorbs its mistakes; a small segmentation error can ruin alignment.
- The end-to-end score is what a translator cares about. Stage scores diagnose *where* a workflow loses points, so contributors know which skill to improve next.

## To do when the first workflow exists

- buddhist-skills: `metadata.type` and `metadata.stages` in the frontmatter schema; check that pinned stages exist; list workflows separately in `SKILLS.md`; teach `ask-buddhistai` to route to them.
- buddhist-benchmarks: a workflow entry in `tasks/index.json` (or a sibling `workflows/` folder) with an end-to-end data set in the standard format (`test.jsonl` + dataset card), a scorer, and `result.json` rows that add per-stage `usage` and wall-clock time.
- Site: a workflow card on the overview, with best overall and best value picks like the stage cards, and a stage breakdown on its page.
