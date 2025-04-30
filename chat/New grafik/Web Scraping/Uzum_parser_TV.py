import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Путь к драйверу (например, chromedriver)
driver = webdriver.Chrome()

# Открытие страницы
driver.get('https://uzum.uz')

# Печать исходного HTML, чтобы проверить структуру
print(driver.page_source)

# Подождите, пока загрузятся карточки товаров
WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#category-products > div'))
)

# Прокручиваем страницу вниз до конца
for _ in range(3):  # Прокручиваем несколько раз
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Подождите, пока элементы загрузятся

# Повторно проверяем наличие всех карточек
elements = WebDriverWait(driver, 60).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#category-products > div'))
)
driver.execute_script("arguments[0].scrollIntoView();", elements[0])

# Найдите все карточки товара
cards = driver.find_elements(By.CSS_SELECTOR, '#category-products > div')

# Проход по карточкам
for card in cards:
    try:
        # Извлекаем подзаголовок товара
        subtitle = card.find_element(By.CSS_SELECTOR, 'div.subtitle.slightly.regular.small-semi-bold').text

        # Извлекаем дополнительную информацию (например, оценку или отзыв)
        additional_info = card.find_element(By.CSS_SELECTOR, 'div:nth-child(4) > div > div > div > span').text

        # Извлекаем цену товара
        price = card.find_element(By.CSS_SELECTOR,
                                  'div.product-card-main-info-wrapper > div > span.currency.product-card-price.slightly.medium').text

        # Печатаем информацию о товаре
        print(f'Подзаголовок: {subtitle}')
        print(f'Дополнительная информация: {additional_info}')
        print(f'Цена: {price}')
        print('---')
    except Exception as e:
        print(f'Ошибка при извлечении данных: {e}')

# Закрытие браузера
driver.quit()
