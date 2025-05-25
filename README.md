# 🗃️ Proyecto ETL: Consolidación de Pedidos y Productos

---

## 🎯 Objetivo

El propósito de este proyecto es **unificar y preparar datos de productos y pedidos**, provenientes de múltiples fuentes (archivos `.csv`, `.txt`, `.json`), para que estén listos para su análisis en una base de datos PostgreSQL.

> Posteriormente, estos datos pueden ser analizados con herramientas como **WEKA**.

---

## 🔄 Proceso ETL: ¿Qué se hace?

**ETL** significa:

1. **Extract (Extracción):**
   Leer los archivos de datos originales desde distintas fuentes y formatos (`.txt`, `.csv`, `.json`).

2. **Transform (Transformación):**
   Corregir errores como:

   * Formato de fechas inconsistente
   * Comillas incorrectas
   * Delimitadores mixtos (`;` y `,`)
   * Columnas desordenadas

3. **Load (Carga):**
   Insertar los datos **limpios y estructurados** en tablas PostgreSQL (`products` y `orders`).

---

## 🧩 Estructura del Proyecto

El proyecto está organizado en 4 partes principales:

| Parte                        | Función                                              |
| ---------------------------- | ---------------------------------------------------- |
| 1️⃣ Verificación de conexión | Asegurar que la conexión a la base de datos funciona |
| 2️⃣ Creación de tablas       | Crear las tablas necesarias (`products`, `orders`)   |
| 3️⃣ Transformación de datos  | Corregir y convertir los archivos fuente             |
| 4️⃣ Carga de datos           | Insertar los datos en PostgreSQL                     |

---

### 1️⃣ Verificación de Conexión a PostgreSQL

Este código nos asegura de que las credenciales sean válidas y que PostgreSQL esté funcionando correctamente.

📄 `db_config.py`

```python
DB_CONFIG = {
    "dbname": "lab_02",
    "user": "postgres",
    "password": "sonar",
    "host": "localhost",
    "port": "5432"
}
```

📄 `connection.py`

```python
import psycopg2
from config.db_config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)
```

---

### 2️⃣ Creación de Tablas (si no existen)

📄 `create_tables.py`

Define dos tablas principales:

* `products`: datos de los productos (nombre, código, precio, proveedor).
* `orders`: pedidos de catálogo y web.

```python
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
```

---

### 3️⃣ Transformación de Datos

#### a. Conversión de `.txt` a `.csv`

Corrige comillas sueltas y cambia los delimitadores a comas.

📄 `txt_to_csv.py`

```python
def corregir_comillas_solas(linea):
    linea = linea.replace(';', ',')
    campos = linea.strip().split(',')

    for i, campo in enumerate(campos):
        campo = campo.strip()
        if campo == '"':
            campos[i] = '""'
        else:
            campos[i] = campo
    return campos
```

```python
def convertir_txt_a_csv(ruta_txt):
    ...
    # Verifica existencia del archivo, convierte encabezado y líneas
```

✅ Este proceso genera archivos limpios como: `Catalog_Orders.csv`, `products.csv`.

---

### 4️⃣ Carga de Datos Limpios

📄 `load_data.py`

#### a. Conversión de fechas

Se usa una función que detecta distintos formatos para asegurar que las fechas sean válidas.

```python
def parse_fecha(fecha_str):
    formatos = [
        "%d/%m/%Y %H:%M:%S",
        ...
    ]
    for fmt in formatos:
        try:
            return datetime.strptime(fecha_str.strip(), fmt)
        except Exception:
            continue
    return None
```

#### b. Función para cargar productos

```python
def cargar_products_csv(path, cur):
    ...
    cur.execute("""INSERT INTO products (...) VALUES (...);""")
```

#### c. Función para cargar pedidos

```python
def cargar_orders_csv(path, cur):
    ...
    if fecha is None:
        print(f"⚠️ Fecha inválida... se omite.")
```

#### d. Carga total

```python
def cargar_todos_los_datos():
    ...
    cargar_products_csv("data/products.csv", cur)
    cargar_orders_csv("data/Catalog_Orders.csv", cur)
    cargar_orders_csv("data/Web_orders.csv", cur)
```

---

## 🚀 Ejecución del Proceso ETL

📄 `main.py`

Este script centraliza todo:

```python
from db.create_tables import crear_tablas
from etl.txt_to_csv import convertir_txt_a_csv
from etl.txt_csv_web import convertir_txt_a_csv_con_reordenacion
from etl.load_data import cargar_todos_los_datos

def main():
    convertir_txt_a_csv("data/Catalog_Orders.txt")
    convertir_txt_a_csv("data/products.txt")
    convertir_txt_a_csv_con_reordenacion("data/Web_orders.txt")

    crear_tablas()
    cargar_todos_los_datos()

if __name__ == "__main__":
    main()
```

📌 Para correr el proceso completo:

```
py main.py
```

---

## 🧪 Verificación (PostgreSQL)

Luego de ejecutar el script, podemos verificar si los datos se insertaron correctamente:

```sql
SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM orders;
```

---

## ✅ Resultado Final

🔹 Se obtienen los datos de productos y pedidos **consolidados, corregidos y cargados** en la base de datos PostgreSQL `lab_02`.

🔹 Listos para ser usados en:

* Análisis con **WEKA**
* Consultas avanzadas con **SQL**

---
