from app.database import get_connection
import psycopg2.extras


class CandidateRouteRepository:

    def get_all(self):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
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
                    FROM candidate_routes
                    ORDER BY estimated_monthly_profit DESC
                """)

                return cursor.fetchall()

    def get_by_id(self, candidate_id: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
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
                    FROM candidate_routes
                    WHERE candidate_id = %s
                """, (candidate_id,))

                return cursor.fetchone()

    def get_by_market(self, market_id: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
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
                    FROM candidate_routes
                    WHERE market_id = %s
                    ORDER BY estimated_monthly_profit DESC
                """, (market_id,))

                return cursor.fetchall()

    def get_by_status(self, planning_status: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
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
                    FROM candidate_routes
                    WHERE planning_status = %s
                    ORDER BY estimated_monthly_profit DESC
                """, (planning_status,))

                return cursor.fetchall()