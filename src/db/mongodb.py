from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import settings
from pymongo import mongo_client
import pymongo


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client[settings.MONGODB_DB]

