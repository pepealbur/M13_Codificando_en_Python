import requests
from bs4 import BeautifulSoup

# URL de la página del Instituto Tecnológico de Pachuca
url = 'https://www.itp.edu.mx'  # Reemplaza esta URL con la correcta si es diferente

# Realizar la solicitud HTTP
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Buscar la sección de actividades extraescolares
    # Nota: Necesitarás adaptar esto basado en la estructura real del HTML
    actividades_extraescolares = soup.find_all('a', href=True, text='Actividades Extraescolares')

    for actividad in actividades_extraescolares:
        print(f"Enlace: {actividad['href']}")
        print(f"Texto: {actividad.get_text()}")

    # Si necesitas buscar en una página específica para actividades extraescolares
    # Puedes realizar una solicitud a esa URL en lugar de la principal
    # Ejemplo:
    # detalle_url = 'https://www.itp.edu.mx/actividades-extraescolares'
    # detalle_response = requests.get(detalle_url)
    # detalle_soup = BeautifulSoup(detalle_response.content, 'html.parser')
    # print(detalle_soup.prettify())
else:
    print(f"Error al acceder a la página: {response.status_code}")