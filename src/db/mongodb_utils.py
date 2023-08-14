from fastapi import FastAPI

from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import settings
from src.db.mongodb import db


def connect_to_mongo(app: FastAPI):
    print('connecting to database')
    db.client = AsyncIOMotorClient(str(settings.MONGODB_CONN_STRING),
                                   maxPoolSize=settings.MONGODB_MAX_CONNECTIONS_COUNT,
                                   minPoolSize=settings.MONGODB_MIN_CONNECTIONS_COUNT)
    app.state._db_client = db.client
    print('connected')


def close_mongo_connection(app: FastAPI):
    print('closing database connection')
    db.client.close()
    print('closed')


async def init_mongo(db_name: str, db_url: str, collection: str):
    """

    Args:
        db_name:
        db_url:
        collection:

    Returns:

    """
    mongo_client = AsyncIOMotorClient(db_url)
    mongo_database = mongo_client[db_name]
    mongo_collections = {
        collection: mongo_database.get_collection(collection),
    }
    # return {0: mongo_client, 1: mongo_database, 2: mongo_collections}
    return mongo_client, mongo_database, mongo_collections