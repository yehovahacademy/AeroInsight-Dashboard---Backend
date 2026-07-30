import httpx

from app.config.settings import settings


class AeroApiClient:
    BASE_URL = "https://aeroapi.flightaware.com/aeroapi"

    def __init__(self):
        self.headers = {
            "x-apikey": settings.AEROAPI_KEY
        }

    async def get_airport(self, airport_code: str):
        raise NotImplementedError("AeroAPI integration pending")

    async def get_flight(self, ident: str):
        raise NotImplementedError("AeroAPI integration pending")

    async def get_arrivals(self, airport_code: str):
        raise NotImplementedError("AeroAPI integration pending")

    async def get_departures(self, airport_code: str):
        raise NotImplementedError("AeroAPI integration pending")