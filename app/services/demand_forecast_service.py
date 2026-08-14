from datetime import date, timedelta


def calculate_demand_score(
    day_index: int,
    weekend: bool = False,
) -> float:
    """
    Generate a baseline demand score.

    This is intentionally a deterministic baseline model.
    It can later be replaced with a trained forecasting model
    once historical booking/load-factor data is available.
    """

    base_demand = 65.0

    # Weekly seasonality
    weekday_effect = {
        0: 2.0,   # Monday
        1: 4.0,   # Tuesday
        2: 5.0,   # Wednesday
        3: 7.0,   # Thursday
        4: 12.0,  # Friday
        5: 10.0,  # Saturday
        6: 15.0,  # Sunday
    }

    score = base_demand + weekday_effect.get(day_index, 0)

    if weekend:
        score += 5.0

    return min(round(score, 2), 100.0)


def classify_demand(score: float) -> str:
    if score >= 85:
        return "VERY_HIGH"
    if score >= 70:
        return "HIGH"
    if score >= 50:
        return "MEDIUM"
    return "LOW"


def estimate_load_factor(demand_score: float) -> float:
    """
    Convert demand score into an estimated load factor.
    """

    load_factor = 45 + (demand_score * 0.45)

    return min(round(load_factor, 2), 95.0)


def calculate_trend(scores: list[float]) -> str:
    if len(scores) < 2:
        return "STABLE"

    first_half = sum(scores[: len(scores) // 2]) / max(len(scores) // 2, 1)
    second_half = sum(scores[len(scores) // 2:]) / max(
        len(scores) - len(scores) // 2,
        1,
    )

    difference = second_half - first_half

    if difference >= 5:
        return "INCREASING"

    if difference <= -5:
        return "DECREASING"

    return "STABLE"


def generate_demand_forecast(
    origin: str,
    destination: str,
    days: int = 7,
) -> dict:
    """
    Generate route-level demand forecast.

    Args:
        origin: Origin IATA code.
        destination: Destination IATA code.
        days: Forecast horizon.

    Returns:
        Dictionary containing forecast and route-level demand intelligence.
    """

    if days < 1 or days > 30:
        raise ValueError("Forecast period must be between 1 and 30 days.")

    origin = origin.upper()
    destination = destination.upper()

    start_date = date.today()

    forecast = []

    for offset in range(days):
        forecast_date = start_date + timedelta(days=offset)

        weekday = forecast_date.weekday()
        weekend = weekday >= 5

        score = calculate_demand_score(
            day_index=weekday,
            weekend=weekend,
        )

        forecast.append(
            {
                "date": forecast_date.isoformat(),
                "day": forecast_date.strftime("%A"),
                "demand_score": score,
                "demand_level": classify_demand(score),
                "estimated_load_factor": estimate_load_factor(score),
            }
        )

    scores = [item["demand_score"] for item in forecast]

    peak_day = max(
        forecast,
        key=lambda item: item["demand_score"],
    )

    average_demand = round(
        sum(scores) / len(scores),
        2,
    )

    average_load_factor = round(
        sum(item["estimated_load_factor"] for item in forecast)
        / len(forecast),
        2,
    )

    trend = calculate_trend(scores)

    overall_level = classify_demand(average_demand)

    if overall_level == "VERY_HIGH":
        recommendation = "Consider increasing capacity on this route."
    elif overall_level == "HIGH":
        recommendation = "High demand supports increased capacity."
    elif overall_level == "MEDIUM":
        recommendation = "Maintain current capacity and monitor demand."
    else:
        recommendation = "Consider reducing capacity or monitoring route performance."

    return {
        "route": f"{origin}-{destination}",
        "origin": origin,
        "destination": destination,
        "forecast_horizon_days": days,
        "average_demand_score": average_demand,
        "demand_level": overall_level,
        "average_load_factor": average_load_factor,
        "trend": trend,
        "peak_day": peak_day,
        "recommendation": recommendation,
        "forecast": forecast,
    }