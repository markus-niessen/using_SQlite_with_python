from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///data/textbook.sqlite3')

with engine.connect() as connection:

    # 1. Alle Bücher nach dem Jahr 2000
    print("Books after 2000:\n")

    results = connection.execute(text("""
        SELECT *
        FROM books
        WHERE publication_year > 2000
    """))

    rows = results.fetchall()

    for row in rows:
        print(row)

    # 2. Anzahl der Ergebnisse anzeigen
    print(f"\nReturned {len(rows)} results\n")


    # 3. Titel + Autorenname alphabetisch sortiert
    print("Books with authors:\n")

    results = connection.execute(text("""
        SELECT books.title, authors.name
        FROM books
        JOIN authors
            ON books.author_id = authors.id
        ORDER BY books.title ASC
    """))

    rows = results.fetchall()

    for row in rows:
        print(f"{row.title} ({row.name})")
