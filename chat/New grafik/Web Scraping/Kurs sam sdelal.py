import requests
import csv
import sys
import os

# Добавляем путь к папке 'Config', где хранится config.py
sys.path.append(r'C:\Users\Admin\PycharmProjects\PythonProject\Config')

# Импортируем api_key из файла config.py
from config import api_key


# Функция для получения и сохранения курсов валют
def fetch_currency_rates():
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&base=EUR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Получаем валюты и курсы
        rates = data['rates']

        # Запись данных в CSV файл
        with open('currency_rates.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Currency', 'Rate'])  # Заголовки

            # Записываем все валюты и курсы в файл
            for currency, rate in rates.items():
                writer.writerow([currency, rate])

        print("Данные успешно сохранены в 'currency_rates.csv'")
    else:
        print("Ошибка при запросе данных. Пожалуйста, проверьте API ключ и интернет-соединение.")


# Вызов функции
fetch_currency_rates()