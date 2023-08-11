import json

from fastapi import APIRouter
from kafka import KafkaProducer


router = APIRouter()


@router.post('/producer/',  tags=['producers'])
async def producer():
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        api_version=(0, 11, 5),
        value_serializer=lambda x:
        json.dumps(x).encode('utf-8')
    )
    for e in range(3):
        data = {'number': e}
        producer.send('event', value=data)
        producer.flush()
    return {'status': 'ok'}


@router.post('/hello/',  tags=['producers'])
async def hello():
    return {'status': 'ok'}