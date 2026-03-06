from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from .paths import project_root

# BaseSettings lets us load settings from environment variables
# This is nicer than sprinkling os.getenv calls all over the project


class Settings(BaseSettings):
    """Typed settings loaded from environment variables and the repo .env file"""

    # Point directly at the repo .env file
    # This avoids confusing behaviour where running code from a different folder
    # causes the settings loader to miss the intended .env file
    model_config = SettingsConfigDict(
        env_file=project_root() / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Keep a harmless default so the template works straight away
    # Teams can replace this with real settings as the project grows
    project_name: str = "your-project-name"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return one cached Settings instance for the current process"""

    # Load settings only when they are actually needed
    # This avoids import-time failures later if someone adds required config fields
    # The cache means we still create the settings object only once per process
    return Settings()
