from pydantic import BaseModel

class Flight(BaseModel):
   flight_number: str
   airline: str
   origin: str
   destination: str
   aircraft: str
   status: str
   altitude: int
   speed: int
   departure_time: str
   arrival_time: str