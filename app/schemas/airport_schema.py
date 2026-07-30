from pydantic import BaseModel


class Airport(BaseModel):
    iata: str
    icao: str | None = None
    name: str
    city: str
    country: str
    latitude: float
    longitude: float