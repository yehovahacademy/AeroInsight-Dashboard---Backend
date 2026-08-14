from pydantic import BaseModel

class DemandForecastDay(BaseModel):
    date: str
    day: str
    demand_score: float
    demand_level: str
    estimated_load_factor: float


class DemandForecastResponse(BaseModel):
    route: str
    origin: str
    destination: str
    forecast_horizon_days: int
    average_demand_score: float
    demand_level: str
    average_load_factor: float
    trend: str
    peak_day: DemandForecastDay
    recommendation: str
    forecast: list[DemandForecastDay]
   