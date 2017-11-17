import requests
from bs4 import BeautifulSoup

def start(url):
    word_list=[]
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
