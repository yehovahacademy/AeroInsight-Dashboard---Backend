import psycopg

DATABASE_URL = "postgresql://postgres:Josh@2005@localhost:5432/AeroInsight"


def get_connection():
    return psycopg.connect( dbname="AeroInsight",
        user="postgres",
        password="Josh@2005",
        host="localhost",
        port=5432,
        )