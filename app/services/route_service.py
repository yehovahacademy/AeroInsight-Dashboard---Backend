from app.repositories.route_repository import route_repository


class RouteService:

    def get_all_routes(self):
        return route_repository.get_all()

    def get_route_by_id(self, route_id: int):
        return route_repository.get_by_id(route_id)

    def get_routes_from_origin(self, origin: str):
        return route_repository.get_from_origin(origin)

    def get_routes_to_destination(self, destination: str):
        return route_repository.get_to_destination(destination)

    def get_route(self, origin: str, destination: str):
        return route_repository.get_route(origin, destination)


route_service = RouteService()