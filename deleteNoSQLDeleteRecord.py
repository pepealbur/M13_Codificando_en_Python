import requests

# URL base de la API
base_url = 'https://66b4e4f59f9169621ea4c20d.mockapi.io/api/v1/contactos'

# ID del registro que deseas eliminar
registro_id = '1'  # Cambia esto al ID del registro que deseas eliminar

# URL del registro específico
url = f'{base_url}/{registro_id}'

# Hacer la solicitud DELETE para eliminar el registro
response = requests.delete(url)

# Comprobar que la solicitud fue exitosa
if response.status_code == 200:
    print(f"Registro con ID {registro_id} eliminado exitosamente.")
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(f"Respuesta del servidor: {response.text}")
