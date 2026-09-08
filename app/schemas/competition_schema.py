from pydantic import BaseModel, Field
from typing import Optional


class CompetitionBase(BaseModel):
    market_id: str
    airline: str
    nonstop: bool
    weekly_frequency: int
    aircraft_type: str
    estimated_market_share: float = Field(..., ge=0, le=100)
    competition_strength: str
    data_type: str = "SYNTHETIC"


class CompetitionCreate(CompetitionBase):
    competition_id: str


class CompetitionResponse(CompetitionBase):
    competition_id: str

    class Config:
        from_attributes = True