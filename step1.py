from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///data/textbook.sqlite3')

with engine.connect() as connection:
    # Run an SQL query
    results = connection.execute(text('SELECT * FROM simple_books'))
    rows = results.fetchall()

    # Print results
    for row in rows:
        print(row)
