from fastapi import HTTPException

from app.repositories.scenario_route_repository import (
    ScenarioRouteRepository
)


class ScenarioRouteService:

    def __init__(self):
        self.repository = ScenarioRouteRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, scenario_route_id: str):
        result = self.repository.get_by_id(scenario_route_id)

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Scenario route not found"
            )

        return result

    def get_by_scenario(self, scenario_id: str):
        return self.repository.get_by_scenario(scenario_id)

    def get_by_market(self, market_id: str):
        return self.repository.get_by_market(market_id)