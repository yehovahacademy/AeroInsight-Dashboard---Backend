from pydantic import BaseModel


class RouteSummary(BaseModel):
    id: str
    origin: str
    destination: str
    originCode: str
    destinationCode: str

    loadFactor: int
    revenue: str
    recommendation: str