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
- built-in AI coding assistant integration with project conventions and data science best-practice standards that load automatically in Copilot, Cursor, Gemini Code Assist, Claude Code, and others

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

Generated projects ship with structured guidance that AI coding assistants pick up automatically. This means assistants like Copilot, Cursor, Gemini Code Assist, and Claude Code generate code that follows your project's conventions without you having to explain them on every prompt.

### What loads automatically

When you open a generated project, your AI assistant reads `AGENTS.md` from the project root without any configuration. This file contains project-specific rules: where code lives, how paths and settings are imported, polars-first conventions, and the commands to run. The following assistants pick it up automatically:

- GitHub Copilot
- Cursor
- Gemini Code Assist (as `AGENT.md`)
- Claude Code (as `CLAUDE.md`)
- OpenAI Codex, Google Jules, Windsurf, Zed, Warp, Amp, and others

All four files (`AGENTS.md`, `AGENT.md`, `CLAUDE.md`, `.github/copilot-instructions.md`) are generated from a single source at `.ai/agent-instructions.md` — edit that file to update conventions across all assistants at once.

### Loading data science best-practice standards

`.ai/ds-rules.md` contains a comprehensive set of analytical standards covering experimental design, hypothesis testing, EDA, data leakage prevention, model evaluation, and visualisation. Load it at the start of any analytical task:

| Assistant | How to load |
|---|---|
| GitHub Copilot in VS Code | Type `/ds-rules` in Copilot Chat |
| Gemini Code Assist | Type `@.ai/ds-rules.md` in the chat |
| Claude Code | Type `@.ai/ds-rules.md` in the chat |
| Cursor | Drag `.ai/ds-rules.md` into the chat window |
| Windsurf | Drag `.ai/ds-rules.md` into the chat window |

### Example usage

Starting an EDA task in Copilot Chat:
```
/ds-rules

I have a dataset at data/raw/survey_2024.parquet with columns: age, income,
region, churn. Walk me through an EDA for a churn prediction project.
```

Starting a modelling task in Cursor:
```
[drag .ai/ds-rules.md into chat]

Build a baseline churn classification model using the processed dataset
at data/processed/features.parquet. Follow the structured analysis workflow
checklist.
```

Starting any task in Claude Code:
```
@.ai/ds-rules.md @AGENTS.md

Write a function in src/ to load and validate the raw survey data,
checking schema, nulls, and class balance.
```

### Updating AI instructions for your project

As your project evolves, update `.ai/agent-instructions.md` to reflect any project-specific conventions. This is the single source of truth — do not edit `AGENTS.md`, `CLAUDE.md`, or `AGENT.md` directly as they are generated files.

---

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

- `data-pandas`
- `validation`
- `vis-static`
- `vis-interactive`
- `ml`

Examples:
```bash
uv sync
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
reports/figures/        generated figures
.ai/                    AI assistant guidance files
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

The AI assistant instruction files (`AGENTS.md`, `CLAUDE.md`, `AGENT.md`,
`.github/copilot-instructions.md`) are generated from
`template/.ai/agent-instructions.md.jinja` — do not edit them directly.
