from app.schemas.whatif_schemas import WhatIfRequest


def calculate_what_if(request: WhatIfRequest):

    # Basic scenario calculations
    estimated_seats_per_flight = 180

    daily_capacity = (
        estimated_seats_per_flight * request.flights_per_day
    )

    estimated_passengers = (
        daily_capacity * (request.load_factor / 100)
    )

    daily_revenue = (
        estimated_passengers * request.average_fare
    )

    return {
        "origin": request.origin,
        "destination": request.destination,
        "aircraft": request.aircraft,
        "flights_per_day": request.flights_per_day,
        "load_factor": request.load_factor,
        "average_fare": request.average_fare,
        "daily_capacity": daily_capacity,
        "estimated_passengers": round(estimated_passengers),
        "daily_revenue": round(daily_revenue, 2),
    }