from app.repositories.monthly_capacity_repository import (
    monthly_capacity_repository
)


class MonthlyCapacityService:

    def get_all_capacity(self):
        return monthly_capacity_repository.get_all()

    def get_capacity_by_id(self, capacity_id: str):
        return monthly_capacity_repository.get_by_id(capacity_id)

    def get_capacity_by_market(
        self,
        market_id: str,
        year: int | None = None,
        month: int | None = None
    ):
        return monthly_capacity_repository.get_by_market(
            market_id=market_id,
            year=year,
            month=month
        )

    def get_capacity_by_origin(self, origin: str):
        return monthly_capacity_repository.get_by_origin(origin)

    def get_capacity_by_destination(self, destination: str):
        return monthly_capacity_repository.get_by_destination(destination)


monthly_capacity_service = MonthlyCapacityService()