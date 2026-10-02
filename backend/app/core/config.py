from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "UWE MSc AI Platform"
    database_url: str = "postgresql://postgres:postgres@db:5432/uwe_ai"
    secret_key: str = "super-secret-key-change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()
