from db.create_tables import crear_tablas
from etl.txt_to_csv import convertir_txt_a_csv
from etl.txt_csv_web import convertir_txt_a_csv_con_reordenacion
from etl.load_data import cargar_todos_los_datos

def main():
    # 1. Convertir los txt a csv corregidos
    convertir_txt_a_csv("data/Catalog_Orders.txt")
    convertir_txt_a_csv("data/products.txt")
    convertir_txt_a_csv_con_reordenacion("data/Web_orders.txt")

    # 2. Crear las tablas
    crear_tablas()

    # 3. Llenar datos a las tablas
    cargar_todos_los_datos()

if __name__ == "__main__":
    main()