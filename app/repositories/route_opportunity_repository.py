from app.database import get_connection
import psycopg2.extras


class RouteOpportunityRepository:

    def get_all(self):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        market_id,
                        origin,
                        destination,
                        planning_year,
                        forecast_demand,
                        existing_capacity,
                        capacity_gap,
                        expected_passengers,
                        expected_load_factor,
                        average_fare,
                        revenue_opportunity,
                        estimated_operating_cost,
                        profit_opportunity,
                        profit_margin,
                        competition_score,
                        demand_score,
                        capacity_gap_score,
                        fare_score,
                        profitability_score,
                        strategic_score,
                        risk_score,
                        opportunity_score,
                        recommendation,
                        data_type
                    FROM public.route_opportunity
                    ORDER BY opportunity_score DESC
                """)

                return cursor.fetchall()

    def get_by_market(self, market_id: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        market_id,
                        origin,
                        destination,
                        planning_year,
                        forecast_demand,
                        existing_capacity,
                        capacity_gap,
                        expected_passengers,
                        expected_load_factor,
                        average_fare,
                        revenue_opportunity,
                        estimated_operating_cost,
                        profit_opportunity,
                        profit_margin,
                        competition_score,
                        demand_score,
                        capacity_gap_score,
                        fare_score,
                        profitability_score,
                        strategic_score,
                        risk_score,
                        opportunity_score,
                        recommendation,
                        data_type
                    FROM public.route_opportunity
                    WHERE market_id = %s
                """, (market_id,))

                return cursor.fetchone()

    def get_by_origin(self, origin: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        market_id,
                        origin,
                        destination,
                        planning_year,
                        forecast_demand,
                        existing_capacity,
                        capacity_gap,
                        expected_passengers,
                        expected_load_factor,
                        average_fare,
                        revenue_opportunity,
                        estimated_operating_cost,
                        profit_opportunity,
                        profit_margin,
                        competition_score,
                        demand_score,
                        capacity_gap_score,
                        fare_score,
                        profitability_score,
                        strategic_score,
                        risk_score,
                        opportunity_score,
                        recommendation,
                        data_type
                    FROM public.route_opportunity
                    WHERE UPPER(origin) = UPPER(%s)
                    ORDER BY opportunity_score DESC
                """, (origin,))

                return cursor.fetchall()

    def get_by_destination(self, destination: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        market_id,
                        origin,
                        destination,
                        planning_year,
                        forecast_demand,
                        existing_capacity,
                        capacity_gap,
                        expected_passengers,
                        expected_load_factor,
                        average_fare,
                        revenue_opportunity,
                        estimated_operating_cost,
                        profit_opportunity,
                        profit_margin,
                        competition_score,
                        demand_score,
                        capacity_gap_score,
                        fare_score,
                        profitability_score,
                        strategic_score,
                        risk_score,
                        opportunity_score,
                        recommendation,
                        data_type
                    FROM public.route_opportunity
                    WHERE UPPER(destination) = UPPER(%s)
                    ORDER BY opportunity_score DESC
                """, (destination,))

                return cursor.fetchall()

    def get_by_recommendation(self, recommendation: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        market_id,
                        origin,
                        destination,
                        planning_year,
                        forecast_demand,
                        existing_capacity,
                        capacity_gap,
                        expected_passengers,
                        expected_load_factor,
                        average_fare,
                        revenue_opportunity,
                        estimated_operating_cost,
                        profit_opportunity,
                        profit_margin,
                        competition_score,
                        demand_score,
                        capacity_gap_score,
                        fare_score,
                        profitability_score,
                        strategic_score,
                        risk_score,
                        opportunity_score,
                        recommendation,
                        data_type
                    FROM public.route_opportunity
                    WHERE UPPER(recommendation) = UPPER(%s)
                    ORDER BY opportunity_score DESC
                """, (recommendation,))

                return cursor.fetchall()

    def get_top_opportunities(self, limit: int = 10):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        market_id,
                        origin,
                        destination,
                        planning_year,
                        forecast_demand,
                        existing_capacity,
                        capacity_gap,
                        expected_passengers,
                        expected_load_factor,
                        average_fare,
                        revenue_opportunity,
                        estimated_operating_cost,
                        profit_opportunity,
                        profit_margin,
                        competition_score,
                        demand_score,
                        capacity_gap_score,
                        fare_score,
                        profitability_score,
                        strategic_score,
                        risk_score,
                        opportunity_score,
                        recommendation,
                        data_type
                    FROM public.route_opportunity
                    ORDER BY opportunity_score DESC
                    LIMIT %s
                """, (limit,))

                return cursor.fetchall()


route_opportunity_repository = RouteOpportunityRepository()