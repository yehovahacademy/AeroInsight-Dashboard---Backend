import csv
from pathlib import Path

from app.schemas.airport_data_schema import AirportData


class AirportLoader:

    def get_airport_by_iata(self, iata: str):
           return self.airports_by_iata.get(iata.upper())

    def get_airport_by_icao(self, icao: str):
            return self.airports_by_icao.get(icao.upper())

    def __init__(self):
        self.airports = []

        self.airports_by_iata = {}
        self.airports_by_icao = {}

    def load_airports(self):

        data_file = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "airports.dat"
        )

        print(f"Loading airports from: {data_file}")

        with open(data_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                 # Skip invalid rows
                    if len(row) < 14:
                        continue
                
                    # Skip airports without an IATA code
                    if row[4] == "\\N" or row[4] == "":
                        continue
                
                    airport = AirportData(
                        id=int(row[0]),
                        name=row[1],
                        city=row[2],
                        country=row[3],
                        iata=row[4],
                        icao=row[5],
                        latitude=float(row[6]),
                        longitude=float(row[7]),
                        altitude=int(float(row[8])),
                        timezone=row[11],
                        airport_type=row[12],
                    )
                
                    self.airports.append(airport)

                    self.airports_by_iata[airport.iata] = airport


                    if airport.icao != "\\N":
                         self.airports_by_icao[airport.icao] = airport
  

        print(f"Loaded {len(self.airports)} airports.")

   



airport_loader = AirportLoader()
airport_loader.load_airports()