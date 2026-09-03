from app.database import get_connection
import psycopg2.extras


class MarketRepository:

    def get_all(self):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        market_id,
                        origin,
                        destination,
                        distance_km,
                        market_region,
                        market_type,
                        business_share,
                        leisure_share,
                        connecting_share,
                        data_type
                    FROM public.markets
                    ORDER BY market_id
                    """
                )

                return cursor.fetchall()

    def get_by_id(self, market_id: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        market_id,
                        origin,
                        destination,
                        distance_km,
                        market_region,
                        market_type,
                        business_share,
                        leisure_share,
                        connecting_share,
                        data_type
                    FROM public.markets
                    WHERE market_id = %s
                    """,
                    (market_id,),
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
                        market_id,
                        origin,
                        destination,
                        distance_km,
                        market_region,
                        market_type,
                        business_share,
                        leisure_share,
                        connecting_share,
                        data_type
                    FROM public.markets
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
                        market_id,
                        origin,
                        destination,
                        distance_km,
                        market_region,
                        market_type,
                        business_share,
                        leisure_share,
                        connecting_share,
                        data_type
                    FROM public.markets
                    WHERE UPPER(destination) = UPPER(%s)
                    ORDER BY origin
                    """,
                    (destination,),
                )

                return cursor.fetchall()

    def get_market(self, origin: str, destination: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        market_id,
                        origin,
                        destination,
                        distance_km,
                        market_region,
                        market_type,
                        business_share,
                        leisure_share,
                        connecting_share,
                        data_type
                    FROM public.markets
                    WHERE
                        UPPER(origin) = UPPER(%s)
                        AND UPPER(destination) = UPPER(%s)
                    """,
                    (origin, destination),
                )

                return cursor.fetchone()


market_repository = MarketRepository()