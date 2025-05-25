from db.connection import get_connection

def crear_tablas():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        type TEXT,
        descrip TEXT,
        price NUMERIC(10, 2),
        cost NUMERIC(10, 2),
        pcode TEXT UNIQUE,
        supplier TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        inv NUMERIC(12, 2),
        order_date TIMESTAMP,
        catalog TEXT,
        pcode TEXT,
        qty NUMERIC(10, 2),
        custnum TEXT
    );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Tablas creadas correctamente.")
