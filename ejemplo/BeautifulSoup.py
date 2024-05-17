# permite parsear principalmente código HTML.
from bs4 import BeautifulSoup

contents = """
<html lang="en">
<head>
<title>Just testing</title>
</head>
<body>
<div class="contenedor">
    <div>
    <h1>Hola como estas h1</h1>
    <h2>Hola como estas h2</h2>
    <p>Hola como estas</p>
    <ol>
    <li>hola</li>
    </ol>
    </div>
</div>
</body>
<html>"""
soup = BeautifulSoup(contents, features="html.parser")

# Localizar todos los elementos de un tipo:
print(soup.find_all("div")) # el elemento sin los paréntesis angulares

# ● Buscar un conjunto de elementos:
soup.find_all(["li", "p"])
# ● Localizar todos los elementos con una propiedad (en el caso de la clase, debe tener un guión bajo por sintaxis):
classResults = soup.find_all(class_="contenedor")
nameResults = soup.find_all(name="username")
print(classResults)
print(nameResults)
# ● Si el atributo a localizar tiene guiones medios (por ejemplo aria-label) no podremos usarlo como nombre de argumento (error sintáctico). Pero sí podemos usar un diccionario en su lugar:
soup.find_all(attrs={"aria-label": "box"})
# ● Buscar por varios parámetros al mismo tiempo (un div que tenga una clase “footer”)
soup.find_all("div", class_="footer")

import re
headers = soup.find_all(re.compile(r'^h\d+.*')) # encontrará todos
print(headers)
# los h1, h2, h3, h... del contenido proporcionado