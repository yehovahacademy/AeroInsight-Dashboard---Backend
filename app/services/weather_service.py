import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(latitude: float, longitude: float):

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ",".join([
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "weather_code",
            "wind_speed_10m",
            "wind_direction_10m",
            "wind_gusts_10m",
            "cloud_cover",
            "pressure_msl",
            "surface_pressure",
            "precipitation",
            "rain",
            "is_day"
        ]),

        "daily": ",".join([
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "sunrise",
            "sunset",
            "wind_speed_10m_max",
            "wind_gusts_10m_max",
            "precipitation_probability_max",
            "precipitation_sum"
        ]),

         "hourly": ",".join([
        "visibility"
    ]),


        "forecast_days": 3,
        "timezone": "auto",
        "models": "best_match"
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()

    print(type(data))
    print(data.keys())

    return data


    return response.json()
