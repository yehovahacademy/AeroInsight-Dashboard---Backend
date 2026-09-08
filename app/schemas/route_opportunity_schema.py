from pydantic import BaseModel, Field


class RouteOpportunityResponse(BaseModel):
    market_id: str

    annual_demand: float = Field(..., ge=0)
    annual_existing_capacity: float = Field(..., ge=0)

    average_load_factor: float = Field(..., ge=0)
    average_fare: float = Field(..., ge=0)

    competition_level: str

    capacity_gap: float

    estimated_revenue_potential: float = Field(..., ge=0)
    estimated_profit_potential: float

    aircraft_suitability_score: float = Field(..., ge=0)
    seasonality_score: float = Field(..., ge=0)
    network_connectivity_score: float = Field(..., ge=0)

    overall_opportunity_score: float = Field(..., ge=0)

    recommendation: str
    data_type: str