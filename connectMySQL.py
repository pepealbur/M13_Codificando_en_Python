import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Establece la conexión
        connection = mysql.connector.connect(
            host='195.179.238.58',            # Ejemplo: 'localhost'
            database='u927419088_testing_sql',  # Ejemplo: 'mi_base_de_datos'
            user='u927419088_admin',          # Ejemplo: 'root'
            password='#Admin12345#'    # Tu contraseña
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")

            # Obtener información del servidor
            db_info = connection.get_server_info()
            print("Información del servidor MySQL:", db_info)

            # Ejecutar una consulta simple
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Conectado a la base de datos:", record)

    except Error as e:
        print("Error al conectar a MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

if __name__ == "__main__":
    connect_to_mysql()
