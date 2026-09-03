from pydantic import BaseModel


class HistoricalTrafficResponse(BaseModel):

    traffic_id: str

    market_id: str

    year: int

    month: int

    origin: str

    destination: str

    passengers: int

    flights: int

    available_seats: int

    load_factor: float

    traffic_type: str

    data_type: str