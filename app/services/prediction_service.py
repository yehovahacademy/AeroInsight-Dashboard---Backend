def calculate_delay_prediction(
    current: dict,
    visibility_m: float,
    fog_risk: str
) -> dict:
    """
    Calculates the probability of a flight delay based on
    current weather conditions.
    """

    score = 0
    reasons = []

    wind_speed = current["wind_speed_10m"]
    wind_gusts = current["wind_gusts_10m"]
    precipitation = current["precipitation"]
    weather_code = current["weather_code"]
    cloud_cover = current["cloud_cover"]

    # Strong wind
    if wind_speed >= 25:
        score += 20
        reasons.append("Strong winds")

    # Wind gusts
    if wind_gusts >= 40:
        score += 15
        reasons.append("Strong wind gusts")

    # Heavy rain
    if precipitation >= 5:
        score += 20
        reasons.append("Heavy rainfall")

    # Thunderstorms
    if weather_code in [95, 96, 99]:
        score += 35
        reasons.append("Thunderstorm activity")

    # Low visibility
    if visibility_m <= 1000:
        score += 30
        reasons.append("Very low visibility")
    

    elif visibility_m <= 5000:
         score += 20
         reasons.append("Reduced visibility")   

    # Fog
    if fog_risk == "High":
         score += 20
         reasons.append("Dense fog")
   

    elif fog_risk == "Moderate":
        score += 10
        reasons.append("Fog formation possible")
         
    

    # Overcast skies
    if cloud_cover >= 90:
        score += 5
        reasons.append("Dense cloud cover")

    # Determine risk level
    if score < 25:
        risk = "Low"
        expected_delay = "0–10 min"

    elif score < 60:
        risk = "Moderate"
        expected_delay = "10–30 min"

    else:
        risk = "High"
        expected_delay = "30–60 min"

    return {
        "probability": min(score, 100),
        "risk": risk,
        "expected_delay": expected_delay,
        "reasons": reasons,
    }







def calculate_aviation_risk(delay_prediction: dict) -> dict:
    """
    Generates an overall aviation risk score based on
    the delay prediction.
    """

    probability = delay_prediction["probability"]

    if probability >= 70:
        return {
            "score": probability,
            "level": "High",
            "color": "red",
            "message": "Challenging flying conditions"
        }

    elif probability >= 40:
        return {
            "score": probability,
            "level": "Moderate",
            "color": "orange",
            "message": "Use caution"
        }

    return {
        "score": probability,
        "level": "Low",
        "color": "green",
        "message": "Good flying conditions"
    }





def generate_aviation_alerts(
    current: dict,
    visibility_m: float,
    fog_risk: str
) -> list:

  

    

#List to hold aviation alerts
    alerts = []

    if current["weather_code"] in [95, 96, 99]:
        alerts.append({
                "title": "Thunderstorm Warning",
                "severity": "High",
                "icon": "⛈️"
            })

    if visibility_m <= 5000:
        alerts.append({
                "title": "Reduced Visibility",
                "severity": "Moderate",
                "icon": "🌫️"
            })    

    if fog_risk == "High":
        alerts.append({
                "title": "Dense Fog",
                "severity": "High",
                "icon": "🌁"
            })
    

    elif fog_risk == "Moderate":
        alerts.append({
            "title": "Fog Formation Possible",
            "severity": "Moderate",
            "icon": "🌁"
        })


    if current["wind_speed_10m"] >= 25:
         alerts.append({
                "title": "Strong Surface Winds",
                "severity": "Moderate",
                "icon": "💨"
            })    


    if current["wind_gusts_10m"] >= 40:
      alerts.append({
        "title": "Strong Wind Gusts",
        "severity": "High",
        "icon": "🌬️"
    })     


    if current["precipitation"] >= 5:
         alerts.append({
                "title": "Heavy Rainfall",
                "severity": "Moderate",
                "icon": "🌧️"
            })  

    return alerts    


   

    
    
    