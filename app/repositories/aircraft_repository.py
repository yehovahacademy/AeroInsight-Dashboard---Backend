from app.database import get_connection
import psycopg2.extras


class AircraftRepository:

    def get_all(self):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        aircraft_type,
                        manufacturer,
                        seats,
                        typical_range_km,
                        estimated_trip_cost_factor,
                        suitability_short_haul,
                        suitability_medium_haul,
                        suitability_long_haul,
                        data_type
                    FROM public.aircraft_types
                    ORDER BY aircraft_type
                    """
                )

                return cursor.fetchall()

    def get_by_type(self, aircraft_type: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        aircraft_type,
                        manufacturer,
                        seats,
                        typical_range_km,
                        estimated_trip_cost_factor,
                        suitability_short_haul,
                        suitability_medium_haul,
                        suitability_long_haul,
                        data_type
                    FROM public.aircraft_types
                    WHERE UPPER(aircraft_type) = UPPER(%s)
                    """,
                    (aircraft_type,),
                )

                return cursor.fetchone()

    def get_by_manufacturer(self, manufacturer: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        aircraft_type,
                        manufacturer,
                        seats,
                        typical_range_km,
                        estimated_trip_cost_factor,
                        suitability_short_haul,
                        suitability_medium_haul,
                        suitability_long_haul,
                        data_type
                    FROM public.aircraft_types
                    WHERE UPPER(manufacturer) = UPPER(%s)
                    ORDER BY aircraft_type
                    """,
                    (manufacturer,),
                )

                return cursor.fetchall()

    def search(self, query: str):
        with get_connection() as connection:
            with connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                search_pattern = f"%{query}%"

                cursor.execute(
                    """
                    SELECT
                        aircraft_type,
                        manufacturer,
                        seats,
                        typical_range_km,
                        estimated_trip_cost_factor,
                        suitability_short_haul,
                        suitability_medium_haul,
                        suitability_long_haul,
                        data_type
                    FROM public.aircraft_types
                    WHERE
                        aircraft_type ILIKE %s
                        OR manufacturer ILIKE %s
                    ORDER BY aircraft_type
                    LIMIT 20
                    """,
                    (
                        search_pattern,
                        search_pattern,
                    ),
                )

                return cursor.fetchall()


aircraft_repository = AircraftRepository()