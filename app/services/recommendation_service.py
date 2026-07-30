def generate_recommendation(load_factor: int, revenue: str) -> str:
    if load_factor >= 90:
        return "Expand"

    if load_factor >= 80:
        return "Increase Frequency"

    if load_factor >= 70:
        return "Maintain"

    if revenue == "Low":
        return "Review"

    return "Monitor"