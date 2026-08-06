from pydantic import BaseModel


class Aircraft(BaseModel):
    name: str
    iata_code: str | None = None
    icao_code: str | None = None
    manufacturer: str


class FleetSummary(BaseModel):
    total_aircraft: int
    manufacturers: int
    aircraft: list[Aircraft]