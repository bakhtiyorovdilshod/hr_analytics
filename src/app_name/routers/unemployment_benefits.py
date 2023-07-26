from fastapi import APIRouter, Request, Response
from typing import Optional
from src.relatives.services.integrator import integrator

from src.relatives.schemas.unemployment_benefits import UserPinfl, UnEmploymentWeightResponse

router = APIRouter(
    prefix='/unemployment',
    tags=['unemployment']
)


@router.post(
    "/family/weights/",
    response_model=UnEmploymentWeightResponse
)
async def family_weights(data: UserPinfl):
    # some async operation could happen here
    rejected_job_offers = await integrator.get_rejected_job_offers(pinfl=data.pinfl)

    return {'status': 'ok'}
