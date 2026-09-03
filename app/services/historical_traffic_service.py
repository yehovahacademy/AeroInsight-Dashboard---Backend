from app.repositories.historical_traffic_repository import historical_traffic_repository


class HistoricalTrafficService:

    def get_all_traffic(self):
        return historical_traffic_repository.get_all()

    def get_traffic_by_id(self, traffic_id: str):
        return historical_traffic_repository.get_by_id(traffic_id)

    def get_traffic_by_market(
        self,
        market_id: str,
        year: int | None = None,
        month: int | None = None
    ):
        return historical_traffic_repository.get_by_market(
            market_id=market_id,
            year=year,
            month=month
        )

    def get_traffic_by_origin(self, origin: str):
        return historical_traffic_repository.get_by_origin(origin)

    def get_traffic_by_destination(self, destination: str):
        return historical_traffic_repository.get_by_destination(destination)


historical_traffic_service = HistoricalTrafficService()