from fastapi import APIRouter, HTTPException
from app.utils.airports import AIRPORTS
from app.services.weather_service import get_weather as fetch_weather

router = APIRouter()

@router.get("/")
def get_weather_by_airport(airport: str):
    airport = airport.upper()
    if airport not in AIRPORTS:
        raise HTTPException(status_code=404, detail="Airport not found")

    airport_data = AIRPORTS[airport]
    latitude = airport_data["latitude"]
    longitude = airport_data["longitude"]

    try:
        weather_data = fetch_weather(latitude, longitude)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "airport": airport,
        "location": {
            "name": airport_data["name"],
            "latitude": latitude,
            "longitude": longitude
        },
        "weather": weather_data
    }