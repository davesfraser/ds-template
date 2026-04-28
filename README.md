# py-template

Base Copier template for modern Python projects.

This repository is the shared upstream for specialised Python project templates.
It owns the common project structure, development tooling, quality gates,
continuous integration, dependency-update automation, and AI-assisted coding
instructions that downstream templates inherit.

Specialised templates should keep domain-specific files, dependencies, examples,
and guidance in their own repositories. This base should stay small, predictable,
and broadly useful.

## What This Template Provides

- `src/` package layout
- `uv` dependency and environment management
- `ruff` linting and formatting
- `mypy` type checking
- `pytest` testing with coverage defaults
- `pre-commit` hooks
- GitHub Actions CI
- Dependabot configuration
- `AGENTS.md` and Copilot-compatible AI coding guidance

## Repository Layout

```text
copier.yaml                 Copier questions and template metadata
template/                   Files copied into generated projects
template/**/*.jinja         Files rendered with Copier/Jinja variables
.github/workflows/          CI for this template repository
justfile                    Local template maintenance commands
.rendered/                  Throwaway rendered output from local checks
```

Root-level files configure this template repository itself. Files under
`template/` become part of generated projects. If a file contains Copier
variables such as `{{ project_name }}`, it must use the `.jinja` suffix.

## Development

Install the template development tools:

```bash
uv sync
```

Render the template with default answers:

```bash
just render
```

Run the full local quality gate:

```bash
just check
```

Remove rendered output:

```bash
just clean
```

`just check` renders the current working tree into `.rendered/`, installs the
generated project dependencies, then runs formatting, linting, type checking,
tests, and packaging checks against the rendered project.

## Working On The Template

- Edit generated project files in `template/`, not `.rendered/`.
- Edit this repository's own tooling at the repo root.
- Run `just check` after changing any `.jinja` file.
- Keep root `pyproject.toml` minimal; generated project standards live in
  `template/pyproject.toml.jinja`.
- Keep `.rendered/` ephemeral. It is for inspection and checks only.

## Downstream Templates

Downstream templates should treat this repository as the canonical Copier base.
They can layer their own files, dependency groups, README content, AGENTS rules,
and workflows on top while tracking updates from this upstream.

Good candidates for downstream specialisation include analytics, AI
engineering, web services, CLIs, and internal company standards.

Shared Python best practices belong here. Domain-specific opinions belong in the
specialised template that needs them.
