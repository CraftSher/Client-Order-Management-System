import requests

url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    needed = ['USD', 'EUR', 'RUB']
    with open('Valyuta_kurslari.txt', 'w', encoding= 'utf-8') as file:
        for currency in data:
            code = currency['Ccy']
            if code in needed:
                name = currency['CcyNm_UZ']
                date = currency['Date']
                rate = currency['Rate']
                line = f"{code} ({name}): {rate} сум - {date}\n"
                print(line.strip())
                file.write(line)
else:
    print("Ошибка запроса:", response.status_code)
