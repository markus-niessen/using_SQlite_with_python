from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///data/textbook.sqlite3")

with engine.connect() as connection:

    # Nutzereingaben
    title_search = input("Enter book title: ")
    start_year = input("Enter start year: ")
    end_year = input("Enter end year: ")

    # Sichere SQL-Abfrage
    query = text("""
        SELECT *
        FROM books
        WHERE publication_year BETWEEN :start_year AND :end_year
        AND title LIKE :title_search
    """)

    # Parameter sicher übergeben
    results = connection.execute(query, {
        "start_year": start_year,
        "end_year": end_year,
        "title_search": f"%{title_search}%"
    })

    rows = results.fetchall()

    # Ergebnisse anzeigen
    for row in rows:
        print(row)

    print(f"\nReturned {len(rows)} results")