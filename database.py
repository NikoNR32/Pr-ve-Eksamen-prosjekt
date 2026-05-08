import sqlite3

def lag_database():
    kobling = sqlite3.connect("database.db")

    sql_filer = [
        "database_kode/Lag_bruker_tabell.sql",
        "database_kode/Lag_produkt_tabell.sql"
    ]

    for filnavn in sql_filer:
        with open(filnavn, "r", encoding="utf-8") as fil:
            sql_kode = fil.read()
            kobling.executescript(sql_kode)

    kobling.commit()
    kobling.close()

    print("Database og tabeller er laget.")

if __name__ == "__main__":
    lag_database()