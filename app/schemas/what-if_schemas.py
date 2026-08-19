from pydantic import BaseModel, Field
from typing import Optional


class WhatIfRequest(BaseModel):
    origin: str
    destination: str

    aircraft: str = "A320"

    flights_per_day: int = Field(
        default=6,
        ge=1,
        le=30
    )

    scenario_flights_per_day: int = Field(
        default=8,
        ge=1,
        le=30
    )

    load_factor: float = Field(
        default=0.84,
        ge=0.0,
        le=1.0
    )

    scenario_load_factor: float = Field(
        default=0.87,
        ge=0.0,
        le=1.0
    )

    average_fare: float = Field(
        default=5800,
        gt=0
    )

    season: Optional[str] = None