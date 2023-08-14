from datetime import datetime

from pydantic import BaseModel, Field


class EventSchema(BaseModel):
    event_id: int = Field(...)
    organization_id: int = Field(...)
    username: str = Field(...)
    full_name: str = Field(...)
    time: str = Field(...)

    class Config:
        json_schema_extra = {
            'example': {
                'event_id': 23,
                'organization_id': 23,
                'username': '82838232',
                'full_name': 'Dilshod Bakhtiyorov',
                'time': '2023-08-09:08:31:00'
            }
        }


def response_model(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message
    }


def error_response_model(error, code, message):
    return {
        'error': error,
        'code': code,
        'message': message
    }