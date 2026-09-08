from pydantic import BaseModel, Field


class OperatingCostResponse(BaseModel):
    cost_id: str
    market_id: str
    aircraft_type: str

    estimated_cost_per_flight: float = Field(..., ge=0)

    fuel_cost_component: float = Field(..., ge=0)
    airport_cost_component: float = Field(..., ge=0)
    crew_cost_component: float = Field(..., ge=0)
    maintenance_cost_component: float = Field(..., ge=0)
    other_cost_component: float = Field(..., ge=0)

    data_type: str