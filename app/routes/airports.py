from fastapi import APIRouter

from app.services.airport_service import airport_service

router = APIRouter(
    prefix="/api/airports",
    tags=["Airports"],
)


@router.get("/{airport_code}")
async def airport_details(airport_code: str):
    return await airport_service.get_airport(airport_code)