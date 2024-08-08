import requests
import json

# URL base de la API
base_url = 'https://66b4e4f59f9169621ea4c20d.mockapi.io/api/v1/contactos'

# ID del registro que deseas modificar
registro_id = '1'  # Cambia esto al ID del registro que deseas modificar

# URL del registro específico
url = f'{base_url}/{registro_id}'

# Datos actualizados del registro
datos_actualizados = {
    "nombre": "Juan Pérez Actualizado",
    "email": "juan.perez.actualizado@example.com",
    "telefono": "+0987654321",
    "direccion": "456 Calle Verdadera, Ciudad Actualizada, País"
}

# Hacer la solicitud PUT para modificar el registro
response = requests.put(url, json=datos_actualizados)

# Comprobar que la solicitud fue exitosa
if response.status_code == 200:
    # Obtener el registro actualizado en formato JSON
    registro_actualizado = response.json()

    # Mostrar el registro actualizado en formato plano
    print("Registro actualizado:")
    for key, value in registro_actualizado.items():
        print(f"{key}: {value}")
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(f"Respuesta del servidor: {response.text}")
