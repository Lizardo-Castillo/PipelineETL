from etl.extract import extract_web_orders, extract_catalog_orders, extract_products
from etl.transform import clean_web_orders, clean_catalog_orders, clean_products, integrate_orders, group_products
from etl.load import load_to_postgres

# Configuración
DB_URL = 'postgresql://usuario:clave@localhost:5432/tienda'

# Extracción
web_df = extract_web_orders('data/web_orders.csv')
catalog_df = extract_catalog_orders('data/catalog_orders.csv')
products_df = extract_products('data/products.json')

# Transformación
web_df_clean = clean_web_orders(web_df)
catalog_df_clean = clean_catalog_orders(catalog_df)
products_df_clean = clean_products(products_df)

orders_integrated = integrate_orders(web_df_clean, catalog_df_clean)
products_grouped = group_products(products_df_clean)

# Carga
load_to_postgres(orders_integrated, 'pedidos', DB_URL)
load_to_postgres(products_grouped, 'productos', DB_URL)
