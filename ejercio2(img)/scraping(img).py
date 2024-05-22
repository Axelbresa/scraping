import requests
from bs4 import BeautifulSoup

def getdata(url):
    r = requests.get(url)
    return r.text

htmldata = getdata("https://www.geeksforgeeks.org/")

print("img")
soup = BeautifulSoup(htmldata, 'html.parser')

valid_extensions = ['.png', '.jpg', '.jpeg', '.webp']
for item in soup.find_all('img'):
    src = item.get('src', '')
    if any(src.lower().endswith(ext) for ext in valid_extensions):
        print(src)
