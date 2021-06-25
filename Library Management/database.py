import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, quantity INTEGER, author TEXT, pages INTEGER)')
conn.commit()

def addNewBooks(title, quantity, author, pages):
    c.execute('INSERT INTO books VALUES (?, ?, ?, ?)', (title, quantity, author, pages))
    conn.commit()

def addExistingBooks(title, quantity):
    c.execute('UPDATE books SET quantity = (quantity + ?) WHERE title = (?)', (quantity, title))
    conn.commit()

def removeBooks(title, quantity):
    c.execute('UPDATE books SET quantity = (quantity - ?) WHERE title = (?)', (quantity, title))
