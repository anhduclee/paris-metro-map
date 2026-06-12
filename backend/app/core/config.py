from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
from pathlib import Path

class Settings(BaseSettings):
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_DATABASE: str

    MONGO_INITDB_ROOT_USERNAME: str | None = None
    MONGO_INITDB_ROOT_PASSWORD: str | None = None

    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    @computed_field
    @property
    def MONGO_URL(self) -> str:
        if self.MONGO_INITDB_ROOT_USERNAME and self.MONGO_INITDB_ROOT_PASSWORD:
            return f"mongodb://{self.MONGO_INITDB_ROOT_USERNAME}:{self.MONGO_INITDB_ROOT_PASSWORD}@{self.MONGO_HOST}:{self.MONGO_PORT}"
        return f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()