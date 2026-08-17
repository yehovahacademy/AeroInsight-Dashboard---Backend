import csv
from pathlib import Path


DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "airlines.dat"
)


def get_all_airlines():
    airlines = []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) < 8:
                continue

            airlines.append({
                "id": row[0],
                "name": row[1],
                "alias": row[2],
                "iata": row[3],
                "icao": row[4],
                "callsign": row[5],
                "country": row[6],
                "active": row[7],
            })

    return airlines