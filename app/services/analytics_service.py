from app.config.flights import FLIGHTS

def get_dashboard_stats():
    total_flights = len(FLIGHTS)

    on_time = len(
        [flight for flight in FLIGHTS if flight["status"] == "On Time"]
    )

    delayed = len(
        [flight for flight in FLIGHTS if flight["status"] == "Delayed"]
    )

    return {
        "total_flights": total_flights,
        "on_time_flights": on_time,
        "delayed_flights": delayed
    }