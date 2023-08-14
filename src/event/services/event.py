from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import settings
from src.event.schemas.event import EventSchema


class EventCrudService:
    collection: str = settings.EVENT_COLLECTIONS

    async def create_event(self,event: EventSchema) -> dict:
        from src.core.app import app
        # event = await db.get_collection('events').insert_one(event.dict())
        # event_out = await db[self.collection].find_one({"_id": event.inserted_id})
        event = app.state.mongo_collection[settings.EVENT_COLLECTIONS].insert_one(event.dict())
        # event_out = app.state.mongo_collection[settings.EVENT_COLLECTIONS].find_one({"_id": event.inserted_id})
        return {}


event_crud_service = EventCrudService()

