from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
 
# URL de la página de inicio de Wikipedia en español
url = "https://listado.mercadolibre.com.pe/iphone-15"
 
# Realizar la solicitud GET a la página
response = requests.get(url)
print(response.text)
 
# Crear el objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

soup2 = BeautifulSoup(response.text, 'lxml')
 
# Encontrar todos los elementos <span> con la clase "mw-headline" (los títulos de los artículos)
title = soup.find_all('h3', class_='ui-search-item__title')
price = soup.find_all('span', class_='andes-money-amount__fraction')
detail = soup.find_all('span', class_='ui-search-item__group__element')
store = soup.find_all('p', class_='ui-search-layout--stack')
 
# Imprimir los títulos de los artículos
for titulo in titulos:
    print(titulo.text)


app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html,**locals()')
app.run(debug=True)