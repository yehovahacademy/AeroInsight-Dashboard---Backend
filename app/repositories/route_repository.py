from app.Database import get_connection
import psycopg2.extras


class RouteRepository:

    def get_all(self):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        route_id,
                        origin,
                        destination,
                        origin_lat,
                        origin_long,
                        destination_lat,
                        destination_long,
                        distance_km,
                        region
                    FROM public.routes
                    ORDER BY route_id
                    """
                )

                return cursor.fetchall()

    def get_by_id(self, route_id: int):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        route_id,
                        origin,
                        destination,
                        origin_lat,
                        origin_long,
                        destination_lat,
                        destination_long,
                        distance_km,
                        region
                    FROM public.routes
                    WHERE route_id = %s
                    """,
                    (route_id,),
                )

                return cursor.fetchone()

    def get_from_origin(self, origin: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        route_id,
                        origin,
                        destination,
                        origin_lat,
                        origin_long,
                        destination_lat,
                        destination_long,
                        distance_km,
                        region
                    FROM public.routes
                    WHERE UPPER(origin) = UPPER(%s)
                    ORDER BY destination
                    """,
                    (origin,),
                )

                return cursor.fetchall()

    def get_to_destination(self, destination: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        route_id,
                        origin,
                        destination,
                        origin_lat,
                        origin_long,
                        destination_lat,
                        destination_long,
                        distance_km,
                        region
                    FROM public.routes
                    WHERE UPPER(destination) = UPPER(%s)
                    ORDER BY origin
                    """,
                    (destination,),
                )

                return cursor.fetchall()

    def get_route(self, origin: str, destination: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        route_id,
                        origin,
                        destination,
                        origin_lat,
                        origin_long,
                        destination_lat,
                        destination_long,
                        distance_km,
                        region
                    FROM public.routes
                    WHERE
                        UPPER(origin) = UPPER(%s)
                        AND UPPER(destination) = UPPER(%s)
                    """,
                    (origin, destination),
                )

                return cursor.fetchone()


route_repository = RouteRepository()