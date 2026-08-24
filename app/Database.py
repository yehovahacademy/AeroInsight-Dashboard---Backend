import os
import psycopg2
import psycopg2.extras
from contextlib import contextmanager

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://aeroinsight_db_user:oL8bfOwLae3BESztUZXZb3kjGsW99rCA@dpg-da1gv87lk1mc73a1n64g-a/aeroinsight_db"
)

@contextmanager
def get_connection():
    conn = psycopg2.connect(DATABASE_URL)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()