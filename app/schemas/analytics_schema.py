from pydantic import BaseModel

class Analytics(BaseModel):
    total_flights: int
    on_time_flights: int
    delayed_flights: int