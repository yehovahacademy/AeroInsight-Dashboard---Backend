from fastapi import APIRouter
from app.services.flight_service import get_all_flights
from app.schemas.flight_schema import Flight

router = APIRouter()

@router.get("/", response_model=list[Flight])
def list_flights():
    return get_all_flights()