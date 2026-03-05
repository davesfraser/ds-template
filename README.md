# your-project-name

A modern data science project template

## What this is

This repo is a starter template for Python data science projects using:

- `uv` for environments and dependency management
- `hatchling` for packaging
- `ruff` for linting and formatting
- `ty` for type checking
- `pytest` for tests
- `marimo` for notebook-style exploration as `.py` files

## Why this template exists

The goal is to start projects with:

- a real `src/` package layout
- clean tooling from day one
- fewer hidden notebook problems (no Jupyter in sight!)
- better reproducibility
- a setup that works well with Git and VS Code

## To use this template

Before starting development, replace the placeholder names used in this repo

### 1. Choose your names

- project/repo name: `my-project-name`
- Python package name: `my_project_name`

### 2. Rename the package folder

Rename:
`src/your_package_name`

to:
`src/my_project_name`

### 3. Update placeholder text inside files

Edit these files and replace placeholder values:

- `pyproject.toml`
- `src/your_package_name/config.py`
- `tests/test_smoke.py`
- `README.md`

### Example

For a project called `customer-churn-model`:

- repo name: `customer-churn-model`
- package name: `customer_churn_model`
- package folder: `src/customer_churn_model`
