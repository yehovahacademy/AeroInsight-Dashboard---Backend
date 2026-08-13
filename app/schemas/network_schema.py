from pydantic import BaseModel
from typing import Optional



class RouteSummary(BaseModel):
    id: str
    origin: str
    destination: str
    originCode: str
    destinationCode: str

    loadFactor: int
    revenue: str
    recommendation: str


class NetworkSummary(BaseModel):
    total_routes: int
    average_load_factor: float
    high_revenue_routes: int
    recommendations: dict[str, int]


class RouteRequest(BaseModel):
    origin: str
    destination: str
    aircraft: Optional[str] = None        # ← was required, now optional
    season: Optional[str] = None          # ← missing, added
    flights_per_day: Optional[str] = None


class RouteAnalysis(BaseModel):
    origin: str
    destination: str
    
    distance_km: float
    estimated_duration: str
    
    demand_score: int
    weather_risk: str
    
    estimated_revenue: float
    estimated_cost: float
    estimated_profit: float
    
    recommendation: str