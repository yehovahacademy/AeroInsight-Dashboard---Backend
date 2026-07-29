import httpx

from app.config.settings import settings


class ApiNinjasClient:

    BASE_URL = "https://api.api-ninjas.com/v1"

    def __init__(self):
        self.headers = {
            "X-Api-Key": settings.API_NINJAS_KEY
        }

    async def get_airports(self, name: str):
        async with httpx.AsyncClient(timeout=10) as client:

            response = await client.get(
                f"{self.BASE_URL}/airports",
                headers=self.headers,
                params={
                    "name": name
                }
            )

            response.raise_for_status()

            return response.json()