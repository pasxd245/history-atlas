# history-atlas — English documentation

Repository entry point: [`../../README.md`](../../README.md). Full documentation in Vietnamese:
[`../vi/README.md`](../vi/README.md).

**Everything a reader actually sees — all 188,000 words of it — is in Vietnamese.** This file
explains what the project is and how it works, for someone who does not read Vietnamese. It is
not a translation of the atlas, and there is no plan to make one: translating the content would
mean redoing the review work in another language, and a machine translation would inherit the
"it has been reviewed" claim without having been.

Before anything else, read the disclaimer in [`../../README.md`](../../README.md): **this is an
AI writing experiment, not historical scholarship.** Do not use it in place of historical
research, do not cite it as evidence, do not treat it as a reference work.

## What the project does

It maps people who shaped human thought from 2000 BCE to 2026, one structured entry each, and
draws the lines of transmission between them.

- **11 chapters**, split into **33 groups** by period (a century, or a wider band for sparse eras).
- **At most 12 people per group** — a hard limit enforced by the linter, not a guideline. It is
  the single most consequential constraint in the project: it forces deserving people out of
  every chapter, and each chapter's editorial note names who was cut and why.
- **377 people** in the main track, plus a **40-person Vietnam appendix** on a separate track,
  excluded from every global statistic because it uses a Vietnamese frame of reference rather
  than a human one.

Each entry carries: years, place, region, fields, date-confidence, a Wikidata Q-ID, a "big
question" tag, roughly 100 words on the contribution, roughly 80 words arguing why this person
and not the alternatives, up to three inherited-from links, up to three influenced links, and
1–2 sources.

## How an entry is selected

Four published criteria, applied explicitly in every entry's "why this person" paragraph:

| | |
|---|---|
| **(a) reach** | how far the contribution travelled |
| **(b) durability** | whether it held up over time |
| **(c) originality** | whether it was genuinely theirs |
| **(d) counterfactual** | what would be different had they not existed |

These are **not moral criteria**, and the project says so where it matters. Mao Zedong is in the
atlas on (a) and (d); the chapter 10 editorial note works through the fact that the same reading
would admit Lenin, Stalin and Hitler, and argues their exclusion on (b). "Influential" does not
mean "admirable."

Selection is editorial judgement, not an objective ranking.

## How it is built

```
content/chXX.md          Markdown written by a language model against prompts/atlas-prompt.md
        │
        ├── parse        atlaslib/parse.py — strict template, no free-form sections
        ├── lint         atlaslib/lint.py  — structure errors block the build; soft issues warn
        ├── Wikidata     names, birth/death years, identity, image links cross-checked (CC0)
        └── render       atlaslib/render.py — static HTML, no framework, no CDN
```

- **Errors stop the build.** Warnings do not: a warning usually marks a deliberate decision, and
  the reason is written into the chapter's editorial note rather than silenced in code.
- **Date tolerance scales with declared confidence** — 5 years for `Cao` (high), 25 for
  `Trung bình` (medium), unbounded for `Thấp` (low). A mismatch past tolerance warns.
- **Matching Wikidata does not mean being right.** Several entries deliberately diverge from
  Wikidata where a better source disagrees — Mulla Sadra's death year follows the *Stanford
  Encyclopedia of Philosophy* rather than Wikidata's traditional date — and each divergence is
  documented so nobody "fixes" it back.
- **Images** are fetched from Wikimedia Commons by `fetch_images.py` under a hard licence policy,
  downloaded rather than hotlinked, and listed individually in `credits.html`. 355 are embedded;
  11 are deliberately omitted with a recorded reason, which `credits.html` lists separately from
  the 45 that simply have no image available.

Tests: `uv run --frozen --group dev pytest`. Several of them exist specifically to stop known
failure modes from recurring — duplicated dark-theme CSS blocks drifting apart, `uv.lock` falling
out of step with `pyproject.toml`, deliberately-skipped images being folded back in with missing
ones.

## Limits worth knowing

- **The prose is model-written.** No historian wrote or reviewed any of it. It is synthesis, not
  primary research.
- **1–2 sources per entry, and their contents were not checked sentence by sentence.** A source
  listed next to a sentence does not mean that source backs that sentence.
- **One entry carries exactly one Q-ID**, which breaks down for modern collaborative science:
  four of the twelve 21st-century entries had to drop a co-discoverer (Charpentier, Weissman,
  Jumper, Perlmutter/Riess) for a reason that is not one of the four criteria.
- **Coverage is uneven.** `Trung Á` (Central Asia) has 8 of 377 entries and none after 1900;
  `Châu Đại Dương` (Oceania) has 2. Chapter 1 is 79% Middle East / North Africa — possibly a real
  gap in the surviving record, but the chapter does not yet say so.
- **334 lines across 44 of the 91 review reports are marked `[KHÔNG KIỂM ĐƯỢC]`** — "could not verify."
  That marker means not yet checked, not "probably wrong"; most need printed sources.

`KNOWN-ISSUES.md` (Vietnamese) is the single backlog for everything still open, with pointers
into the review reports that found each item. `reviews/` holds all 91 reports.

## Repository layout

```
index.html · overview.html · credits.html   generated site; open with file:// or serve statically
chapters/chXX.html                          generated, one file per chapter
content/chXX.md                             the source prose; content/images.yaml overrides images
atlaslib/                                   common · parse · lint · render
build.py · fetch_images.py                  the pipeline
data/                                       persons.json · images.json · wikidata-cache.json
assets/                                     style.css · app.js · theme.js · vendored d3 + mermaid · img/
reviews/                                    91 independent review reports — the audit trail
prompts/atlas-prompt.md                     the fixed prompt the prose is written against
```

Citations of the form `PLAN §…` across the documentation refer to an internal design document
that is not published in this repository. It records why the thresholds and conventions are what
they are. You do not need it to build or read the atlas.
