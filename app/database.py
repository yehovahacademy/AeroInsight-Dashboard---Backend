import os
import psycopg2
from contextlib import contextmanager
from dotenv import load_dotenv

print("Before load_dotenv:", os.getenv("DATABASE_URL"))

load_dotenv()

print("Afetr load_dotenv:", os.getenv("DATABASE_URL"))

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    print(
        "DATABASE HOST:",
        DATABASE_URL.split("@")[-1].split("/")[0]
    )
else:
    print("DATABASE_URL is NOT SET")


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