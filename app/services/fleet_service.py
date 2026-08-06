from pathlib import Path
import csv

DATA_FILE = Path(__file__).parent.parent / "data" / "planes.dat"


class FleetService:

    def __init__(self):
        self.aircraft = self.load_planes()

    def extract_manufacturer(self, aircraft_name: str):

        if aircraft_name.startswith("Airbus"):
            return "Airbus"

        if aircraft_name.startswith("Boeing"):
            return "Boeing"

        if "ATR" in aircraft_name:
            return "ATR"

        if aircraft_name.startswith("Embraer"):
            return "Embraer"

        if aircraft_name.startswith("Bombardier"):
            return "Bombardier"

        if aircraft_name.startswith("McDonnell"):
            return "McDonnell Douglas"

        if aircraft_name.startswith("Cessna"):
            return "Cessna"

        return aircraft_name.split()[0]

    def load_planes(self):

        planes = []

        with open(DATA_FILE, encoding="utf-8") as file:

            reader = csv.reader(file)

            for row in reader:

                if len(row) != 3:
                    continue

                name, iata, icao = row

                planes.append(
                    {
                        "name": name,
                        "iata_code": None if iata == r"\N" else iata,
                        "icao_code": None if icao == r"\N" else icao,
                        "manufacturer": self.extract_manufacturer(name),
                    }
                )

        return planes

    def get_summary(self):

        manufacturers = {
            aircraft["manufacturer"]
            for aircraft in self.aircraft
        }

        return {
            "total_aircraft": len(self.aircraft),
            "manufacturers": len(manufacturers),
            "aircraft": self.aircraft,
        }


fleet_service = FleetService()