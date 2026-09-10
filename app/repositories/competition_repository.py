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
                        airline,
                        nonstop,
                        weekly_frequency,
                        aircraft_type,
                        estimated_market_share,
                        competition_strength,
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
                        airline,
                        nonstop,
                        weekly_frequency,
                        aircraft_type,
                        estimated_market_share,
                        competition_strength,
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
                        airline,
                        nonstop,
                        weekly_frequency,
                        aircraft_type,
                        estimated_market_share,
                        competition_strength,
                        data_type
                    FROM public.competition
                    WHERE market_id = %s
                    ORDER BY estimated_market_share DESC
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
                        airline,
                        nonstop,
                        weekly_frequency,
                        aircraft_type,
                        estimated_market_share,
                        competition_strength,
                        data_type
                    FROM public.competition
                    WHERE UPPER(airline) = UPPER(%s)
                    ORDER BY market_id
                """, (airline,))

                return cursor.fetchall()


competition_repository = CompetitionRepository()