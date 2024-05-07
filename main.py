import csv
import os

import requests
from bs4 import BeautifulSoup

from scrap_categorie import scrap_categorie
from liens_categories import liens_categories


categories = liens_categories()
               
for categorie in categories:
    url_categorie = f"https://books.toscrape.com/catalogue/category/books/{categorie}/index.html"
    links = []

    scrap_categorie(url_categorie, categorie, links)








    
    

    






