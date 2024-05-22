import os
import requests
from bs4 import BeautifulSoup

os.makedirs("./ejercio2(img)/imagenes", exist_ok=True)

def getdata(url):
    r = requests.get(url)
    return r.text

htmldata = getdata("https://www.geeksforgeeks.org/")

soup = BeautifulSoup(htmldata, 'html.parser')

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

valid_extensions = ['.png', '.jpg', '.jpeg', '.webp']
for item in soup.find_all('img'):
    src = item.get('src', '')
    if any(src.lower().endswith(ext) for ext in valid_extensions):
        download_image(src)

