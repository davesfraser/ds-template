# ds-template

[![CI](https://github.com/davesfraser/ds-template/actions/workflows/template-smoke.yaml/badge.svg)](https://github.com/davesfraser/ds-template/actions/workflows/template-smoke.yaml)
[![Copier](https://img.shields.io/badge/copier-template-blue)](https://copier.readthedocs.io/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A modern Python data science project template for practitioners who want to
start quickly without ending up with a messy repo. It encourages reproducible,
code-first analytics and ships with project guidance that AI coding assistants
can load automatically.

This repository is a fully materialised downstream of
[`py-template`](https://github.com/davesfraser/py-template). It keeps the shared
Python project mechanics from the base template and adds data-science structure:
notebooks, data folders, scientific dependency groups, analysis guidance, and
DS-specific AI coding skills.

## What This Template Is For

`ds-template` is for data science work where exploratory analysis is expected
to mature into maintainable project code. It assumes code runs from a checked
out project repository, with reusable logic in `src/` and exploratory work in
version-controlled Python notebooks.

It is a good fit for:

- solo data scientists who want a clean starting point
- small DS teams who want consistent project structure
- analytics, statistics, modelling, and reporting projects
- people who like notebooks for exploration but want durable code in `src/`

It is not aimed at:

- pure package/library projects
- heavyweight MLOps platforms
- notebook-only workflows where almost everything lives in `.ipynb` files

## What You Get

- `src/` package layout with typed settings and project path constants
- `uv` dependency and environment management
- `ruff`, `mypy`, `pytest`, coverage, pre-commit, and GitHub Actions CI
- marimo notebooks under `notebooks/marimo/`
- data, model, report, figure, docs, examples, and script folders
- scientific dependency groups for notebooks, data, stats, validation,
  visualisation, ML, and apps
- generated `.copier-answers.yml` for future `copier update`
- DS-specific `AGENTS.md` guidance and `.github/skills/`

## Create A New Project

Use Copier, not GitHub's "Use this template" button. Copier renders project
names, package names, metadata, and update-tracking files correctly.

```bash
uvx copier copy https://github.com/davesfraser/ds-template.git my-new-project
cd my-new-project
```

Copier will ask for:

- `project_name`: human-readable title
- `project_slug`: repository/distribution name
- `package_name`: Python import package
- `project_description`
- `author_name` and `author_email`
- `python_min_version`: `3.12` or `3.13`

## First 5 Minutes

Set up the environment, install Git hooks, create the lockfile, and make the
first commit.

```bash
uv sync
git init
uv run pre-commit install
git add .
git add uv.lock
git add .copier-answers.yml
git commit -m "Initial project from template"
code .
```

Run the local checks once so you know the generated project is healthy:

```bash
uv run ruff format --check .
uv run ruff check src tests notebooks scripts
uv run marimo check notebooks/marimo
uv run mypy src tests
uv run pytest -q
uv build
```

Open the starter notebook:

```bash
uv run marimo edit notebooks/marimo/01_exploration.py
```

## AI Coding Assistant Support

Generated projects include project-specific assistant guidance.

`.github/copilot-instructions.md` gives GitHub Copilot the project's coding
conventions when the project is opened in VS Code. `AGENTS.md` gives compatible
AI coding assistants the same project rules.

Generated projects also include skills under `.github/skills/`:

| Skill | Use it for |
| --- | --- |
| `ds-workflow` | Planning an analysis from a business question or dataset |
| `ds-eda` | Loading data, quality checks, and exploratory analysis |
| `ds-stats` | Hypothesis testing, effect sizes, and study design |
| `ds-modelling` | Feature engineering, pipelines, and model training |
| `ds-evaluation` | Metrics, calibration, model interpretation, and subgroups |
| `ds-visualisation` | Charts, figures, tables, labels, and colour choices |
| `marimo` | Writing or editing `.py` notebook files |
| `streamlit` | Creating Streamlit applications |

A good starting prompt is to ask for a plan before code:

```text
/ds-workflow

Business question: What factors drive resale price for second-hand vehicles
in this dataset, and what price should I list my car for?

Dataset: data/raw/vehicles.csv

Before writing any code:
1. List the planned deliverables.
2. Identify which workflow stages apply.
3. Identify which skills apply at each stage.
```

## Project Layout

Generated projects use this structure:

```text
src/<package_name>/       reusable package code
tests/                    pytest tests
tests/fixtures/           shared test fixtures
notebooks/marimo/         exploratory notebook-style work
data/raw/                 source data, read-only
data/interim/             intermediate transformed data
data/processed/           final analysis-ready data
data/external/            third-party reference data
models/                   model artefacts
reports/                  written analysis outputs
reports/figures/          generated figures
docs/                     project documentation
docs/decisions/           design decision records
examples/                 small runnable examples
scripts/                  reproducible entrypoints and utilities
.github/skills/           AI coding assistant skills
.github/workflows/        GitHub Actions CI
AGENTS.md                 AI assistant coding instructions
pyproject.toml            project metadata and tool configuration
uv.lock                   locked dependencies
.copier-answers.yml       Copier update metadata
```

Use `src/` for logic you want to keep. Use `notebooks/marimo/` for exploration,
iteration, and lightweight demos. Use `scripts/` for end-to-end entrypoints that
orchestrate `src/` functions.

## Dependency Groups

By default, `uv sync` installs:

- base dependencies
- `dev`
- `notebook`
- `data`
- `stats`

Optional groups are available when needed:

| Group | What it adds |
| --- | --- |
| `data-pandas` | pandas and pandas-stubs |
| `validation` | pandera with polars support |
| `vis-static` | matplotlib and seaborn |
| `vis-interactive` | plotly |
| `ml` | scikit-learn |
| `app` | streamlit |

Examples:

```bash
uv sync --group data-pandas
uv sync --group validation
uv sync --group vis-static --group vis-interactive
uv sync --group ml
uv sync --all-groups
```

Use `uv add` instead of hand-editing `pyproject.toml` where possible:

```bash
uv add duckdb
uv add --dev mypy
uv add --group vis-static matplotlib seaborn
uv add --group ml xgboost
```

If code in `src/` imports a package at runtime, add it to base dependencies. If
it is only for a particular optional workflow, add it to a named group.

## Updating A Generated Project

Generated projects should update from `ds-template`, not directly from
`py-template`. Base template improvements flow into `ds-template` first, then
into generated projects through Copier.

Commit `.copier-answers.yml` in generated projects. Copier uses it to know how
the project was rendered and how future updates should be applied.

Recommended update process:

```bash
git status
uvx copier update
uv sync
uv run pre-commit run --all-files
uv run pytest -q
git add .
git add uv.lock
git add .copier-answers.yml
git commit -m "Update project from ds-template"
```

Commit or stash local work before running `copier update`. If Copier reports
conflicts, resolve them like normal Git conflicts and keep project-specific work
unless the incoming template change is clearly a shared tooling or structure
fix.

## Lockfile And CI Policy

Generated projects are rendered without a `uv.lock`. The first `uv sync` creates
it. Commit that file early and keep it in version control.

Generated project CI installs from the committed lockfile with
`uv sync --frozen --all-groups`. Dependabot is configured to open weekly PRs for
uv dependency and GitHub Actions updates.

Template maintenance CI is different on purpose: it renders a sample project and
checks that the onboarding path still works.

## Maintaining This Template

This repository is the template source, not a generated project.

The `template/` directory contains the Copier template source. Files ending in
`.jinja` are rendered during `copier copy`; plain files are copied as-is.

`.jinja` template files cannot be linted or formatted directly because ruff and
mypy do not understand Jinja syntax. Quality checks run against rendered output
in `.rendered/`.

Useful commands:

| Command | What it does |
| --- | --- |
| `just check` | Render template and run the full check suite |
| `just render` | Render only, into `.rendered/` |
| `just clean` | Delete `.rendered/` |

Run the full local quality gate before opening a PR:

```bash
just check
```

This renders the template, installs all dependency groups, then runs formatting,
linting, marimo checks, type checking, tests, and packaging checks against the
rendered project.

## Upstream Sync

The update chain is:

```text
py-template -> ds-template -> generated user projects
```

This template tracks `py-template` manually. See `UPSTREAM.md` for the current
base ref, downstream-owned overlay areas, extension blocks, and validation
process.
