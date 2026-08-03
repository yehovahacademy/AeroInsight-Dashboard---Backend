from pydantic import BaseModel

class AirportOverview(BaseModel):
    iata: str
    icao: str
    name: str
    city: str
    country: str
    latitude: float
    longitude: float
    elevation_ft: int
    timezone: str
    airport_type: str
    runways: int



class WeatherInfo(BaseModel):
    temperature: float
    condition: str
    humidity: int
    wind_speed: float
    visibility: float


class AirportStatistics(BaseModel):
    daily_flights: int
    on_time_percentage: int
    average_delay_minutes: int


class Connectivity(BaseModel):
    connected_airports: int
    top_routes: list[str]
    major_airlines: list[str]


class AirportIntelligenceResponse(BaseModel):
    airport: AirportOverview
    weather: WeatherInfo
    statistics: AirportStatistics
    connectivity: Connectivity