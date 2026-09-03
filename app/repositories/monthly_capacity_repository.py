from app.database import get_connection
import psycopg2.extras


class MonthlyCapacityRepository:

    def get_all(self):
        conn = get_connection()

        try:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        capacity_id,
                        market_id,
                        year,
                        month,
                        existing_seats,
                        existing_flights,
                        average_aircraft_size,
                        average_load_factor,
                        capacity_type,
                        data_type
                    FROM public.monthly_capacity
                    ORDER BY year, month, market_id
                """)

                return cursor.fetchall()

        finally:
            conn.close()

    def get_by_id(self, capacity_id: str):
        conn = get_connection()

        try:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        capacity_id,
                        market_id,
                        year,
                        month,
                        existing_seats,
                        existing_flights,
                        average_aircraft_size,
                        average_load_factor,
                        capacity_type,
                        data_type
                    FROM public.monthly_capacity
                    WHERE capacity_id = %s
                """, (capacity_id,))

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
                        capacity_id,
                        market_id,
                        year,
                        month,
                        existing_seats,
                        existing_flights,
                        average_aircraft_size,
                        average_load_factor,
                        capacity_type,
                        data_type
                    FROM public.monthly_capacity
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
                        c.capacity_id,
                        c.market_id,
                        c.year,
                        c.month,
                        c.existing_seats,
                        c.existing_flights,
                        c.average_aircraft_size,
                        c.average_load_factor,
                        c.capacity_type,
                        c.data_type
                    FROM public.monthly_capacity c
                    JOIN public.markets m
                        ON c.market_id = m.market_id
                    WHERE UPPER(m.origin) = UPPER(%s)
                    ORDER BY c.year, c.month, m.destination
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
                        c.capacity_id,
                        c.market_id,
                        c.year,
                        c.month,
                        c.existing_seats,
                        c.existing_flights,
                        c.average_aircraft_size,
                        c.average_load_factor,
                        c.capacity_type,
                        c.data_type
                    FROM public.monthly_capacity c
                    JOIN public.markets m
                        ON c.market_id = m.market_id
                    WHERE UPPER(m.destination) = UPPER(%s)
                    ORDER BY c.year, c.month, m.origin
                """, (destination,))

                return cursor.fetchall()

        finally:
            conn.close()


monthly_capacity_repository = MonthlyCapacityRepository()