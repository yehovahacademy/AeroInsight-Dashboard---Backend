from app.Database import get_connection


class AirportLoader:

    def get_airport_by_iata(self, iata: str):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        airport_id,
                        iata_code,
                        icao_code,
                        airport_name,
                        city,
                        country,
                        latitude,
                        longitude
                    FROM public.airports
                    WHERE UPPER(iata_code) = UPPER(%s)
                    """,
                    (iata,),
                )

                row = cursor.fetchone()

                if row is None:
                    return None

                return self._format_airport(row)


    def get_airport_by_icao(self, icao: str):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        airport_id,
                        iata_code,
                        icao_code,
                        airport_name,
                        city,
                        country,
                        latitude,
                        longitude
                    FROM public.airports
                    WHERE UPPER(icao_code) = UPPER(%s)
                    """,
                    (icao,),
                )

                row = cursor.fetchone()

                if row is None:
                    return None

                return self._format_airport(row)


    def search_airports(self, query: str):
        with get_connection() as connection:
            with connection.cursor() as cursor:

                search_pattern = f"%{query}%"

                cursor.execute(
                    """
                    SELECT
                        airport_id,
                        iata_code,
                        icao_code,
                        airport_name,
                        city,
                        country,
                        latitude,
                        longitude
                    FROM public.airports
                    WHERE
                        UPPER(iata_code) = UPPER(%s)
                        OR UPPER(icao_code) = UPPER(%s)
                        OR airport_name ILIKE %s
                        OR city ILIKE %s
                        OR country ILIKE %s
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

                rows = cursor.fetchall()

                return [
                    self._format_airport(row)
                    for row in rows
                ]


    def _format_airport(self, row):
        return {
            "id": row[0],
            "iata": row[1],
            "icao": row[2],
            "name": row[3],
            "city": row[4],
            "country": row[5],
            "latitude": row[6],
            "longitude": row[7],
        }


airport_loader = AirportLoader()