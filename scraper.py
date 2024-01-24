import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Scraper:
    def __init__(self):
        self.url = os.getenv("URL")

    def ip(self):
        ip_address = requests.get(self.url).text
        return ip_address