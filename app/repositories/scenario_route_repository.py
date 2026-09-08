from app.database import get_connection
import psycopg2.extras


class ScenarioRouteRepository:

    def get_all(self):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        scenario_route_id,
                        scenario_id,
                        candidate_id,
                        market_id,
                        origin,
                        destination,
                        proposed_aircraft,
                        proposed_flights_per_day,
                        estimated_monthly_passengers,
                        estimated_monthly_revenue,
                        estimated_monthly_cost,
                        estimated_monthly_profit,
                        estimated_load_factor,
                        planning_status,
                        data_type
                    FROM scenario_routes
                    ORDER BY scenario_route_id
                """)

                return cursor.fetchall()

    def get_by_id(self, scenario_route_id: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        scenario_route_id,
                        scenario_id,
                        candidate_id,
                        market_id,
                        origin,
                        destination,
                        proposed_aircraft,
                        proposed_flights_per_day,
                        estimated_monthly_passengers,
                        estimated_monthly_revenue,
                        estimated_monthly_cost,
                        estimated_monthly_profit,
                        estimated_load_factor,
                        planning_status,
                        data_type
                    FROM scenario_routes
                    WHERE scenario_route_id = %s
                """, (scenario_route_id,))

                return cursor.fetchone()

    def get_by_scenario(self, scenario_id: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        scenario_route_id,
                        scenario_id,
                        candidate_id,
                        market_id,
                        origin,
                        destination,
                        proposed_aircraft,
                        proposed_flights_per_day,
                        estimated_monthly_passengers,
                        estimated_monthly_revenue,
                        estimated_monthly_cost,
                        estimated_monthly_profit,
                        estimated_load_factor,
                        planning_status,
                        data_type
                    FROM scenario_routes
                    WHERE scenario_id = %s
                    ORDER BY estimated_monthly_profit DESC
                """, (scenario_id,))

                return cursor.fetchall()

    def get_by_market(self, market_id: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        scenario_route_id,
                        scenario_id,
                        candidate_id,
                        market_id,
                        origin,
                        destination,
                        proposed_aircraft,
                        proposed_flights_per_day,
                        estimated_monthly_passengers,
                        estimated_monthly_revenue,
                        estimated_monthly_cost,
                        estimated_monthly_profit,
                        estimated_load_factor,
                        planning_status,
                        data_type
                    FROM scenario_routes
                    WHERE market_id = %s
                    ORDER BY estimated_monthly_profit DESC
                """, (market_id,))

                return cursor.fetchall()