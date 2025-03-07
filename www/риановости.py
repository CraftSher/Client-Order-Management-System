from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://ria.ru/'

# Инициализируем браузер
driver = webdriver.Chrome() # Убедитесь, что у вас установлен ChromeDriver
driver.get(url)

# Получаем HTML-код страницы после загрузки JavaScript
html = driver.page_source

# Закрываем браузер
driver.quit()

# Парсим HTML-код с помощью Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('span.cell-list_item-title')

for title in titles:
    text = title.text.strip()
    if text:
        print(text)
    else:
        print("Заголовок пустой")

print(f"Найдено {len(titles)} заголовков")
