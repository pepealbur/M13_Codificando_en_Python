import requests
import json

# URL de la API
url = 'https://66b4e4f59f9169621ea4c20d.mockapi.io/api/v1/contactos'

# Hacer la solicitud GET a la API
response = requests.get(url)

# Comprobar que la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()

    # ID del registro que deseas mostrar
    registro_id = '1'  # Cambia esto al ID del registro que deseas mostrar

    # Buscar el registro con el ID especificado
    registro = next((item for item in data if item['id'] == registro_id), None)

    if registro:
        # Mostrar el registro en formato plano
        print("Registro encontrado:")
        for key, value in registro.items():
            print(f"{key}: {value}")
    else:
        print(f"No se encontró un registro con el ID {registro_id}")
else:
    print(f"Error en la solicitud: {response.status_code}")
