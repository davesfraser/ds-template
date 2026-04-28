# py-template — Base Copier template for Python projects

This is a Copier template repository, not a runnable project.
AI coding assistants working in this repo must follow the rules below.

---

# How this repo works

The `template/` directory contains the Copier template source.
Files with a `.jinja` suffix are rendered through Jinja2 during `copier copy`.
Plain files are copied as-is.

Template variables (defined in `copier.yaml`):
- `{{ project_name }}` — human-readable project title
- `{{ project_slug }}` — kebab-case slug
- `{{ package_name }}` — snake_case Python package name
- `{{ project_description }}` — one-line description
- `{{ author_name }}`, `{{ author_email }}`
- `{{ python_min_version }}` — minimum Python version (3.12 or 3.13)

---

# Development rules

RULE: `.jinja` files cannot be linted or formatted directly — ruff and mypy
do not understand Jinja syntax. All quality checks run against the rendered
output in `.rendered/`.
RULE: For any change to a `.jinja` file, run `just check` before pushing.
This renders the template and runs the full quality gate against `.rendered/`.
RULE: Do not edit files in `.rendered/` — it is ephemeral output. Fix the
corresponding `.jinja` source in `template/` instead.
RULE: When adding a new file to the template, decide whether it needs `.jinja`
suffix (contains template variables) or not (static content copied as-is).
RULE: The `copier.yaml` `_exclude` list controls which files are NOT copied
into generated projects — check it when adding repo-level files that should
not propagate.

---

# Commands

| Command        | What it does                                          |
|----------------|-------------------------------------------------------|
| `just check`   | Render template and run full check suite — mirrors CI |
| `just render`  | Render only, output goes to `.rendered/`              |
| `just clean`   | Delete the `.rendered/` directory                     |

---

# Project stack

- Python 3.13+
- uv for dependency management
- Copier for template rendering
- ruff for linting and formatting
- mypy for type checking (excludes `template/`)
- pytest for testing rendered output
- pre-commit for git hooks

---

# Linting

Root `pyproject.toml` has minimal ruff config (E4/E7/E9, F, I only).
The template's `pyproject.toml.jinja` has the full rule set — those rules
apply to rendered projects, not to this repo directly.
