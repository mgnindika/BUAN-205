# BUAN B205 — Business Analytics with AI

Course site: **https://mgnindika.github.io/BUAN-205/**

| | |
|---|---|
| [`index.html`](index.html) | Landing page students open first |
| [`Introduction_BUAN_with_AI.html`](Introduction_BUAN_with_AI.html) | Introduction module |
| [`module4/`](module4/) | Module 4: Data Visualization |

## Module 4

- `module4/index.html` — student lecture notes (no answers)
- `module4/module4-notebook/` — reactive marimo notebook, exported to WebAssembly.
  Pandas, NumPy and matplotlib run in the student's browser through Pyodide; no server, no install.
- `module4/module4_notebook.py` — notebook source
- `module4/SuperMarket_Analysis.xlsx` — practice lab and Data Viz Challenge dataset

Rebuild the notebook after editing the source:

```
pip install marimo
marimo edit module4/module4_notebook.py
marimo export html-wasm module4/module4_notebook.py -o module4/module4-notebook --mode run -f
```

Use `--mode edit` instead of `--mode run` to give students a version they can change and re-run.

## Publishing

GitHub Pages serves the `main` branch root. `.nojekyll` at the repo root keeps Jekyll
from rewriting the notebook bundle.

The instructor copy (`module4/instructor.html`, with answers) is published too, at the
owner's decision. GitHub Pages has no access control, so **it is publicly readable by
anyone with the URL, including students.** It carries `noindex, nofollow` to keep it out
of search results and is linked from no page, so it is reachable only by typing the
address — but that is obscurity, not protection. Students use `module4/index.html`, which
contains no answers.
