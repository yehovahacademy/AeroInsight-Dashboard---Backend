from app.clients.aeroapi_client import AeroApiClient


class FlightService:

    def __init__(self):
        self.client = AeroApiClient()

    async def get_flight(self, ident: str):
        return await self.client.get_flight(ident)


flight_service = FlightService()