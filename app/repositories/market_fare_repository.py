from app.database import get_connection
import psycopg2.extras


class MarketFareRepository:

    def get_all(self):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        fare_id,
                        market_id,
                        year,
                        month,
                        average_one_way_fare_inr,
                        business_fare_index,
                        leisure_fare_index,
                        fare_volatility,
                        data_type
                    FROM public.market_fares
                    ORDER BY year, month, market_id
                    """
                )

                return cursor.fetchall()

    def get_by_id(self, fare_id: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        fare_id,
                        market_id,
                        year,
                        month,
                        average_one_way_fare_inr,
                        business_fare_index,
                        leisure_fare_index,
                        fare_volatility,
                        data_type
                    FROM public.market_fares
                    WHERE fare_id = %s
                    """,
                    (fare_id,)
                )

                return cursor.fetchone()

    def get_by_market(self, market_id: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        fare_id,
                        market_id,
                        year,
                        month,
                        average_one_way_fare_inr,
                        business_fare_index,
                        leisure_fare_index,
                        fare_volatility,
                        data_type
                    FROM public.market_fares
                    WHERE market_id = %s
                    ORDER BY year, month
                    """,
                    (market_id,)
                )

                return cursor.fetchall()

    def get_by_period(self, year: int, month: int):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        fare_id,
                        market_id,
                        year,
                        month,
                        average_one_way_fare_inr,
                        business_fare_index,
                        leisure_fare_index,
                        fare_volatility,
                        data_type
                    FROM public.market_fares
                    WHERE year = %s
                    AND month = %s
                    ORDER BY market_id
                    """,
                    (year, month)
                )

                return cursor.fetchall()


market_fare_repository = MarketFareRepository()