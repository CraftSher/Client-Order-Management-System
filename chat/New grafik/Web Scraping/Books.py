import requests
from bs4 import BeautifulSoup

def scrape_books():
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    page = 1

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
            price = book.select_one('.price_color').text.strip()
            availability = book.select_one('.availability').text.strip()
            rating_class = book.select_one('p.star-rating')['class']
            rating = rating_class[1] if len(rating_class) > 1 else 'Unknown'

            print(f'Название: {title}')
            print(f'Цена: {price}')
            print(f'Наличие: {availability}')
            print(f'Рейтинг: {rating}')
            print('---')

        page += 1

scrape_books()