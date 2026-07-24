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
        current = weather_data["current"]
        daily = weather_data["daily"]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    forecast = []

    for i in range(len(daily["time"])):
        forecast.append({
            "date": daily["time"][i],
            "max_temp": daily["temperature_2m_max"][i],
            "min_temp": daily["temperature_2m_min"][i],
            "rain_probability": daily["precipitation_probability_max"][i],
            "rainfall": daily["precipitation_sum"][i],
            "wind_speed": daily["wind_speed_10m_max"][i],
            "wind_gusts": daily["wind_gusts_10m_max"][i],
            "weather_code": daily["weather_code"][i],
            "sunrise": daily["sunrise"][i],
            "sunset": daily["sunset"][i],
        })

    return {
        "airport": airport,
        "city": airport_data["name"],

        "current": {
            "temperature": current["temperature_2m"],
            "feels_like": current["apparent_temperature"],
            "humidity": current["relative_humidity_2m"],
            "weather_code": current["weather_code"],
            "wind_speed": current["wind_speed_10m"],
            "wind_gusts": current["wind_gusts_10m"],
            "wind_direction": current["wind_direction_10m"],
            "cloud_cover": current["cloud_cover"],
            "pressure": current["pressure_msl"],
            "surface_pressure": current["surface_pressure"],
            "rain": current["rain"],
            "precipitation": current["precipitation"],
            "is_day": bool(current["is_day"]),
        },

        "forecast": forecast
    }