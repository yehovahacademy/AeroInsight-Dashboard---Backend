from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_NINJAS_KEY: str
    AVIATIONSTACK_API_KEY: str | None = None
    FLIGHTAWARE_API_KEY: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()