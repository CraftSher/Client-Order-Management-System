from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Используем webdriver_manager для автоматической установки и использования ChromeDriver
service = Service(ChromeDriverManager().install())

# Открываем браузер через Selenium
driver = webdriver.Chrome(service=service)

# Загружаем страницу
url = "https://qalampir.uz/"
driver.get(url)

# Даем странице время на загрузку
driver.implicitly_wait(10)

# Получаем HTML-код страницы
html = driver.page_source

# Закрываем браузер
driver.quit()

# Теперь парсим страницу с помощью BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Находим все элементы новостей
news_items = soup.find_all('a', class_='carousel-caption-content-item')

if not news_items:
    print("Не найдены новости на странице.")
else:
    # Для каждой новости получаем заголовок, дату и ссылку
    for item in news_items:
        title = item.find('p', class_='carousel-caption-content-item-title').get_text(strip=True)
        date = item.find('p', class_='carousel-caption-content-item-date').get_text(strip=True)
        link = item.get('href')

        print(f"Заголовок: {title}")
        print(f"Дата: {date}")
        print(f"Ссылка: {link}")

        # Ищем изображение (если оно есть)
        img_tag = item.find('img')
        if img_tag:
            img_src = img_tag.get('src')
            print(f"Изображение: {img_src}")

        print('-' * 40)