"""Shared helpers for build.py and check.py. Standard library only."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"


def load_languages():
    data = json.loads((ROOT / "languages.json").read_text(encoding="utf-8"))
    return {l["name"]: l for l in data["languages"]}


def parse_frontmatter(path):
    """Return (top-level fields, metadata fields) from a SKILL.md. Flat YAML only."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None
    block = m.group(1)
    top = {k: v.strip().strip('"') for k, v in re.findall(r"^(\w[\w-]*):[ \t]*(.*)$", block, re.M)}
    meta = {}
    mm = re.search(r"^metadata:[ \t]*\n((?:[ \t]+.*\n?)*)", block + "\n", re.M)
    if mm:
        for k, v in re.findall(r"^[ \t]+(\w[\w-]*):[ \t]*(.*?)[ \t]*(?:#.*)?$", mm.group(1), re.M):
            meta[k] = v.strip().strip('"')
    return top, meta


def split_name(name, languages):
    """Split a skill folder name into (task, source_language, target_language).

    toc-extraction-tibetan            -> (toc-extraction, tibetan, None)
    translation-tibetan-to-english    -> (translation, tibetan, english)
    ask-buddhistai                    -> (None, None, None)   language-neutral
    """
    by_len = sorted(languages, key=len, reverse=True)
    target = None
    rest = name
    for lang in by_len:
        if rest.endswith(f"-to-{lang}"):
            target = lang
            rest = rest[: -len(f"-to-{lang}")]
            break
    for lang in by_len:
        if rest.endswith(f"-{lang}") and len(rest) > len(lang) + 1:
            return rest[: -len(lang) - 1], lang, target
    if target:
        return None, None, "INVALID"
    return None, None, None


def collect_skills():
    languages = load_languages()
    skills = []
    for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
        name = skill_md.parent.name
        top, meta = parse_frontmatter(skill_md)
        task, lang, target = split_name(name, languages)
        skills.append({
            "name": name,
            "path": f"./skills/{name}",
            "top": top,
            "meta": meta,
            "task": task,
            "language": lang,
            "target": target,
        })
    return skills, languages
