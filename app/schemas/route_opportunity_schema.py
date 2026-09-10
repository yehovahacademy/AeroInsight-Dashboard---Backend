from pydantic import BaseModel, Field


class RouteOpportunityResponse(BaseModel):
    market_id: str

    origin: str
    destination: str
    planning_year: int

    forecast_demand: float = Field(..., ge=0)
    existing_capacity: float = Field(..., ge=0)
    capacity_gap: float

    expected_passengers: float = Field(..., ge=0)
    expected_load_factor: float = Field(..., ge=0)
    average_fare: float = Field(..., ge=0)

    revenue_opportunity: float = Field(..., ge=0)
    estimated_operating_cost: float = Field(..., ge=0)
    profit_opportunity: float

    profit_margin: float

    competition_score: float = Field(..., ge=0)
    demand_score: float = Field(..., ge=0)
    capacity_gap_score: float = Field(..., ge=0)
    fare_score: float = Field(..., ge=0)
    profitability_score: float = Field(..., ge=0)
    strategic_score: float = Field(..., ge=0)
    risk_score: float = Field(..., ge=0)

    opportunity_score: float = Field(..., ge=0)

    recommendation: str
    data_type: str