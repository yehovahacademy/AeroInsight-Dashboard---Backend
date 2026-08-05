from app.clients.aeroapi_client import AeroAPIClient
from app.services.airport_loader import AirportLoader


class AirportService:

    def __init__(self):
        self.loader = AirportLoader()
        self.client = AeroAPIClient()

    async def get_airport(self, airport_code: str):
        return await self.client.get_airport(airport_code)

    async def get_airport(self, airport_code):
        static = self.loader.get_airport_by_iata(airport_code)
        
        live = await self.client.get_airport(airport_code)
        
        return {
                "static": static,
                "live": live
            }


airport_service = AirportService()