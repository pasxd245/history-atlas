# history-atlas — an atlas of influential people (2000 BCE – 2026)

**The content of this project is written in Vietnamese.** This file is the English entry point.
Full documentation: **[English](docs/en/README.md)** · **[Tiếng Việt](docs/vi/README.md)**

> ## Read this first: an AI writing experiment, not historical scholarship
>
> This project asks a question about **AI**, not a question about **history**: under tight
> constraints — word caps, a closed vocabulary, published selection criteria, automated
> linting and one review pass — how far can a language model write, and where does it break?
> Intellectual history here is the **material being tested**, not a vouched-for product.
>
> **The discipline of history has a method, and that method is what makes it worth trusting.**
> Reading primary sources in their own language. Interrogating them: who wrote this, for whom,
> what is hidden, who benefits. Knowing where a claim stands among competing readings. Then
> putting your name under a conclusion and defending it before colleagues in the field. That is
> the work of years, often of a lifetime, and it is the reason a statement about the past can be
> believed. **This atlas does none of it.**
>
> That is not polite modesty — it is what the project itself measured. The review pass found
> exactly the errors that only reading the primary text can catch: the Locke entry had
> *Two Treatises* refuting Hobbes, when Book I names Sir Robert Filmer outright and never names
> Hobbes at all; the Sor Juana entry named the wrong bishop of Puebla, one who had died more
> than thirty years before the *Respuesta*. And 334 lines still carry the marker
> `[KHÔNG KIỂM ĐƯỢC]` ("could not verify") across 44 of 91 review reports — claims that can only
> be settled by printed books and someone able to read them. **Every one of those errors is one
> more demonstration of why that method exists.**
>
> So the three points below are not legal cover. They are where the project knows it stands:
>
> - **Do not use it in place of historical research.** It cannot replace it, and does not aim to.
> - **Do not cite it as evidence** — in coursework, an article, a piece of writing, or an argument.
> - **Do not treat it as a reference work.** The *Nguồn* ("Sources") section of each entry is a
>   place to go on from, not a place to stop. Read the people who gave their lives to writing them.
>
> What it is good for: a starting point and an excuse to be curious, which then pushes you toward
> the real sources. And, for people working on AI, a specimen showing how a model writing under
> constraint fails — every failure found is recorded in the open, in `reviews/` and
> `KNOWN-ISSUES.md`, with nothing scrubbed.
>
> If you work in history and you find something wrong here: that error belongs to this project,
> not to your field. Report it and the project improves — and the way it acknowledges that is by
> fixing it publicly and leaving the correction visible, not quietly deleting it.
>
> This describes the current version. If real experts ever review it, this section has to be rewritten.

## What it is

A static website mapping people who shaped human thought, from 2000 BCE to 2026. Prose is written
by a language model into Markdown against a fixed template; `build.py` lints it, cross-checks
names and dates against Wikidata, and generates HTML. Images come from Wikimedia Commons under a
hard-coded licence policy. No Node, no server, no CDN — open `index.html` with `file://` if you like.

**v0.0.1** — 11 of 11 chapters · 33 of 33 groups · 377 people in the main track, plus 40 in a
Vietnam appendix. 355 embedded images. Build: 0 errors.

> **First release, not a finished one.** Every chapter has had at least one independent review
> pass (by an AI agent, not a specialist). What remains open is listed in `KNOWN-ISSUES.md`.

## Quick start

```bash
uv sync --extra images
uv run --frozen python build.py --offline   # lint + generate HTML, no network
python -m http.server 8099                  # then open http://localhost:8099
```

`build.py` without `--offline` also cross-checks Wikidata. `uv run --frozen --group dev pytest` runs the tests.

## Documentation

| | |
|---|---|
| **[docs/en/README.md](docs/en/README.md)** | English — what the project is, how it is built, its limits |
| **[docs/vi/README.md](docs/vi/README.md)** | Tiếng Việt — full documentation: structure, workflow, lint, images, remaining work |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Vietnamese. Rules that must be followed before writing an entry |
| [KNOWN-ISSUES.md](KNOWN-ISSUES.md) | Vietnamese. Every known open issue, with pointers into `reviews/` |
| [reviews/](reviews/) | Vietnamese. 91 independent review reports — the project's audit trail |

`CONTRIBUTING.md` and `KNOWN-ISSUES.md` stay at the repository root on purpose: GitHub gives
`CONTRIBUTING.md` special treatment there, the generated site links `KNOWN-ISSUES.md` as a
sibling file, and 51 files — including published chapter prose — already reference them by path.

## Licence

Three kinds of material, three licences:

| Part | Licence | File |
|---|---|---|
| **Code** — `build.py`, `fetch_images.py`, `atlaslib/`, `tests/`, configuration | MIT | [`LICENSE`](LICENSE) |
| **Content** — `content/`, `reviews/`, `prompts/`, `.md` files, prose in the HTML | CC BY-SA 4.0 | [`LICENSE-CONTENT`](LICENSE-CONTENT) |
| **Images** — `assets/img/` | each keeps its own Commons licence (Public domain / CC0 / CC BY / CC BY-SA) | listed per image in `credits.html` |

Third-party libraries in `assets/` (`LICENSE-mermaid.txt` MIT, `LICENSE-d3.txt` ISC) and Wikidata
data (CC0) keep their own terms. The licence grants you reuse; it does **not** warrant that the
content is correct.
