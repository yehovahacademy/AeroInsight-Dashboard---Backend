from fastapi import APIRouter
from app.schemas.route_analyze_schema import NetworkSummary, RouteRequest


router = APIRouter(
    prefix="/api/network",
    tags=["Network Planning"],
)

@router.post("/analyze_route")
async def analyze_route(data: RouteRequest):

    distance = 1000
    revenue = 800000
    cost = 500000
    profit = revenue - cost

    return {
        "origin": data.origin,
        "destination": data.destination,
        "distance_km": distance,
        "estimated_duration": "2h 15m",
        "demand_score": 75,
        "weather_risk": "Low",
        "estimated_revenue": revenue,
        "estimated_cost": cost,
        "estimated_profit": profit,
        "recommendation": (
            "Route shows positive profitability and "
            "appears suitable for further network evaluation."
        ),
    }