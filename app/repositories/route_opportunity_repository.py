from app.database import get_connection
import psycopg2.extras


class RouteOpportunityRepository:

    def get_all(self):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        market_id,
                        annual_demand,
                        annual_existing_capacity,
                        average_load_factor,
                        average_fare,
                        competition_level,
                        capacity_gap,
                        estimated_revenue_potential,
                        estimated_profit_potential,
                        aircraft_suitability_score,
                        seasonality_score,
                        network_connectivity_score,
                        overall_opportunity_score,
                        recommendation,
                        data_type
                    FROM route_opportunity
                    ORDER BY overall_opportunity_score DESC
                """)

                return cursor.fetchall()

    def get_by_market(self, market_id: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        market_id,
                        annual_demand,
                        annual_existing_capacity,
                        average_load_factor,
                        average_fare,
                        competition_level,
                        capacity_gap,
                        estimated_revenue_potential,
                        estimated_profit_potential,
                        aircraft_suitability_score,
                        seasonality_score,
                        network_connectivity_score,
                        overall_opportunity_score,
                        recommendation,
                        data_type
                    FROM route_opportunity
                    WHERE market_id = %s
                """, (market_id,))

                return cursor.fetchone()

    def get_by_recommendation(self, recommendation: str):
        with get_connection() as conn:
            with conn.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        market_id,
                        annual_demand,
                        annual_existing_capacity,
                        average_load_factor,
                        average_fare,
                        competition_level,
                        capacity_gap,
                        estimated_revenue_potential,
                        estimated_profit_potential,
                        aircraft_suitability_score,
                        seasonality_score,
                        network_connectivity_score,
                        overall_opportunity_score,
                        recommendation,
                        data_type
                    FROM route_opportunity
                    WHERE recommendation = %s
                    ORDER BY overall_opportunity_score DESC
                """, (recommendation,))

                return cursor.fetchall()