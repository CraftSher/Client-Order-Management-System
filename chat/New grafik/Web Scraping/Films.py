import requests
from bs4 import BeautifulSoup

url = "https://www.kinopoisk.ru/lists/movies/top250/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Найди все карточки фильмов
films = soup.find_all('div', class_="desktop-list-main-info")

for film in films[:10]:  # первые 10 фильмов
    # 1. Название
    name = film.find('span', class_="styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj").text.strip()

    # 2. Год
    year_text = film.find('span', class_="desktop-list-main-info_secondaryText__M_aus").text.strip()
    year = year_text.split(",")[1].strip()  # Получаем только год

    # 3. Рейтинг
    rating = film.find('span', class_="styles_kinopoiskValuePositive__7AAZG").text.strip()

    print(f"Название: {name}")
    print(f"Год: {year}")
    print(f"Рейтинг: {rating}")
    print()

print(soup.prettify())