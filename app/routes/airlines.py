from fastapi import APIRouter
from app.services.airline_service import get_all_airlines
from app.schemas.airline_schema import Airline

router = APIRouter()

@router.get("/", response_model=list[Airline])
def list_airlines():
    return get_all_airlines()