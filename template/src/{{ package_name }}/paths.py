from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    """Return the absolute path to the checked-out project root."""
    return Path(__file__).resolve().parents[2]


# Add project-level path constants here as the project grows.
# Keeping them in one module avoids rebuilding paths from strings throughout
# the codebase.
# project-template:extension:path-constants:start
DATA_DIR = project_root() / "data"
DATA_RAW = DATA_DIR / "raw"
DATA_INTERIM = DATA_DIR / "interim"
DATA_PROCESSED = DATA_DIR / "processed"
DATA_EXTERNAL = DATA_DIR / "external"

MODELS_DIR = project_root() / "models"
FIGURES_DIR = project_root() / "reports" / "figures"
NOTEBOOKS_DIR = project_root() / "notebooks"
# project-template:extension:path-constants:end
