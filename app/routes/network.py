from fastapi import APIRouter

from app.schemas.network_schema import (
    NetworkSummary,
    RouteRequest,
    RouteAnalysis,
)
from app.services.network_service import analyze_route

router = APIRouter()


@router.get("/summary", response_model=NetworkSummary)
async def summary():
    return {
        "total_routes": 0,
        "average_load_factor": 0,
        "high_revenue_routes": 0,
        "recommendations": {},
    }


@router.post("/analyze_route", response_model=RouteAnalysis)
async def analyze_route_endpoint(request: RouteRequest):
    return await analyze_route(request)