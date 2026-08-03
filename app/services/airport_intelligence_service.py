# app/services/airport_intelligence_service.py

from fastapi import HTTPException

from app.utils.airport_database import AIRPORTS


class AirportIntelligenceService:
    """
    Service responsible for collecting and preparing
    airport intelligence data.
    """

    async def get_airport(self, iata: str):
        """
        Get airport details from the local database.
        """
        airport = AIRPORTS.get(iata.upper())

        if not airport:
            raise HTTPException(
                status_code=404,
                detail=f"Airport '{iata}' not found."
            )

        return airport

    async def get_weather(self, airport: dict):
        """
        Placeholder weather service.

        Replace this with your existing weather service
        or Open-Meteo integration.
        """

        return {
            "temperature": 29,
            "condition": "Partly Cloudy",
            "humidity": 82,
            "wind_speed": 14,
            "visibility": 10
        }

    async def get_statistics(self, airport: dict):
        """
        Placeholder operational statistics.
        """

        return {
            "daily_flights": 945,
            "on_time_percentage": 86,
            "average_delay_minutes": 12
        }

    async def get_connectivity(self, airport: dict):
        """
        Placeholder connectivity information.
        """

        return {
            "connected_airports": 124,
            "top_routes": [
                "DEL",
                "BLR",
                "HYD",
                "MAA",
                "CCU"
            ],
            "major_airlines": [
                "IndiGo",
                "Air India",
                "Akasa Air",
                "SpiceJet",
                "Vistara"
            ]
        }

    async def analyze_airport(self, iata: str):
        """
        Main service entry point.

        Combines all airport intelligence into a single response.
        """

        airport = await self.get_airport(iata)

        weather = await self.get_weather(airport)

        statistics = await self.get_statistics(airport)

        connectivity = await self.get_connectivity(airport)

        return {
            "airport": airport,
            "weather": weather,
            "statistics": statistics,
            "connectivity": connectivity
        }


airport_intelligence_service = AirportIntelligenceService()