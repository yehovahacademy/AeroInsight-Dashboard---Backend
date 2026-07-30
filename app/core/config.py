from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    AEROAPI_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()