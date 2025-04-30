import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_cbu_rates():
    """Парсим курсы валют с сайта ЦБ Узбекистана"""
    url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


if __name__ == "__main__":
    print("Получаем курсы валют...")
    rates = get_cbu_rates()

    if rates:
        for curr in rates:
            if curr['Ccy'] in ['USD', 'EUR', 'RUB']:
                print(f"{curr['CcyNm_RU']}: {curr['Rate']} сум")

