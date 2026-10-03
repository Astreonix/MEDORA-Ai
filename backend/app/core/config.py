from functools import lru_cache
from typing import Any

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "MEDORA API"
    environment: str = "development"
    database_url: str = "sqlite+pysqlite:///:memory:"
    jwt_secret: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    cors_origins: list[str] = [
        "http://localhost:5173",
        "https://medora-ai-psi.vercel.app",
    ]
    max_upload_bytes: int = 15 * 1024 * 1024
    llm_provider: str = "fallback"
    gemini_api_key: str = ""
    gemini_model: str = "gemini-1.5-flash"
    gemini_embed_model: str = "text-embedding-004"
    rag_min_score: float = 0.45
    emergency_number: str = "local emergency services"
    enable_demo: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", case_sensitive=False)

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_origins(cls, value: Any) -> Any:
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value

    @field_validator("database_url", mode="before")
    @classmethod
    def normalize_database_url(cls, value: Any) -> str:
        if not value:
            return "sqlite+pysqlite:///:memory:"
        value = str(value).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1].strip()
        if value.startswith("postgres://"):
            return "postgresql+psycopg://" + value[len("postgres://") :]
        if value.startswith("postgresql://") and "+psycopg" not in value:
            return "postgresql+psycopg://" + value[len("postgresql://") :]
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()