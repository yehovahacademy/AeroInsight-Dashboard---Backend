from app.database import get_connection
import psycopg2.extras


class HistoricalTrafficRepository:

    def get_all(self):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        traffic_id,
                        market_id,
                        year,
                        month,
                        origin,
                        destination,
                        passengers,
                        flights,
                        available_seats,
                        load_factor,
                        traffic_type,
                        data_type
                    FROM public.historical_traffic
                    ORDER BY year, month, market_id
                    """
                )

                return cursor.fetchall()

    def get_by_id(self, traffic_id: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        traffic_id,
                        market_id,
                        year,
                        month,
                        origin,
                        destination,
                        passengers,
                        flights,
                        available_seats,
                        load_factor,
                        traffic_type,
                        data_type
                    FROM public.historical_traffic
                    WHERE traffic_id = %s
                    """,
                    (traffic_id,),
                )

                return cursor.fetchone()

    def get_by_market(
        self,
        market_id: str,
        year: int | None = None,
        month: int | None = None,
    ):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                query = """
                    SELECT
                        traffic_id,
                        market_id,
                        year,
                        month,
                        origin,
                        destination,
                        passengers,
                        flights,
                        available_seats,
                        load_factor,
                        traffic_type,
                        data_type
                    FROM public.historical_traffic
                    WHERE market_id = %s
                """

                params = [market_id]

                if year is not None:
                    query += " AND year = %s"
                    params.append(year)

                if month is not None:
                    query += " AND month = %s"
                    params.append(month)

                query += " ORDER BY year, month"

                cursor.execute(query, params)

                return cursor.fetchall()

    def get_by_origin(self, origin: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        traffic_id,
                        market_id,
                        year,
                        month,
                        origin,
                        destination,
                        passengers,
                        flights,
                        available_seats,
                        load_factor,
                        traffic_type,
                        data_type
                    FROM public.historical_traffic
                    WHERE UPPER(origin) = UPPER(%s)
                    ORDER BY year, month, destination
                    """,
                    (origin,),
                )

                return cursor.fetchall()

    def get_by_destination(self, destination: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        traffic_id,
                        market_id,
                        year,
                        month,
                        origin,
                        destination,
                        passengers,
                        flights,
                        available_seats,
                        load_factor,
                        traffic_type,
                        data_type
                    FROM public.historical_traffic
                    WHERE UPPER(destination) = UPPER(%s)
                    ORDER BY year, month, origin
                    """,
                    (destination,),
                )

                return cursor.fetchall()


historical_traffic_repository = HistoricalTrafficRepository()