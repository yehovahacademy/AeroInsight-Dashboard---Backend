from fastapi import HTTPException

from app.repositories.route_opportunity_repository import (
    RouteOpportunityRepository
)


class RouteOpportunityService:

    def __init__(self):
        self.repository = RouteOpportunityRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_market(self, market_id: str):
        result = self.repository.get_by_market(market_id)

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Route opportunity not found"
            )

        return result

    def get_by_recommendation(self, recommendation: str):
        return self.repository.get_by_recommendation(
            recommendation
        )