from pydantic import BaseModel, Field


class ScenarioRouteResponse(BaseModel):
    scenario_route_id: str
    scenario_id: str
    candidate_id: str
    market_id: str

    origin: str
    destination: str

    proposed_aircraft: str
    proposed_flights_per_day: float = Field(..., ge=0)

    estimated_monthly_passengers: float = Field(..., ge=0)
    estimated_monthly_revenue: float = Field(..., ge=0)
    estimated_monthly_cost: float = Field(..., ge=0)

    estimated_monthly_profit: float

    estimated_load_factor: float = Field(..., ge=0)

    planning_status: str
    data_type: str