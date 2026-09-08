from pydantic import BaseModel, Field


class MarketFareResponse(BaseModel):
    fare_id: str
    market_id: str

    year: int
    month: int = Field(..., ge=1, le=12)

    average_one_way_fare_inr: float = Field(..., ge=0)

    business_fare_index: float = Field(..., ge=0)
    leisure_fare_index: float = Field(..., ge=0)

    fare_volatility: float = Field(..., ge=0)

    data_type: str