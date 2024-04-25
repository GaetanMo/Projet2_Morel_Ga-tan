import csv

import requests
from bs4 import BeautifulSoup



url_book = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

response = requests.get(url_book)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,"html.parser")

#Url de la page
product_page_url = url_book

#Tableau "product description" qui contient certaines infos qui m'intéressent extraites dans lignes_tableau
tableau = soup.find_all("td")

#J'associe les valeurs du tableau aux variables demandées
UPC = tableau[0].text
price_including_tax = tableau[3].text
price_excluding_tax = tableau[2].text
number_available = tableau[5].text

#Je scrap le titre du livre
title = soup.find("h1").text

#Je scrap la description du livre
paragraphes = soup.find_all('p')
product_description = paragraphes[3].text

#Je scrap la catégorie du livre (et j'enleve des retours à la lignes inutiles)
chemin = soup.find_all("li")
category = chemin[2].text
category = category.replace('\n', '')

#Je scrap les avis (étoiles), sauf qu'ils étaient dans une class et ça s'est enregistré sous forme de liste, j'ai donc dû utiliser .join pour qu'ils ne soient plus dans une liste
paragraphe_avis = paragraphes[2]
review_rating_list = paragraphe_avis['class']
review_rating = ' : '.join(review_rating_list)
review_rating = review_rating.replace('"', '')

#Je scrap l'URL de l'image
image_url_line = soup.find("img")
image_url_src = image_url_line["src"]
image_url_src = image_url_src.replace('../../', '') #J'enlève les ../../ en trop avant le "média"
lien_general = "https://books.toscrape.com/"
image_url = lien_general + image_url_src



#liste dans l'ordre des informations à mettre dans le fichier csv
liste_informations = [product_page_url, UPC, title, price_including_tax, price_excluding_tax, number_available,product_description, category, review_rating, image_url]





"""
#Création fichier CSV

en_tete = ['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']

#Pour ouvrir un fichier data.csv correspondant au cas où

with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete)
    writer.writerow(liste_informations)
"""