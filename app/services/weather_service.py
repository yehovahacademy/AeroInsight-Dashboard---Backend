import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"
AWC_BASE_URL = "https://aviationweather.gov/api/data"


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


def get_metar(icao: str):

    url = f"{AWC_BASE_URL}/metar"

    params = {
        "ids": icao.upper(),
        "format": "json"
    }

    headers = {
        "User-Agent": "AeroInsight/1.0"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    return response.json()


def calculate_weather_risk(metar: dict):

    score = 0
    factors = []

    # -------------------------
    # Visibility Risk
    # -------------------------
    visibility = metar.get("visib")

    if visibility is not None:

        if visibility < 1:
            score += 40
            factors.append("Very low visibility")

        elif visibility < 3:
            score += 30
            factors.append("Low visibility")

        elif visibility < 5:
            score += 15
            factors.append("Reduced visibility")

    # -------------------------
    # Wind Risk
    # -------------------------
    wind_speed = metar.get("wspd")

    if wind_speed is not None:

        if wind_speed >= 30:
            score += 30
            factors.append("Very strong winds")

        elif wind_speed >= 20:
            score += 20
            factors.append("Strong winds")

        elif wind_speed >= 15:
            score += 10
            factors.append("Moderate-to-strong winds")

    # -------------------------
    # Weather Risk
    # -------------------------
    weather = metar.get("wxString") or ""

    weather = weather.upper()

    if "TS" in weather:
        score += 30
        factors.append("Thunderstorm activity")

    elif "SN" in weather:
        score += 25
        factors.append("Snow")

    elif "FG" in weather:
        score += 30
        factors.append("Fog")

    elif "RA" in weather:
        score += 15
        factors.append("Rain")

    # -------------------------
    # Flight Category
    # -------------------------
    flight_category = metar.get("fltCat")

    if flight_category == "LIFR":
        score += 40
        factors.append("LIFR conditions")

    elif flight_category == "IFR":
        score += 25
        factors.append("IFR conditions")

    elif flight_category == "MVFR":
        score += 10
        factors.append("MVFR conditions")

    # -------------------------
    # Cap score
    # -------------------------
    score = min(score, 100)

    # -------------------------
    # Risk level
    # -------------------------
    if score >= 70:
        level = "SEVERE"

    elif score >= 45:
        level = "HIGH"

    elif score >= 20:
        level = "MODERATE"

    else:
        level = "LOW"

    return {
        "score": score,
        "level": level,
        "factors": factors
    }

def calculate_taf_risk(taf: dict):

    score = 0
    factors = []

    # -------------------------
    # Visibility Risk
    # -------------------------
    visibility = taf.get("visib")

    if visibility is not None:

        if visibility < 1:
            score += 35
            factors.append("Very low forecast visibility")

        elif visibility < 3:
            score += 25
            factors.append("Low forecast visibility")

        elif visibility < 5:
            score += 10
            factors.append("Reduced forecast visibility")

    # -------------------------
    # Wind Risk
    # -------------------------
    wind_speed = taf.get("wspd")
    wind_gust = taf.get("wgst")

    if wind_speed is not None:

        if wind_speed >= 30:
            score += 25
            factors.append("Very strong forecast winds")

        elif wind_speed >= 20:
            score += 15
            factors.append("Strong forecast winds")

        elif wind_speed >= 15:
            score += 8
            factors.append("Moderate-to-strong forecast winds")

    if wind_gust is not None and wind_gust >= 30:
        score += 10
        factors.append("Strong wind gusts")

    # -------------------------
    # Weather Risk
    # -------------------------
    weather = (taf.get("wxString") or "").upper()

    if "TS" in weather:
        score += 30
        factors.append("Thunderstorm forecast")

    if "RA" in weather:
        score += 15
        factors.append("Rain forecast")

    if "BR" in weather:
        score += 10
        factors.append("Mist forecast")

    if "FG" in weather:
        score += 25
        factors.append("Fog forecast")

    # -------------------------
    # Cumulonimbus Risk
    # -------------------------
    clouds = taf.get("clouds", [])

    for cloud in clouds:

        if cloud.get("type") == "CB":
            score += 20
            factors.append("Cumulonimbus clouds forecast")
            break

    # -------------------------
    # Cap score
    # -------------------------
    score = min(score, 100)

    # -------------------------
    # Risk level
    # -------------------------
    if score >= 70:
        level = "SEVERE"

    elif score >= 45:
        level = "HIGH"

    elif score >= 20:
        level = "MODERATE"

    else:
        level = "LOW"

    return {
        "score": score,
        "level": level,
        "factors": factors
    }

def get_taf(icao: str):

    url = f"{AWC_BASE_URL}/taf"

    params = {
        "ids": icao.upper(),
        "format": "json"
    }

    headers = {
        "User-Agent": "AeroInsight/1.0"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    return response.json()


def analyze_taf_forecast(taf_data: list):

    if not taf_data:
        return {
            "forecast_risk": None,
            "periods": []
        }

    taf = taf_data[0]

    periods = []

    for forecast in taf.get("fcsts", []):

        risk = calculate_taf_risk(forecast)

        periods.append({
            "time_from": forecast.get("timeFrom"),
            "time_to": forecast.get("timeTo"),
            "change_type": forecast.get("fcstChange"),
            "visibility": forecast.get("visib"),
            "wind_speed": forecast.get("wspd"),
            "wind_gust": forecast.get("wgst"),
            "weather": forecast.get("wxString"),
            "risk": risk
        })

    return {
        "forecast_periods": periods
    }







def get_airsigmet():

    url = f"{AWC_BASE_URL}/airsigmet"

    params = {
        "format": "json"
    }

    headers = {
        "User-Agent": "AeroInsight/1.0"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    return response.json()


def get_isigmet():

    url = f"{AWC_BASE_URL}/isigmet"

    params = {
        "format": "json"
    }

    headers = {
        "User-Agent": "AeroInsight/1.0"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    return response.json()


def get_sigmet():

    domestic = get_airsigmet()
    international = get_isigmet()

    return {
        "domestic": domestic,
        "international": international
    }





def calculate_sigmet_risk(sigmet: dict):

    score = 0
    factors = []

    hazard = (sigmet.get("hazard") or "").upper()

    # -------------------------
    # Hazard type
    # -------------------------
    if "CONVECTIVE" in hazard:
        score += 40
        factors.append("Convective SIGMET")

    elif "TURBULENCE" in hazard:
        score += 35
        factors.append("Severe turbulence")

    elif "ICING" in hazard:
        score += 35
        factors.append("Severe icing")

    elif "ASH" in hazard:
        score += 50
        factors.append("Volcanic ash")

    else:
        score += 20
        factors.append(f"SIGMET hazard: {hazard}")

    # -------------------------
    # Severity
    # -------------------------
    severity = sigmet.get("severity")

    if severity is not None:

        if severity >= 5:
            score += 30
            factors.append("High SIGMET severity")

        elif severity >= 3:
            score += 20
            factors.append("Moderate SIGMET severity")

        elif severity >= 1:
            score += 10
            factors.append("Low SIGMET severity")

    # -------------------------
    # Movement
    # -------------------------
    movement_speed = sigmet.get("movementSpd")

    if movement_speed is not None and movement_speed >= 20:
        score += 10
        factors.append("Rapidly moving hazard")

    # -------------------------
    # Cap score
    # -------------------------
    score = min(score, 100)

    # -------------------------
    # Risk level
    # -------------------------
    if score >= 70:
        level = "SEVERE"

    elif score >= 45:
        level = "HIGH"

    elif score >= 20:
        level = "MODERATE"

    else:
        level = "LOW"

    return {
        "score": score,
        "level": level,
        "factors": factors
    }


def analyze_sigmets(sigmet_data: dict):

    analyzed = []

    for region, sigmets in sigmet_data.items():

        if not isinstance(sigmets, list):
            continue

        for sigmet in sigmets:

            risk = calculate_sigmet_risk(sigmet)

            analyzed.append({
                "region": region,

                "icao": sigmet.get("icaoId"),
                "fir": sigmet.get("firId"),
                "fir_name": sigmet.get("firName"),

                "series": sigmet.get("seriesId"),

                "hazard": sigmet.get("hazard"),
                "qualifier": sigmet.get("qualifier"),

                "severity": sigmet.get("severity"),

                "valid_from": sigmet.get("validTimeFrom"),
                "valid_to": sigmet.get("validTimeTo"),

                "altitude": {
                    "low": (
                        sigmet.get("altitudeLow1")
                        if sigmet.get("altitudeLow1") is not None
                        else sigmet.get("base")
                    ),
                    "high": (
                        sigmet.get("altitudeHi1")
                        if sigmet.get("altitudeHi1") is not None
                        else sigmet.get("top")
                    )
                },

                "movement": {
                    "direction": (
                        sigmet.get("movementDir")
                        if sigmet.get("movementDir") is not None
                        else sigmet.get("dir")
                    ),
                    "speed": (
                        sigmet.get("movementSpd")
                        if sigmet.get("movementSpd") is not None
                        else sigmet.get("spd")
                    )
                },

                "coordinates": sigmet.get("coords", []),

                "risk": risk
            })

    return analyzed

