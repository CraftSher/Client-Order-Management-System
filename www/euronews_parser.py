import requests
from bs4 import BeautifulSoup

url = 'https://ru.euronews.com/'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('h2.m-object_title.qa-article-title')

for title in titles:
    text = title.text.strip()
    if text:
        print(text)
    else:
        print("Заголовок пустой")

print(f"Найдено {len(titles)} заголовков")