from pydantic import BaseModel


class WhatIfRequest(BaseModel):
    origin: str
    destination: str
    aircraft: str
    flights_per_day: int
    load_factor: float
    average_fare: float