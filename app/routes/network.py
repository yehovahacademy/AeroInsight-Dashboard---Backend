from fastapi import APIRouter
from app.schemas.network_schema import RouteRequest, RouteAnalysis
from app.services.network_service import analyze_route


router = APIRouter()


@router.post("/analyze_route", response_model=RouteAnalysis)
def analyze_route_endpoint(request: RouteRequest):

    return analyze_route(request)