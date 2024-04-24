import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")


product_page_url = url

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

#Je scrap la catégorie du livre
chemin = soup.find_all("li")
category = chemin[2].text

#Je scrap les avis (étoiles)
paragraphe_avis = paragraphes[2]
review_rating = paragraphe_avis['class']


#liste dans l'ordre des informations à mettre dans le fichier csv
liste_informations = [product_page_url, UPC, title, price_including_tax, price_excluding_tax, number_available,product_description, category, review_rating]

print(liste_informations)



""" Prototype de création du fichier csv

en_tete = ['product_page_url', 'universal_ product_code (upc)', 'title, price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']

with open('data.csv', 'w') as csv_file:
writer = csv.writer(csv_file, delimiter=',')
writer.writerow(en_tete)

"""
