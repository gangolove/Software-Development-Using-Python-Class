#name:Douglas Marshall
#ass:16.8
#Des: Takes books and prints title



import sqlalchemy as sa

# connect to books database
engine = sa.create_engine("sqlite:///books.db")
metadata = sa.MetaData()

# reflect the existing books table
books = sa.Table("books", metadata, autoload_with=engine)

#Add books
with engine.begin() as conn:
    conn.execute(books.insert(), [
        {"title": "The Golden Compass", "author": "Philip Pullman", "year": 1995},
        {"title": "The Subtle Knife", "author": "Philip Pullman", "year": 1997},
        {"title": "The Amber Spyglass", "author": "Philip Pullman", "year": 2000},
        {"title": "Harry Potter and the Prisoner of Azkaban", "author": "J.K. Rowling", "year": 1999},
        {"title": "The Fellowship of the Ring", "author": "J.R.R. Tolkien", "year": 1954},
    ])

#print titles alphabetically
with engine.connect() as conn:
    rows = conn.execute(sa.select(books.c.title).order_by(books.c.title))
    for row in rows:
        print(row[0])