from pydantic import BaseModel, Field


class CandidateRouteResponse(BaseModel):
    candidate_route_id: str
    market_id: str

    origin: str
    destination: str

    planning_year: int
    aircraft_type: str

    flights_per_day: int = Field(..., ge=0)
    annual_flights: int = Field(..., ge=0)

    distance_km: int = Field(..., ge=0)
    block_time_hours: float = Field(..., ge=0)

    seat_capacity: int = Field(..., ge=0)
    annual_seat_capacity: int = Field(..., ge=0)

    forecast_demand: int = Field(..., ge=0)
    expected_passengers: int = Field(..., ge=0)
    expected_load_factor: float = Field(..., ge=0)

    average_fare: float = Field(..., ge=0)
    ancillary_revenue_per_passenger: float = Field(..., ge=0)
    cargo_revenue: float = Field(..., ge=0)

    total_revenue: float = Field(..., ge=0)

    fuel_cost: float = Field(..., ge=0)
    maintenance_cost: float = Field(..., ge=0)
    crew_cost: float = Field(..., ge=0)
    airport_cost: float = Field(..., ge=0)
    navigation_cost: float = Field(..., ge=0)
    handling_cost: float = Field(..., ge=0)
    catering_cost: float = Field(..., ge=0)
    aircraft_ownership_or_lease_cost: float = Field(..., ge=0)
    other_cost: float = Field(..., ge=0)

    total_cost: float = Field(..., ge=0)
    operating_profit: float