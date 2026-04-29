# ds-template

Specialised Copier template for code-first data science projects.

This repository is a fully materialised downstream of `py-template`. It keeps
the shared Python project mechanics from the base template and applies a
data-science overlay for notebooks, data folders, scientific dependency groups,
analysis guidance, and DS-specific AI coding skills.

## What This Template Provides

- `src/` package layout with typed settings and project path constants
- `uv` dependency and environment management
- scientific dependency groups for notebooks, data, stats, validation,
  visualisation, ML, and apps
- marimo notebooks under `notebooks/marimo/`
- data/model/report folders with Git-friendly placeholders
- ruff, mypy, pytest, coverage, pre-commit, and GitHub Actions CI
- DS-specific `AGENTS.md` guidance and `.github/skills/`
- generated `.copier-answers.yml` for future `copier update`

## Use The Template

```bash
copier copy https://github.com/davesfraser/ds-template.git <project>
```

Generated projects should commit both `uv.lock` and `.copier-answers.yml`.

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

`just check` renders the current working tree into `.rendered/`, installs all
dependency groups, then runs formatting, linting, marimo checks, type checking,
tests, and packaging checks against the rendered project.

## Upstream Sync

This template tracks `py-template` manually. See `UPSTREAM.md` for the exact
base ref, downstream-owned overlay areas, extension blocks used, and validation
commands.

The update chain is:

```text
py-template -> ds-template -> generated user projects
```

Generated projects update from `ds-template` with `copier update`. They should
not pull directly from `py-template`; base template improvements are first
synced into this repository by maintainers and then released through
`ds-template`.
