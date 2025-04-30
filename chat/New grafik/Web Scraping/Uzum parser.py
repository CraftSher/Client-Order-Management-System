import requests
from bs4 import BeautifulSoup

url = 'https://uzum.uz/uz/search?query=televizor&needsCorrection=1'
headers = {"User-Agent": "Mozila/5.0"}
response = requests.get(url, headers=headers)

print("Статус:", response.status_code)
print("HTML длина:", len(response.text))

soup = BeautifulSoup(response.text, 'html.parser')
cards = soup.find_all('div', attrs={"data-test-id": "product-card"})

print(f"Найдено карточек: {len(cards)}")