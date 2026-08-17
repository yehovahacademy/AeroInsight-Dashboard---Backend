from psycopg import conninfo
from psycopg_pool import ConnectionPool


DATABASE_URL = conninfo.make_conninfo(
    dbname="AeroInsight",
    user="postgres",
    password="Josh@2005",
    host="localhost",
    port=5432,
)


pool = ConnectionPool(
    conninfo=DATABASE_URL,
    min_size=2,
    max_size=10,
    open=False,
)


def open_pool():
    pool.open()


def close_pool():
    pool.close()


def get_connection():
    return pool.connection()