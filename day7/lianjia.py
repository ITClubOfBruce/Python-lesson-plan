import requests
from bs4 import BeautifulSoup
import lxml

def get_html():
    url = 'https://bj.lianjia.com/zufang'  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.select('div.content__article > div.content__list > div > div > p.content__list--item--title.twoline > a')
    for title in titles:
        print(title.get_text())


get_html()