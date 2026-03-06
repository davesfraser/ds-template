# Marks your project as a real Python package
# This file can also define what the package exposes at top level

from .config import Settings, get_settings

# Re-export the settings type and loader so users have one clean import path
# Export get_settings rather than a pre-built settings object
# This keeps package import simple and avoids hidden side effects during import
__all__ = ["Settings", "get_settings"]
