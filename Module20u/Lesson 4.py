# scores_dict = {'Ваня':33, 'Петя': 60, 'Лена': 45}
#
# for key, score in scores_dict.items():
#     print(key, ':', score)

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

for i_title, i_code in goods.items():
    total_quantity = 0
    total_cost = 0
    for j_good in store[i_code]:
        total_quantity += j_good['quantity']
        total_cost += j_good['price'] * j_good['quantity']
    print(f'{i_title} - {j_good['quantity']} шт, стоимость {total_cost} рублей')