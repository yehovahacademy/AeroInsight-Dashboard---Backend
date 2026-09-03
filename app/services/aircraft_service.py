from app.repositories.aircraft_repository import aircraft_repository


class AircraftService:

    def get_all_aircraft(self):
        return aircraft_repository.get_all()

    def get_aircraft_by_type(self, aircraft_type: str):
        return aircraft_repository.get_by_type(aircraft_type)

    def get_aircraft_by_manufacturer(self, manufacturer: str):
        return aircraft_repository.get_by_manufacturer(manufacturer)

    def search_aircraft(self, query: str):
        return aircraft_repository.search(query)


aircraft_service = AircraftService()