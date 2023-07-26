from pydantic import BaseModel, Field


class UserPinfl(BaseModel):
    """
        user pinfl is needed for getting the result of weights
    """
    pinfl: str = Field(..., max_length=14)


class UnEmploymentWeightResponse(BaseModel):
    pass


