from pydantic import BaseModel


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


class RouteResponse(BaseModel):
    routes: list[Route]    