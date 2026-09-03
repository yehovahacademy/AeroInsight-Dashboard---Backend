from fastapi import APIRouter, HTTPException, Query

from app.services.monthly_demand_service import monthly_demand_service


router = APIRouter(tags=["Monthly Demand"])


@router.get("/")
async def get_all_demand():

    demand = monthly_demand_service.get_all_demand()

    return {
        "count": len(demand),
        "demand": demand
    }


@router.get("/market/{market_id}")
async def get_demand_by_market(
    market_id: str,
    year: int | None = Query(default=None, ge=2020),
    month: int | None = Query(default=None, ge=1, le=12)
):

    demand = monthly_demand_service.get_demand_by_market(
        market_id=market_id,
        year=year,
        month=month
    )

    return {
        "count": len(demand),
        "demand": demand
    }


@router.get("/origin/{origin}")
async def get_demand_by_origin(origin: str):

    demand = monthly_demand_service.get_demand_by_origin(origin)

    return {
        "count": len(demand),
        "demand": demand
    }


@router.get("/destination/{destination}")
async def get_demand_by_destination(destination: str):

    demand = monthly_demand_service.get_demand_by_destination(destination)

    return {
        "count": len(demand),
        "demand": demand
    }


@router.get("/{demand_id}")
async def get_demand_by_id(demand_id: str):

    demand = monthly_demand_service.get_demand_by_id(demand_id)

    if demand is None:
        raise HTTPException(
            status_code=404,
            detail="Monthly demand record not found"
        )

    return demand
