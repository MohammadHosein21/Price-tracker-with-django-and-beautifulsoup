import requests
import lxml
from bs4 import BeautifulSoup

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = float(price[1:])

    return name, price