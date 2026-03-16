# 2026 Python data science template

A modern Python data science project template for practitioners who want to start quickly without ending up with a messy repo. It encourages reproducible analytics and ships with structured best-practice guidance that AI coding assistants load automatically — so generated code follows your project standards from day one.

## What this template is

This template is for code-first data science work where exploratory analysis is expected to mature into maintainable project code.

It assumes code runs from a checked-out project repository.

It is not trying to be a general-purpose library template or a package designed to be installed and used outside the repo.

It gives you:

- a clean `src/` layout for reusable project code inside a checked-out repo
- fast modern tooling with `uv`, `ruff`, `mypy`, and `pytest`
- Git-friendly notebook-style work with marimo
- sensible VS Code defaults
- a lightweight CI baseline
- dependency groups that are easy to extend
- built-in GitHub Copilot integration with project conventions and data science best-practice standards that load automatically

It is **not** aimed at notebook-only or Jupyter-heavy workflows where almost everything lives in `.ipynb` files.

## Who this template is for

This is a good fit for:

- solo data scientists who want a clean starting point
- small DS teams who want consistent project structure
- analytics or modelling projects that will grow into reusable code
- people who like notebooks for exploration but want version-controlled Python files

It may not be a good fit for:

- pure package/library templates
- heavyweight MLOps platforms
- notebook-only exploratory work with no intention of moving logic into `src/`

## AI coding assistant integration

Generated projects ship with GitHub Copilot integration out of the box.

`.github/copilot-instructions.md` loads automatically when you open the project in VS Code, giving Copilot your project conventions without any configuration.

Seven skills live in `.github/skills/` and load automatically based on the task at hand:

| Skill | Activates when |
|---|---|
| `ds-workflow` | Given a business question or dataset to analyse — invoke this first |
| `ds-eda` | Loading data, checking quality, exploring distributions |
| `ds-stats` | Hypothesis testing, effect sizes, experimental design |
| `ds-modelling` | Pipelines, feature engineering, model training |
| `ds-evaluation` | Model metrics, SHAP, calibration, subgroup analysis |
| `ds-visualisation` | Charts, figures, tables, colour, labelling |
| `marimo` | Writing or editing `.py` notebook files |
| `streamlit` | Creating streamlit web applications |

You can also invoke any skill manually in Copilot Chat, for example `/ds-workflow` or `/ds-stats`.

### Example prompt

The most effective way to start an analysis is to hand Copilot a business question, a dataset, and ask it to plan before writing any code:

```
/ds-workflow

Business question: What factors drive resale price for second-hand vehicles
in this dataset, and what price should I list my car for?

Dataset: data/raw/vehicles.csv

Before writing any code:
1. List the planned deliverables (notebooks, src/ modules, tests, script, report, figures)
2. Identify which workflow stages apply to this question
3. Identify which skills apply at each stage
```

Asking Copilot to plan deliverables and stages before writing forces it to engage the workflow and skill guidance properly. Skipping straight to "write me the EDA" produces lower-quality output that ignores the standards.

## Create a new project from this template

Use Copier, not GitHub's "Use this template" button.

Copier handles project naming, package naming, and file rendering properly.
```bash
uvx copier copy https://github.com/YOUR-ORG/YOUR-REPO.git my-new-project
cd my-new-project
```

## First 5 minutes in a new project

Set up the environment, install Git hooks, create the lockfile, and make the first commit.
```bash
uv sync
uv run pre-commit install
git add .
git add uv.lock
git commit -m "Initial project from template"
code .
```

Run the local checks once so you know the project is healthy before making changes.
```bash
uv run ruff format --check .
uv run ruff check src tests notebooks
uv run mypy src tests
uv run pytest
```

## Dependency groups

By default, `uv sync` installs:

- base dependencies
- `dev`
- `notebook`
- `data`
- `stats`

Optional groups are available when needed:

| Group | What it adds |
|---|---|
| `data-pandas` | pandas and pandas-stubs — opt-in only, required by some libraries (e.g. statsmodels formula API) |
| `validation` | pandera with polars support |
| `vis-static` | matplotlib and seaborn |
| `vis-interactive` | plotly |
| `ml` | scikit-learn |
| `app` | streamlit - for building and running the project as an app |

Examples:
```bash
uv sync --group data-pandas
uv sync --group validation
uv sync --group vis-static --group vis-interactive
uv sync --group ml
uv sync --all-groups
```

## Adding dependencies

Use `uv add` instead of hand-editing `pyproject.toml` where possible.

Use these rules:

- if code in `src/` imports it, add it to base dependencies
- if it is a dev tool, add it to `dev`
- if it is an optional project capability, add it to a named group

Examples:
```bash
uv add duckdb
uv add --dev mypy
uv add --group vis-static matplotlib seaborn
uv add --group ml xgboost
```

## Updating an existing project from the template

If the template has improved since you created your project, pull the changes in with:
```bash
uvx copier update
```

Copier will show you a diff of what would change and let you accept or reject each update. Commit the result as a normal change to your project.

## Project layout
```text
src/                    reusable project code
tests/                  automated tests
scripts/                reproducible analysis entrypoints
notebooks/marimo/       exploratory notebook-style work as Python files
data/                   raw, interim, processed, external
models/                 model artefacts
reports/                analysis reports and generated figures
.github/skills/         Copilot skill definitions
```

Use `src/` for logic you want to keep.

Use `notebooks/marimo/` for exploration, iteration, and lightweight demos.

Use `scripts/` for end-to-end pipeline entrypoints that orchestrate `src/` functions.

## Lockfile and CI policy

New projects are rendered without a `uv.lock`.

The first `uv sync` creates it.

Commit that file early and keep it in version control.

Generated project CI assumes the lockfile is committed and uses `uv sync --frozen`.

Template maintenance CI is different on purpose: it renders a sample project and checks that the onboarding path still works.

## Maintainer notes

### Development workflow

`.jinja` template files cannot be linted or formatted directly — ruff and mypy
do not understand Jinja syntax. All code quality checks run against the rendered
output in `.rendered/`, not the source template files.

For any change to a `.jinja` file, run the full check suite locally before pushing:
```bash
just check
```

This renders the template into `.rendered/` and runs format, lint, marimo check,
mypy, pytest, and build against the output — the same steps CI runs. Errors come
back with real line numbers from the rendered file. Find the equivalent location
in the `.jinja` source and fix it there.

To inspect the rendered project directly:
```bash
just render
code .rendered
```

### Available commands

| Command        | What it does                                          |
|----------------|-------------------------------------------------------|
| `just check`   | Render template and run full check suite — mirrors CI |
| `just render`  | Render only, output goes to `.rendered/`              |
| `just clean`   | Delete the `.rendered/` directory                     |

### Making a release

1. Update the version in the template repo's `pyproject.toml`
2. Write release notes in GitHub Releases
3. Tag the release: `git tag vX.Y.Z`
4. Push: `git push && git push --tags`

Copier uses git tags to identify template versions — the tag is required
for `copier update` to work correctly in projects generated from this template.

### Keeping root and template files aligned

A few files exist both at the repo root and under `template/`.
Keep them aligned on purpose:

- `.vscode/settings.json`
- `.vscode/extensions.json`
- `.editorconfig`
- `.gitattributes`

A few others are similar but intentionally not identical because the template
repo and generated repos have different jobs:

- `.pre-commit-config.yaml`
- `.gitignore`
- GitHub Actions workflows
