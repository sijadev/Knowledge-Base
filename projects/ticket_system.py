# !/usr/bin/env python3

import psycopg2
import csv
import sys

DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "admin"
DB_NAME = "knowledge_base"
DB_PASSWORD = "admin123"


def test_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=5432
        )
        print("✅ Verbindung erfolgreich!")
        conn.close()
    except Exception as e:
        print(f"❌ Fehler: {e}")


def export_all_tickets():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME,
            user=DB_USER, password=DB_PASSWORD, port=5432
        )
        cursor = conn.cursor()

        query = """
                SELECT ticket_number, \
                       kurzbeschreibung, \
                       c.name as kategorie,
                       priority, \
                       status, \
                       eingangsdatum, \
                       bearbeiter
                FROM solutions s
                         JOIN categories c ON s.category_id = c.id
                ORDER BY eingangsdatum DESC LIMIT 500 \
                """

        cursor.execute(query)

        with open('/tmp/tickets_all.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow([desc[0] for desc in cursor.description])
            writer.writerows(cursor.fetchall())

        print("✅ Exported to /tmp/tickets_all.csv")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Fehler: {e}")


def export_open_tickets():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME,
            user=DB_USER, password=DB_PASSWORD, port=5432
        )
        cursor = conn.cursor()

        query = """
                SELECT ticket_number, \
                       kurzbeschreibung, \
                       c.name as kategorie,
                       priority, \
                       status, \
                       eingangsdatum, \
                       bearbeiter
                FROM solutions s
                         JOIN categories c ON s.category_id = c.id
                WHERE s.status IN ('Offen', 'In Bearbeitung')
                ORDER BY priority DESC \
                """

        cursor.execute(query)

        with open('tickets_open.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow([desc[0] for desc in cursor.description])
            writer.writerows(cursor.fetchall())

        print("✅ Exported to tickets_open.csv")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Fehler: {e}")


def create_ticket(kurzbeschreibung, detaillierung, category_id, department_id, prioritaet, bearbeiter):
    try:
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME,
            user=DB_USER, password=DB_PASSWORD, port=5432
        )
        cursor = conn.cursor()

        cursor.execute("""
                       INSERT INTO solutions
                       (ticket_number, category_id, department_id, ticket_type_id, priority, status,
                        kurzbeschreibung, detaillierte_beschreibung, eingangsdatum, bearbeiter, loesung_qualitaet)
                       VALUES ('TK-TEST-001', %s, %s, 1, %s, 'Offen', %s, %s, CURRENT_TIMESTAMP, %s, 0)
                       """, (category_id, department_id, prioritaet, kurzbeschreibung, detaillierung, bearbeiter))

        conn.commit()
        print("✅ Ticket erstellt!")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Fehler: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]

        if cmd == "test":
            test_connection()
        elif cmd == "export-all":
            export_all_tickets()
        elif cmd == "export-open":
            export_open_tickets()
        elif cmd == "create-ticket":
            create_ticket(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
    else:
        print("Verfügbare Befehle: test, export-all, export-open, create-ticket")