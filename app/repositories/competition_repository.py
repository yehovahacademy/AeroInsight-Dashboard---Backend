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
                        year,
                        airline_name,
                        is_direct_competitor,
                        frequency_per_week,
                        aircraft_type,
                        market_share,
                        competitive_strength,
                        data_type
                    FROM public.competition_new
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
                        year,
                        airline_name,
                        is_direct_competitor,
                        frequency_per_week,
                        aircraft_type,
                        market_share,
                        competitive_strength,
                        data_type
                    FROM public.competition_new
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
                        year,
                        airline_name,
                        is_direct_competitor,
                        frequency_per_week,
                        aircraft_type,
                        market_share,
                        competitive_strength,
                        data_type
                    FROM public.competition_new
                    WHERE market_id = %s
                    ORDER BY year DESC, market_share DESC
                """, (market_id,))

                return cursor.fetchall()

    def get_by_market_and_year(
    self,
    market_id: str,
    year: int
):
     with get_connection() as connection:
        with connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
        ) as cursor:

            cursor.execute("""
                SELECT
                    competition_id,
                    market_id,
                    year,
                    airline_name,
                    is_direct_competitor,
                    frequency_per_week,
                    aircraft_type,
                    market_share,
                    competitive_strength,
                    data_type
                FROM public.competition_new
                WHERE market_id = %s
                AND year = %s
                ORDER BY market_share DESC
            """, (market_id, year))

            return cursor.fetchall()        

    def get_by_airline(self, airline_name: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute("""
                    SELECT
                        competition_id,
                        market_id,
                        year,
                        airline_name,
                        is_direct_competitor,
                        frequency_per_week,
                        aircraft_type,
                        market_share,
                        competitive_strength,
                        data_type
                    FROM public.competition_new
                    WHERE UPPER(airline_name) = UPPER(%s)
                    ORDER BY market_id, year DESC
                """, (airline_name,))

                return cursor.fetchall()


competition_repository = CompetitionRepository()