import requests
from bs4 import BeautifulSoup


class WebScrape:
    def trigger_error(self, err_message):
        self.has_error = True
        self.err_message = err_message

    def __init__(self, url):
        self.has_error = False
        response = requests.get(url)
        self.soup = BeautifulSoup(response.content, "html.parser")
