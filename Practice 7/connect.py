import psycopg2
from config import load_config

def get_connection():
    try:
        connection = psycopg2.connect(**load_config)
        return connection
    except Exception as error:
        print("Ошибка при подключении к базе данных:", error)
        return None