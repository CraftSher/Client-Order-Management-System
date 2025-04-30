# import requests
# from bs4 import BeautifulSoup
#
# url = "https://kun.uz"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# articles = soup.find_all('div', class_='col-lg-6 col-md-6 col-sm-12')
#
# for article in articles:
#     title = article.find('a', class_= 'card-title')
#     link = article.find('a', class_= 'card-title')['href']
#
#     if title and link:
#         print(f'Заголовок: {title.text.strip()}')
#         print(f'Ссылка: {url}{link}')
#         print('-' * 50)

import requests
from bs4 import BeautifulSoup

url = "https://kun.uz"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Печатаем весь HTML-код, чтобы понять его структуру
print(soup.prettify()[:1000])  # выводим первые 1000 символов страницы для анализа

# Пробуем найти элементы с новостями
articles = soup.find_all('div', class_='col-lg-6 col-md-6 col-sm-12')

# Печатаем найденные элементы для отладки
print(f'Найдено {len(articles)} статей')

# Печатаем информацию о первых нескольких статьях
for article in articles[:3]:  # выводим только первые 3 статьи для проверки
    print(article.prettify())