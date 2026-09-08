from typing import List

from fastapi import HTTPException

from app.repositories.market_fare_repository import market_fare_repository
from app.schemas.market_fare_schema import MarketFareResponse


class MarketFareService:

    def get_all(self) -> List[MarketFareResponse]:
        return market_fare_repository.get_all()

    def get_by_id(self, fare_id: str) -> MarketFareResponse:
        fare = market_fare_repository.get_by_id(fare_id)

        if not fare:
            raise HTTPException(
                status_code=404,
                detail=f"Market fare '{fare_id}' not found"
            )

        return fare

    def get_by_market(
        self,
        market_id: str
    ) -> List[MarketFareResponse]:

        return market_fare_repository.get_by_market(market_id)

    def get_by_period(
        self,
        year: int,
        month: int
    ) -> List[MarketFareResponse]:

        return market_fare_repository.get_by_period(
            year,
            month
        )


market_fare_service = MarketFareService()