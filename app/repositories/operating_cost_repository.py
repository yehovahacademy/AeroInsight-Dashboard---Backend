from app.database import get_connection
import psycopg2.extras


class OperatingCostRepository:

    def get_all(self):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        cost_id,
                        market_id,
                        year,
                        aircraft_type,
                        estimated_cost_per_flight,
                        fuel_cost_component,
                        airport_cost_component,
                        crew_cost_component,
                        maintenance_cost_component,
                        other_cost_component,
                        data_type
                    FROM public.operating_costs
                    ORDER BY year, market_id, aircraft_type
                """)

                return cursor.fetchall()

    def get_by_id(self, cost_id: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        cost_id,
                        market_id,
                        year,
                        aircraft_type,
                        estimated_cost_per_flight,
                        fuel_cost_component,
                        airport_cost_component,
                        crew_cost_component,
                        maintenance_cost_component,
                        other_cost_component,
                        data_type
                    FROM public.operating_costs
                    WHERE cost_id = %s
                """, (cost_id,))

                return cursor.fetchone()

    def get_by_market(
        self,
        market_id: str,
        year: int | None = None
    ):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                query = """
                    SELECT
                        cost_id,
                        market_id,
                        year,
                        aircraft_type,
                        estimated_cost_per_flight,
                        fuel_cost_component,
                        airport_cost_component,
                        crew_cost_component,
                        maintenance_cost_component,
                        other_cost_component,
                        data_type
                    FROM public.operating_costs
                    WHERE market_id = %s
                """

                params = [market_id]

                if year is not None:
                    query += " AND year = %s"
                    params.append(year)

                query += " ORDER BY year, aircraft_type"

                cursor.execute(query, params)

                return cursor.fetchall()

    def get_by_aircraft(
        self,
        aircraft_type: str,
        year: int | None = None
    ):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                query = """
                    SELECT
                        cost_id,
                        market_id,
                        year,
                        aircraft_type,
                        estimated_cost_per_flight,
                        fuel_cost_component,
                        airport_cost_component,
                        crew_cost_component,
                        maintenance_cost_component,
                        other_cost_component,
                        data_type
                    FROM public.operating_costs
                    WHERE aircraft_type = %s
                """

                params = [aircraft_type]

                if year is not None:
                    query += " AND year = %s"
                    params.append(year)

                query += " ORDER BY year, market_id"

                cursor.execute(query, params)

                return cursor.fetchall()


operating_cost_repository = OperatingCostRepository()