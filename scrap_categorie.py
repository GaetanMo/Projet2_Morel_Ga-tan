import csv
import os

import requests
from bs4 import BeautifulSoup

from scrap_un_livre import scrap_un_livre


def scrap_categorie(url_première_page, categorie, stockage):
    response_category = requests.get(url_première_page)
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
        scrap_categorie(page_suivante, categorie, stockage)

    
    en_tete = ['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']

    dossier_categories = "categories"

    if not os.path.exists(dossier_categories):
        os.makedirs(dossier_categories)


    chemin_fichiers_csv = os.path.abspath(os.path.join(dossier_categories, f"{categorie.replace('/','')}.csv"))

    with open(chemin_fichiers_csv, 'w') as csv_file: #Création fichier CSV
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(en_tete) #Première ligne = en_tete
        for link in stockage: #Pour tous les liens dans la liste links, on éxécute les deux lignes suivantes
            informations_livre = scrap_un_livre(link)
            writer.writerow(informations_livre) 
