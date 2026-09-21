import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium", app_title="Module 4: Data Visualization, Reactive Notebook")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import io, gzip, base64

    # One look for every chart in this notebook
    NAVY, MAROON, GOLD, GRAY, SOFT = "#0b2545", "#7B1E2E", "#C8922A", "#B9B3AD", "#57504C"
    mpl.rcParams.update({
        "figure.figsize": (8, 3.8), "figure.dpi": 110,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.edgecolor": "#999999", "axes.titleweight": "bold", "axes.titlesize": 12,
        "axes.titlelocation": "left", "font.size": 10,
    })
    return GOLD, GRAY, MAROON, NAVY, SOFT, base64, gzip, io, mo, np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Data visualization, the reactive way
    **BUAN B205, Module 4.** Nuwan Indika, Ph.D., College of Business, Loyola University New Orleans

    This is a **reactive notebook** built with [marimo](https://marimo.io). Move any slider, menu, or switch, and every chart and number that depends on it recomputes on its own. You never press "run."

    Everything here is real Python (pandas, NumPy, matplotlib). It runs inside your browser tab through **WebAssembly**, using **Pyodide**, which is Python compiled to run in a web page. There is no server and no install, and nothing you do here is sent anywhere. The first load takes a few seconds while Python starts up.

    **How to use it in class:** read the short idea, play with the controls, and answer the *Notice* question. Then copy the *Ask AI* prompt into Claude and push further. At the end, you'll ask Claude to help you **build your own reactive demo**.
    """)
    return


@app.cell(hide_code=True)
def _(base64, gzip, io, pd):
    # Supermarket sales: 1,000 purchases, 3 branches, Jan 1 - Mar 30, 2019.
    # The CSV is packed (gzip + base64) inside the notebook so it works offline in the browser.
    _BLOB = "H4sIADWesWoC/619ydIkR3LenU8xD/CzLPalb9KIy6Vp1HbQsYlpkTDDAGONHlLQ08s/j6xK98itPCHjgW1jhqz8IyM8fPmW//zty88//NvHH3/8/tvHH//66/df/vz12x++//aXrx//8PXnP3399vHP3375019/+P6Hn378+evH//z5x+9/+Mu3H3/4+vFf//rl5+/4r/77l5++/vrxX758//rxP37889ePf/7y25+//vz94799+f7jz//6N//pp6//5+N/ffn5X3/5+ePz1z//Cz3y77/+mf6bj3/8+uWn7//2hy8//+kP//L1y1/pUTU9Sv+oHzm1R68+fwTn+986/7cuf/j4ybWPv/uPLz/99PX7R3/4v/mHH//vl49/+vLbX3778fuX//j4p1++0WOfD/+7n77+8P3bLz//+MMfvvzww9dff/3l24/0mj4/QvvIH809QlgeH/+WHuzdp9A//vjl13+jZxf11vrB/0grxO/804//++uv33+j/ymVR4z02jG5Rw45r8+NeO0QP/747eufaOV++PLtTx/1kUyLkhtetX2k1h8utdeahEr//EQ//FyTdvrg//6XX759/5Uf/P3bl3//+tNHo9f29Nolpkes7fnaYVmOWF9Pzo84r7Z++MFqN/oP8T1LqI/iy7owgb5n+xTd6xcSfc/jdz94fGmPlj7KR4qR9k14vT+enj7FIt6/nb//zket8ZELrcNHreER2/rw9OH9p9jEsjvT94zlEcpH+Kjl4VN5fU76JV8/0Z7XeyX8zR+//Pjtl4/P9IQvP335bXr83//yy5+Wh//7129f/pVWJSesCu08eu/6+gF6ccebsaofyI9+8QN0In785Wd9iNKD9iGtvHs0v/6AK/ioroqPms8ffvBdQ35kT8/3rtISiWPasUR0qPiYFvqo5i1DR7VnOv+B/pFaXfe8DxwC8uvl6+mO3Fn3FB++Y8OkHB+pi+NUP3z5lOSOCbaw6LEBsRVTpyevp4h+rn8KfqxHftTz1d5GgB4fNdAByt09UhR7MeON/RIP8Rktr0vHsiMcZlceJYpw6D2OjtPhME3R9uqdaVcXj0OfKZCmuF4RnoNWVw+nr237iHR4Sl0OT/BuvYFolbG5nXp8o3c/XfK9y8I96KU/Gv1QVCuTdTxM9yJuoTuC9nfK/lG9ioj+E4Wu9fnt4s03n7XVR2+0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"
    sm = pd.read_csv(io.StringIO(gzip.decompress(base64.b64decode(_BLOB)).decode()))
    sm["Date"] = pd.to_datetime(sm["Date"])
    sm["Hour"] = sm["Time"].str.slice(0, 2).astype(int)
    sm["Day"] = sm["Date"].dt.strftime("%a")
    sm["Month"] = sm["Date"].dt.strftime("%b")
    DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    MONTHS = ["Jan", "Feb", "Mar"]

    # Small textbook datasets from the Module 4 notes
    scarf = [150, 170, 140, 150, 180, 180, 210, 230, 140, 200, 170, 160, 290, 200, 210, 110, 90, 140, 150, 230]
    electronics = pd.DataFrame({"commercials": [2, 5, 1, 3, 4, 1, 5, 3, 4, 2],
                                "sales": [50, 57, 41, 54, 54, 38, 63, 48, 59, 46]})
    kirk = pd.DataFrame({
        "month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
        "North": [95, 100, 120, 115, 100, 85, 135, 110, 100, 50, 40, 40],
        "South": [40, 45, 55, 65, 60, 50, 75, 65, 60, 70, 75, 80]})
    kirk["Total"] = kirk["North"] + kirk["South"]
    return DAYS, MONTHS, electronics, kirk, scarf, sm


@app.cell(hide_code=True)
def _(mo, sm):
    mo.hstack([
        mo.stat(value=f"{len(sm):,}", label="Purchases", caption="supermarket dataset"),
        mo.stat(value=f"${sm.Sales.sum():,.0f}", label="Total sales", caption="Jan 1 to Mar 30, 2019"),
        mo.stat(value=str(sm.Branch.nunique()), label="Branches", caption=", ".join(sorted(sm.Branch.unique()))),
        mo.stat(value=str(sm["Product line"].nunique()), label="Product lines", caption="six groups"),
    ], justify="space-around")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 1. Preattentive attributes: count the 7s
    Your eye notices **color, size, and length** before you start thinking. Pick a hint and count the 7s again. The numbers never change. Only how they look does.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    hint = mo.ui.radio(options=["No hint", "Color", "Size", "Color + size"], value="No hint", inline=True, label="Hint")
    hint
    return (hint,)


@app.cell(hide_code=True)
def _(MAROON, hint, mo):
    _rows = ["7341345640", "3069045863", "2722994521", "2245209204", "2407693004", "7789267247",
             "6133214490", "3662755254", "1140634051", "3752757739", "3386955364", "7603099029",
             "4694826583", "9392284398", "5882912485", "1740119958"]
    def _cell(d):
        style = ""
        if d == "7" and hint.value in ("Color", "Color + size"):
            style += f"color:{MAROON};font-weight:800;"
        if d == "7" and hint.value in ("Size", "Color + size"):
            style += "font-size:1.45em;font-weight:800;"
        return f'<span style="display:inline-block;width:1.6em;text-align:center;{style}">{d}</span>'
    _html = "<br>".join("".join(_cell(d) for d in r) for r in _rows)
    mo.Html(f'<div style="font-family:monospace;font-size:1.05rem;line-height:1.55;background:#f4f3f1;padding:12px 16px;border-radius:10px;display:inline-block">{_html}</div>')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Notice": mo.md("With which hint could you count fastest? Why is *color* a risky choice for about 1 in 12 men?"),
        "Ask AI (copy into Claude)": mo.md("```\nExplain preattentive attributes to a first-year business student in under 150 words, with one example from a monthly sales report. Which attribute is best for showing amounts, and why?\n```"),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 2. Data-ink ratio: declutter it yourself
    **Non-data ink** is anything that doesn't show data. Uncheck items one at a time and watch the chart get easier to read. Then turn on the highlight.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    _opts = ["Gridlines", "Gray background", "Border", "Legend", "Markers", "Decimal labels", "ALL-CAPS title"]
    clutter = mo.ui.multiselect(options=_opts, value=_opts, label="Clutter to keep")
    highlight = mo.ui.switch(value=False, label="Highlight the best day")
    mo.hstack([clutter, highlight], justify="start", gap=2)
    return clutter, highlight


@app.cell(hide_code=True)
def _(MAROON, NAVY, clutter, highlight, mo, plt, scarf):
    _on = set(clutter.value)
    _fig, _ax = plt.subplots()
    _days = list(range(1, 21))
    _ax.plot(_days, scarf, color=NAVY, lw=2.2, marker="s" if "Markers" in _on else None, label="Sales (units)")
    if "Gridlines" in _on:
        _ax.grid(True, color="#9a9a9a", lw=1)
    if "Gray background" in _on:
        _ax.set_facecolor("#e6e6e6")
    if "Border" in _on:
        for _s in _ax.spines.values():
            _s.set_visible(True); _s.set_color("black"); _s.set_linewidth(2)
    if "Legend" in _on:
        _ax.legend(loc="upper left", frameon=True, edgecolor="black")
    if "Decimal labels" in _on:
        _ax.yaxis.set_major_formatter(lambda v, p: f"{v:.2f}")
    _ax.set_title("SCARF SALES" if "ALL-CAPS title" in _on else "Scarf sales, units per day")
    _ax.set_xlabel("Day"); _ax.set_ylim(0, 340); _ax.set_xticks([1, 5, 10, 15, 20])
    if highlight.value:
        _best = max(range(20), key=lambda i: scarf[i])
        _ax.scatter([_best + 1], [scarf[_best]], s=90, color=MAROON, zorder=5)
        _ax.annotate(f"Day {_best+1}: {scarf[_best]}, best day", (_best + 1, scarf[_best]),
                     xytext=(10, 0), textcoords="offset points", color=MAROON, fontweight="bold", va="center")
    _fig.tight_layout()
    mo.vstack([_fig, mo.md(f"**Clutter items still on: {len(_on)} of 7.** Average: {sum(scarf)/len(scarf):.0f} units per day.")])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Notice": mo.md("Which single item made the biggest difference when you removed it? Is there anything you'd *keep* (for example, light gridlines) and why?"),
        "Ask AI (copy into Claude)": mo.md("```\nList 6 things in a default Excel chart that are usually non-data ink. For each, say whether to delete it, lighten it, or keep it. Then give me one example where removing gridlines makes a chart WORSE.\n```"),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3. Build a PivotTable (crosstab) with menus
    This is what Excel's PivotTable does. Choose the rows, columns, and value, and the table rebuilds instantly. Darker cells are bigger numbers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    _cats = ["Branch", "Product line", "Customer type", "Gender", "Payment", "Day", "Month"]
    ct_rows = mo.ui.dropdown(_cats, value="Product line", label="Rows")
    ct_cols = mo.ui.dropdown(_cats, value="Branch", label="Columns")
    ct_val = mo.ui.dropdown(["Sales", "Quantity", "Rating", "Count of purchases"], value="Sales", label="Value")
    ct_agg = mo.ui.dropdown(["Sum", "Average"], value="Sum", label="Summarize by")
    ct_show = mo.ui.dropdown(["Values", "% of grand total", "% of column total"], value="Values", label="Show as")
    mo.hstack([ct_rows, ct_cols, ct_val, ct_agg, ct_show], wrap=True, justify="start")
    return ct_agg, ct_cols, ct_rows, ct_show, ct_val


@app.cell(hide_code=True)
def _(DAYS, MONTHS, ct_agg, ct_cols, ct_rows, ct_show, ct_val, mo, plt, sm):
    mo.stop(ct_rows.value == ct_cols.value, mo.callout(mo.md("Pick **different** variables for rows and columns."), kind="warn"))
    _order = {"Day": DAYS, "Month": MONTHS}
    if ct_val.value == "Count of purchases":
        _t = sm.pivot_table(index=ct_rows.value, columns=ct_cols.value, values="Sales", aggfunc="count", margins=True, margins_name="Total")
        _fmt = "{:,.0f}"
    else:
        _t = sm.pivot_table(index=ct_rows.value, columns=ct_cols.value, values=ct_val.value,
                            aggfunc="sum" if ct_agg.value == "Sum" else "mean", margins=True, margins_name="Total")
        _fmt = "${:,.0f}" if (ct_val.value == "Sales" and ct_agg.value == "Sum") else "{:,.2f}"
    for _dim, _axis in ((ct_rows.value, 0), (ct_cols.value, 1)):
        if _dim in _order:
            _t = _t.reindex(_order[_dim] + ["Total"], axis=_axis)
    _pct = ct_show.value != "Values"
    _nonadd = ct_agg.value == "Average" or ct_val.value == "Rating"
    if _pct and _nonadd:
        _note = mo.callout(mo.md("Percentages only make sense for **sums or counts**. Averages don't add up to a total, so switch *Summarize by* to **Sum** (and don't use Rating)."), kind="warn")
        mo.stop(True, _note)
    if ct_show.value == "% of grand total":
        _t = _t / _t.loc["Total", "Total"] * 100; _fmt = "{:.1f}%"
    elif ct_show.value == "% of column total":
        _t = _t / _t.loc["Total"] * 100; _fmt = "{:.1f}%"
    _inner = _t.drop(index="Total").drop(columns="Total")
    _lo, _hi = float(_inner.min().min()), float(_inner.max().max())
    _cmap = plt.get_cmap("Blues")
    def _bg(v):
        if _hi == _lo: return "#ffffff", "#111"
        _x = 0.08 + 0.6 * (v - _lo) / (_hi - _lo)
        _r, _g, _b, _ = _cmap(_x)
        return f"rgb({int(_r*255)},{int(_g*255)},{int(_b*255)})", ("#fff" if _x > 0.5 else "#111")
    _h = ['<table style="border-collapse:collapse;font-family:system-ui,sans-serif;font-size:14px">',
          f'<tr><th style="text-align:left;padding:6px 10px;border-bottom:2px solid #222">{ct_rows.value}</th>']
    _h += [f'<th style="text-align:right;padding:6px 10px;border-bottom:2px solid #222">{c}</th>' for c in _t.columns]
    _h.append("</tr>")
    for _r in _t.index:
        _tot = _r == "Total"
        _h.append(f'<tr><td style="padding:6px 10px;font-weight:600;{"border-top:2px solid #222" if _tot else ""}">{_r}</td>')
        for _c in _t.columns:
            _v = _t.loc[_r, _c]
            _txt = "–" if _v != _v else _fmt.format(_v)
            if _tot or _c == "Total" or _v != _v:
                _sty = f'font-weight:700;{"border-top:2px solid #222;" if _tot else ""}'
            else:
                _bgc, _fg = _bg(_v); _sty = f"background:{_bgc};color:{_fg};"
            _h.append(f'<td style="text-align:right;padding:6px 10px;{_sty}">{_txt}</td>')
        _h.append("</tr>")
    _h.append("</table>")
    mo.Html('<div style="overflow-x:auto">' + "".join(_h) + "</div>")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Notice": mo.md("Set Rows = Product line, Columns = Branch, Show as = % of column total. Each branch has a different *specialty*. What is it for each? Then switch to Customer type × Gender with **Average** Sales. Who spends most per visit?"),
        "Ask AI (copy into Claude, attach the Excel file)": mo.md("```\nI attached SuperMarket_Analysis.xlsx. Build a crosstab of total Sales with Product line as rows and Branch as columns, then show each cell as % of its branch total. Name each branch's strongest and weakest product line with numbers.\n```\nThen **check the AI** against the table above."),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4. Where should the axis start? An honesty test
    Here are total sales by product line. Drag the slider to start the axis higher, the way Excel sometimes does automatically. Watch how big the differences *look*, compared with how big they *are*.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    axis_start = mo.ui.slider(start=0, stop=48000, step=1000, value=0, label="Axis starts at ($)", show_value=True, full_width=True)
    axis_start
    return (axis_start,)


@app.cell(hide_code=True)
def _(GRAY, MAROON, axis_start, mo, plt, sm):
    _pl = sm.groupby("Product line")["Sales"].sum().sort_values()
    _fig, _ax = plt.subplots(figsize=(8, 3.4))
    _cols = [GRAY] * (len(_pl) - 1) + [MAROON]
    _ax.barh(_pl.index, _pl.values - axis_start.value, left=axis_start.value, color=_cols)
    _ax.set_xlim(axis_start.value, 60000)
    _ax.xaxis.set_major_formatter(lambda v, p: f"${v/1000:.0f}K")
    for _i, _v in enumerate(_pl.values):
        _ax.text(_v + 300, _i, f"${_v/1000:.1f}K", va="center", fontsize=9)
    _ax.set_title("Sales by product line")
    _fig.tight_layout()
    _real = _pl.max() / _pl.min()
    _looks = (_pl.max() - axis_start.value) / (_pl.min() - axis_start.value)
    _kind = "success" if axis_start.value == 0 else ("warn" if _looks < 2 else "danger")
    mo.vstack([_fig, mo.callout(mo.md(
        f"The top bar is really **{_real:.2f}×** the bottom bar. On this chart it **looks {_looks:.2f}×** as long."
        + ("" if axis_start.value == 0 else " A bar chart that doesn't start at zero exaggerates differences.")), kind=_kind)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Notice": mo.md("At what axis start does a 14% difference start to look like a 'huge winner'? Why is a cut axis OK for a *scatter* or *line* chart but not for *bars*?"),
        "Ask AI (copy into Claude)": mo.md("```\nMy bar chart of six product lines (sales $49K to $56K) starts the axis at $45,000. Explain in plain words why that misleads, and rewrite my chart title so it tells the honest story.\n```"),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5. Scatter charts, trendlines, and the danger of predicting too far
    **Part A.** Pick any two numeric columns from the supermarket data. The trendline, *r*, and R² update live.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    _num = ["Unit price", "Quantity", "Sales", "Rating"]
    sx = mo.ui.dropdown(_num, value="Quantity", label="x-axis")
    sy = mo.ui.dropdown(_num, value="Sales", label="y-axis")
    sb = mo.ui.dropdown(["All branches", "Alex", "Cairo", "Giza"], value="All branches", label="Branch")
    mo.hstack([sx, sy, sb], justify="start")
    return sb, sx, sy


@app.cell(hide_code=True)
def _(MAROON, NAVY, mo, np, plt, sb, sm, sx, sy):
    mo.stop(sx.value == sy.value, mo.callout(mo.md("Pick two **different** columns."), kind="warn"))
    _d = sm if sb.value == "All branches" else sm[sm.Branch == sb.value]
    _x, _y = _d[sx.value].to_numpy(float), _d[sy.value].to_numpy(float)
    _b1, _b0 = np.polyfit(_x, _y, 1)
    _r = np.corrcoef(_x, _y)[0, 1]
    _fig, _ax = plt.subplots()
    _ax.scatter(_x, _y, s=12, alpha=0.45, color=NAVY)
    _xs = np.linspace(_x.min(), _x.max(), 50)
    _ax.plot(_xs, _b0 + _b1 * _xs, color=MAROON, lw=2.5)
    _ax.set_xlabel(sx.value); _ax.set_ylabel(sy.value)
    _ax.set_title(f"{sy.value} vs. {sx.value}  ({len(_d)} purchases)")
    _fig.tight_layout()
    _word = ("strong" if abs(_r) >= 0.6 else "moderate" if abs(_r) >= 0.3 else "weak" if abs(_r) >= 0.1 else "essentially no")
    mo.vstack([_fig, mo.hstack([
        mo.stat(value=f"{_r:.2f}", label="correlation r", caption=f"{_word} {'positive' if _r > 0 else 'negative'} relationship" if abs(_r) >= 0.1 else "no relationship"),
        mo.stat(value=f"{_r**2:.2f}", label="R²"),
        mo.stat(value=f"ŷ = {_b0:.2f} + {_b1:.2f}x", label="trendline"),
    ], justify="space-around")])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Part B.** The electronics store data from the notes: TV commercials and weekly sales (in $100s). Slide the number of commercials and read the prediction. The store only ever ran **1 to 5** commercials.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    n_ads = mo.ui.slider(start=0, stop=12, step=1, value=3, label="Commercials this week", show_value=True, full_width=True)
    n_ads
    return (n_ads,)


@app.cell(hide_code=True)
def _(GOLD, MAROON, NAVY, electronics, mo, n_ads, np, plt):
    _x, _y = electronics.commercials.to_numpy(float), electronics.sales.to_numpy(float)
    _b1, _b0 = np.polyfit(_x, _y, 1)
    _pred = _b0 + _b1 * n_ads.value
    _fig, _ax = plt.subplots(figsize=(8, 3.4))
    _ax.axvspan(0.8, 5.2, color="#eef3f7", zorder=0, label="range we have data for")
    _ax.scatter(_x, _y, s=55, color=NAVY, zorder=3)
    _xs = np.linspace(0, 12, 50)
    _ax.plot(_xs, _b0 + _b1 * _xs, color=MAROON, lw=2, ls="--")
    _ax.scatter([n_ads.value], [_pred], s=140, color=GOLD, edgecolor="black", zorder=4)
    _ax.set_xlim(-0.3, 12.3); _ax.set_ylim(20, 105)
    _ax.set_xlabel("Number of commercials"); _ax.set_ylabel("Sales ($100s)")
    _ax.legend(loc="upper left", frameon=False)
    _fig.tight_layout()
    _inside = 1 <= n_ads.value <= 5
    mo.vstack([_fig, mo.callout(mo.md(
        f"Predicted sales: **${_pred*100:,.0f}**. "
        + ("That's inside our data, so it's a reasonable estimate." if _inside else
           "⚠️ That's **outside** the 1–5 range we observed (extrapolation). The line may not hold out here.")),
        kind="success" if _inside else "danger")])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Notice": mo.md("In Part A, try Unit price vs. Rating. What does *r* tell you? Is 'no relationship' a useful business finding? In Part B, what does each extra commercial mean **in dollars**?"),
        "Ask AI (copy into Claude)": mo.md("```\nA store's trendline is ŷ = 36.15 + 4.95x, where x = commercials and y = weekly sales in $100s. Explain the slope in dollars. Then predict sales at 10 commercials and give three reasons that prediction might be wrong.\n```"),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 6. Time charts and two classic traps
    February has only 28 days, and our data **ends March 30**. Change the grain, then use the two switches. See which "drops" survive a fair comparison.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    grain = mo.ui.radio(["Day", "Week", "Month"], value="Week", inline=True, label="Group by")
    per_day = mo.ui.switch(value=False, label="Show sales per day")
    drop_partial = mo.ui.switch(value=False, label="Hide partial periods")
    split = mo.ui.switch(value=False, label="Split by branch")
    mo.hstack([grain, per_day, drop_partial, split], wrap=True, justify="start", gap=2)
    return drop_partial, grain, per_day, split


@app.cell(hide_code=True)
def _(MAROON, NAVY, SOFT, drop_partial, grain, mo, pd, per_day, plt, sm, split):
    _d = sm.copy()
    if grain.value == "Day":
        _d["period"] = _d.Date; _full = 1
    elif grain.value == "Week":
        _d["period"] = pd.Timestamp("2019-01-01") + pd.to_timedelta((_d.Date - pd.Timestamp("2019-01-01")).dt.days // 7 * 7, unit="D"); _full = 7
    else:
        _d["period"] = _d.Date.dt.to_period("M").dt.to_timestamp(); _full = None
    _days = _d.groupby("period").Date.nunique()
    if _full is None:
        _full_len = _days.index.to_series().dt.days_in_month
    else:
        _full_len = pd.Series(_full, index=_days.index)
    _partial = _days < _full_len
    _groups = ["Alex", "Cairo", "Giza"] if split.value else [None]
    _fig, _ax = plt.subplots()
    _colors = {None: NAVY, "Alex": NAVY, "Cairo": MAROON, "Giza": "#C8922A"}
    for _g in _groups:
        _s = (_d if _g is None else _d[_d.Branch == _g]).groupby("period").Sales.sum().reindex(_days.index, fill_value=0)
        if per_day.value: _s = _s / _days
        if drop_partial.value: _s = _s[~_partial]
        _lbl = _g or "All branches"
        if grain.value == "Month" and not split.value:
            _b = _ax.bar(_s.index.strftime("%b"), _s.values, color=NAVY, width=0.55)
            _ax.bar_label(_b, labels=[f"${v:,.0f}" for v in _s.values], padding=3, fontsize=9)
        elif grain.value == "Month":
            _ax.plot(_s.index.strftime("%b"), _s.values, marker="o", lw=2.4, color=_colors[_g], label=_lbl)
        else:
            _ax.plot(_s.index, _s.values, lw=1.4 if grain.value == "Day" else 2.4, color=_colors[_g], label=_lbl,
                     marker="o" if grain.value == "Week" else None, ms=4)
    if grain.value == "Week" and not drop_partial.value:
        for _p in _days.index[_partial]:
            _ax.axvspan(_p, _p + pd.Timedelta(days=_days[_p]), color="#f6e3c5", zorder=0)
            _ax.annotate(f"only {_days[_p]} days", (_p, _ax.get_ylim()[1]), fontsize=9, color=SOFT, va="top")
    if split.value: _ax.legend(frameon=False, ncol=3, loc="lower left")
    _ax.set_ylim(bottom=0)
    _ax.yaxis.set_major_formatter(lambda v, p: f"${v/1000:.1f}K" if per_day.value else f"${v/1000:.0f}K")
    _ax.set_title(f"Sales {'per day' if per_day.value else 'total'} by {grain.value.lower()}")
    _fig.autofmt_xdate() if grain.value != "Month" else None
    _fig.tight_layout()
    _msg = {
        "Day": "Daily data is noisy. Try Week or Month to see the trend.",
        "Week": "The last 'week' is only 5 days (Mar 26–30). Turn on **per day** or **hide partial** before calling it a crash.",
        "Month": "February has 28 days, and March is missing the 31st. Turn on **per day** for a fair comparison.",
    }[grain.value]
    mo.vstack([_fig, mo.callout(mo.md(_msg), kind="info")])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Notice": mo.md("Is February still the weakest month *per day*? By how much, compared with the raw totals? When you split by branch, which branch fell most from January to February?"),
        "Ask AI (copy into Claude)": mo.md("```\nMy manager says 'February was our worst month and the last week of March was a disaster.' February has 28 days and our data ends March 30. What adjustment should we make before comparing periods of different lengths? Explain like I'm new to analytics.\n```"),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 7. Totals can hide the real story (Kirkland)
    Kirkland's air compressor sales, from the notes. Switch between the total and the regions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    kview = mo.ui.radio(["Total only", "North and South"], value="Total only", inline=True, label="View")
    kview
    return (kview,)


@app.cell(hide_code=True)
def _(MAROON, NAVY, kirk, kview, plt):
    _fig, _ax = plt.subplots(figsize=(8, 3.4))
    if kview.value == "Total only":
        _ax.plot(kirk.month, kirk.Total, color="#222", lw=2.6); _ax.text(11.2, kirk.Total.iloc[-1], "Total", va="center", fontweight="bold")
        _ax.set_ylim(0, 250)
    else:
        for _c, _col in (("North", NAVY), ("South", MAROON)):
            _ax.plot(kirk.month, kirk[_c], color=_col, lw=2.6); _ax.text(11.2, kirk[_c].iloc[-1], _c, va="center", color=_col, fontweight="bold")
        _ax.set_ylim(0, 150)
    _ax.set_xlim(-0.3, 12); _ax.set_title("Kirkland air compressor sales ($100s)")
    _fig.tight_layout()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 8. Histograms: what does a typical purchase look like?
    Change the number of bins. The data doesn't change, but the picture can. The **mean** and **median** lines show why one number can mislead.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    hvar = mo.ui.dropdown(["Sales", "Rating", "Unit price", "Quantity"], value="Sales", label="Variable")
    bins = mo.ui.slider(start=3, stop=60, step=1, value=12, label="Bins", show_value=True)
    mo.hstack([hvar, bins], justify="start", gap=2)
    return bins, hvar


@app.cell(hide_code=True)
def _(GOLD, MAROON, NAVY, bins, hvar, mo, plt, sm):
    _v = sm[hvar.value]
    _fig, _ax = plt.subplots()
    _ax.hist(_v, bins=bins.value, color=NAVY, edgecolor="white")
    _ax.axvline(_v.mean(), color=MAROON, lw=2.2, label=f"mean {_v.mean():,.2f}")
    _ax.axvline(_v.median(), color=GOLD, lw=2.2, ls="--", label=f"median {_v.median():,.2f}")
    _ax.legend(frameon=False); _ax.set_title(f"Distribution of {hvar.value} (1,000 purchases)")
    _ax.set_ylabel("Number of purchases")
    _fig.tight_layout()
    _skew = _v.skew()
    mo.vstack([_fig, mo.md(f"Skewness = **{_skew:.2f}**. " + (
        "Skewed right: a few big purchases pull the mean above the median, so the median is the better 'typical' value." if _skew > 0.5 else
        "Fairly symmetric: mean and median tell a similar story." ))])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Notice": mo.md("Look at **Rating**. Real customer ratings usually pile up at 8–10. What's odd here, and what might it say about where this data came from? Try 3 bins, then 60. Which setting hides the shape, and which one turns it into noise?"),
        "Ask AI (copy into Claude)": mo.md("```\nThe mean sale is $322.97 and the median is $253.85. Explain to a store manager what that difference tells us about customer purchases, and which number she should use as 'a typical sale'.\n```"),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 9. Heat map: when is the store busy? (and why color choice matters)
    Pick a measure, a branch, and a **color scheme**. The same numbers can look calm, alarming, or confusing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    hm_metric = mo.ui.dropdown(["Number of purchases", "Total sales"], value="Total sales", label="Measure")
    hm_branch = mo.ui.dropdown(["All branches", "Alex", "Cairo", "Giza"], value="All branches", label="Branch")
    hm_cmap = mo.ui.dropdown({"Sequential (light to dark blue)": "Blues", "Diverging (blue-white-red)": "RdBu_r", "Rainbow (avoid)": "jet"},
                             value="Sequential (light to dark blue)", label="Colors")
    mo.hstack([hm_metric, hm_branch, hm_cmap], justify="start", wrap=True)
    return hm_branch, hm_cmap, hm_metric


@app.cell(hide_code=True)
def _(DAYS, hm_branch, hm_cmap, hm_metric, mo, plt, sm):
    _d = sm if hm_branch.value == "All branches" else sm[sm.Branch == hm_branch.value]
    _agg = "count" if hm_metric.value == "Number of purchases" else "sum"
    _t = _d.pivot_table(index="Day", columns="Hour", values="Sales", aggfunc=_agg, fill_value=0).reindex(DAYS)
    _fig, _ax = plt.subplots(figsize=(8.5, 3.6))
    _im = _ax.imshow(_t.values, cmap=hm_cmap.value, aspect="auto")
    _ax.set_yticks(range(7), DAYS); _ax.set_xticks(range(len(_t.columns)), [f"{h}:00" for h in _t.columns], fontsize=8)
    for _s in _ax.spines.values(): _s.set_visible(False)
    _fig.colorbar(_im, ax=_ax, fraction=0.03)
    _ax.set_title(f"{hm_metric.value} by day and hour ({hm_branch.value})")
    _fig.tight_layout()
    _dtot = _t.sum(axis=1); _htot = _t.sum(axis=0)
    _f = (lambda v: f"{v:,.0f} purchases") if _agg == "count" else (lambda v: f"${v:,.0f}")
    mo.vstack([_fig, mo.hstack([
        mo.stat(value=_dtot.idxmax(), label="busiest day", caption=_f(_dtot.max())),
        mo.stat(value=_dtot.idxmin(), label="quietest day", caption=_f(_dtot.min())),
        mo.stat(value=f"{_htot.idxmax()}:00", label="busiest hour", caption=_f(_htot.max())),
        mo.stat(value=f"{_htot.idxmin()}:00", label="quietest hour", caption=_f(_htot.min())),
    ], justify="space-around")])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Notice": mo.md("In the diverging scheme, what does **white** mean? Is that midpoint meaningful for sales? Why does the rainbow scheme make it hard to rank cells? Which branch has a different busiest day?"),
        "Ask AI (copy into Claude)": mo.md("```\nA store manager wants a heat map of sales by day of week and hour to schedule staff. Which color scheme should I use and why? What is one risk of scheduling from only 3 months of data?\n```"),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 10. Bubble charts: area vs. radius, and a zoomed axis
    Each bubble is a product line: x = average rating, y = total sales, and size = number of purchases. Two common mistakes can make small differences look big. Try both.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    size_rule = mo.ui.radio(["Size by area (correct)", "Size stretched from smallest to largest (exaggerates)"], value="Size by area (correct)", inline=True, label="Bubble size")
    zoom = mo.ui.switch(value=True, label="Let the rating axis zoom in")
    mo.hstack([size_rule, zoom], justify="start", gap=2)
    return size_rule, zoom


@app.cell(hide_code=True)
def _(NAVY, plt, size_rule, sm, zoom):
    _g = sm.groupby("Product line").agg(rating=("Rating", "mean"), sales=("Sales", "sum"), n=("Sales", "size"))
    _base = (_g.n / _g.n.max())
    if size_rule.value.startswith("Size by area"):
        _s = _base * 1600                                   # area proportional to the count: honest
    else:
        _s = 60 + 2400 * (_g.n - _g.n.min()) / (_g.n.max() - _g.n.min())   # like a bar axis that doesn't start at zero
    _fig, _ax = plt.subplots(figsize=(8, 4))
    _ax.scatter(_g.rating, _g.sales, s=_s, color=NAVY, alpha=0.55, edgecolor="white")
    for _name, _r in _g.iterrows():
        _ax.annotate(f"{_name} ({int(_r.n)})", (_r.rating, _r.sales), fontsize=8, ha="center", va="bottom", xytext=(0, 12), textcoords="offset points")
    if zoom.value: _ax.set_xlim(_g.rating.min() - 0.05, _g.rating.max() + 0.05)
    else: _ax.set_xlim(4, 10)
    _ax.set_ylim(45000, 60000); _ax.set_xlabel("Average rating (1–10)"); _ax.set_ylabel("Total sales")
    _ax.yaxis.set_major_formatter(lambda v, p: f"${v/1000:.0f}K")
    _ax.set_title("Product lines: rating, sales, and number of purchases")
    _fig.tight_layout()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Notice": mo.md("Turn the zoom **off**. What happens to the 'differences' in rating? Switch to *stretched* sizing. Does 152 purchases vs. 178 purchases now look like a bigger gap than it is? Which earlier section made the same mistake with bars?"),
        "Ask AI (copy into Claude)": mo.md("```\nAverage customer ratings for six product lines range from 6.84 to 7.11 on a 1-10 scale. Excel zooms my bubble chart axis to 6.8-7.1. Explain how that changes what readers believe, and what axis range I should use.\n```"),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 11. Waterfall: how sales moved month to month
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    wf_branch = mo.ui.dropdown(["All branches", "Alex", "Cairo", "Giza"], value="All branches", label="Branch")
    wf_branch
    return (wf_branch,)


@app.cell(hide_code=True)
def _(GOLD, MONTHS, NAVY, plt, sm, wf_branch):
    _d = sm if wf_branch.value == "All branches" else sm[sm.Branch == wf_branch.value]
    _m = _d.groupby("Month").Sales.sum().reindex(MONTHS)
    _steps = [("Jan", 0, _m["Jan"]), ("Feb change", _m["Jan"], _m["Feb"] - _m["Jan"]),
              ("Mar change", _m["Feb"], _m["Mar"] - _m["Feb"]), ("Mar", 0, _m["Mar"])]
    _fig, _ax = plt.subplots(figsize=(7.5, 3.6))
    for _i, (_lab, _start, _delta) in enumerate(_steps):
        _col = "#222" if _lab in ("Jan", "Mar") else (NAVY if _delta >= 0 else GOLD)
        _ax.bar(_i, _delta, bottom=_start, color=_col, width=0.6)
        _top = _start + max(_delta, 0)
        _ax.text(_i, _top + _m.max() * 0.015, (f"${_delta:,.0f}" if _lab in ("Jan", "Mar") else f"{'+' if _delta >= 0 else '−'}${abs(_delta):,.0f}"),
                 ha="center", fontsize=9, fontweight="bold")
    _ax.set_xticks(range(4), [s[0] for s in _steps]); _ax.set_ylim(0, _m.max() * 1.15)
    _ax.yaxis.set_major_formatter(lambda v, p: f"${v/1000:.0f}K")
    _ax.set_title(f"From January to March sales ({wf_branch.value})")
    _fig.tight_layout()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 12. Mini dashboard: a preview of the Data Viz Challenge
    Filter by branch and customer type, and every KPI and chart updates together. That's what a dashboard should do. Ask yourself whether each piece helps the manager make a **decision**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    db_branch = mo.ui.dropdown(["All branches", "Alex", "Cairo", "Giza"], value="All branches", label="Branch")
    db_ctype = mo.ui.dropdown(["All customers", "Member", "Normal"], value="All customers", label="Customer type")
    mo.hstack([db_branch, db_ctype], justify="start", gap=2)
    return db_branch, db_ctype


@app.cell(hide_code=True)
def _(DAYS, GRAY, MAROON, NAVY, db_branch, db_ctype, mo, plt, sm):
    _d = sm
    if db_branch.value != "All branches": _d = _d[_d.Branch == db_branch.value]
    if db_ctype.value != "All customers": _d = _d[_d["Customer type"] == db_ctype.value]
    _kpis = mo.hstack([
        mo.stat(value=f"${_d.Sales.sum():,.0f}", label="Sales", caption=f"{_d.Sales.sum()/sm.Sales.sum():.0%} of chain"),
        mo.stat(value=f"{len(_d):,}", label="Purchases"),
        mo.stat(value=f"${_d.Sales.mean():,.2f}", label="Avg purchase", caption=f"median ${_d.Sales.median():,.2f}"),
        mo.stat(value=f"{_d.Rating.mean():.2f}", label="Avg rating", caption="out of 10"),
    ], justify="space-around")
    _fig, _axs = plt.subplots(1, 3, figsize=(11, 3.3))
    _pl = _d.groupby("Product line").Sales.sum().sort_values()
    _axs[0].barh([s.replace(" and ", " & ").replace(" accessories", " acc.") for s in _pl.index], _pl.values,
                 color=[GRAY] * (len(_pl) - 1) + [MAROON])
    _axs[0].set_title("Sales by product line"); _axs[0].xaxis.set_major_formatter(lambda v, p: f"${v/1000:.0f}K")
    _dw = _d.groupby("Day").Sales.sum().reindex(DAYS)
    _axs[1].bar(DAYS, _dw.values, color=[MAROON if v == _dw.max() else NAVY for v in _dw.values])
    _axs[1].set_title("Sales by day of week"); _axs[1].yaxis.set_major_formatter(lambda v, p: f"${v/1000:.0f}K")
    _hr = _d.groupby("Hour").Sales.sum()
    _axs[2].plot(_hr.index, _hr.values, color=NAVY, lw=2.4, marker="o", ms=4)
    _axs[2].scatter([_hr.idxmax()], [_hr.max()], color=MAROON, s=70, zorder=5)
    _axs[2].set_title("Sales by hour"); _axs[2].set_ylim(bottom=0); _axs[2].yaxis.set_major_formatter(lambda v, p: f"${v/1000:.0f}K")
    _fig.tight_layout()
    mo.vstack([_kpis, _fig])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Notice": mo.md("Does every branch have the same best product line? The same best day? Which filter combination gives the most surprising picture? Could you build this same view in Excel with slicers?"),
        "Ask AI (copy into Claude)": mo.md("```\nHere is a description of our dashboard: 4 KPIs (sales, purchases, average purchase, average rating) and 3 charts (sales by product line, by day of week, by hour), filterable by branch and customer type. Critique it like a skeptical regional manager. Which piece would you remove, and what one chart is missing?\n```"),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 13. Build your own reactive demo with Claude
    You've been *using* reactive charts. Now **build one**. You don't need to be a programmer, because Claude writes the code and you direct it and check it.

    **Step 1. Get a notebook.** Open [molab.marimo.io](https://molab.marimo.io) for a free marimo notebook in your browser, or install it on your laptop with `pip install marimo` and then run `marimo edit`.

    **Step 2. Ask Claude for a cell.** Copy one of these prompts into [claude.ai](https://claude.ai), then paste the code it gives you into a new cell. *Tip:* first paste in marimo's own [rules for AI assistants](CLAUDE.md), which sit next to this page, so Claude writes code that follows marimo's rules.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({
        "Starter: a slider that changes a chart": mo.md("```\nWrite a marimo notebook (Python) with two cells. Cell 1: a mo.ui.slider called 'weeks' from 1 to 13. Cell 2: using pandas and matplotlib, simulate weekly sales that start at $25,000 and grow 2% per week, and plot the first 'weeks' weeks as a line chart with a clean, decluttered style (no gridlines, no top/right spines, a title that states the finding). Explain each line in plain English for a business student.\n```"),
        "Supermarket: your own filter": mo.md("```\nI have a CSV with columns Branch, Product line, Customer type, Gender, Sales, Date, Payment, Rating. Write marimo cells that (1) load it with pandas, (2) add a mo.ui.dropdown to pick a Payment method, and (3) show a sorted horizontal bar chart of total Sales by Product line for that payment method, highlighting the top bar in one color and the rest in gray. Keep the code short and comment every step.\n```"),
        "Challenge: a 'what-if' pricing demo": mo.md("```\nBuild a marimo demo for a business analytics class: sliders for price increase (0-20%) and customer loss (0-30%). Using a starting point of $322,967 in sales, compute and chart old vs new revenue, and show a mo.callout that turns red if revenue falls. Explain what 'reactive' means in marimo in two sentences.\n```"),
        "Fix it: when your code breaks": mo.md("```\nHere is my marimo cell and the error it shows: [paste both]. Explain the error in plain words, fix it, and tell me what I should check next time. (Reminder: in marimo, each variable can be defined in only one cell.)\n```"),
    })
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Step 3. Check it like an analyst.** Does the chart follow this module's rules: honest axes, little clutter, color used on purpose? Do the numbers match what you get in Excel? If not, tell Claude exactly what's wrong and ask it to fix it.

    **Step 4. Share it.** In a terminal, `marimo export html-wasm your_notebook.py -o site --mode run` turns your notebook into a web page anyone can open, just like this one.

    ---
    *Data: a supermarket sales practice dataset (1,000 purchases, Jan–Mar 2019) and textbook examples from the Module 4 notes. The small datasets are typed in, and the supermarket file is packed inside this page, so nothing is downloaded or uploaded while you work.*
    """)
    return


if __name__ == "__main__":
    app.run()
