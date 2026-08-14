from fastapi import APIRouter, HTTPException

from app.schemas.demand_forecast_schema import DemandForecastResponse
from app.services.demand_forecast_service import generate_demand_forecast


router = APIRouter(
    prefix="/demand",
    tags=["Demand Forecast"],
)


@router.get(
    "/forecast/{origin}/{destination}",
    response_model=DemandForecastResponse,
)
async def demand_forecast(
    origin: str,
    destination: str,
    days: int = 7,
):
    try:
        return generate_demand_forecast(
            origin=origin,
            destination=destination,
            days=days,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )