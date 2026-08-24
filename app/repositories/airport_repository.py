from app.Database import get_connection
import psycopg2
import psycopg2.extras


class AirportRepository:

    def get_all(self):
        with get_connection() as connection:
           with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT
                    airport_id,
                    iata_code,
                    icao_code,
                    airport_name,
                    city,
                    state,
                    latitude,
                    longitude,
                    elevation,
                    airport_type,
                    timezone
                FROM public.airports
                ORDER BY airport_name
                """
            )

            return cursor.fetchall()


    def get_by_iata(self, iata: str):
        with get_connection() as connection:
            with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT
                        airport_id,
                        iata_code,
                        icao_code,
                        airport_name,
                        city,
                        state,
                        latitude,
                        longitude,
                        elevation,
                        airport_type,
                        timezone
                    FROM public.airports
                    WHERE UPPER(iata_code) = UPPER(%s)
                    """,
                    (iata,),
                )

                return cursor.fetchone()

    def get_by_icao(self, icao: str):
        with get_connection() as connection:
            with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT
                        airport_id,
                        iata_code,
                        icao_code,
                        airport_name,
                        city,
                        state,
                        latitude,
                        longitude,
                        elevation,
                        airport_type,
                        timezone
                    FROM public.airports
                    WHERE UPPER(icao_code) = UPPER(%s)
                    """,
                    (icao,),
                )

                return cursor.fetchone()

    def search(self, query: str):
        with get_connection() as connection:
            with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:

                search_pattern = f"%{query}%"

                cursor.execute(
                    """
                    SELECT
                        airport_id,
                        iata_code,
                        icao_code,
                        airport_name,
                        city,
                        state,
                        latitude,
                        longitude,
                        elevation,
                        airport_type,
                        timezone
                    FROM public.airports
                    WHERE
                        UPPER(iata_code) = UPPER(%s)
                        OR UPPER(icao_code) = UPPER(%s)
                        OR airport_name ILIKE %s
                        OR city ILIKE %s
                        OR state ILIKE %s
                    ORDER BY airport_name
                    LIMIT 20
                    """,
                    (
                        query,
                        query,
                        search_pattern,
                        search_pattern,
                        search_pattern,
                    ),
                )

                return cursor.fetchall()


airport_repository = AirportRepository()