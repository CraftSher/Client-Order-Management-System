goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
total_quantity = 0
total_price = 0

for item_name, code in goods.items():
    if code in store:
        for item_data in store[code]:
            quantity = item_data['quantity']
            price = item_data['price']
            total_price += quantity * price
            total_quantity += quantity
        print(f'{item_name} — {total_quantity} штук, стоимость {total_price} рублей')


