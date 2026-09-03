from app.repositories.monthly_demand_repository import monthly_demand_repository


class MonthlyDemandService:

    def get_all_demand(self):
        return monthly_demand_repository.get_all()

    def get_demand_by_id(self, demand_id: str):
        return monthly_demand_repository.get_by_id(demand_id)

    def get_demand_by_market(
        self,
        market_id: str,
        year: int | None = None,
        month: int | None = None
    ):
        return monthly_demand_repository.get_by_market(
            market_id=market_id,
            year=year,
            month=month
        )

    def get_demand_by_origin(self, origin: str):
        return monthly_demand_repository.get_by_origin(origin)

    def get_demand_by_destination(self, destination: str):
        return monthly_demand_repository.get_by_destination(destination)


monthly_demand_service = MonthlyDemandService()