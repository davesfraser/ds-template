# {{ project_name }}

{{ project_description }}

This repository contains a modern Python project.
AI coding assistants must follow the rules in this document when generating or modifying code.

---

# Core rules

RULE: Use `uv` for dependency management and command execution.
RULE: Keep reusable code in `src/`.
RULE: Put tests in `tests/`.
RULE: Write or update tests for behavioural changes.
RULE: Run ruff, mypy, and pytest before considering work complete.
RULE: Do not hardcode secrets, credentials, tokens, or environment-specific paths.
RULE: Prefer typed, small, testable functions.
RULE: Keep IO, configuration, and side effects separate from pure logic where practical.
RULE: Do not introduce new dependencies unless they are clearly justified.

---

# Project stack

- Python {{ python_min_version }}+
- uv for package and environment management
- ruff for linting and formatting
- mypy for static type checking
- pytest for tests

---

# Project structure

```text
src/{{ package_name }}/     reusable project code
tests/                      pytest tests
