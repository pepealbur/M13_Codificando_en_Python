import mysql.connector
from mysql.connector import Error
import pandas as pd

def fetch_and_export_to_excel():
    try:
        # Establecer la conexión
        connection = mysql.connector.connect(
            host='195.179.238.58',            # Reemplaza con tu host, ej: 'localhost'
            database='u927419088_testing_sql',  # Reemplaza con el nombre de tu base de datos
            user='u927419088_admin',          # Reemplaza con tu usuario de MySQL
            password='#Admin12345#'    # Reemplaza con tu contraseña de MySQL
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")

            # Crear un cursor y ejecutar la consulta
            query = "SELECT * FROM curso;"
            cursor = connection.cursor()
            cursor.execute(query)

            # Obtener los nombres de las columnas
            column_names = [i[0] for i in cursor.description]

            # Fetch all rows from the executed query
            rows = cursor.fetchall()

            # Convertir los registros en un DataFrame de pandas
            df = pd.DataFrame(rows, columns=column_names)

            # Exportar a un archivo Excel
            df.to_excel("cursos.xlsx", index=False)
            print("Datos exportados a cursos.xlsx")

    except Error as e:
        print("Error al conectar a MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

if __name__ == "__main__":
    fetch_and_export_to_excel()
