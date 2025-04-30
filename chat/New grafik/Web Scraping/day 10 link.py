import requests
from bs4 import BeautifulSoup
import csv

url = "https://kun.uz/news/category/jahon"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    news_block = soup.find("div", class_="news-page__list")

    if news_block:
        articles = news_block.find_all("a", class_="news-page__item")

        if articles:
            for article in articles:
                title = article.find("h3", class_="news-page__item-title")
                if title:
                    title = title.text.strip()
                else:
                    title = "Нет заголовка"

                link = "https://kun.uz" + article.get("href")

                time = article.find("div", class_="gray-date")
                if time:
                    time = time.text.strip()
                else:
                    time = "Нет времени"

                image = article.find("img")
                if image:
                    image = image.get("src")
                else:
                    image = "Нет изображения"

                # Вывод информации
                print(f"Время: {time}")
                print(f"Заголовок: {title}")
                print(f"Ссылка: {link}")
                print(f"Картинка: {image}")
                print("-" * 50)
        else:
            print("Статьи не найдены.")
    else:
        print("Блок с новостями не найден.")
else:
    print(f"Ошибка при запросе: {response.status_code}")

# Открываем CSV файл для записи
with open('news.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Записываем заголовки
    writer.writerow(["Время", "Заголовок", "Ссылка", "Картинка"])

    for article in articles:
        title = article.find("h3", class_="news-page__item-title")
        if title:
            title = title.text.strip()
        else:
            title = "Нет заголовка"

        link = "https://kun.uz" + article.get("href")

        time = article.find("div", class_="gray-date")
        if time:
            time = time.text.strip()
        else:
            time = "Нет времени"

        image = article.find("img")
        if image:
            image = image.get("src")
        else:
            image = "Нет изображения"

        # Записываем данные
        writer.writerow([time, title, link, image])

print("Данные успешно сохранены в 'news.csv'")