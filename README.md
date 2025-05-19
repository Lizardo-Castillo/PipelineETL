# ETL Proyecto: Consolidación de Pedidos y Productos

## 📄 Informe: Documentación del ETL

### 🌍 Objetivo

Consolidar información de pedidos y productos desde múltiples fuentes (CSV, JSON) en una base de datos PostgreSQL para su posterior análisis.

---

### ⚙️ Extract

* Se utilizaron `pandas.read_csv` y `pandas.read_json` para leer los archivos.
* Se manejaron separadores inconsistentes (`;`) y fechas en formato europeo (`dayfirst=True`).

---

### ✏️ Transform

* Se normalizaron los nombres de columnas y tipos de datos.
* Se eliminaron valores nulos o corruptos.
* Se integraron las tablas de pedidos (`web_orders` + `catalog_orders`) en una sola tabla unificada: `pedidos`.
* Los productos se agruparon por tipo y proveedor para consolidar precios y costos.

---

### 🚧 Load

* Se utilizó `SQLAlchemy` para establecer la conexión con PostgreSQL.
* Se creó un esquema con dos tablas:

  * `pedidos`
  * `productos`

---

### 📅 Estructura del Proyecto

```
.
├── config.py
├── extract.py
├── transform.py
├── load.py
├── main.py
├── data/
│   ├── web_orders.csv
│   ├── catalog_orders.csv
│   └── products.json
└── README.md
```

---

### ⚡ Tecnologías Utilizadas

* Python 3.x
* Pandas
* SQLAlchemy
* PostgreSQL

---
