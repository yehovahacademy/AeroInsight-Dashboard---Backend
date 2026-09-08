from typing import List

from fastapi import APIRouter

from app.schemas.market_fare_schema import MarketFareResponse
from app.services.market_fare_service import market_fare_service


router = APIRouter()


@router.get(
    "/",
    response_model=List[MarketFareResponse],
    summary="Get all market fares"
)
def get_all_market_fares():

    return market_fare_service.get_all()


@router.get(
    "/{fare_id}",
    response_model=MarketFareResponse,
    summary="Get market fare by ID"
)
def get_market_fare(fare_id: str):

    return market_fare_service.get_by_id(fare_id)


@router.get(
    "/market/{market_id}",
    response_model=List[MarketFareResponse],
    summary="Get market fare history"
)
def get_market_fare_history(market_id: str):

    return market_fare_service.get_by_market(
        market_id
    )


@router.get(
    "/period/{year}/{month}",
    response_model=List[MarketFareResponse],
    summary="Get market fares by period"
)
def get_market_fares_by_period(
    year: int,
    month: int
):

    return market_fare_service.get_by_period(
        year,
        month
    )