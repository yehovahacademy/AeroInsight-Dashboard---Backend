from typing import Optional

from fastapi import APIRouter, HTTPException

from app.services.flight_service import get_all_flights
from app.schemas.flight_schema import Flight
from app.services.flight_service import get_flight_by_number

router = APIRouter()


@router.get("/", response_model=list[Flight])
def list_flights(
    airline: Optional[str] = None,
    origin: Optional[str] = None,
    destination: Optional[str] = None,
    status: Optional[str] = None,
):
    return get_all_flights(
        airline=airline,
        origin=origin,
        destination=destination,
        status=status,
    )
@router.get("/{flight_number}", response_model=Flight)
def get_flight(flight_number: str):
    flight = get_flight_by_number(flight_number)
    if flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight