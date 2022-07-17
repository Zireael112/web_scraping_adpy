import bs4
import requests
from fake_headers import Headers

KEYWORDS = ['Фриланс', 'Java', 'Assembler', 'Python']

HEADERS = Headers(browser='chrome', os='win').generate()
base_url = 'https://habr.com'
url = base_url + '/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text

soap = bs4.BeautifulSoup(text, features='html.parser')
articles = soap.find_all('article')

for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item-link')
    hubs = [hub.find('span').text for hub in hubs]
    for hub in hubs:
        if hub in KEYWORDS:
            dates = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
            title = article.find('h2').find('span').text
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            print(f'Дата - {dates}\n Заголовок - {title}\n Ссылка - {base_url + href}\n')