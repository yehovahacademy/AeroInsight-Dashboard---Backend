from fastapi import APIRouter, HTTPException

from app.services.airport_loader import airport_loader


router = APIRouter(
    prefix="/api/airports",
    tags=["Airports"],
)

@router.get("/")
async def get_all_airports():
    return airport_loader.get_all_airports()

@router.get("/search/{query}")
async def search_airports(query: str):
    return airport_loader.search_airports(query)




   