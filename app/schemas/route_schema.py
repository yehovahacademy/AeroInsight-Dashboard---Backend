from pydantic import BaseModel


class RouteResponse(BaseModel):
    route_id: int
    origin_iata: str
    destination_iata: str
    origin_latitude: float
    origin_longitude: float
    destination_latitude: float
    destination_longitude: float
    distance_km: int
    region: str