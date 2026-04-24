from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGO_URL)
database = client[settings.MONGO_DB_NAME]

async def get_db() -> AsyncIOMotorDatabase:
    return database