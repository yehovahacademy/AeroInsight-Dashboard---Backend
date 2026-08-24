from app.repositories.airport_repository import airport_repository


class AirportLoader:

    def get_airport_by_iata(self, iata: str):
        row = airport_repository.get_by_iata(iata)

        if row is None:
            return None

        return self._format_airport(row)


    def get_airport_by_icao(self, icao: str):
        row = airport_repository.get_by_icao(icao)

        if row is None:
            return None

        return self._format_airport(row)


    def search_airports(self, query: str):
        rows = airport_repository.search(query)

        return [
            self._format_airport(row)
            for row in rows
        ]



    def get_all_airports(self):
        rows = airport_repository.get_all()

        return [
                self._format_airport(row)
                for row in rows
            ]
    

    


    def _format_airport(self, row):
        return {
           "id": row["id"],
        "iata": row["iata"],
        "icao": row["icao"],
        "name": row["name"],
        "city": row["city"],
        "state": row["state"],
        "latitude": row["latitude"],
        "longitude": row["longitude"],
        "elevation": row["elevation"],
        "type": row["type"],
        "timezone": row["timezone"],
        }


airport_loader = AirportLoader()