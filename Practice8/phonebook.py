import psycopg2
from config import DB_CONFIG

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True 
    cursor = conn.cursor()

    print("--- 1. Тест поиска по паттерну ---")
    cursor.execute("SELECT * FROM get_contacts_by_pattern(%s)", ('Ali',))
    for row in cursor.fetchall():
        print(row)

    print("\n--- 2. Тест Upsert процедуры ---")
    cursor.execute("CALL upsert_contact(%s, %s)", ('Aidos', '+77011234567'))
    print("Контакт успешно добавлен/обновлен через процедуру.")

    print("\n--- 3. Тест массовой вставки (Bulk Insert) ---")
    names = ['Baurzhan', 'Dinara', 'InvalidUser']
    phones = ['+77029998877', '87015554433', '123'] 
    cursor.execute("CALL bulk_insert_contacts(%s, %s)", (names, phones))

    print("\n--- 4. Тест пагинации ---")
    cursor.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (2, 0))
    for row in cursor.fetchall():
        print(row)

    print("\n--- 5. Тест удаления контакта ---")
    cursor.execute("CALL delete_contact(%s)", ('InvalidUser',))
    print("Процедура удаления выполнена.")

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()