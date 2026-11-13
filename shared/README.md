# Shared resources

One copy of each resource that more than one skill uses. Skills and benchmarks refer to these files by path in this repo instead of keeping their own copies.

| Folder | What goes there | Format |
| --- | --- | --- |
| [`glossaries/`](./glossaries/README.md) | Term lists: source term, preferred rendering, alternatives, notes | TSV, one file per language pair |
| [`transliteration/`](./transliteration/README.md) | Romanization schemes and conversion tables (Wylie, EWTS, THL, IAST, ...) | TSV or Markdown |
| [`style-guides/`](./style-guides/README.md) | House style for translations and editions: capitalization, honorifics, citations | Markdown |

Changes here affect every skill, so each change gets a `CHANGELOG.md` entry. If a change would alter benchmark scores, note it on the affected leaderboards in buddhist-benchmarks.

Where an organization prefers a different rendering, add it as an alternative with the organization named in the notes, rather than replacing the existing entry.
