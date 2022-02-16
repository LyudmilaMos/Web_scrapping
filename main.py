import requests

import bs4

base_url = 'https://habr.com'

url = base_url + '/ru/all/'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

#   определяем список ключевых слов

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

#   Ваш код

response = requests.get(url, headers=HEADERS)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')

for article in articles:

    hubs = article.find_all(class_='tm-articles-snippet__hubs-items')
    hubs = [hub.text.strip() for hub in hubs]

    date_article = article.find(class_='tm-article-snippet__datetime-published').text

    title_article = article.find('h2').find('span').text
    
    href = article.find(class_='tm-article-snippet__title-link').attrs['href']
    link_article = base_url + href

    for hub in KEYWORDS:

        if hub.lower() in title_article.lower():

            print(f'дата: {date_article} - заголовок: {title_article} - ссылка: {link_article}')
