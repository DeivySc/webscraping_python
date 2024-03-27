from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template

url = 'https://listado.mercadolibre.com.pe/iphone-15'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('li', class_='ui-search-layout__item')

product_list = []
for product in products:
    title = soup.find('h3').get_text
    price = soup.find('span', class_='andes-money-amount__fraction').get_text
    post_link = soup.find("a")["href"]
    img_link = soup.find("img")["data-src"]


#Servicio
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', products=product_list)

