from fastapi import APIRouter, HTTPException, Query

from app.services.historical_traffic_service import (
    historical_traffic_service,
)


router = APIRouter(
    tags=["Historical Traffic"],
)


@router.get("/")
async def get_all_traffic():
    traffic = historical_traffic_service.get_all_traffic()

    return {
        "count": len(traffic),
        "traffic": traffic,
    }


@router.get("/market/{market_id}")
async def get_traffic_by_market(
    market_id: str,
    year: int | None = Query(default=None, ge=2020),
    month: int | None = Query(default=None, ge=1, le=12),
):
    traffic = historical_traffic_service.get_traffic_by_market(
        market_id=market_id,
        year=year,
        month=month,
    )

    return {
        "count": len(traffic),
        "traffic": traffic,
    }


@router.get("/origin/{origin}")
async def get_traffic_by_origin(origin: str):
    traffic = historical_traffic_service.get_traffic_by_origin(origin)

    return {
        "count": len(traffic),
        "traffic": traffic,
    }


@router.get("/destination/{destination}")
async def get_traffic_by_destination(destination: str):
    traffic = historical_traffic_service.get_traffic_by_destination(
        destination
    )

    return {
        "count": len(traffic),
        "traffic": traffic,
    }


@router.get("/{traffic_id}")
async def get_traffic_by_id(traffic_id: str):
    traffic = historical_traffic_service.get_traffic_by_id(traffic_id)

    if traffic is None:
        raise HTTPException(
            status_code=404,
            detail="Historical traffic record not found",
        )

    return traffic