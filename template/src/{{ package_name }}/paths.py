from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    """Return the absolute path to the checked-out project root."""
    return Path(__file__).resolve().parents[2]


# Add project-level path constants here as the project grows.
# Keeping them in one module avoids rebuilding paths from strings throughout
# the codebase.
