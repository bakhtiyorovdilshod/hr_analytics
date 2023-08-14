from fastapi import APIRouter, Depends
from fastapi import status
from motor.motor_asyncio import AsyncIOMotorClient

from src.db.mongodb import get_database
from src.event.schemas.event import EventSchema, response_model
from src.event.services.event import event_crud_service

router = APIRouter()


@router.post(
    '/',
    name="event:create",
    response_description='event create api',
    status_code=status.HTTP_201_CREATED
)
async def event_create(obj_in: EventSchema):
    event_data = EventSchema(**obj_in.dict())
    new_event = await event_crud_service.create_event(event=event_data)
    return response_model(new_event, "Event added successfully.")