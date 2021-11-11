import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, word):
        self.word = word
        self.search = requests.get('https://www.urbandictionary.com/define.php?term='+self.word)

    def getResponse(self):
        soup = BeautifulSoup(self.search.text, 'html.parser')
        heading = soup.find_all("div", class_ = "def-header")
        meaning = soup.find_all("div", class_ = "meaning")
        example = soup.find_all("div", class_ = "example")
        result = [heading[0].get_text(), meaning[0].get_text(), example[0].get_text()]
        return result
