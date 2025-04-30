import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "https://www.ozon.ru"
products_data = []
page_number = 1

# Добавляем headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9",
}

while True:
    page_url = f"https://www.ozon.ru/category/zdorove-i-krasota-15150/?page={page_number}"
    response = requests.get(page_url, headers=headers)  # добавили headers здесь
    soup = BeautifulSoup(response.text, "html.parser")

    print(f"Парсинг страницы {page_number}...")  # отладка
    print(soup.prettify()[:1000])  # показать часть HTML для проверки

    items = soup.find_all("div", class_="b5v3 b5v4 b5v5")  # Возможно, тут класс нужно будет поменять

    if not items:
        print("Товары не найдены на странице", page_number)
        break

    for item in items:
        title = item.find("span", class_="b5v7")
        price = item.find("span", class_="b5v9")
        link_tag = item.find("a", class_="b5v6")

        if title and price and link_tag:
            link = link_tag["href"]
            product = {
                "title": title.text.strip(),
                "price": price.text.strip(),
                "link": base_url + link
            }
            products_data.append(product)
            print(f"Добавлено: {product['title']}")

    page_number += 1
    time.sleep(1)

# Сохраняем в CSV
with open("ozon_health_products.csv", mode="w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Link"])
    for product in products_data:
        writer.writerow([product["title"], product["price"], product["link"]])

print("Данные сохранены в ozon_health_products.csv")