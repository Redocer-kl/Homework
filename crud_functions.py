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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')
    connection.commit()

def get_all_products():
    connection = sqlite3.connect("not_telegram.db")
    cursor.execute("SELECT * FROM Products")
    connection.close()
    return cursor.fetchall()


def add_user(username, email, age):
    connection = sqlite3.connect("not_telegram.db")
    if not is_included(username):
        cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, ?)
        ''', (username, email, age, 1000))

    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect("not_telegram.db")

    cursor.execute('''
    SELECT EXISTS(SELECT 1 FROM Users WHERE username=?)
    ''', (username,))

    result = cursor.fetchone()[0]
    connection.close()

    return bool(result)

initiate_db()

