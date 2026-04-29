# Upstream Base

- Upstream repository: `davesfraser/py-template`
- Upstream ref: `c94cf630972ed4aeafde5e1cb0c2bb463c71dc43`
- Last sync date: 2026-04-29
- DS overlay source: `ds-template-source/archive/pre-split-ds-template`
- DS overlay source ref: `cbaa8d84f7a0ac19f8e053063bab0613c55a0647`

## Downstream-Owned Overlay

- Copier defaults: data-science project name and description.
- Dependency groups: `notebook`, `data`, `data-pandas`, `stats`,
  `validation`, `vis-static`, `vis-interactive`, `ml`, and `app`.
- Generated folders: `data/`, `notebooks/marimo/`, `models/`, and
  `reports/figures/`.
- Package additions: data-science path constants, settings fields, and smoke
  tests.
- Guidance: generated README/AGENTS DS workflow sections.
- Tooling: marimo CI check, notebook/script lint paths, large-file pre-commit
  safeguard.
- Skills: `.github/skills/*/SKILL.md.jinja`.

## Extension Blocks Used

- `project-template:extension:dependency-groups`
- `project-template:extension:uv-default-groups`
- `project-template:extension:ruff-settings`
- `project-template:extension:ruff-select`
- `project-template:extension:ruff-per-file-ignores`
- `project-template:extension:mypy-settings`
- `project-template:extension:path-constants`
- `project-template:extension:settings-fields`
- `project-template:extension:smoke-tests`
- `project-template:extension:agent-commands`
- `project-template:extension:agent-linting`
- `project-template:extension:downstream-rules`
- `project-template:extension:readme-common-commands-after`
- `project-template:extension:readme-domain`

## Validation

Run from this template repository:

```bash
just check
```

Rendered project checks included in `just check`:

```bash
uv sync --all-groups
uv run ruff format --check .
uv run ruff check src tests notebooks scripts
uv run marimo check notebooks/marimo
uv run mypy src tests
uv run pytest -q
uv build
```

## Sync From py-template

Use this process when bringing new base-template changes into `ds-template`.
The public `main` branch is protected, so publish the sync as a pull request.

```bash
git checkout main
git pull origin main
git fetch py-template
git checkout -b sync/py-template-<version-or-date>
```

Review the change between the currently recorded base ref and the target ref:

```bash
git diff <old-py-template-ref>..<new-py-template-ref>
```

Apply base-owned changes into this repository, keeping data-science additions
inside `project-template:extension:*` blocks or in clearly DS-owned files and
folders. Then update the upstream ref and sync date at the top of this file.

Validate before pushing:

```bash
just check
```

Push the branch and open a pull request:

```bash
git push origin sync/py-template-<version-or-date>
```

Generated projects created from `ds-template` should update from `ds-template`
with `copier update`, not directly from `py-template`.
