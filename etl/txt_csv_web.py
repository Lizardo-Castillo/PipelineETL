import os

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

def reordenar_campos(campos):
    """
    Reordena los campos para que estén en el orden:
    ID, INV, DATE, CATALOG, PCODE, QTY, custnum
    """
    if len(campos) < 7:
        return campos  # No hay suficientes campos para reordenar

    return [
        campos[0],  # ID
        campos[1],  # INV
        campos[3],  # DATE
        campos[4],  # CATALOG
        campos[2],  # PCODE
        campos[5],  # QTY
        campos[6],  # custnum
    ]

def convertir_txt_a_csv_con_reordenacion(ruta_txt):
    if not os.path.isfile(ruta_txt):
        print(f"❌ Archivo no encontrado: {ruta_txt}")
        return

    ruta_csv = os.path.splitext(ruta_txt)[0] + ".csv"

    with open(ruta_txt, 'r', encoding='utf-8') as f_entrada, \
         open(ruta_csv, 'w', encoding='utf-8', newline='') as f_salida:

        encabezado_linea = f_entrada.readline().strip().replace(';', ',')
        f_salida.write(encabezado_linea + '\n')

        for linea in f_entrada:
            campos = corregir_comillas_solas(linea)

            if len(campos) < 7:
                campos.extend(['""'] * (7 - len(campos)))

            campos = reordenar_campos(campos)

            f_salida.write(','.join(campos) + '\n')

    print(f"✅ Archivo reordenado y convertido a CSV: {ruta_csv}")

# ======= USO COMO SCRIPT =======
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python etl/reorder_txt_to_csv.py <archivo.txt>")
    else:
        convertir_txt_a_csv_con_reordenacion(sys.argv[1])
