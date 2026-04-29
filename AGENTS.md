# ds-template — Data Science Copier template

This is a Copier template repository, not a runnable generated project.
AI coding assistants working in this repo must follow the rules below.

---

# How this repo works

This repository is a fully materialised downstream of `py-template`.

The `template/` directory contains the Copier template source. Files with a
`.jinja` suffix are rendered through Jinja2 during `copier copy`. Plain files
are copied as-is.

Template variables are defined in `copier.yaml`:

- `{{ project_name }}` — human-readable project title
- `{{ project_slug }}` — kebab-case slug
- `{{ package_name }}` — snake_case Python package name
- `{{ project_description }}` — one-line description
- `{{ author_name }}`, `{{ author_email }}`
- `{{ python_min_version }}` — minimum Python version

---

# Development rules

RULE: `.jinja` files cannot be linted or formatted directly.
RULE: For any change to a `.jinja` file, run `just check` before pushing.
RULE: Do not edit files in `.rendered/`; fix the corresponding source in
`template/` instead.
RULE: Keep base-owned content close to `py-template` and put DS-owned changes
inside `project-template:extension:*` blocks or clearly DS-owned folders.
RULE: Update `UPSTREAM.md` whenever syncing from a new `py-template` ref.

---

# Commands

| Command        | What it does                                          |
|----------------|-------------------------------------------------------|
| `just check`   | Render template and run full check suite — mirrors CI |
| `just render`  | Render only, output goes to `.rendered/`              |
| `just clean`   | Delete the `.rendered/` directory                     |

---

# Project stack

- Python 3.13+ for template maintenance
- Generated projects support Python 3.12 or 3.13
- uv for dependency management
- Copier for template rendering
- ruff for linting and formatting
- mypy for type checking
- pytest for tests
- marimo for generated notebooks
