import psycopg2
from connect import get_connection

def create_table():
    conn = get_connection()
    if conn:
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS contacts (
                            id SERIAL PRIMARY KEY,
                            first_name VARCHAR(100) NOT NULL,
                            phone VARCHAR(50) NOT NULL
                        )
                    """)
            print("Таблица 'contacts' успешно создана или уже существовала.")
        except Exception as e:
            print("Ошибка при создании таблицы:", e)
        finally:
            conn.close()

def add_contact(name, phone):
    conn = get_connection()
    if conn:
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
                        (name, phone)
                    )
            print(f"Контакт {name} ({phone}) успешно добавлен!")
        except Exception as e:
            print("Ошибка при добавлении:", e)
        finally:
            conn.close()

def get_all_contacts():
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, first_name, phone FROM contacts")
                rows = cursor.fetchall()
                
                print("\n--- Список всех контактов ---")
                if not rows:
                    print("Список пуст.")
                for row in rows:
                    print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
                print("-----------------------------\n")
        except Exception as e:
            print("Ошибка при чтении данных:", e)
        finally:
            conn.close()

def search_contact(name_to_find):
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                # Используем ILIKE для поиска без учета регистра
                cursor.execute(
                    "SELECT id, first_name, phone FROM contacts WHERE first_name ILIKE %s",
                    (f"%{name_to_find}%",)
                )
                rows = cursor.fetchall()
                
                print(f"\n--- Результаты поиска по запросу '{name_to_find}' ---")
                if not rows:
                    print("Ничего не найдено.")
                for row in rows:
                    print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
                print("----------------------------------------------\n")
        except Exception as e:
            print("Ошибка при поиске:", e)
        finally:
            conn.close()

def delete_y(first_name):
    conn=get_connection()
    if conn:
        try:
           with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM contacts WHERE first_name=%s",
                        (f"%{first_name}%",)
                    )
                    print("delete")
        except Exception as e:
            print("Ошибка при поиске:", e)
        finally:
            conn.close()

if __name__ == "__main__":
    # create_table()
    # get_all_contacts()
    delete_y("Ivan")
    get_all_contacts()