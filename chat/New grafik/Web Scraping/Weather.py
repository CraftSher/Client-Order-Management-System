import requests

API_KEY = "c550cb15bd632560e1a42c8602397f0e"  # Убедитесь, что пробела в конце нет
CITY = 'Ташкент, УЗ'  # Укажите город с кодом страны
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if data['cod'] == 200:
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    print(f"Weather in {CITY}: {temperature}°C, {description}, Humidity: {humidity}%")
else:
    print(f"Error: {data['cod']} - {data.get('message', 'Unknown error')}")