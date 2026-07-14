from typing import Optional

from fastapi import APIRouter

from app.services.flight_service import get_all_flights
from app.schemas.flight_schema import Flight

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