from pydantic import BaseModel


class AirportData(BaseModel):
    id: int
    name: str
    city: str
    country: str
    iata: str
    icao: str
    latitude: float
    longitude: float
    altitude: int
    timezone: str
    airport_type: str