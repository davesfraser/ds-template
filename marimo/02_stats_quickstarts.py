import marimo

__generated_with = "0.20.4"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import statsmodels.formula.api as smf
    from scipy import stats
    from statsmodels.stats.anova import anova_lm

    return anova_lm, mo, np, pd, smf, stats


@app.cell
def _(np, pd):
    # Produce some dummy data

    n = 80
    rng = np.random.default_rng(42)

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
    return a, b, df_anova, df_reg, x, y


@app.cell
def _(a, b, mo, np, pd, stats):
    ttest_res = stats.ttest_ind(a, b, equal_var=False)

    ttest_df = pd.DataFrame(
        {
            "statistic": [ttest_res.statistic],
            "pvalue": [ttest_res.pvalue],
            "df": [getattr(ttest_res, "df", np.nan)],
        }
    )

    try:
        ci = ttest_res.confidence_interval(confidence_level=0.95)
        ttest_df["ci_low_95"] = ci.low
        ttest_df["ci_high_95"] = ci.high
    except Exception:
        pass

    cohen_d = (np.mean(a) - np.mean(b)) / np.sqrt(
        ((np.std(a, ddof=1) ** 2) + (np.std(b, ddof=1) ** 2)) / 2
    )
    ttest_df["cohen_d"] = cohen_d

    mo.ui.table(
        data=ttest_df,
        pagination=False,
        label="Welch t test results",
    )
    return


@app.cell
def _(mo, pd, stats, x, y):
    corr_res = stats.pearsonr(x, y)

    corr_df = pd.DataFrame(
        {
            "r": [corr_res.statistic],
            "pvalue": [corr_res.pvalue],
            "n": [len(x)],
        }
    )

    mo.vstack(
        [
            mo.md("## 2 Pearson correlation test"),
            mo.ui.table(data=corr_df, pagination=False, label="Correlation results"),
        ]
    )
    return


@app.cell
def _(mo, pd, stats):
    chi_table = pd.DataFrame(
        [[30, 10], [15, 25]],
        index=["A", "B"],
        columns=["Yes", "No"],
    )

    chi2, p, dof, expected = stats.chi2_contingency(chi_table.values)

    chi2_df = pd.DataFrame({"chi2": [chi2], "pvalue": [p], "dof": [dof]})
    expected_df = pd.DataFrame(expected, index=chi_table.index, columns=chi_table.columns)

    mo.vstack(
        [
            mo.md("## 3 Chi square test of independence"),
            mo.ui.table(data=chi2_df, pagination=False, label="Test results"),
            mo.ui.tabs(
                {
                    "Observed": mo.ui.table(data=chi_table, pagination=False, label="Observed"),
                    "Expected": mo.ui.table(data=expected_df, pagination=False, label="Expected"),
                }
            ),
        ]
    )
    return


@app.cell
def _(anova_lm, df_anova, mo, smf):
    anova_model = smf.ols("value ~ C(group)", data=df_anova).fit()
    anova_df = anova_lm(anova_model, typ=2)

    mo.vstack(
        [
            mo.md("## 4 One way ANOVA via statsmodels"),
            mo.ui.table(data=anova_df, pagination=False, label="ANOVA table"),
        ]
    )
    return


@app.cell
def _(df_reg, mo, smf):
    ols_model = smf.ols("y ~ x1 + x2", data=df_reg).fit()
    summary_text = ols_model.summary().as_text()

    mo.vstack(
        [
            mo.md("## 5 OLS regression summary"),
            mo.plain_text(summary_text),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
