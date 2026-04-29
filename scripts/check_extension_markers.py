from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_EXTENSION_BLOCKS = {
    "template/AGENTS.md.jinja": [
        "priority-rules",
        "agent-commands",
        "agent-linting",
        "downstream-rules",
    ],
    "template/README.md.jinja": [
        "readme-common-commands-before",
        "readme-common-commands-after",
        "readme-domain",
    ],
    "template/.github/workflows/CI.yaml.jinja": [
        "ci-install",
        "ci-extra-checks",
    ],
    "template/.pre-commit-config.yaml": [
        "pre-commit-hooks",
    ],
    "template/pyproject.toml.jinja": [
        "project-dependencies",
        "dependency-groups",
        "uv-default-groups",
        "pytest-testpaths",
        "pytest-addopts",
        "ruff-settings",
        "ruff-select",
        "ruff-ignore",
        "ruff-per-file-ignores",
        "mypy-settings",
    ],
    "template/src/{{ package_name }}/paths.py": [
        "path-constants",
    ],
    "template/src/{{ package_name }}/settings.py": [
        "settings-fields",
    ],
    "template/tests/test_smoke.py.jinja": [
        "smoke-tests",
    ],
}


def marker(name: str, edge: str) -> str:
    return f"project-template:extension:{name}:{edge}"


def resolve_marker_path(relative_path: str) -> Path | None:
    """Return the template source path for a marker inventory entry."""
    path = ROOT / relative_path
    if path.exists():
        return path

    jinja_path = ROOT / f"{relative_path}.jinja"
    if jinja_path.exists():
        return jinja_path

    return None


def check_file(relative_path: str, block_names: list[str]) -> list[str]:
    path = resolve_marker_path(relative_path)
    if path is None:
        return [f"{relative_path}: missing file"]

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    for name in block_names:
        start = marker(name, "start")
        end = marker(name, "end")
        start_count = text.count(start)
        end_count = text.count(end)
        if start_count != 1:
            errors.append(f"{relative_path}: expected exactly one {start!r}, found {start_count}")
        if end_count != 1:
            errors.append(f"{relative_path}: expected exactly one {end!r}, found {end_count}")
        if start_count == 1 and end_count == 1 and text.index(start) > text.index(end):
            errors.append(f"{relative_path}: {start!r} appears after {end!r}")
    return errors


def main() -> int:
    errors = [
        error
        for relative_path, block_names in REQUIRED_EXTENSION_BLOCKS.items()
        for error in check_file(relative_path, block_names)
    ]
    if errors:
        print("Extension marker check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Extension marker check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
