# from bs4 import BeautifulSoup
#
# html = """
# <html>
#   <body>
#     <div class="news">
#       <h2>Заголовок 1</h2>
#       <p class="date">2025-04-22</p>
#       <a href="/news/1">Читать далее</a>
#     </div>
#     <div class="news">
#       <h2>Заголовок 2</h2>
#       <p class="date">2025-04-21</p>
#       <a href="/news/2">Читать далее</a>
#     </div>
#   </body>
# </html>
# """
#
# soup = BeautifulSoup(html, 'html.parser')
#
# # Найдём все блоки с новостями
# news_blocks = soup.find_all('div', class_='news')
#
# # Пройдёмся по каждой новости и выведем заголовок, дату и ссылку
# for block in news_blocks:
#     title = block.find('h2').text
#     date = block.find('p', class_='date').text
#     link = block.find('a')['href']
#     print(f"{date} | {title} | Ссылка: {link}")

# ========================================================================

import csv
import json
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <div class="article" data-id="101">
      <h2 class="title">Python для начинающих</h2>
      <div class="meta">
        <span class="author">Иван Петров</span>
        <span class="date">2025-04-22</span>
      </div>
      <a href="/articles/101">Читать</a>
    </div>
    <div class="article" data-id="102">
      <h2 class="title">Парсинг HTML на Python</h2>
      <div class="meta">
        <span class="date">2025-04-20</span>
        <span class="author">Мария Сидорова</span>
      </div>
      <a href="/articles/102">Читать</a>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
articles = soup.find_all('div', class_='article')

results = []

for article in articles:
    title = article.find('h2', class_='title').text
    author = article.find('span', class_='author').text
    date = article.find('span', class_='date').text
    link = article.find('a')['href']
    if date == '2025-04-22':
        results.append({
            'title': title,
            'author': author,
            'date': date,
            'link': link
        })

# Сохраняем в JSON-файл
with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# Сохраняем в CSV
with open('articles.csv', 'w', encoding='utf-8', newline='') as f_csv:
    writer = csv.DictWriter(f_csv, fieldnames=['title', 'author', 'date', 'link'])
    writer.writeheader()
    writer.writerows(results)

print("Данные сохранены в articles.json и articles.csv")