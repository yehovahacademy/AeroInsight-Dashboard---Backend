from fastapi import APIRouter, HTTPException, Query

from app.services.aircraft_service import aircraft_service


router = APIRouter(
    tags=["Aircraft"],
)


@router.get("/")
async def get_all_aircraft():
    aircraft = aircraft_service.get_all_aircraft()

    return {
        "count": len(aircraft),
        "aircraft": aircraft,
    }


@router.get("/search")
async def search_aircraft(
    q: str = Query(..., min_length=1)
):
    aircraft = aircraft_service.search_aircraft(q)

    return {
        "count": len(aircraft),
        "aircraft": aircraft,
    }


@router.get("/manufacturer/{manufacturer}")
async def get_aircraft_by_manufacturer(manufacturer: str):
    aircraft = aircraft_service.get_aircraft_by_manufacturer(manufacturer)

    return {
        "count": len(aircraft),
        "aircraft": aircraft,
    }


@router.get("/{aircraft_type}")
async def get_aircraft_by_type(aircraft_type: str):
    aircraft = aircraft_service.get_aircraft_by_type(aircraft_type)

    if aircraft is None:
        raise HTTPException(
            status_code=404,
            detail="Aircraft type not found",
        )

    return aircraft