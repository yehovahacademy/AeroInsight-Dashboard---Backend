from app.database import get_connection
import psycopg2.extras


class MonthlyDemandRepository:

    def get_all(self):
        conn = get_connection()

        try:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute("""
                    SELECT
                        demand_id,
                        market_id,
                        year,
                        month,
                        total_demand,
                        business_demand,
                        leisure_demand,
                        connecting_demand,
                        seasonality_index,
                        demand_growth_index,
                        data_type
                    FROM public.monthly_demand
                    ORDER BY year, month, market_id
                """)

                return cursor.fetchall()

        finally:
            conn.close()

    def get_by_id(self, demand_id: str):
        conn = get_connection()

        try:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute("""
                    SELECT
                        demand_id,
                        market_id,
                        year,
                        month,
                        total_demand,
                        business_demand,
                        leisure_demand,
                        connecting_demand,
                        seasonality_index,
                        demand_growth_index,
                        data_type
                    FROM public.monthly_demand
                    WHERE demand_id = %s
                """, (demand_id,))

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
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:

                query = """
                    SELECT
                        demand_id,
                        market_id,
                        year,
                        month,
                        total_demand,
                        business_demand,
                        leisure_demand,
                        connecting_demand,
                        seasonality_index,
                        demand_growth_index,
                        data_type
                    FROM public.monthly_demand
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
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute("""
                    SELECT
                        d.demand_id,
                        d.market_id,
                        d.year,
                        d.month,
                        d.total_demand,
                        d.business_demand,
                        d.leisure_demand,
                        d.connecting_demand,
                        d.seasonality_index,
                        d.demand_growth_index,
                        d.data_type
                    FROM public.monthly_demand d
                    JOIN public.markets m
                        ON d.market_id = m.market_id
                    WHERE UPPER(m.origin) = UPPER(%s)
                    ORDER BY d.year, d.month, m.destination
                """, (origin,))

                return cursor.fetchall()

        finally:
            conn.close()

    def get_by_destination(self, destination: str):
        conn = get_connection()

        try:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute("""
                    SELECT
                        d.demand_id,
                        d.market_id,
                        d.year,
                        d.month,
                        d.total_demand,
                        d.business_demand,
                        d.leisure_demand,
                        d.connecting_demand,
                        d.seasonality_index,
                        d.demand_growth_index,
                        d.data_type
                    FROM public.monthly_demand d
                    JOIN public.markets m
                        ON d.market_id = m.market_id
                    WHERE UPPER(m.destination) = UPPER(%s)
                    ORDER BY d.year, d.month, m.origin
                """, (destination,))

                return cursor.fetchall()

        finally:
            conn.close()


monthly_demand_repository = MonthlyDemandRepository()