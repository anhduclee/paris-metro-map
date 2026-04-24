from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field

class Settings(BaseSettings):
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_USER: str | None = None
    MONGO_PASSWORD: str | None = None
    MONGO_DB_NAME: str

    @computed_field
    @property
    def MONGO_URL(self) -> str:
        if self.MONGO_USER and self.MONGO_PASSWORD:
            return f"mongodb://{self.MONGO_USER}:{self.MONGO_PASSWORD}@{self.MONGO_HOST}:{self.MONGO_PORT}"
        return f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()