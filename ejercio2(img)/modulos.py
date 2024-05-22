# Importamos los paquetes
import os
import requests
from bs4 import BeautifulSoup

# Creamos una carperta imagenes
os.makedirs("./ejercio2(img)/imagenes", exist_ok=True)

# Hace una solicitud GET a la URL y devuelve el contenido en formato de texto (HTML).
def getdata(url):
    r = requests.get(url)
    return r.text

# Parseamos el HTML y en soup se guarda la estructura del HTML.
def parsearHtml():
    htmldata = getdata("https://www.geeksforgeeks.org/")
    soup = BeautifulSoup(htmldata, 'html.parser')
    valid_extensions = ['.png', '.jpg', '.jpeg', '.webp']
    img_extension(soup, valid_extensions)

# Valimos si las extensiones de la img es jpg, png, jpeg o webp
def img_extension(soup, valid_extensions):
    for item in soup.find_all('img'):
        src = item.get('src', '')
        if any(src.lower().endswith(ext) for ext in valid_extensions):
            download_image(src)

# Las images lo guardamos  en la carpeta imagenes
def download_image(url, folder="./ejercio2(img)/imagenes"):
    try:
        response = requests.get(url, stream=True)
        # Extraer el nombre del archivo de la URL
        filename = os.path.join(folder, url.split("/")[-1])
        # Guardar la imagen en la carpeta
        with open(filename, 'wb') as file:
            for i in response:
                file.write(i)
        print(f"Imagen descargada: {filename}")
    except Exception as e:
        print(f"No se pudo descargar {url}. Error: {e}")

# Llamamos a la funcion
parsearHtml()
