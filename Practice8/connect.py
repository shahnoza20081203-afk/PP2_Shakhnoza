import psycopg2
from config import DB_CONFIG

def get_connection():
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        return connection
    except Exception as error:
        print(f"Ошибка при подключении к базе данных: {error}")
        return None