import sqlite3
from tabulate import tabulate


def print_apps_table():

    db_path = "WebApp/db.sqlite3"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, app_name, create_date, description FROM app_app")
    rows = cursor.fetchall()

    if not rows:
        print("No records found in the App table.")
        return

    headers = ["ID", "App Name", "Create Date", "Description"]
    print('-'*30, 'List of all apps', '-'*30)
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    conn.close()
