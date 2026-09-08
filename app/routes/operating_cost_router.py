from typing import List

from fastapi import APIRouter

from app.schemas.operating_cost_schema import (
    OperatingCostResponse
)

from app.services.operating_cost_service import (
    OperatingCostService
)


router = APIRouter(
    prefix="/operating-costs",
    tags=["Operating Costs"]
)

service = OperatingCostService()


@router.get("/", response_model=List[OperatingCostResponse])
def get_all_operating_costs():

    return service.get_all()


@router.get(
    "/market/{market_id}",
    response_model=List[OperatingCostResponse]
)
def get_operating_costs_by_market(market_id: str):

    return service.get_by_market(market_id)


@router.get(
    "/aircraft/{aircraft_type}",
    response_model=List[OperatingCostResponse]
)
def get_operating_costs_by_aircraft(aircraft_type: str):

    return service.get_by_aircraft(aircraft_type)


@router.get(
    "/{cost_id}",
    response_model=OperatingCostResponse
)
def get_operating_cost(cost_id: str):

    return service.get_by_id(cost_id)