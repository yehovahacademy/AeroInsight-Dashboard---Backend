import os
import psycopg2
from psycopg2.extensions import connection

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:Josh%402005@localhost:5432/AeroInsight"
)


def get_connection() -> connection:
    return psycopg2.connect(DATABASE_URL)