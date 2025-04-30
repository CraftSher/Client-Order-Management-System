import requests

TOKEN = '7513671181:AAGGMYYPtVHTtz6FkA3vvKdFhU60s_WfqzQ'
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(url)
print(response.json())