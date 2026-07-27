def calculate_fog_risk(visibility_m: float, humidity: int) -> str:
    """
    Returns the fog risk based on visibility and humidity.
    """

    if visibility_m <= 1000:
        return "High"

    if visibility_m <= 5000 and humidity >= 90:
        return "Moderate"

    return "Low"