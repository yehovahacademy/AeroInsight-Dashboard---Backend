from app.repositories.market_repository import market_repository


class MarketService:

    def get_all_markets(self):
        return market_repository.get_all()

    def get_market_by_id(self, market_id: str):
        return market_repository.get_by_id(market_id)

    def get_market_from_origin(self, origin: str):
        return market_repository.get_from_origin(origin)

    def get_market_to_destination(self, destination: str):
        return market_repository.get_to_destination(destination)

    def get_market(self, origin: str, destination: str):
        return market_repository.get_market(origin, destination)


market_service = MarketService()