import random
from bs4 import BeautifulSoup as bs
import requests


def parser_uk():
    # Стартова сторінка парсингу
    result_list = []
    url_uk = 'https://muzati.net/sborniki/ukrainian-music'

    # Глибина парсингу(кількість сторінок)
    first_page = []
    for k in range(1, 11):
        first_page.append(f'{url_uk}?page{k}')

    # Парсинг випадкової сторінки
    parser_page = requests.get(random.choice(first_page))
    soup = bs(parser_page.text, 'lxml')
    parser_list = soup.find_all('a', class_='track-fav', )

    # Посилання на пісню
    for x in parser_list:
        result_link = x['href']
        result_list.append(f'https://muzati.net{result_link}')

    # Парсинг випадкової пісні
    random_song = random.choice(result_list)
    internal_page = requests.get(random_song)
    soup1 = bs(internal_page.text, 'lxml')
    internal_parser_list = soup1.find_all('a', class_='loadbtnjs', )

    # Повертаємо посилання на скачування пісні
    for k in internal_parser_list:
        return f'https://muzati.net{k["href"]}'
