import requests
import json

# URL de la API
url = 'https://66b4e4f59f9169621ea4c20d.mockapi.io/api/v1/contactos'

# Datos del nuevo registro
nuevo_registro = {
    "nombre": "Juan Pérez",
    "email": "juan.perez@example.com",
    "telefono": "+1234567890",
    "direccion": "123 Calle Falsa, Ciudad, País"
}

# Hacer la solicitud POST para agregar el nuevo registro
response = requests.post(url, json=nuevo_registro)

# Comprobar que la solicitud fue exitosa
if response.status_code == 201:
    # Obtener el registro agregado en formato JSON
    registro_agregado = response.json()

    # Mostrar el registro agregado en formato plano
    print("Registro agregado:")
    for key, value in registro_agregado.items():
        print(f"{key}: {value}")
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(f"Respuesta del servidor: {response.text}")
