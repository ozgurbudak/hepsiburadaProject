from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self, url):
        self.url = url

    def parse(self):
        print("parsing: ", self.url)
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, 'html.parser')

        return_dict = {}
        product_price = soup.find('span', attrs={'class': 'price'}).get("content")
        product_name = soup.find('h1', attrs={'class': 'product-name'}).text.strip()
        product_image = soup.find('img', attrs={'class': 'product-image'}).get("src")

        return_dict['price'] = product_price
        return_dict['title'] = product_name
        return_dict['image'] = product_image

        return return_dict
