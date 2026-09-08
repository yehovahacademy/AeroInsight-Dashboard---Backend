from typing import List

from fastapi import APIRouter

from app.services.competition_service import competition_service
from app.schemas.competition_schema import CompetitionResponse

router = APIRouter()


@router.get(
    "/",
    response_model=List[CompetitionResponse],
    summary="Get All Competition"
)
def get_all_competition():
    return competition_service.get_all()


@router.get(
    "/market/{market_id}",
    response_model=List[CompetitionResponse],
    summary="Get Competition By Market"
)
def get_competition_by_market(market_id: str):
    return competition_service.get_by_market(market_id)


@router.get(
    "/airline/{airline}",
    response_model=List[CompetitionResponse],
    summary="Get Competition By Airline"
)
def get_competition_by_airline(airline: str):
    return competition_service.get_by_airline(airline)


@router.get(
    "/{competition_id}",
    response_model=CompetitionResponse,
    summary="Get Competition By ID"
)
def get_competition_by_id(competition_id: str):
    return competition_service.get_by_id(competition_id)