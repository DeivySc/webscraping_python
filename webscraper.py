#Demo de webScraping

import requests
from bs4 import BeautifulSoup
 
# URL de la página de inicio de Wikipedia en español
url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
 
# Realizar la solicitud GET a la página
response = requests.get(url)
#print(response.text)
 
# Crear el objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
 
# Encontrar todos los elementos <span> con la clase "mw-headline" (los títulos de los artículos)
titulos = soup.find_all('span', class_='mw-headline')
 
# Imprimir los títulos de los artículos
for titulo in titulos:
    print(titulo.text)