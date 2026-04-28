from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    """Return the absolute path to the checked-out project root."""
    return Path(__file__).resolve().parents[2]


# Path constants for every folder the template creates
# Import these directly rather than rebuilding paths from strings throughout
# your code — it keeps things consistent and easy to refactor
#
# Example:
#   from {{ package_name }}.paths import DATA_RAW, MODELS_DIR
#   df = pd.read_parquet(DATA_RAW / "survey_2024.parquet")
