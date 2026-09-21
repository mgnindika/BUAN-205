# BUAN B205, Module 4: Data Visualization

- `index.html`: student lecture notes (no answers)
- `instructor.html`: instructor copy, same notes with 52 answer-key boxes. Published
  on GitHub Pages at the owner's decision, so it is **publicly readable by anyone with
  the URL**. Unlinked and `noindex`, but not private. Students use `index.html`.
- `module4-notebook/`: the reactive marimo notebook (Pyodide/WebAssembly, runs in the browser)
- `module4_notebook.py`: notebook source. To edit: `pip install marimo`, then `marimo edit module4_notebook.py`
- `SuperMarket_Analysis.xlsx`: practice lab and Data Viz Challenge dataset

Rebuild the notebook after edits:

    marimo export html-wasm module4_notebook.py -o module4-notebook --mode run -f
