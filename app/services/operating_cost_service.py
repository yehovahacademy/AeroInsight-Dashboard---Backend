from fastapi import HTTPException

from app.repositories.operating_cost_repository import (
    OperatingCostRepository
)


class OperatingCostService:

    def __init__(self):
        self.repository = OperatingCostRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, cost_id: str):
        result = self.repository.get_by_id(cost_id)

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Operating cost record not found"
            )

        return result

    def get_by_market(self, market_id: str):
        return self.repository.get_by_market(market_id)

    def get_by_aircraft(self, aircraft_type: str):
        return self.repository.get_by_aircraft(aircraft_type)