import requests
import lxml
from bs4 import BeautifulSoup

def get_link_data(url):
    headers = {
        "User-Agent": "",
        "Accept-Language": ""
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = float(price[1:])

    return name, price