from typing import List

from fastapi import APIRouter

from app.schemas.route_opportunity_schema import (
    RouteOpportunityResponse
)

from app.services.route_opportunity_service import (
    RouteOpportunityService
)


router = APIRouter(
    prefix="/route-opportunity",
    tags=["Route Opportunity"]
)

service = RouteOpportunityService()


@router.get(
    "/",
    response_model=List[RouteOpportunityResponse]
)
def get_all_route_opportunities():

    return service.get_all()


@router.get(
    "/recommendation/{recommendation}",
    response_model=List[RouteOpportunityResponse]
)
def get_route_opportunities_by_recommendation(
    recommendation: str
):

    return service.get_by_recommendation(
        recommendation
    )


@router.get(
    "/{market_id}",
    response_model=RouteOpportunityResponse
)
def get_route_opportunity(market_id: str):

    return service.get_by_market(market_id)