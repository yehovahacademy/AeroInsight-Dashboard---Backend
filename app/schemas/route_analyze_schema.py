# schemas.py
from pydantic import BaseModel
from typing import Optional, List

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
    aircraft: Optional[str] = None
    season: Optional[str] = None
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

# New: Simple route response for current backend
class SimpleRouteResponse(BaseModel):
    route_id: str
    origin_iata: str
    destination_iata: str
    distance_km: float
    region: str
    coordinates: Optional[dict] = None
    
    # Optional fields that will be populated when profitability engine is ready
    estimated_revenue: Optional[float] = None
    estimated_cost: Optional[float] = None
    estimated_profit: Optional[float] = None
    recommendation: Optional[str] = None