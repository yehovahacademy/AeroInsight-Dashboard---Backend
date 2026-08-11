from fastapi import APIRouter, HTTPException
from app.utils.airports import AIRPORTS
import logging
from app.utils.risk_engine import calculate_fog_risk
from app.services.prediction_service import calculate_delay_prediction
from app.services.prediction_service import (
    calculate_delay_prediction,
    calculate_aviation_risk,
    generate_aviation_alerts,
)
from app.services.weather_service import get_weather as fetch_weather, get_metar,calculate_weather_risk, get_taf, analyze_taf_forecast, get_sigmet, analyze_sigmets

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/intelligence/{icao}")
def get_weather_intelligence(icao: str):

    icao = icao.upper()

    try:
        # -------------------------
        # METAR
        # -------------------------
        metar_data = get_metar(icao)

        if not metar_data:
            raise HTTPException(
                status_code=404,
                detail=f"No METAR data available for {icao}"
            )

        metar = metar_data[0]

        current_risk = calculate_weather_risk(metar)

        # -------------------------
        # TAF
        # -------------------------
        taf_data = get_taf(icao)

        if taf_data:
            forecast_analysis = analyze_taf_forecast(taf_data)
        else:
            forecast_analysis = {
                "forecast_periods": []
            }

        # -------------------------
        # SIGMET
        # -------------------------
        sigmet_data = get_sigmet()

        sigmet_analysis = analyze_sigmets(sigmet_data)

        # -------------------------
        # Return combined data
        # -------------------------
        return {
            "icao": icao,
            "source": "AviationWeather.gov",

            "current_conditions": {
                "metar": metar,
                "risk": current_risk
            },

            "forecast": {
                "taf": taf_data,
                "analysis": forecast_analysis
            },

            "hazards": {
                "sigmet": sigmet_analysis
            }
        }

    except HTTPException:
        raise

    except Exception as e:

        print("Weather intelligence error:", e)

        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate weather intelligence for {icao}: {str(e)}"
        )


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

    first_visibility = visibility_forecast[0]["visibility_m"]
    first_fog_risk = visibility_forecast[0]["fog_risk"]
    delay_prediction = calculate_delay_prediction(
        current,
        first_visibility,
        first_fog_risk
    )
    aviation_risk = calculate_aviation_risk(delay_prediction)

    aviation_alerts = generate_aviation_alerts(
    current,
    first_visibility,
    first_fog_risk
)
    

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
        "delay_prediction": delay_prediction,
        "aviation_risk": aviation_risk,
        "aviation_alerts": aviation_alerts
}
    