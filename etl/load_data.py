import csv
from datetime import datetime
from db.connection import get_connection  # Asegúrate que este archivo exista

def parse_fecha(fecha_str):
    formatos = [
        "%d/%m/%Y %H:%M:%S",
        "%m/%d/%y %H:%M:%S",
        "%d/%m/%y %H:%M:%S",
        "%m/%d/%Y %H:%M:%S",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%d/%m/%y",
        "%m/%d/%y",
    ]
    for fmt in formatos:
        try:
            return datetime.strptime(fecha_str.strip(), fmt)
        except Exception:
            continue
    return None  # Si no puede parsear, devuelve None

def cargar_products_csv(path, cur):
    print(f"📥 Cargando {path}...")
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO products (id, type, descrip, price, cost, pcode, supplier)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """, (
                int(row['ID']),
                row['TYPE'],
                row['DESCRIP'],
                float(row['PRICE']),
                float(row['COST']),
                row['PCODE'],
                row['supplier']
            ))

def cargar_orders_csv(path, cur):
    print(f"📥 Cargando {path}...")
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            fecha = parse_fecha(row['DATE'])
            if fecha is None:
                print(f"⚠️  Fecha inválida en ID {row['ID']}, se omite.")
                continue
            cur.execute("""
                INSERT INTO orders (id, inv, order_date, catalog, pcode, qty, custnum)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """, (
                int(row['ID']),
                float(row['INV']),
                fecha,
                row['CATALOG'],
                row['PCODE'],
                float(row['QTY']),
                row['custnum']
            ))

def cargar_todos_los_datos():
    conn = get_connection()
    cur = conn.cursor()

    # Carga de productos
    cargar_products_csv("data/products.csv", cur)

    # Carga de órdenes
    cargar_orders_csv("data/Catalog_Orders.csv", cur)
    cargar_orders_csv("data/Web_orders.csv", cur)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Todos los datos fueron cargados en la base de datos.")
