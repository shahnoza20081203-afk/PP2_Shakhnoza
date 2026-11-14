import csv
import json
import psycopg2
from psycopg2.extras import Json

from connect import connect

from pathlib import Path

PAGE_SIZE = 5


def print_contacts(rows):
    if not rows:
        print("No contacts found.")
        return

    for row in rows:
        print(row)


def search_contacts(cur):
    query = input("Search by name, email, or phone: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (query,))
    print_contacts(cur.fetchall())


def add_or_update_contact(cur, conn):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print("Contact saved successfully!")


def bulk_insert_contacts(cur, conn):
    users = []
    count = int(input("How many users? "))

    for i in range(count):
        print(f"\nUser {i + 1}")
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        users.append({"name": name, "phone": phone})

    cur.execute(
        "CALL bulk_insert_contacts(%s, %s)",
        (Json(users), None)
    )
    result = cur.fetchone()
    conn.commit()
    print("Incorrect records:", result[0] if result else [])


def show_contacts_pages(cur):
    page = 0

    while True:
        cur.execute(
            "SELECT * FROM get_contacts_page(%s, %s)",
            (PAGE_SIZE, page * PAGE_SIZE)
        )
        rows = cur.fetchall()

        print(f"\n--- Page {page + 1} ---")
        print_contacts(rows)

        command = input("Type next, prev, or quit: ").strip().lower()

        if command == "next":
            if rows:
                page += 1
            else:
                print("There are no more contacts.")
        elif command == "prev":
            if page > 0:
                page -= 1
            else:
                print("You are already on the first page.")
        elif command == "quit":
            break
        else:
            print("Unknown command.")


def filter_by_group(cur):
    group_name = input("Enter group (Family, Work, Friend, Other): ").strip()

    cur.execute(
        """
        SELECT c.id, c.first_name, c.email, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        LEFT JOIN phones p ON p.contact_id = c.id
        WHERE g.name ILIKE %s
        ORDER BY c.first_name
        """,
        (group_name,)
    )
    print_contacts(cur.fetchall())


def sort_contacts(cur):
    print("Sort by: 1. Name  2. Birthday  3. Date added")
    choice = input("Choose sort order: ").strip()

    sort_columns = {
        "1": "c.first_name",
        "2": "c.birthday",
        "3": "c.date_added",
    }

    column = sort_columns.get(choice)
    if column is None:
        print("Invalid choice.")
        return

    cur.execute(
        f"""
        SELECT c.id, c.first_name, c.email, c.birthday,
               c.date_added, g.name
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        ORDER BY {column} NULLS LAST
        """
    )
    print_contacts(cur.fetchall())


def delete_contact(cur, conn):
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        cur.execute("CALL delete_contact(%s, %s)", (name, None))
    elif choice == "2":
        phone = input("Enter phone: ").strip()
        cur.execute("CALL delete_contact(%s, %s)", (None, phone))
    else:
        print("Invalid choice.")
        return

    conn.commit()
    print("Delete operation completed!")


def export_contacts(cur):
    cur.execute(
        """
        SELECT
            c.id,
            c.first_name,
            c.email,
            c.birthday,
            c.date_added,
            g.name,
            COALESCE(
                json_agg(
                    json_build_object('phone', p.phone, 'type', p.type)
                ) FILTER (WHERE p.id IS NOT NULL),
                '[]'::json
            )
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        LEFT JOIN phones p ON p.contact_id = c.id
        GROUP BY c.id, g.name
        ORDER BY c.id
        """
    )

    contacts = []
    for row in cur.fetchall():
        contacts.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "birthday": row[3].isoformat() if row[3] else None,
            "date_added": row[4].isoformat() if row[4] else None,
            "group": row[5],
            "phones": row[6],
        })

    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=2)

    print("Contacts exported to contacts.json")


def import_contacts(cur, conn):
    filename = input("JSON file [contacts.json]: ").strip() or "contacts.json"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            contacts = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        print("Could not read JSON file:", error)
        return

    for contact in contacts:
        name = (contact.get("name") or "").strip()
        if not name:
            print("Skipping a contact without a name.")
            continue

        cur.execute(
            "SELECT id FROM contacts WHERE LOWER(first_name) = LOWER(%s) LIMIT 1",
            (name,)
        )
        existing = cur.fetchone()

        if existing:
            action = input(
                f"{name} already exists. Skip or overwrite? (s/o): "
            ).strip().lower()

            if action == "s":
                continue
            elif action != "o":
                print("Invalid choice; skipping contact.")
                continue

            contact_id = existing[0]
            cur.execute(
                """
                UPDATE contacts
                SET email = %s, birthday = %s, group_id = (
                    SELECT id FROM groups WHERE name = %s
                )
                WHERE id = %s
                """,
                (
                    contact.get("email"),
                    contact.get("birthday"),
                    contact.get("group") or "Other",
                    contact_id
                )
            )
            cur.execute("DELETE FROM phones WHERE contact_id = %s", (contact_id,))
        else:
            group_name = contact.get("group") or "Other"
            cur.execute(
                "INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO NOTHING",
                (group_name,)
            )
            cur.execute(
                """
                INSERT INTO contacts (first_name, email, birthday, group_id)
                VALUES (
                    %s, %s, %s,
                    (SELECT id FROM groups WHERE name = %s)
                )
                RETURNING id
                """,
                (
                    name,
                    contact.get("email"),
                    contact.get("birthday"),
                    group_name
                )
            )
            contact_id = cur.fetchone()[0]

        group_name = contact.get("group") or "Other"
        cur.execute(
            "INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO NOTHING",
            (group_name,)
        )
        cur.execute(
            "UPDATE contacts SET group_id = (SELECT id FROM groups WHERE name = %s) WHERE id = %s",
            (group_name, contact_id)
        )

        for phone in contact.get("phones", []):
            number = phone.get("phone")
            phone_type = phone.get("type", "mobile")
            if number:
                cur.execute(
                    """
                    INSERT INTO phones (contact_id, phone, type)
                    VALUES (%s, %s, %s)
                    """,
                    (contact_id, number, phone_type)
                )

    conn.commit()
    print("JSON import completed.")

