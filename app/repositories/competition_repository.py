from app.database import get_connection
import psycopg2.extras


class CompetitionRepository:

    def get_all(self):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        competition_id,
                        market_id,
                        airline_name AS airline,
                        is_direct_competitor AS nonstop,
                        frequency_per_week AS weekly_frequency,
                        aircraft_type,
                        market_share AS estimated_market_share,
                        competitive_strength AS competition_strength,
                        data_type
                    FROM public.competition
                    ORDER BY competition_id
                """)

                return cursor.fetchall()

    def get_by_id(self, competition_id: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        competition_id,
                        market_id,
                        airline_name AS airline,
                        is_direct_competitor AS nonstop,
                        frequency_per_week AS weekly_frequency,
                        aircraft_type,
                        market_share AS estimated_market_share,
                        competitive_strength AS competition_strength,
                        data_type
                    FROM public.competition
                    WHERE competition_id = %s
                """, (competition_id,))

                return cursor.fetchone()

    def get_by_market(self, market_id: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        competition_id,
                        market_id,
                        airline_name AS airline,
                        is_direct_competitor AS nonstop,
                        frequency_per_week AS weekly_frequency,
                        aircraft_type,
                        market_share AS estimated_market_share,
                        competitive_strength AS competition_strength,
                        data_type
                    FROM public.competition
                    WHERE market_id = %s
                    ORDER BY market_share DESC
                """, (market_id,))

                return cursor.fetchall()

    def get_by_airline(self, airline: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        competition_id,
                        market_id,
                        airline_name AS airline,
                        is_direct_competitor AS nonstop,
                        frequency_per_week AS weekly_frequency,
                        aircraft_type,
                        market_share AS estimated_market_share,
                        competitive_strength AS competition_strength,
                        data_type
                    FROM public.competition
                    WHERE UPPER(airline_name) = UPPER(%s)
                    ORDER BY market_id
                """, (airline,))

                return cursor.fetchall()


competition_repository = CompetitionRepository()