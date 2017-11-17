import requests
from bs4 import BeautifulSoup


def craigslist_spider(max_pages):
    page = 10
    while page <= max_pages:
        url = 'https://austin.craigslist.org/search/apa?s=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('a', {'class': 'result-title hdrlnk'}):
            href = 'https://austin.craigslist.org/search/apa?s=' + link.get('href')
            print(href)

        page += 10


craigslist_spider(10)   