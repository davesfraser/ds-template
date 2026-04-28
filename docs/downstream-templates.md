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

## First Downstream: ds-template

`ds-template` should be rebuilt as the first downstream template. It should add
scientific dependency groups, marimo notebooks, data/model/report folders,
analysis-specific path constants and settings, data-science skills, and
data-science AGENTS rules on top of this base.
