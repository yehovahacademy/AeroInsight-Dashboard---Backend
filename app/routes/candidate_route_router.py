from typing import List

from fastapi import APIRouter

from app.schemas.candidate_route_schema import (
    CandidateRouteResponse
)

from app.services.candidate_route_service import (
    CandidateRouteService
)


router = APIRouter(
    prefix="/candidate-routes",
    tags=["Candidate Routes"]
)

service = CandidateRouteService()


@router.get(
    "/",
    response_model=List[CandidateRouteResponse]
)
def get_all_candidate_routes():

    return service.get_all()


@router.get(
    "/market/{market_id}",
    response_model=List[CandidateRouteResponse]
)
def get_candidate_routes_by_market(
    market_id: str
):

    return service.get_by_market(market_id)


@router.get(
    "/status/{planning_status}",
    response_model=List[CandidateRouteResponse]
)
def get_candidate_routes_by_status(
    planning_status: str
):

    return service.get_by_status(planning_status)


@router.get(
    "/{candidate_id}",
    response_model=CandidateRouteResponse
)
def get_candidate_route(
    candidate_id: str
):

    return service.get_by_id(candidate_id)