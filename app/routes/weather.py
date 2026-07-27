from fastapi import APIRouter, HTTPException
from app.utils.airports import AIRPORTS
from app.services.weather_service import get_weather as fetch_weather
import logging
from app.utils.risk_engine import calculate_fog_risk

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
def get_weather_by_airport(airport: str):
    airport = airport.upper()

    airport_data = AIRPORTS.get(airport)

    if not airport_data:
        raise HTTPException(
            status_code=404,
            detail="Airport not found"
        )

    try:
        weather_data = fetch_weather(
            airport_data["latitude"],
            airport_data["longitude"]
        )

        current = weather_data["current"]
        daily = weather_data["daily"]
        hourly = weather_data["hourly"]

    except KeyError as e:
        logger.exception("Missing weather field")
        raise HTTPException(
            status_code=500,
            detail=f"Missing weather field: {e}"
        )

    except Exception:
        logger.exception("Weather service error")
        raise HTTPException(
            status_code=500,
            detail="Unable to fetch weather data."
        )

    forecast = [
        {
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
        }
        for i in range(len(daily["time"]))
    ]

    visibility_forecast = [
    {
        "time": hourly["time"][i],
        "visibility_m": hourly["visibility"][i],
        "visibility_km": round(hourly["visibility"][i] / 1000, 1),
        "fog_risk": calculate_fog_risk(
            hourly["visibility"][i],
            current["relative_humidity_2m"]
        )
    }
    for i in range(min(6, len(hourly["time"])))
]
    

    current_weather = {
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
    }

    return {
        "airport": airport,
        "city": airport_data["name"],
        "current": current_weather,
        "forecast": forecast,
        "visibility_forecast": visibility_forecast,
    }