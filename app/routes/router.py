from fastapi import APIRouter, HTTPException

from app.services.route_service import route_service


router = APIRouter(
    prefix="/api/routes",
    tags=["Routes"],
)


@router.get("/")
async def get_all_routes():
    routes = route_service.get_all_routes()

    return {
        "count": len(routes),
        "routes": routes,
    }


@router.get("/from/{origin}")
async def get_routes_from_origin(origin: str):
    routes = route_service.get_routes_from_origin(origin)

    return {
        "count": len(routes),
        "routes": routes,
    }


@router.get("/to/{destination}")
async def get_routes_to_destination(destination: str):
    routes = route_service.get_routes_to_destination(destination)

    return {
        "count": len(routes),
        "routes": routes,
    }


@router.get("/{origin}/{destination}")
async def get_route(origin: str, destination: str):
    route = route_service.get_route(origin, destination)

    if route is None:
        raise HTTPException(
            status_code=404,
            detail="Route not found",
        )

    return route


@router.get("/{route_id}")
async def get_route_by_id(route_id: int):
    route = route_service.get_route_by_id(route_id)

    if route is None:
        raise HTTPException(
            status_code=404,
            detail="Route not found",
        )

    return route