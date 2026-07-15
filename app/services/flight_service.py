import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "flights.json"

def load_flights():
    print(f"Reading file: {DATA_FILE}")
    print(f"Exists: {DATA_FILE.exists()}")

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    print("First 100 characters:")
    print(repr(content[:100]))

    return json.loads(content)


def get_all_flights(
    airline: str | None = None,
    origin: str | None = None,
    destination: str | None = None,
    status: str | None = None
):
    """
    Return flights with optional filters.
    """

    flights = load_flights()

    if airline:
        flights = [
            flight
            for flight in flights
            if flight["airline"].lower() == airline.lower()
        ]

    if origin:
        flights = [
            flight
            for flight in flights
            if flight["origin"].lower() == origin.lower()
        ]

    if destination:
        flights = [
            flight
            for flight in flights
            if flight["destination"].lower() == destination.lower()
        ]

    if status:
        flights = [
            flight
            for flight in flights
            if flight["status"].lower() == status.lower()
        ]

    return flights


def get_flight_by_number(flight_number: str):
    flights = load_flights()

    print("Searching for:", flight_number)

    for flight in flights:
        print("Checking:", flight["flight_number"])

        if flight["flight_number"].lower() == flight_number.lower():
            print("Match Found!")
            return flight

    print("No Match Found")
    return None
