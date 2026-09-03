from pydantic import BaseModel


class MonthlyCapacityResponse(BaseModel):

    capacity_id: str

    market_id: str

    year: int

    month: int

    existing_seats: int

    existing_flights: int

    average_aircraft_size: float

    average_load_factor: float

    capacity_type: str

    data_type: str