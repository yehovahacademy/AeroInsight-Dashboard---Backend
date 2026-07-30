from fastapi import APIRouter
from app.clients.aeroapi_client import AeroAPIClient


router = APIRouter()


@router.get("/test/{flight}")
def test_flight(flight:str):

    client = AeroAPIClient()

    return client.get_flight(flight)