#name:Douglas Marshall
#ass:16.4
#Des: creates book table


#imports library
import sqlite3

#connect to (or create) the database
conn = sqlite3.connect("books.db")
cur = conn.cursor()

#create the table
cur.execute('''CREATE TABLE books (title TEXT, author TEXT, year INTEGER)''')

#insert books
cur.execute('INSERT INTO books VALUES("The Golden Compass", "Philip Pullman", 1995)')

cur.execute('INSERT INTO books VALUES("The Subtle Knife", "Philip Pullman", 1997)')

cur.execute('INSERT INTO books VALUES("The Amber Spyglass", "Philip Pullman", 2000)')

cur.execute('INSERT INTO books VALUES("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 1999)')

cur.execute('INSERT INTO books VALUES("The Fellowship of the Ring", "J.R.R. Tolkien", 1954)')
#save
conn.commit()
#close the database
conn.close()