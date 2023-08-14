import secrets
import os
from typing import List, Optional, Union
from pydantic_settings import BaseSettings

from pydantic import AnyHttpUrl, HttpUrl
from databases import DatabaseURL
import os
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # JWT Token Config
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 #7 days
    JWT_ALGORITHM: str = "HS256"
    JWT_AUDIENCE: str = "smartgoo:auth"
    JWT_TOKEN_PREFIX: str = "Bearer"

    SERVER_NAME: str = ''
    SERVER_HOST: str = ''

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:5173"]

    PROJECT_NAME: str = 'Hr Analytics'
    VERSION: str = '1.0.0'
    SENTRY_DSN: Optional[HttpUrl] = None

    # MongoDB config
    MONGODB_MAX_CONNECTIONS_COUNT: int = 10
    MONGODB_MIN_CONNECTIONS_COUNT: int = 10
    MONGODB_HOST: str = os.environ.get('MONGODB_HOST')
    MONGODB_PORT: int = os.environ.get('MONGODB_PORT')
    MONGODB_USER: str = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
    MONGODB_PASSWORD: str = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
    MONGODB_DB: str = os.environ.get('MONGO_INITDB_DATABASE')
    MONGODB_CONN_STRING: str = os.environ.get('DATABASE_URL')

    EVENT_COLLECTIONS: str = 'events'

    class Config:
        case_sensitive = True


settings = Settings()
