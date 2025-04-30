import requests
import schedule
import time
from telegram import Bot
from datetime import datetime
import asyncio

TELEGRAM_TOKEN = "7513671181:AAGGMYYPtVHTtz6FkA3vvKdFhU60s_WfqzQ"
CHAT_ID = "3520675"
bot = Bot(token=TELEGRAM_TOKEN)
today = datetime.now().strftime("%Y-%m-%d")
URL = f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/all/{today}/"


def fetch_currency_rates():
    today = datetime.now().strftime("%Y-%m-%d")
    URL = f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/all/{today}/"
    response = requests.get(URL, timeout=10)
    if response.status_code != 200:
        return "Ошибка получения данных"

    data = response.json()
    needed = ['USD', 'EUR', 'RUB']
    lines = []

    for currency in data:
        code = currency['Ccy']
        if code in needed:
            name = currency['CcyNm_UZ']
            date = currency['Date']
            rate = currency['Rate']
            lines.append(f"{code} ({name}): {rate} сум - {date}")

    return "\n".join(lines)


async def send_rates():
    rates_text = fetch_currency_rates()
    await bot.send_message(chat_id=CHAT_ID, text=rates_text)


def job():
    asyncio.run(send_rates())


# Запланировать на каждый день в 08:00
schedule.every().day.at("09:00").do(job)

print("Бот запущен и будет отправлять курсы каждый день в 09:00.")

while True:
    schedule.run_pending()
    time.sleep(30)
def job_send_rates():
    text = fetch_currency_rates()
    if text:
        bot.send_message(chat_id=CHAT_ID, text=text)

# Запуск разовой проверки
if __name__ == "__main__":
    print(fetch_currency_rates())

    # А теперь планирование на каждый день в 09:00
    schedule.every().day.at("09:00").do(job_send_rates)
    while True:
        schedule.run_pending()
        time.sleep(30)

