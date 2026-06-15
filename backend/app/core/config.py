from pydantic_settings import BaseSettings
from pydantic import computed_field
from pathlib import Path

class Settings(BaseSettings):
    MONGO_INITDB_DATABASE: str
    MONGO_INITDB_ROOT_USERNAME: str | None = None
    MONGO_INITDB_ROOT_PASSWORD: str | None = None

    @computed_field
    @property
    def MONGO_URL(self) -> str:
        if self.MONGO_INITDB_ROOT_USERNAME and self.MONGO_INITDB_ROOT_PASSWORD:
            return f"mongodb://{self.MONGO_INITDB_ROOT_USERNAME}:{self.MONGO_INITDB_ROOT_PASSWORD}@database:27017"
        return f"mongodb://database:27017"

settings = Settings()