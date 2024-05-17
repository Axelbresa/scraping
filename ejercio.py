import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
from collections import deque
import os

# Obtener la ruta actual del script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Función para extraer enlaces de una página
def extract_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        return [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
    except requests.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
        return []

# Función para extraer <h1> y <p> de una página
def extract_h1_p(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
        p_tags = [p.get_text(strip=True) for p in soup.find_all('p')]
        return h1_tags, p_tags
    except requests.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
        return [], []

# Función principal del crawler con límite de profundidad y número de páginas
def web_crawler(start_url, max_pages=10, max_depth=2):
    visited = set()
    data = {}
    queue = deque([(start_url, 0)])

    while queue and len(visited) < max_pages:
        url, depth = queue.popleft()
        if url in visited or depth > max_depth:
            continue
        visited.add(url)
        print(f"Crawling: {url} at depth {depth}")
        
        links = extract_links(url)
        h1_tags, p_tags = extract_h1_p(url)
        data[url] = {"h1": h1_tags, "p": p_tags}
        
        if depth < max_depth:
            for link in links:
                if link not in visited:
                    queue.append((link, depth + 1))

    # Guardar los datos en un archivo JSON en la misma carpeta del script
    output_file = os.path.join(current_dir, "output.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=True, indent=4)

    # Imprimir los datos guardados
    print(data)
    # print(json.dumps(data, ensure_ascii=False, indent=4))

# URL inicial para el crawler
start_url = "https://www.fundacioncva.cl/?gad_source=1&gclid=Cj0KCQjwgJyyBhCGARIsAK8LVLPaMRLTK2WfhaWQ-4eYFtiSjDcjwONtCRS7eVwGJnP9ILuRmxx3QNEaAqpUEALw_wcB"

web_crawler(start_url, max_pages=5, max_depth=2)
