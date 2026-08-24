from app.services.aircraft_service import get_aircraft_capacity

def calculate_what_if(request):

    capacity = get_aircraft_capacity(request.aircraft)

    passengers = capacity * request.load_factor

    revenue_per_flight = passengers * request.average_fare

    daily_revenue = revenue_per_flight * request.flights_per_day

    return {
        "aircraft": request.aircraft,
        "capacity": capacity,
        "estimated_passengers": round(passengers),
        "revenue_per_flight": round(revenue_per_flight),
        "daily_revenue": round(daily_revenue)
    }