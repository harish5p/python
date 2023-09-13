import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"}
        self.response = requests.get(url = self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "lxml")
        
    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"
        
    def product_price(self):
        price = self.soup.find("span", {"class": "a-price-whole"})
        if price is not None:
            return price.text.strip()
        else:
            return "Tag not found"
        
device = PriceTracer(url="https://www.amazon.in/boAt-Rockerz-255-Pro-Earphones/dp/B08TV2P1N8/")
print(device.product_title())
print(device.product_price())
        
    