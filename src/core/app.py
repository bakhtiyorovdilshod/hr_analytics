from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from src.event.routers.consumer import router as consumer_router
from src.event.routers.producer import router as producer_router
from src.event.routers.event import router as event_router
from src.core.utils import create_start_app_handler, create_stop_app_handler
from ..db.mongodb_utils import init_mongo

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(prefix='/api/v1', router=consumer_router)
app.include_router(prefix='/api/v1', router=producer_router)
app.include_router(prefix='/api/v1', router=event_router)


# @app.on_event("startup")
# async def startup():
#     listen_kafka()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_event_handler("startup", create_start_app_handler(app))
# app.add_event_handler("shutdown", create_stop_app_handler(app))


@app.on_event("startup")
async def startup_event():
    print('startup')
    app.state.mongo_client, app.state.mongo_db, app.state.mongo_collection = await init_mongo(
        settings.MONGODB_DB, settings.MONGODB_CONN_STRING, settings.EVENT_COLLECTIONS
    )


@app.on_event("shutdown")
async def shutdown_event():
    print('shutdown_event')


