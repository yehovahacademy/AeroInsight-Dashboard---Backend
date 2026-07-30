from fastapi import APIRouter

from app.services.flight_service import flight_service

router = APIRouter(
    prefix="/api/flights",
    tags=["Flights"],
)


@router.get("/{ident}")
async def flight_details(ident: str):
    return await flight_service.get_flight(ident)