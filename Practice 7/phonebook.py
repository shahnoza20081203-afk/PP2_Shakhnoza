# phonebook.py
import csv
import psycopg2
from connect import get_connection

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        phone VARCHAR(50) NOT NULL
    )
    """
    conn = get_connection()
    if conn:
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
            print("Таблица 'contacts' успешно готова к работе.")
        except Exception as e:
            print("Ошибка при создании таблицы:", e)
        finally:
            conn.close()

def insert_from_csv(filename="contacts.csv"):
    conn = get_connection()
    if not conn:
        return
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            with conn:
                with conn.cursor() as cursor:
                    for row in reader:
                        cursor.execute(
                            "SELECT id FROM contacts WHERE phone = %s", (row['phone'],)
                        )
                        if not cursor.fetchone():
                            cursor.execute(
                                "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
                                (row['first_name'], row['phone'])
                            )
        print(f"Данные из файла {filename} успешно импортированы.")
    except Exception as e:
        print("Ошибка при чтении CSV:", e)
    finally:
        conn.close()

def add_contact_console():
    name = input("Введите имя контакта: ").strip()
    phone = input("Введите номер телефона: ").strip()
    
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
            print("Ошибка при добавлении контакта:", e)
        finally:
            conn.close()

def query_contacts():
    print("\n--- Фильтры поиска ---")
    print("1. Показать все контакты")
    print("2. Поиск по имени")
    print("3. Поиск по префиксу телефона")
    choice = input("Выберите вариант (1-3): ").strip()
    
    conn = get_connection()
    if not conn:
        return
    
    try:
        with conn.cursor() as cursor:
            if choice == '1':
                cursor.execute("SELECT id, first_name, phone FROM contacts")
            elif choice == '2':
                name = input("Введите имя или его часть: ").strip()
                cursor.execute(
                    "SELECT id, first_name, phone FROM contacts WHERE first_name ILIKE %s",
                    (f"%{name}%",)
                )
            elif choice == '3':
                prefix = input("Введите префикс телефона: ").strip()
                cursor.execute(
                    "SELECT id, first_name, phone FROM contacts WHERE phone LIKE %s",
                    (f"{prefix}%",)
                )
            else:
                print("Неверный выбор.")
                return
            
            rows = cursor.fetchall()
            if rows:
                print("\n--- Список контактов ---")
                for row in rows:
                    print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
                print("------------------------")
            else:
                print("Контакты не найдены.")
    except Exception as e:
        print("Ошибка при поиске:", e)
    finally:
        conn.close()

def update_contact():
    phone_to_update = input("Введите номер телефона контакта, который хотите изменить: ").strip()
    
    conn = get_connection()
    if not conn:
        return
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, first_name, phone FROM contacts WHERE phone = %s", (phone_to_update,))
            contact = cursor.fetchone()
            if not contact:
                print("Контакт с таким номером не найден.")
                return
            
            print(f"Найден контакт: Имя: {contact[1]}, Телефон: {contact[2]}")
            print("Что вы хотите изменить?")
            print("1. Имя")
            print("2. Телефон")
            choice = input("Выберите (1-2): ").strip()
            
            with conn:
                if choice == '1':
                    new_name = input("Введите новое имя: ").strip()
                    cursor.execute("UPDATE contacts SET first_name = %s WHERE phone = %s", (new_name, phone_to_update))
                    print("Имя успешно обновлено!")
                elif choice == '2':
                    new_phone = input("Введите новый телефон: ").strip()
                    cursor.execute("UPDATE contacts SET phone = %s WHERE phone = %s", (new_phone, phone_to_update))
                    print("Телефон успешно обновлен!")
                else:
                    print("Неверный выбор.")
    except Exception as e:
        print("Ошибка при обновлении:", e)
    finally:
        conn.close()

def delete_contact():
    print("\n--- Удаление контакта ---")
    print("1. Удалить по телефону")
    print("2. Удалить по имени")
    choice = input("Выберите вариант (1-2): ").strip()
    
    conn = get_connection()
    if not conn:
        return
    
    try:
        with conn:
            with conn.cursor() as cursor:
                if choice == '1':
                    phone = input("Введите номер телефона для удаления: ").strip()
                    cursor.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
                    print("Контакт удален.")
                elif choice == '2':
                    name = input("Введите имя для удаления: ").strip()
                    cursor.execute("DELETE FROM contacts WHERE first_name ILIKE %s", (name,))
                    print("Контакт(ы) удален(ы).")
                else:
                    print("Неверный выбор.")
    except Exception as e:
        print("Ошибка при удалении:", e)
    finally:
        conn.close()

def main():
    create_table()
    insert_from_csv()
    
    while True:
        print("\n=== Телефонная книга (PhoneBook) ===")
        print("1. Посмотреть / Найти контакты")
        print("2. Добавить контакт (через консоль)")
        print("3. Обновить контакт")
        print("4. Удалить контакт")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == '1':
            query_contacts()
        elif choice == '2':
            add_contact_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()