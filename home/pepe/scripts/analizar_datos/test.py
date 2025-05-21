import csv

def procesar_datos(archivo_csv):
    with open(archivo_csv, 'r', newline='') as archivo:
        lector_csv = csv.reader(archivo)
        encabezados = next(lector_csv)  
        print(f"Encabezados: {encabezados}")

        for fila in lector_csv:
            print(fila)


archivo_csv = "datos.csv"

print(f"Procesando el archivo {archivo_csv}...")
procesar_datos(archivo_csv)
