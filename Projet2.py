import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

product_page_url = url

#tableau de toutes les infos rangées dans le tableau "Product Information" (les 7 lignes "tr")
table_informations = soup.find_all("tr")

#Je récupère la ligne qui m'intéresse et l'associe à la valeur correspondante
UPC = table_informations[0].text
price_including_tax = table_informations[3].text
price_excluding_tax = table_informations[2].text
number_available = table_informations[5].text


title = soup.find("h1")


print(number_available)