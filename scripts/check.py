#!/usr/bin/env python3
"""Check that promoted skills are listed everywhere and carry promotion metadata.

Run from the repo root: python3 scripts/check.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NOT_SHIPPED = {"in-progress", "deprecated"}
NO_METADATA_NEEDED = {"router"}
REQUIRED_METADATA = ["source", "variant", "version", "benchmark", "score", "promoted"]

errors = []


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
        return {}, ""
    block = m.group(1)
    top = dict(re.findall(r"^(\w[\w-]*):\s*(.*)$", block, re.M))
    meta = {}
    mm = re.search(r"^metadata:\s*\n((?:[ \t]+.*\n?)*)", block + "\n", re.M)
    if mm:
        meta = dict(re.findall(r"^[ \t]+(\w[\w-]*):\s*(.*?)\s*(?:#.*)?$", mm.group(1), re.M))
    return top, meta


plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
listed = {p.removeprefix("./").rstrip("/") for p in plugin.get("skills", [])}
readme = (ROOT / "README.md").read_text(encoding="utf-8")

shipped = set()
for skill_md in sorted(SKILLS.glob("*/*/SKILL.md")):
    folder = skill_md.parent
    bucket = folder.parent.name
    rel = folder.relative_to(ROOT).as_posix()
    top, meta = frontmatter(skill_md)
    if top.get("name") != folder.name:
        errors.append(f"{rel}: frontmatter name {top.get('name')!r} does not match folder name")
    if not top.get("description"):
        errors.append(f"{rel}: missing description")
    if bucket in NOT_SHIPPED:
        if rel in listed:
            errors.append(f"{rel}: {bucket} skills must not be in plugin.json")
        continue
    shipped.add(rel)
    if rel not in listed:
        errors.append(f"{rel}: not listed in .claude-plugin/plugin.json")
    if f"./{rel}/SKILL.md" not in readme:
        errors.append(f"{rel}: not linked from README.md")
    bucket_readme = folder.parent / "README.md"
    if not bucket_readme.exists() or f"./{folder.name}/SKILL.md" not in bucket_readme.read_text(encoding="utf-8"):
        errors.append(f"{rel}: not linked from {bucket}/README.md")
    if bucket not in NO_METADATA_NEEDED:
        missing = [k for k in REQUIRED_METADATA if not meta.get(k)]
        if missing:
            errors.append(f"{rel}: metadata missing {', '.join(missing)}")

for rel in sorted(listed - shipped):
    errors.append(f"plugin.json lists {rel}, which is not a shipped skill")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(shipped)} shipped skill(s)")
