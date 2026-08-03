from pydantic import BaseModel

class AirportOverview(BaseModel):
    airport_name: str
    iata: str
    icao: str
    city: str
    country: str
    latitude: float
    longitude: float
    timezone: str
    elevation_ft: int
    airport_type: str