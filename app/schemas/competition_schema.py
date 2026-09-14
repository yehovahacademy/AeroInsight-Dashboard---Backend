
from pydantic import BaseModel, Field


class CompetitionBase(BaseModel):
    market_id: str
    year: int = Field(..., ge=2021, le=2026)
    airline_name: str
    is_direct_competitor: bool
    frequency_per_week: int = Field(..., gt=0)
    aircraft_type: str
    market_share: float = Field(..., ge=0, le=100)
    competitive_strength: str
    data_type: str = "SYNTHETIC"


class CompetitionCreate(CompetitionBase):
    competition_id: str


class CompetitionResponse(CompetitionBase):
    competition_id: str

    class Config:
        from_attributes = True

