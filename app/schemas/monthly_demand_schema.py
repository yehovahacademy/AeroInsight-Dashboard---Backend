from pydantic import BaseModel


class MonthlyDemandResponse(BaseModel):

    demand_id: str

    market_id: str

    year: int

    month: int

    total_demand: int

    business_demand: int

    leisure_demand: int

    connecting_demand: int

    seasonality_index: float

    demand_growth_index: float

    data_type: str