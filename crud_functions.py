import sqlite3
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )
    ''')
    connection.commit()

def get_all_products():
    connection = sqlite3.connect("not_telegram.db")
    cursor.execute("SELECT * FROM Products")
    connection.close()
    return cursor.fetchall()




initiate_db()

