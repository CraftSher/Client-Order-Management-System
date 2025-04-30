from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext
import re
from deep_translator import GoogleTranslator
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
import requests

# Здесь ваш токен бота
TOKEN = '7272092020:AAEThVo04XManuCReraGLTP3v3aXZBMh250'

# Состояния для ConversationHandler
CITY = 1


# Функция для команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Я твой Telegram бот. Напиши /help для помощи.')


# Функция для команды /help
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start - Приветствие\n"
        "/currency - Курс валюты\n"
        "/weather - Узнать погоду в городе\n"
    )


# Функция для команды /weather
async def weather(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Введите название города, чтобы узнать погоду:')
    return CITY


async def get_weather(update: Update, context: CallbackContext) -> int:
    city = update.message.text.strip()

    try:
        # Перевод города на английский язык
        translator = GoogleTranslator(source='auto', target='en')
        city_en = translator.translate(city).strip()

        # Иногда перевод добавляет странные символы, убираем лишнее
        city_en = city_en.replace(",", "").replace(".", "").strip()
    except Exception as e:
        await update.message.reply_text(
            "Ошибка при переводе. Пожалуйста, попробуйте написать город на английском языке."
        )
        return CITY

    api_key = "039f27c91fba50c6551b50033c18b077"  # Замени на свой настоящий API-ключ!
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_en}&appid={api_key}&units=metric&lang=ru'

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            await update.message.reply_text(
                f"Не удалось найти информацию о городе {city} ({city_en}). Проверьте правильность написания."
            )
            return CITY

        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        await update.message.reply_text(
            f"Погода в {city}:\nТемпература: {temperature}°C\nОписание: {description}"
        )
        return ConversationHandler.END

    except Exception as e:
        await update.message.reply_text(
            "Произошла ошибка при получении данных о погоде. Попробуйте ещё раз."
        )
        return ConversationHandler.END


# Функция для отмены команды
async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Отменено. Для начала используйте команду /start')
    return ConversationHandler.END


# Основная функция, которая запускает бота
def main():
    # Создаем объект Application с твоим токеном
    application = Application.builder().token(TOKEN).build()

    # Создаем ConversationHandler для погоды
    weather_handler = ConversationHandler(
        entry_points=[CommandHandler('weather', weather)],
        states={
            CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_weather)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(weather_handler)

    # Запуск бота
    application.run_polling()


if __name__ == "__main__":
    main()