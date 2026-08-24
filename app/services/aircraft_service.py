AIRCRAFT_CAPACITY = {
    "A320": 180,
    "A321neo": 236,
    "B737 MAX": 178,
    "B777": 396,
    "ATR 72": 78,
}


def get_aircraft_capacity(aircraft: str):
    capacity = AIRCRAFT_CAPACITY.get(aircraft)

    if capacity is None:
        raise ValueError(f"Unsupported aircraft: {aircraft}")

    return capacity