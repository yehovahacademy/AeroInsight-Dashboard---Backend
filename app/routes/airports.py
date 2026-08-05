from fastapi import APIRouter, HTTPException

from app.services.airport_loader import airport_loader

router = APIRouter(
    prefix="/api/airports",
    tags=["Airports"],
)

@router.get("/search/{query}")
async def search_airports(query: str):
    return airport_loader.search_airports(query)


@router.get("/{airport_code}")
async def airport_details(airport_code: str):
    airport = airport_loader.get_airport_by_iata(airport_code)

    if airport is None:
        raise HTTPException(status_code=404, detail="Airport not found")

    return airport