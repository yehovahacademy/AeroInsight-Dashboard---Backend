from fastapi import HTTPException

from app.repositories.candidate_route_repository import (
    CandidateRouteRepository
)


class CandidateRouteService:

    def __init__(self):
        self.repository = CandidateRouteRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, candidate_id: str):
        result = self.repository.get_by_id(candidate_id)

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Candidate route not found"
            )

        return result

    def get_by_market(self, market_id: str):
        return self.repository.get_by_market(market_id)

    def get_by_status(self, planning_status: str):
        return self.repository.get_by_status(planning_status)