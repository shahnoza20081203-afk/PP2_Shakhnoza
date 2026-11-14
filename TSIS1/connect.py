import psycopg2
from config import DB_CONFIG

def connect():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Connected to PostgreSQL successfully!")
        return conn

    except psycopg2.Error as error:
        print("Database connection error:", error)
        raise
