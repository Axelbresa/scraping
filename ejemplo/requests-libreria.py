import requests

response = requests.get("https://pypi.org")

print("Contenido de la pagina")
print(response.text)
print("Estado de la peticion")
print(response.status_code) # 200

print("Busqueda url")
payload = { "q": "tu busqueda" }
response = requests.get("https://pypi.org", params=payload)
print(response.url) # https://pypi.org/?q=astro

print("peticion del json")
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
print(data)