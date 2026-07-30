from app.clients.aeroapi_client import AeroApiClient


class AirportService:

    def __init__(self):
        self.client = AeroApiClient()

    async def get_airport(self, airport_code: str):
        return await self.client.get_airport(airport_code)


airport_service = AirportService()