# This file makes the folder a proper Python package and controls
# what you get when you do `from {{ package_name }} import ...`

from importlib.metadata import PackageNotFoundError, version

from .config import Settings, get_settings

__all__ = ["Settings", "__version__", "get_settings"]

# Read the version from the installed package metadata, which is written
# by hatchling from pyproject.toml at install time
# This means pyproject.toml is the only place you ever need to change it
try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    # Fallback for the rare case where someone runs files directly
    # before running `uv sync`. Returns a sentinel so the import
    # still works rather than crashing.
    __version__ = "0.0.0+unknown"
