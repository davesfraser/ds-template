# your-project-name

A modern Python data science project template with reproducible environments, a proper `src/` layout, fast tooling, and Git-friendly notebook-style exploration.

## What it is

This repo is a starter template for Python data science projects using:

- `uv` for environment and dependency management
- `hatchling` for packaging
- `ruff` for linting and formatting
- `ty` for type checking
- `pytest` for tests
- `marimo` for notebook-style exploration as `.py` files

The goal is to give you a strong default project structure from day one rather than starting with a loose folder of scripts and notebooks.

## Why this template exists

I wanted to create a starting point for data science projects that is relevant for 2026, it is designed to give you:

- a real `src/` package layout
- clean tooling from the start
- reproducible environments via a lockfile
- notebook-style exploration in `marimo/` without hidden state all over the place (Jupyter begone!)
- a setup that works well with git and VS Code
- lightweight packaging so the project behaves like a real Python package, not just a folder on your machine

## Template defaults and design choices

### Python version

This template targets **Python 3.14+** by default via `pyproject.toml`.

That means the tooling, type checking, linting, and CI are all set up around a modern Python baseline rather than trying to support a wide historical range of versions.

If your project needs broader compatibility, change `requires-python` in `pyproject.toml` and update CI to test the versions that you care about.

### Dependency management with uv

This template uses `uv` as the main workflow tool for Python environments, dependencies, lockfiles, and command execution.

Why this is a good default:

- it is fast
- it keeps project setup simple
- it gives you a lockfile for reproducible installs
- it handles dependency groups cleanly
- it lets you run project commands without needing a pile of shell-specific setup

By default, `uv sync` installs:

- the base project dependencies
- the `dev` dependency group

Other groups are opt-in so a fresh project does not become bloated by default.

Current optional groups in this template are:

- `notebook`
- `data`
- `validation`
- `vis-static`
- `vis-interactive`
- `ml`

Examples:

```bash
uv sync
uv sync --group notebook
uv sync --group data --group ml
uv sync --all-groups
```

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
