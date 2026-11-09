
from connect import connect
from psycopg2.extras import Json
import psycopg2


def main():
    conn = connect()
    cur = conn.cursor()

    try:
        while True:
            print("\n===== PHONEBOOK =====")
            print("1. Search contacts")
            print("2. Add or update contact")
            print("3. Bulk insert contacts")
            print("4. Show contacts (Pagination)")
            print("5. Delete contact")
            print("0. Exit")

            choice = input("Choose option: ")

            try:
                if choice == "1":
                    pattern = input("Enter name, surname or phone: ")

                    cur.execute(
                        "SELECT * FROM search_contacts(%s)",
                        (pattern,)
                    )

                    results = cur.fetchall()

                    for row in results:
                        print(row)

                    if not results:
                        print("No contacts found.")

                elif choice == "2":
                    name = input("Enter name: ")
                    phone = input("Enter phone: ")

                    cur.execute(
                        "CALL upsert_contact(%s, %s)",
                        (name, phone)
                    )

                    conn.commit()
                    print("Contact saved successfully!")

                elif choice == "3":
                    users = []

                    count = int(input("How many users? "))

                    for i in range(count):
                        print(f"\nUser {i + 1}")

                        name = input("Enter name: ")
                        phone = input("Enter phone: ")

                        users.append({
                            "name": name,
                            "phone": phone
                        })

                    cur.execute(
                        "CALL bulk_insert_contacts(%s, %s)",
                        (Json(users), None)
                    )

                    invalid = cur.fetchone()[0]

                    conn.commit()

                    print("Incorrect records:", invalid)

                elif choice == "4":
                    limit = int(input("Contacts per page: "))
                    offset = int(input("Offset: "))

                    cur.execute(
                        "SELECT * FROM get_contacts_page(%s, %s)",
                        (limit, offset)
                    )

                    results = cur.fetchall()

                    for row in results:
                        print(row)

                    if not results:
                        print("No contacts on this page.")

                elif choice == "5":
                    print("1. Delete by name")
                    print("2. Delete by phone")

                    delete_choice = input("Choose: ")

                    if delete_choice == "1":
                        name = input("Enter name: ")

                        cur.execute(
                            "CALL delete_contact(%s, %s)",
                            (name, None)
                        )

                    elif delete_choice == "2":
                        phone = input("Enter phone: ")

                        cur.execute(
                            "CALL delete_contact(%s, %s)",
                            (None, phone)
                        )

                    else:
                        print("Invalid choice!")
                        continue

                    conn.commit()
                    print("Delete operation completed!")

                elif choice == "0":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice!")

            except (psycopg2.Error, ValueError) as error:
                conn.rollback()
                print("Error:", error)

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
