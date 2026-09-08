from app.database import get_connection
import psycopg2.extras


class OperatingCostRepository:

    def get_all(self):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        cost_id,
                        market_id,
                        aircraft_type,
                        estimated_cost_per_flight,
                        fuel_cost_component,
                        airport_cost_component,
                        crew_cost_component,
                        maintenance_cost_component,
                        other_cost_component,
                        data_type
                    FROM operating_costs
                    ORDER BY cost_id
                """)

                return cursor.fetchall()

    def get_by_id(self, cost_id: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        cost_id,
                        market_id,
                        aircraft_type,
                        estimated_cost_per_flight,
                        fuel_cost_component,
                        airport_cost_component,
                        crew_cost_component,
                        maintenance_cost_component,
                        other_cost_component,
                        data_type
                    FROM operating_costs
                    WHERE cost_id = %s
                """, (cost_id,))

                return cursor.fetchone()

    def get_by_market(self, market_id: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        cost_id,
                        market_id,
                        aircraft_type,
                        estimated_cost_per_flight,
                        fuel_cost_component,
                        airport_cost_component,
                        crew_cost_component,
                        maintenance_cost_component,
                        other_cost_component,
                        data_type
                    FROM operating_costs
                    WHERE market_id = %s
                    ORDER BY aircraft_type
                """, (market_id,))

                return cursor.fetchall()

    def get_by_aircraft(self, aircraft_type: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        cost_id,
                        market_id,
                        aircraft_type,
                        estimated_cost_per_flight,
                        fuel_cost_component,
                        airport_cost_component,
                        crew_cost_component,
                        maintenance_cost_component,
                        other_cost_component,
                        data_type
                    FROM operating_costs
                    WHERE aircraft_type = %s
                    ORDER BY market_id
                """, (aircraft_type,))

                return cursor.fetchall()