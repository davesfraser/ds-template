# Marks your project as a real Python package
# This file defines what the package exposes at top level

from .config import Settings, get_settings

# Re-export the settings type and loader so users have one clean import path
# Export get_settings rather than a pre-built settings object
# This keeps package import simple and avoids hidden side effects during import
__all__ = ["Settings", "__version__", "get_settings"]

# Single source of truth for the package version
# Matches the version in pyproject.toml
# Usage: from {{ package_name }} import __version__
__version__ = "0.1.0"
