import os
import psycopg2
from psycopg2.extensions import connection

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://aeroinsight_db_user:oL8bfOwLae3BESztUZXZb3kjGsW99rCA@dpg-da1gv87lk1mc73a1n64g-a/aeroinsight_db"
)


def get_connection() -> connection:
    return psycopg2.connect(DATABASE_URL)