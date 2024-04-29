import csv

import requests
from bs4 import BeautifulSoup


def scrap_url_livres(url_page_actuelle, categorie, stockage):
    response_category = requests.get(url_page_actuelle)
    response_category.encoding = 'utf-8'
    soup = BeautifulSoup(response_category.text, "html.parser")

    # Isoler le div qui contient le lien de la page des livres
    divs = soup.find_all('div', class_="image_container")

    # Obtenir les liens des livres sur la page
    for div in divs:
        a = div.find('a')
        link = a['href'].replace('../../../', '')
        stockage.append("https://books.toscrape.com/catalogue/" + link)

    bouton_suivant = soup.find("li", class_="next")
    if bouton_suivant: 
        page_suivante = bouton_suivant.find("a")["href"]
        page_suivante = f"https://books.toscrape.com/catalogue/category/books/{categorie}/" + page_suivante
        scrap_url_livres(page_suivante, categorie, stockage)