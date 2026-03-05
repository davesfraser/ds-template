import marimo

app = marimo.App(width="full")


@app.cell
def __(mo):
    mo.md(
        """
# Stats quickstarts

Base R style building blocks in Python using SciPy plus statsmodels

To run this notebook
1 install groups
   uv sync --group data --group notebook --group stats
2 open marimo
   uv run marimo edit marimo/02_stats_quickstarts.py

If you use Polars for wrangling, do that first, then convert right at the stats layer
df_pd = df_pl.to_pandas()
"""
    )
    return


@app.cell
def __():
    import numpy as np
    import pandas as pd
    import statsmodels.formula.api as smf
    from scipy import stats
    from statsmodels.stats.anova import anova_lm

    rng = np.random.default_rng(42)
    return anova_lm, np, pd, rng, smf, stats


@app.cell
def __(mo, np, pd, rng):
    n = 80

    a = rng.normal(loc=0.0, scale=1.0, size=n)
    b = rng.normal(loc=0.4, scale=1.1, size=n)

    x = rng.normal(size=n)
    y = 0.6 * x + rng.normal(scale=0.8, size=n)

    df_anova = pd.DataFrame(
        {
            "group": np.repeat(["control", "treat_a", "treat_b"], repeats=[n, n, n]),
            "value": np.concatenate(
                [
                    rng.normal(loc=0.0, scale=1.0, size=n),
                    rng.normal(loc=0.3, scale=1.0, size=n),
                    rng.normal(loc=0.7, scale=1.0, size=n),
                ]
            ),
        }
    )

    df_reg = pd.DataFrame(
        {
            "x1": rng.normal(size=n),
            "x2": rng.normal(size=n),
        }
    )
    df_reg["y"] = 1.2 + 0.9 * df_reg["x1"] - 0.4 * df_reg["x2"] + rng.normal(scale=1.0, size=n)

    mo.md("Synthetic example data created")
    return a, b, df_anova, df_reg, x, y


@app.cell
def __(mo, np, pd, stats, a, b):
    mo.md("## 1 Welch two sample t test")

    res = stats.ttest_ind(a, b, equal_var=False)

    out = pd.DataFrame(
        {
            "statistic": [res.statistic],
            "pvalue": [res.pvalue],
            "df": [getattr(res, "df", np.nan)],
        }
    )

    try:
        ci = res.confidence_interval(confidence_level=0.95)
        out["ci_low_95"] = ci.low
        out["ci_high_95"] = ci.high
    except Exception:
        pass

    d = (np.mean(a) - np.mean(b)) / np.sqrt(
        ((np.std(a, ddof=1) ** 2) + (np.std(b, ddof=1) ** 2)) / 2
    )
    out["cohen_d"] = d

    return out


@app.cell
def __(mo, pd, stats, x, y):
    mo.md("## 2 Pearson correlation test")

    r = stats.pearsonr(x, y)

    out = pd.DataFrame(
        {
            "r": [r.statistic],
            "pvalue": [r.pvalue],
            "n": [len(x)],
        }
    )
    return out


@app.cell
def __(mo, pd, stats):
    mo.md("## 3 Chi square test of independence")

    table = pd.DataFrame(
        [[30, 10], [15, 25]],
        index=["A", "B"],
        columns=["Yes", "No"],
    )

    chi2, p, dof, expected = stats.chi2_contingency(table.values)

    out = pd.DataFrame({"chi2": [chi2], "pvalue": [p], "dof": [dof]})
    expected_df = pd.DataFrame(expected, index=table.index, columns=table.columns)

    return table, out, expected_df


@app.cell
def __(mo, anova_lm, smf, df_anova):
    mo.md("## 4 One way ANOVA via statsmodels")

    model = smf.ols("value ~ C(group)", data=df_anova).fit()
    table = anova_lm(model, typ=2)

    return table


@app.cell
def __(mo, smf, df_reg):
    mo.md("## 5 OLS regression summary")

    model = smf.ols("y ~ x1 + x2", data=df_reg).fit()
    summary_text = model.summary().as_text()

    return mo.code(summary_text)


if __name__ == "__main__":
    app.run()
