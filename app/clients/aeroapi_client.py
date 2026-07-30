import requests

from app.core.config import settings


class AeroAPIClient:

    BASE_URL = "https://aeroapi.flightaware.com/aeroapi"


    def __init__(self):

        self.headers = {
            "x-apikey": settings.AEROAPI_KEY
        }


    def get_flight(self, ident):

        url = f"{self.BASE_URL}/flights/{ident}"

        response = requests.get(
            url,
            headers=self.headers
        )

        response.raise_for_status()

        return response.json()