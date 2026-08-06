from fastapi import APIRouter
from app.services.fleet_service import fleet_service

router = APIRouter(prefix="/fleet", tags=["Fleet"])


@router.get("/")
def get_fleet():

    return fleet_service.get_summary()