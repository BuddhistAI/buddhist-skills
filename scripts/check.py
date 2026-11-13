#!/usr/bin/env python3
"""Validate skills/ and make sure generated files are current.

python3 scripts/check.py            # local checks only
python3 scripts/check.py --tasks    # also check metadata.task against buddhist-benchmarks
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skills_lib import ROOT, collect_skills  # noqa: E402
from build import build  # noqa: E402

TASKS_URL = "https://raw.githubusercontent.com/BuddhistAI/buddhist-benchmarks/main/tasks/index.json"
LANGUAGE_META = ["task", "language", "language-code", "benchmark", "score", "version", "source", "promoted"]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

errors, warnings = [], []
skills, languages = collect_skills()

for s in skills:
    where = f"skills/{s['name']}"
    top, meta = s["top"], s["meta"]
    if top is None:
        errors.append(f"{where}: SKILL.md has no frontmatter")
        continue
    if not NAME_RE.match(s["name"]):
        errors.append(f"{where}: folder name must be lowercase kebab-case")
    if top.get("name") != s["name"]:
        errors.append(f"{where}: frontmatter name {top.get('name')!r} must equal folder name")
    if not top.get("description"):
        errors.append(f"{where}: missing description")
    if s["target"] == "INVALID":
        errors.append(f"{where}: '-to-<language>' needs a source language before it, e.g. translation-tibetan-to-english")
        continue
    if s["language"] is None:
        continue
    missing = [k for k in LANGUAGE_META if not meta.get(k)]
    if missing:
        errors.append(f"{where}: metadata missing {', '.join(missing)}")
    if meta.get("language") and meta["language"] != s["language"]:
        errors.append(f"{where}: metadata.language {meta['language']!r} does not match folder suffix {s['language']!r}")
    code = languages[s["language"]]["code"]
    if meta.get("language-code") and meta["language-code"] != code:
        errors.append(f"{where}: metadata.language-code should be {code!r} (see languages.json)")
    if meta.get("task") and meta["task"] != s["task"]:
        errors.append(f"{where}: metadata.task {meta['task']!r} does not match folder name task {s['task']!r}")
    if s["target"] and meta.get("target-language") != s["target"]:
        errors.append(f"{where}: metadata.target-language must be {s['target']!r}")

for path in sorted(ROOT.glob("skills/*")):
    if path.is_dir() and not (path / "SKILL.md").exists():
        errors.append(f"skills/{path.name}: folder has no SKILL.md")

marketplace, catalog = build()
if (ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8") != marketplace:
    errors.append(".claude-plugin/marketplace.json is out of date: run python3 scripts/build.py")
if (ROOT / "SKILLS.md").read_text(encoding="utf-8") != catalog:
    errors.append("SKILLS.md is out of date: run python3 scripts/build.py")

if "--tasks" in sys.argv:
    try:
        with urllib.request.urlopen(TASKS_URL, timeout=20) as r:
            known = {t["id"] for t in json.load(r)["tasks"]}
        for s in skills:
            if s["task"] and s["task"] not in known:
                errors.append(f"skills/{s['name']}: task {s['task']!r} is not defined in buddhist-benchmarks tasks/index.json")
    except Exception as e:  # network or repo not ready yet
        warnings.append(f"could not fetch task list ({e}); task IDs not checked")

for w in warnings:
    print(f"warning: {w}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(skills)} skill(s)")
