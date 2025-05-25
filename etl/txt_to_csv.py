import os

def corregir_comillas_solas(linea):
    """
    Corrige campos que solo contengan una comilla doble " sola, 
    agregando otra para que sea "" (campo vacío válido).
    Además, reemplaza ; por , para normalizar delimitadores.
    """
    linea = linea.replace(';', ',')
    campos = linea.strip().split(',')

    for i, campo in enumerate(campos):
        campo = campo.strip()
        if campo == '"':
            campos[i] = '""'
        else:
            campos[i] = campo
    return campos

def convertir_txt_a_csv(ruta_txt):
    if not os.path.isfile(ruta_txt):
        print(f"❌ Archivo no encontrado: {ruta_txt}")
        return

    ruta_csv = os.path.splitext(ruta_txt)[0] + ".csv"

    with open(ruta_txt, 'r', encoding='utf-8') as f_entrada, \
         open(ruta_csv, 'w', encoding='utf-8', newline='') as f_salida:

        encabezado = f_entrada.readline().strip().replace(';', ',')
        num_campos = len(encabezado.split(','))
        f_salida.write(encabezado + '\n')

        for linea in f_entrada:
            campos = corregir_comillas_solas(linea)

            if len(campos) < num_campos:
                campos.extend(['""'] * (num_campos - len(campos)))

            linea_corregida = ','.join(campos)
            f_salida.write(linea_corregida + '\n')

    print(f"✅ Archivo convertido y guardado: {ruta_csv}")

# ======== USO DIRECTO COMO SCRIPT ========
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python etl/txt_to_csv.py <ruta_al_archivo_txt>")
    else:
        convertir_txt_a_csv(sys.argv[1])
