import csv

import requests
from bs4 import BeautifulSoup

import scrap_un_livre


links = []

def scrap_url_livres_page_actuelle(url_page_actuelle):

    global links

    response_category = requests.get(url_page_actuelle)
    response_category.encoding = 'utf-8'

    soup = BeautifulSoup(response_category.text,"html.parser")


    #J'isole le div qui contient le lien de la page des livres 
    divs = soup.find_all('div', class_="image_container")

    #Cette boucle me permet d'obtenir les liens des livres sur la page (en faisant print(links))
    for div in divs: 
        a = div.find('a')
        link = a['href']
        link = link.replace('../../../', '')
        links.append("https://books.toscrape.com/catalogue/" + link) 



def visiter_pages():

    url_category = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"

    response_category = requests.get(url_category)
    response_category.encoding = 'utf-8'
    soup = BeautifulSoup(response_category.text,"html.parser")

    scrap_url_livres_page_actuelle(url_category)

    bouton_suivant = soup.find("li", class_="next")

    if bouton_suivant:
        page_suivante = bouton_suivant.find("a")["href"]
        page_suivante = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/" + page_suivante
        scrap_url_livres_page_actuelle(page_suivante)
    else:
        return None




print(len(links))







