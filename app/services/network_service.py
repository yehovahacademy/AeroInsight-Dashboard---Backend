from fastapi import APIRouter, HTTPException
from app.schemas.network_schema import NetworkSummary, RouteRequest  # ← add RouteRequest schema


router = APIRouter(
    prefix="/api/network",
    tags=["Network Planning"],
)


@router.get("/summary", response_model=NetworkSummary)
async def summary():
    return network_service.get_summary()


@router.post("/analyze_route")          # ← decorator added
async def analyze_route(data: RouteRequest):  # ← async + typed body
    distance = 1000
    revenue = 800000
    cost = 500000
    profit = revenue - cost

    return {
        "origin": data.origin,
        "destination": data.destination,
        "distance_km": distance,
        "estimated_duration": "2h 10m",
        "demand_score": 75,
        "weather_risk": "Low",
        "estimated_revenue": revenue,
        "estimated_cost": cost,
        "estimated_profit": profit,
        "recommendation": "Increase flight frequency",
    }