def import_contacts_csv(cur, conn):
    filename = input("CSV file [contacts.csv]: ").strip() or "contacts.csv"

    try:
        file_path = Path(__file__).resolve().parent / filename

        with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
            rows = list(csv.DictReader(file))
    except OSError as error:
        print("Could not read CSV file:", error)
        return

    allowed_groups = {"Family", "Work", "Friend", "Other"}
    allowed_phone_types = {"home", "work", "mobile"}
    imported_phones = set()

    for row in rows:
        name = (row.get("name") or "").strip()
        phone = (row.get("phone") or "").strip()
        email = (row.get("email") or "").strip() or None
        birthday = (row.get("birthday") or "").strip() or None
        group_name = (row.get("group") or "Other").strip()
        phone_type = (row.get("phone_type") or "mobile").strip().lower()

        if not name or not phone:
            print(f"Skipping row with missing name or phone: {row}")
            continue

        if group_name not in allowed_groups:
            print(f"Skipping {name}: unknown group '{group_name}'.")
            continue

        if phone_type not in allowed_phone_types:
            print(f"Skipping {name}: invalid phone type '{phone_type}'.")
            continue

        cur.execute(
            "SELECT id FROM groups WHERE name = %s",
            (group_name,)
        )
        group = cur.fetchone()

        if group:
            group_id = group[0]
        else:
            cur.execute(
                "INSERT INTO groups (name) VALUES (%s) RETURNING id",
                (group_name,)
            )
            group_id = cur.fetchone()[0]

        cur.execute(
            """
            SELECT id FROM contacts
            WHERE LOWER(first_name) = LOWER(%s)
            LIMIT 1
            """,
            (name,)
        )
        existing = cur.fetchone()

        if existing:
            contact_id = existing[0]
            cur.execute(
                """
                UPDATE contacts
                SET email = %s, birthday = %s, group_id = %s
                WHERE id = %s
                """,
                (email, birthday, group_id, contact_id)
            )
        else:
            cur.execute(
                """
                INSERT INTO contacts (first_name, phone, email, birthday, group_id)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (name, phone, email, birthday, group_id)
            )
            contact_id = cur.fetchone()[0]

        phone_key = (contact_id, phone)
        if phone_key not in imported_phones:
            cur.execute(
                """
                SELECT 1 FROM phones
                WHERE contact_id = %s AND phone = %s
                LIMIT 1
                """,
                (contact_id, phone)
            )
            if cur.fetchone() is None:
                cur.execute(
                    """
                    INSERT INTO phones (contact_id, phone, type)
                    VALUES (%s, %s, %s)
                    """,
                    (contact_id, phone, phone_type)
                )
            imported_phones.add(phone_key)

    conn.commit()
    print("CSV import completed.")


def main():
    conn = connect()
    if conn is None:
        print("Could not connect to the database.")
        return

    cur = conn.cursor()

    try:
        while True:
            print("\n===== PHONEBOOK =====")
            print("1. Search contacts")
            print("2. Add or update contact")
            print("3. Bulk insert contacts")
            print("4. Show contacts by pages")
            print("5. Delete contact")
            print("6. Filter by group")
            print("7. Sort contacts")
            print("8. Export contacts to JSON")
            print("9. Import contacts from JSON")
            print("10. Import contacts from CSV")
            print("0. Exit")

            choice = input("Choose option: ").strip()

            try:
                if choice == "1":
                    search_contacts(cur)
                elif choice == "2":
                    add_or_update_contact(cur, conn)
                elif choice == "3":
                    bulk_insert_contacts(cur, conn)
                elif choice == "4":
                    show_contacts_pages(cur)
                elif choice == "5":
                    delete_contact(cur, conn)
                elif choice == "6":
                    filter_by_group(cur)
                elif choice == "7":
                    sort_contacts(cur)
                elif choice == "8":
                    export_contacts(cur)
                elif choice == "9":
                    import_contacts(cur, conn)
                elif choice == "10":
                    import_contacts_csv(cur, conn)
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