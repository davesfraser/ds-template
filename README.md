# 2026 Data science template

A modern Python data science project template with reproducible environments, a proper `src/` layout, fast tooling, and Git-friendly notebook-style exploration.
***Read this first and later replace it with your own README!***

## What this template is

This repo is a starter template for Python data science projects using:

- `copier` for converting this template into a personalised project
- `uv` for environment and dependency management
- `hatchling` for packaging
- `ruff` for linting and formatting
- `ty` for type checking
- `pytest` for tests
- `marimo` for notebook-style exploration as `.py` files
- Ships with basic CI testing for all code pushed to master, see `.github/workflows/CI.yaml`)

The goal is to give you a strong default project structure from day one rather than starting with a loose folder of scripts and notebooks.

## Create a new project from this template

**NOTE: Recommended path for users wanting to utilise this template for a project is ***copier*****

- Copier handles renaming the project and package to meet your requirements, it also excludes any files that are not needed
- Github offers 'Use this template' but don't use it. Copier is super simple, uv can temporarily and seamlessly install copier and also convert the template for you in one line!

```bash
uvx copier copy https://github.com/YOUR-ORG/YOUR-REPO.git my-new-project
cd my-new-project
uv sync
code .
```

## Why this template exists

I wanted to create a starting point for data science projects that is relevant for 2026, it is designed to give you:

- a real `src/` package layout
- clean tooling from the start
- reproducible environments via a lockfile
- notebook-style exploration in `notebooks/marimo/` without hidden state all over the place (Jupyter begone!)
- a setup that works well with git and VS Code
- lightweight packaging so the project behaves like a real Python package, not just a folder on your machine

## Template defaults and design choices

### Python version

This template targets **Python 3.13+** by default via `pyproject.toml`.
That means the tooling, type checking, linting, and CI are all set up around a modern Python baseline rather than trying to support a wide historical range of versions.
If your project needs broader compatibility you can request a different version upon setup with copier.

### Dependency management with uv

This template uses `uv` as the main workflow tool for Python environments, dependencies, lockfiles, and command execution.

Why this is a good default:

- it is fast
- it keeps project setup simple
- it gives you a lockfile for reproducible installs
- it handles dependency groups cleanly
- it lets you run project commands without needing a pile of shell-specific setup

This template defines grouped dependencies so projects can stay tidy as they grow.

By default, `uv sync` installs:

- the base project dependencies
- the `dev` dependency group
- the `notebook` dependency group
- the `data` dependency group
- the `stats` dependency group

This is intentional
A fresh clone should allow a data scientist to have all the package dependencies they need to get started
The remaining groups are opt-in so the default environment still stays somewhat focused rather than turning into a kitchen sink.

Optional groups in this template are:

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

## Common commands

| Task | Command |
|------|---------|
| Install all dependencies | `uv sync --all-groups` |
| Format code | `uv run ruff format .` |
| Lint | `uv run ruff check src tests notebooks` |
| Type check | `uv run ty check` |
| Run tests | `uv run pytest` |
| Full quality check (matches CI) | `uv run ruff format --check . && uv run ruff check src tests notebooks && uv run ty check && uv run pytest` |
| Open exploration notebook | `uv run marimo edit notebooks/marimo/01_exploration.py` |

### Type checking — `ty`

This template uses [`ty`](https://github.com/astral-sh/ty) for type checking. It's fast,
built by the same team as `ruff` and `uv`, and handles the vast majority of DS code well.

One thing to know: `ty` is pre-1.0, so you may occasionally hit a false positive.
Suppress it inline with a comment rather than working around it in your code:
```python
result = some_untyped_call()  # ty: ignore[possibly-unbound]
```

If your project needs `mypy` (e.g. for mypy plugins), just add it to the `dev` group
alongside `ty` — they coexist fine.

## Next steps

This template is a strong baseline, not a kitchen sink!

Depending on the kind of project, you may want to add a few extra tools later:

### For data science projects
You might want to add:
- `DuckDB` for fast local analytics and SQL-first exploration
- `DVC` if data or model artefacts get too large for Git or change often

### For machine learning projects
You might want to add:
- `MLflow` for experiment tracking and model lifecycle
- `XGBoost` or `LightGBM` for boosted tree models
- `PyTorch` if you are training neural networks

### For AI and LLM projects
You might want to add:
- `LangChain` or `LangGraph` for agent and tool-calling workflows
- `LlamaIndex` for retrieval-heavy or RAG-style applications
- `DSPy` if you want a more programmatic approach to LM workflows
- `OpenTelemetry` for tracing and observability

### General advice
Add these only when or if the project actually needs them!

Best practice is to start with a clean reproducible baseline.
