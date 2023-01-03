from pprint import pprint

import requests
from bs4 import BeautifulSoup

class ParsesNews:
    __URL = 'https://www.securitylab.ru'
    __HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    @classmethod
    def __get_html(cls, url=None):
        if url:
            req = requests.get(url=url, headers=cls.__HEADERS)
        else:
            req = requests.get(url=cls.__URL, headers=cls.__HEADERS)

        return req

    @classmethod
    def __get_data(cls, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('a', class_='article-card inline-card')
        news = []
        for item in items:
            news.append({
                "title": item.find('h2', class_="article-card-title").getText(),
                "date": item.find('time').getText(),
                'caption': item.find('p').getText(),
                'link': cls.__URL + item.get("href")
            })
        return news

    @classmethod
    def parser(cls):
        html = cls.__get_html(cls.__URL)
        if html.status_code == 200:
            news = []
            for i in range(1, 3):
                html = cls.__get_html(f"{cls.__URL}/news/page1_{i}.php")
                current_page = cls.__get_data(html.text)
                news.extend(current_page)
            return news
        else:
            raise Exception("Bad Request!")
