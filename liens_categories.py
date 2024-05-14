import requests
from bs4 import BeautifulSoup



def liens_categories():
    url_page_accueil = "https://books.toscrape.com/index.html"

    response_category = requests.get(url_page_accueil)
    response_category.encoding = 'utf-8'
    soup = BeautifulSoup(response_category.text, "html.parser")

    links_categories = []

    lis = soup.find('ul', class_="nav nav-list").find('ul').find_all('li')

    for li in lis:
        a = li.find('a')
        link = a['href'].replace('catalogue/category/books/', '').replace('/index.html', '')
        links_categories.append(link)

    return links_categories
