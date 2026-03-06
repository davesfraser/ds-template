from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    # Find the repo root from this file location
    # Useful in DS projects because code often needs stable paths to data/, models/, reports/, etc
    return Path(__file__).resolve().parents[2]


# Common path constant for data files
DATA_DIR = project_root() / "data"
