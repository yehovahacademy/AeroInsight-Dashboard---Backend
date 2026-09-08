from typing import List
from fastapi import HTTPException

from app.repositories.competition_repository import competition_repository
from app.schemas.competition_schema import CompetitionResponse


class CompetitionService:

    def get_all(self) -> List[CompetitionResponse]:
        records = competition_repository.get_all()
        return records

    def get_by_id(self, competition_id: str) -> CompetitionResponse:
        record = competition_repository.get_by_id(competition_id)
        if not record:
            raise HTTPException(
                status_code=404,
                detail=f"Competition with id '{competition_id}' not found"
            )
        return record

    def get_by_market(self, market_id: str) -> List[CompetitionResponse]:
        records = competition_repository.get_by_market(market_id)
        return records

    def get_by_airline(self, airline: str) -> List[CompetitionResponse]:
        records = competition_repository.get_by_airline(airline)
        return records


competition_service = CompetitionService()