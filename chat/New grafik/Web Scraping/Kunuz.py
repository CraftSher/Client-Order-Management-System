import requests
from bs4 import BeautifulSoup
import time
import csv

base_url = "https://kun.uz"
response = requests.get(base_url)

# Проверяем, удалось ли загрузить страницу
if response.status_code != 200:
    print(f"Ошибка при загрузке страницы: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("a", class_="small-cards__default-text")

news_data = []

# Пытаемся парсить каждый заголовок, ссылки и информацию
for a in titles:
    title = a.text.strip()
    link = base_url + a['href']

    # Переход на внутреннюю страницу
    try:
        inner_response = requests.get(link)
        if inner_response.status_code != 200:
            print(f"Ошибка при загрузке страницы: {inner_response.status_code}")
            continue
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        continue

    inner_soup = BeautifulSoup(inner_response.text, "html.parser")

    stats_div = inner_soup.find("div", class_="news-inner__content-stats")

    if stats_div:
        spans = stats_div.find_all("span")
        if len(spans) >= 3:
            full_date = spans[0].text.strip()
            views = spans[1].text.strip()
            read_time = spans[2].text.strip()
        else:
            full_date = "Дата не найдена"
            views = "Просмотры не найдены"
            read_time = "Время чтения не найдено"
    else:
        full_date = "Дата не найдена"
        views = "Просмотры не найдены"
        read_time = "Время чтения не найдено"

    news_data.append([title, link, full_date, views, read_time])

    print(f"Добавлено: {title}")
    time.sleep(1)  # Пауза между запросами

# Сохраняем данные в CSV
with open("kunuz_news.csv", mode="w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Заголовок", "Ссылка", "Дата публикации", "Просмотры", "Время чтения"])
    writer.writerows(news_data)

print("Все данные сохранены в kunuz_news.csv")