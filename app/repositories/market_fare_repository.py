from app.database import get_connection
import psycopg2.extras


class MarketFareRepository:

    def get_all(self):
        conn = get_connection()

        try:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
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
                """)

                return cursor.fetchall()

        finally:
            conn.close()

    def get_by_id(self, fare_id: str):
        conn = get_connection()

        try:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
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
                """, (fare_id,))

                return cursor.fetchone()

        finally:
            conn.close()

    def get_by_market(
        self,
        market_id: str,
        year: int | None = None,
        month: int | None = None
    ):
        conn = get_connection()

        try:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                query = """
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

        finally:
            conn.close()

    def get_by_origin(self, origin: str):
        conn = get_connection()

        try:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        f.fare_id,
                        f.market_id,
                        f.year,
                        f.month,
                        f.average_one_way_fare_inr,
                        f.business_fare_index,
                        f.leisure_fare_index,
                        f.fare_volatility,
                        f.data_type
                    FROM public.market_fares f
                    JOIN public.markets m
                        ON f.market_id = m.market_id
                    WHERE UPPER(m.origin) = UPPER(%s)
                    ORDER BY f.year, f.month, m.destination
                """, (origin,))

                return cursor.fetchall()

        finally:
            conn.close()

    def get_by_destination(self, destination: str):
        conn = get_connection()

        try:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        f.fare_id,
                        f.market_id,
                        f.year,
                        f.month,
                        f.average_one_way_fare_inr,
                        f.business_fare_index,
                        f.leisure_fare_index,
                        f.fare_volatility,
                        f.data_type
                    FROM public.market_fares f
                    JOIN public.markets m
                        ON f.market_id = m.market_id
                    WHERE UPPER(m.destination) = UPPER(%s)
                    ORDER BY f.year, f.month, m.origin
                """, (destination,))

                return cursor.fetchall()

        finally:
            conn.close()


market_fare_repository = MarketFareRepository()