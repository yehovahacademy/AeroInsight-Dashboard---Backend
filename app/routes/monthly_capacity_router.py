from fastapi import APIRouter, HTTPException, Query

from app.services.monthly_capacity_service import (
    monthly_capacity_service
)


router = APIRouter(tags=["Monthly Capacity"])


@router.get("/")
async def get_all_capacity():

    capacity = monthly_capacity_service.get_all_capacity()

    return {
        "count": len(capacity),
        "capacity": capacity
    }


@router.get("/market/{market_id}")
async def get_capacity_by_market(
    market_id: str,
    year: int | None = Query(default=None, ge=2020),
    month: int | None = Query(default=None, ge=1, le=12)
):

    capacity = monthly_capacity_service.get_capacity_by_market(
        market_id=market_id,
        year=year,
        month=month
    )

    return {
        "count": len(capacity),
        "capacity": capacity
    }


@router.get("/origin/{origin}")
async def get_capacity_by_origin(origin: str):

    capacity = monthly_capacity_service.get_capacity_by_origin(origin)

    return {
        "count": len(capacity),
        "capacity": capacity
    }


@router.get("/destination/{destination}")
async def get_capacity_by_destination(destination: str):

    capacity = (
        monthly_capacity_service
        .get_capacity_by_destination(destination)
    )

    return {
        "count": len(capacity),
        "capacity": capacity
    }


@router.get("/{capacity_id}")
async def get_capacity_by_id(capacity_id: str):

    capacity = monthly_capacity_service.get_capacity_by_id(
        capacity_id
    )

    if capacity is None:
        raise HTTPException(
            status_code=404,
            detail="Monthly capacity record not found"
        )

    return capacity