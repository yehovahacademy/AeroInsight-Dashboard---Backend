from typing import List

from fastapi import APIRouter

from app.schemas.scenario_route_schema import (
    ScenarioRouteResponse
)

from app.services.scenario_route_service import (
    ScenarioRouteService
)


router = APIRouter(
    prefix="/scenario-routes",
    tags=["Scenario Routes"]
)

service = ScenarioRouteService()


@router.get(
    "/",
    response_model=List[ScenarioRouteResponse]
)
def get_all_scenario_routes():

    return service.get_all()


@router.get(
    "/scenario/{scenario_id}",
    response_model=List[ScenarioRouteResponse]
)
def get_scenario_routes(scenario_id: str):

    return service.get_by_scenario(scenario_id)


@router.get(
    "/market/{market_id}",
    response_model=List[ScenarioRouteResponse]
)
def get_market_scenario_routes(market_id: str):

    return service.get_by_market(market_id)


@router.get(
    "/{scenario_route_id}",
    response_model=ScenarioRouteResponse
)
def get_scenario_route(scenario_route_id: str):

    return service.get_by_id(scenario_route_id)