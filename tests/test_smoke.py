from __future__ import annotations

# Import something simple from the package
# This proves the package can be imported and basic config works
from your_package_name.config import settings


def test_settings_load() -> None:
    # Tiny smoke test
    # Good starter test because it catches broken imports or config setup early
    assert settings.project_name == "your-project-name"
