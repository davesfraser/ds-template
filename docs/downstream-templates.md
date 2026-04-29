# Downstream Templates

This repository is the canonical base for specialised Python Copier templates.
Downstream templates should stay fully materialised repositories that sync from
this base, then apply their own domain-specific overlay.

Copier supports applying multiple templates to one generated project with
separate answers files, but that is a user workflow. For specialised templates,
prefer a one-command user experience: users copy the specialised template once,
and maintainers keep that template aligned with `py-template`.

## Ownership

Base-owned files define shared Python project standards:

- Copier questions and validation
- package skeleton under `src/`
- generic README and AGENTS rules
- uv, ruff, mypy, pytest, coverage, pre-commit, Dependabot, and CI defaults
- extension placeholders such as `docs/`, `examples/`, `scripts/`,
  `tests/fixtures/`, `.github/skills/`, and `py.typed`

Downstream-owned files define domain behaviour:

- domain dependency groups and default install groups
- domain folders, examples, tests, scripts, and documentation
- domain-specific AI coding agent skills
- domain-specific AGENTS rules and README sections
- extra CI and pre-commit checks required by the domain

## Overlay Process

1. Start the downstream template from a known `py-template` release or commit.
2. Reapply downstream-owned files and changes at the extension markers.
3. Keep the generic base rules intact unless the downstream template has a
   clear reason to override them.
4. Render the downstream template locally and run its full quality gate.
5. Record the synced `py-template` ref in the downstream template's changelog or
   maintainer notes.

Use the `project-template:extension:*` comments as stable patch anchors. They
are not a custom templating system; they are human-readable seams that make
future syncs less fragile.

Prefer paired blocks:

```text
project-template:extension:<name>:start
downstream-owned content goes here
project-template:extension:<name>:end
```

When syncing from `py-template`, keep base-owned content outside those blocks
as close to upstream as possible. Put downstream additions inside the relevant
blocks or in clearly downstream-owned files and folders.

## Downstream Maintainer Notes

Each downstream template should keep a small `UPSTREAM.md` or maintainer note
with this shape:

```markdown
# Upstream Base

- Upstream repository: davesfraser/py-template
- Upstream ref: <tag-or-commit>
- Last sync date: <yyyy-mm-dd>

## Downstream-Owned Overlay

- Dependency groups:
- Generated folders:
- Package additions:
- README/AGENTS sections:
- CI/pre-commit additions:
- Skills/examples/scripts:

## Extension Blocks Used

- project-template:extension:<name>

## Validation

- just check
- rendered-project domain checks
```

This file is maintainer-facing. It does not need to be copied into generated
projects unless the downstream template intentionally wants users to see it.

## Release And Sync Checklist

Before rebuilding or updating a downstream template:

1. Run `just check` in `py-template`.
2. Tag or record the exact `py-template` commit to sync from.
3. Review this document for base-owned and downstream-owned boundaries.
4. Apply the downstream overlay at the extension markers.
5. Run the downstream template's full quality gate.
6. Record the synced `py-template` ref in the downstream changelog or maintainer notes.

Use semver-style tags such as `v0.1.0` and `v0.2.0` for `py-template` releases.
Treat changes to extension markers, generated project layout, CI, or tool
defaults as downstream-facing changes and mention them in release notes.

## Extension Marker Inventory

Current stable anchors are paired `:start` / `:end` blocks:

- `project-template:extension:project-dependencies` - add runtime dependencies.
- `project-template:extension:dependency-groups` - add optional dependency groups.
- `project-template:extension:uv-default-groups` - adjust default installed groups.
- `project-template:extension:pytest-testpaths` - add test directories.
- `project-template:extension:pytest-addopts` - add pytest flags.
- `project-template:extension:ruff-settings` - add top-level Ruff settings.
- `project-template:extension:ruff-select` - add Ruff rule families.
- `project-template:extension:ruff-ignore` - add ignored Ruff rules.
- `project-template:extension:ruff-per-file-ignores` - add file-specific lint policy.
- `project-template:extension:mypy-settings` - add mypy settings or overrides.
- `project-template:extension:ci-install` - adjust CI dependency installation.
- `project-template:extension:ci-extra-checks` - add CI quality steps.
- `project-template:extension:pre-commit-hooks` - add local commit hooks.
- `project-template:extension:path-constants` - add package-level path constants.
- `project-template:extension:settings-fields` - add settings fields.
- `project-template:extension:smoke-tests` - add template smoke tests.
- `project-template:extension:priority-rules` - add high-priority downstream AGENTS rules near the top.
- `project-template:extension:agent-commands` - add AGENTS command guidance.
- `project-template:extension:agent-linting` - add AGENTS linting/type guidance.
- `project-template:extension:downstream-rules` - add AGENTS rules.
- `project-template:extension:readme-common-commands-before` - add README commands before base checks.
- `project-template:extension:readme-common-commands-after` - add README commands after base checks.
- `project-template:extension:readme-domain` - add generated README guidance.

`just check` runs `scripts/check_extension_markers.py` so accidental marker
removal or malformed block ordering fails before rendering.

## First Downstream: ds-template

`ds-template` should be rebuilt as the first downstream template. It should add
scientific dependency groups, marimo notebooks, data/model/report folders,
analysis-specific path constants and settings, data-science skills, and
data-science AGENTS rules on top of this base.
