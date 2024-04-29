import csv
import os

import requests
from bs4 import BeautifulSoup

from scrap_un_livre import scrap_un_livre
from scrap_url_livres import scrap_url_livres
from parcourir_categories import parcourir_categories


categories = parcourir_categories()

for categorie in categories:
    url_categorie = f"https://books.toscrape.com/catalogue/category/books/{categorie}/index.html"
    links = []

    scrap_url_livres(url_categorie, categorie, links)

    en_tete = ['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']

    nom_du_fichier = f"{categorie.replace('/','')}.csv"

    with open(nom_du_fichier, 'w') as csv_file: #Création fichier CSV
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(en_tete) #Première ligne = en_tete
        for link in links: #Pour tous les liens dans la liste links, on éxécute les deux lignes suivantes
            informations_livre = scrap_un_livre(link)
            writer.writerow(informations_livre)







    
    

    






