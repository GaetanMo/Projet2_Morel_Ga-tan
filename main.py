import csv

import requests
from bs4 import BeautifulSoup

from scrap_un_livre import scrap_un_livre


def scrap_url_livres(url_page_actuelle, stockage): #fonction qui permet de scrap les URL de tous les livres de la catégorie sequential-art
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
        page_suivante = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/" + page_suivante
        scrap_url_livres(page_suivante, stockage)


#Lance la fonction pour visiter la catégorie sequential art, et les stocker dans la liste links
url_sequentialart = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
links = []
scrap_url_livres(url_sequentialart, links)

#Création de l'entête du fichier CSV
en_tete = ['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']

with open('data.csv', 'w') as csv_file: #Création fichier CSV
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete) #Première ligne = en_tete
    for link in links: #Pour tous les liens dans la liste links, on éxécute les deux lignes suivantes
        informations_livre = scrap_un_livre(link)
        writer.writerow(informations_livre)


    
    

    






