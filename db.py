import sqlite3

DB_NAME = "prices.db"

def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE NOT NULL,
            price TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_product(url, price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO products (url, price) VALUES (?, ?)", (url, price))
    conn.commit()
    conn.close()

def update_price(url, new_price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE url = ?", (new_price, url))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

create_db()  # Run on startup
