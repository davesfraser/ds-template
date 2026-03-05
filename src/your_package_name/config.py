from __future__ import annotations

# BaseSettings lets us load settings from environment variables
# This is nicer than sprinkling os.getenv calls all over the project
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # A typed place for project settings
    # Good for API keys, file paths, feature flags, and similar config

    model_config = SettingsConfigDict(
        # Load values from a local .env file if present
        env_file=".env",
        env_file_encoding="utf-8",
        # Ignore extra env vars instead of crashing
        # Helpful because real machines usually have lots of unrelated env vars
        extra="ignore",
    )

    # Very small starter example setting
    project_name: str = "your-project-name"


# Create one shared settings object to import across the project
settings = Settings()
