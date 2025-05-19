# config.py

# Configuración de conexión a PostgreSQL
DB_CONFIG = {
    'user': 'sonar',
    'password': 'sonar',
    'host': 'localhost',
    'port': 5432,
    'database': 'tienda'
}

# Construir la URL de conexión para SQLAlchemy
DB_URL = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
         f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

# Rutas a los archivos de datos
DATA_PATHS = {
    'web_orders': 'data/web_orders.csv',
    'catalog_orders': 'data/catalog_orders.csv',
    'products': 'data/products.json'
}
