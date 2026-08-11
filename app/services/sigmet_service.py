from math import radians, sin, cos, sqrt, atan2


def calculate_distance_km(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float
):
    """
    Calculate great-circle distance between two coordinates.
    Returns distance in kilometers.
    """

    earth_radius = 6371.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earth_radius * c



def get_minimum_sigmet_distance(
    airport_lat: float,
    airport_lon: float,
    coords: list
):
    """
    Find the minimum distance between an airport
    and the coordinates defining a SIGMET area.
    """

    if not coords:
        return None

    distances = []

    for point in coords:

        lat = point.get("lat")
        lon = point.get("lon")

        if lat is None or lon is None:
            continue

        distance = calculate_distance_km(
            airport_lat,
            airport_lon,
            lat,
            lon
        )

        distances.append(distance)

    if not distances:
        return None

    return min(distances)



def classify_sigmet_impact(distance_km):
    """
    Classify how close a SIGMET is to an airport.
    """

    if distance_km is None:
        return "NO_IMPACT"

    if distance_km <= 50:
        return "DIRECT"

    if distance_km <= 200:
        return "NEARBY"

    return "NO_IMPACT"





if __name__ == "__main__":

    airport_lat = 19.1
    airport_lon = 72.859

    sigmet_coords = [
        {"lat": 19.5, "lon": 73.0},
        {"lat": 20.0, "lon": 73.5},
        {"lat": 18.8, "lon": 72.5}
    ]

    distance = get_minimum_sigmet_distance(
        airport_lat,
        airport_lon,
        sigmet_coords
    )

    impact = classify_sigmet_impact(distance)

    print("Minimum distance:", distance)
    print("Impact:", impact)



    def analyze_airport_sigmet_impact(
    airport_lat: float,
    airport_lon: float,
    sigmets: list
):
    results = []

    for sigmet in sigmets:

        coords = sigmet.get("coords", [])

        distance = get_minimum_sigmet_distance(
            airport_lat,
            airport_lon,
            coords
        )

        impact = classify_sigmet_impact(distance)

        results.append({
            "icao": sigmet.get("icaoId"),
            "fir": sigmet.get("firId"),
            "hazard": sigmet.get("hazard"),
            "severity": sigmet.get("severity"),
            "series": sigmet.get("seriesId"),

            "distance_km": round(distance, 2)
            if distance is not None else None,

            "impact": impact,

            "valid_from": sigmet.get("validTimeFrom"),
            "valid_to": sigmet.get("validTimeTo")
        })

    return results





def get_relevant_sigmets(
    airport_lat: float,
    airport_lon: float,
    sigmets: list
):
    analyzed = analyze_airport_sigmet_impact(
        airport_lat,
        airport_lon,
        sigmets
    )

    return [
        sigmet
        for sigmet in analyzed
        if sigmet["impact"] != "NO_IMPACT"
    ]