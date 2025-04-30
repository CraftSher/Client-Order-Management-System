import requests
from bs4 import BeautifulSoup
import csv

def scrape_books():
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    page = 1
    target_title = "Ol"   # Название или его часть

    # Список для хранения найденных книг
    found_books = []

    while True:
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            print(f'Завершено. Последняя доступная страница: {page - 1}')
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.select('article.product_pod')

        if not books:
            print('Книги не найдены на странице.')
            break

        print(f'\n=== Страница {page} ===')

        for book in books:
            title = book.h3.a['title']
            if target_title.lower() in title.lower():  # Поиск подстроки без учета регистра
                price = book.select_one('.price_color').text.strip()
                availability = book.select_one('.availability').text.strip()
                rating_class = book.select_one('p.star-rating')['class']
                rating = rating_class[1] if len(rating_class) > 1 else 'Unknown'

                # Добавляем книгу в список найденных
                found_books.append({
                    'title': title,
                    'price': price,
                    'availability': availability,
                    'rating': rating
                })

        page += 1

    # Если книги найдены, сохраняем их в CSV
    if found_books:
        with open('found_books.csv', mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Цена', 'Наличие', 'Рейтинг'])  # Заголовки
            for book in found_books:
                writer.writerow([book['title'], book['price'], book['availability'], book['rating']])

        print(f'Найдено {len(found_books)} книг. Данные сохранены в "found_books.csv".')
    else:
        print('Книги не найдены.')

scrape_books()