# Este programa carga un archivo Excel llamado "calificaciones_alumnos.xlsx" que contiene las calificaciones de los alumnos
# en diferentes materias. Luego, agrega una nueva columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100 con un decimal,
# y guarda el archivo con las modificaciones.

import pandas as pd
import numpy as np

# Definir el nombre del archivo
archivo = 'calificaciones_alumnos.xlsx'

try:
    # Cargar el archivo Excel
    df = pd.read_excel(archivo)
    print("Archivo cargado exitosamente.")

    # Generar valores aleatorios entre 0 y 100 con un decimal para la nueva columna "Mat_Fisica"
    df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, df.shape[0]), 1)
    print("Columna 'Mat_Fisica' agregada.")

    # Guardar el DataFrame modificado de vuelta al archivo Excel
    df.to_excel(archivo, index=False)
    print("Archivo guardado exitosamente.")

except FileNotFoundError:
    print(f"Error: El archivo '{archivo}' no se encontró.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")