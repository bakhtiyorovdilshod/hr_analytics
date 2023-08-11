import json
from fastapi import APIRouter
from kafka import KafkaConsumer

router = APIRouter()


@router.post('/consumer/',  tags=['consumers'])
async def consumer():
    consumer = KafkaConsumer(
        'event',
        bootstrap_servers=['localhost:29092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        api_version=(0, 11, 5)
    )
    result = []
    for message in consumer:
        message = message.value
        result.append(message)
        # event_collection.insert_one(message)
        print('{} added'.format(message))
    return {'status': 'ok'}


