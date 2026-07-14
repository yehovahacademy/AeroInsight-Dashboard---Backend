from pydantic import BaseModel

class Airline(BaseModel):
    id: int
    name: str
    iata: str
    icao: str
    country: str
    logo: str

