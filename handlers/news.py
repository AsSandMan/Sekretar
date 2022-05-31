from bs4 import BeautifulSoup
import requests

def request_to_site(url):
    headers = {
        'accept': '*/*',
         'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    try:
        request = requests.get(url, headers=headers)
        return request.text
    except requests.exceptions.ConnectionError:
        print('Проверьте интернет соедиение')
        exit(1)
 

# Парсим yandex новости по региону
URL_MAIN = 'https://yandex.ru/news'
YAN_DOM = 'https://yandex.ru'


def parse_news(url: str):
    html_doc = request_to_site(url)
    soup = BeautifulSoup(html_doc, 'html.parser')

    # if soup is None:
    #     raise Exception()
    try:
        title_news = soup.findAll('h2', {'class': 'story__title'})  # заголовок и ссылка на новость
        newsdates = soup.find_all('div', attrs={'class': 'story__date'})  # текст, где есть дата
        print(title_news)

    except AttributeError as e:
        print("Нет данных")
        raise e

    # список заголовков
    title_list = [x.find('a').string for x in title_news]

    # выбираем ссылки
    link_list = [x.find('a')['href'] for x in title_news]
    link_list_1 = []  # добавляем домен, где его нет
    for x in link_list:
        if x[:17] != YAN_DOM:
            new_link = YAN_DOM + x
            link_list_1.append(new_link)
        else:
            link_list_1.append(x)