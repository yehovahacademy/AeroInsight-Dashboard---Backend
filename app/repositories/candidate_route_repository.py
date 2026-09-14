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
                        candidate_route_id,
                        market_id,
                        origin,
                        destination,
                        planning_year,
                        aircraft_type,
                        flights_per_day,
                        annual_flights,
                        distance_km,
                        block_time_hours,
                        seat_capacity,
                        annual_seat_capacity,
                        forecast_demand,
                        expected_passengers,
                        expected_load_factor,
                        average_fare,
                        ancillary_revenue_per_passenger,
                        cargo_revenue,
                        total_revenue,
                        fuel_cost,
                        maintenance_cost,
                        crew_cost,
                        airport_cost,
                        navigation_cost,
                        handling_cost,
                        catering_cost,
                        aircraft_ownership_or_lease_cost,
                        other_cost,
                        total_cost,
                        operating_profit
                    FROM public.candidate_routes
                    ORDER BY operating_profit DESC
                """)

                return cursor.fetchall()

    def get_by_id(self, candidate_route_id: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        candidate_route_id,
                        market_id,
                        origin,
                        destination,
                        planning_year,
                        aircraft_type,
                        flights_per_day,
                        annual_flights,
                        distance_km,
                        block_time_hours,
                        seat_capacity,
                        annual_seat_capacity,
                        forecast_demand,
                        expected_passengers,
                        expected_load_factor,
                        average_fare,
                        ancillary_revenue_per_passenger,
                        cargo_revenue,
                        total_revenue,
                        fuel_cost,
                        maintenance_cost,
                        crew_cost,
                        airport_cost,
                        navigation_cost,
                        handling_cost,
                        catering_cost,
                        aircraft_ownership_or_lease_cost,
                        other_cost,
                        total_cost,
                        operating_profit
                    FROM public.candidate_routes
                    WHERE candidate_route_id = %s
                """, (candidate_route_id,))

                return cursor.fetchone()

    def get_by_market(self, market_id: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        candidate_route_id,
                        market_id,
                        origin,
                        destination,
                        planning_year,
                        aircraft_type,
                        flights_per_day,
                        annual_flights,
                        distance_km,
                        block_time_hours,
                        seat_capacity,
                        annual_seat_capacity,
                        forecast_demand,
                        expected_passengers,
                        expected_load_factor,
                        average_fare,
                        ancillary_revenue_per_passenger,
                        cargo_revenue,
                        total_revenue,
                        fuel_cost,
                        maintenance_cost,
                        crew_cost,
                        airport_cost,
                        navigation_cost,
                        handling_cost,
                        catering_cost,
                        aircraft_ownership_or_lease_cost,
                        other_cost,
                        total_cost,
                        operating_profit
                    FROM public.candidate_routes
                    WHERE market_id = %s
                    ORDER BY operating_profit DESC
                """, (market_id,))

                return cursor.fetchall()