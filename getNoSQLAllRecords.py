import requests
import pandas as pd
import json

# URL de la API
url = 'https://66b4e4f59f9169621ea4c20d.mockapi.io/api/v1/contactos'

# Hacer la solicitud GET a la API
response = requests.get(url)

# Comprobar que la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()

    # Mostrar los datos en formato JSON formateado
    import json

    print(json.dumps(data, indent=4))

    # Convertir los datos a un DataFrame de pandas
    df = pd.DataFrame(data)

    # Mostrar el DataFrame
    print(df)

    # Exportar el DataFrame a un archivo CSV
    df.to_csv('contactos.csv', index=False)

    print("Datos exportados a contactos.csv")
else:
    print(f"Error en la solicitud: {response.status_code}")
