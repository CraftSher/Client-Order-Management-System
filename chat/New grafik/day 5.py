# def find_reviews(data):
#     found = []
#     if isinstance(data, dict) and 'text' in data and 'rating' in data:
#         found.append(data)
#     elif isinstance(data, dict):
#         for value in data.values():
#             found += find_reviews(value)
#     elif isinstance(data, list):
#         for item in data:
#             found += find_reviews(item)
#     return found
#
#     # Твоя рекурсивная логика будет здесь
#
#     return found
#
# site_list = [
#     {
#         'Smartphone': {
#             'html': {
#                 'head': {'title': 'Отзывы о Smartphone'},
#                 'body': {
#                     'h2': 'Что думают о Smartphone наши клиенты',
#                     'reviews': [
#                         {'text': 'Хороший телефон', 'rating': 5},
#                         {'text': 'Батарея слабая', 'rating': 3}
#                     ]
#                 }
#             }
#         }
#     },
#     {
#         'Laptop': {
#             'html': {
#                 'head': {'title': 'Отзывы о Laptop'},
#                 'body': {
#                     'h2': 'Что думают о Laptop наши клиенты',
#                     'reviews': [
#                         {'text': 'Мощный и лёгкий', 'rating': 4},
#                         {'text': 'Экран тусклый', 'rating': 2}
#                     ]
#                 }
#             }
#         }
#     }
# ]
#
# reviews = find_reviews(site_list)
# for review in reviews:
#     print(review)

#--------------------------------------------------------------------
# def print_reviews(data):
#     if isinstance(data, dict):
#         for key, value in data.items():
#             print_reviews(value)  # рекурсивный вызов
#     elif isinstance(data, list):
#         for item in data:
#             print_reviews(item)
#     else:
#         return  # если это не список и не словарь — игнорируем

# def find_and_print_reviews(data):
#     if isinstance(data, dict):
#         if 'name' in data and 'reviews' in data:
#             print(f"\nПродукт: {data['name']}")
#             for review in data['reviews']:
#                 print(f"  Отзыв: {review['text']} — Рейтинг: {review['rating']}")
#         else:
#             for value in data.values():
#                 find_and_print_reviews(value)
#     elif isinstance(data, list):
#         for item in data:
#             find_and_print_reviews(item)
#
#
# site = {
#     'html': {
#         'body': {
#             'products': [
#                 {
#                     'name': 'Телевизор',
#                     'reviews': [
#                         {'text': 'Хорошее качество', 'rating': 5},
#                         {'text': 'Доставка быстро', 'rating': 4}
#                     ]
#                 },
#                 {
#                     'name': 'Пылесос',
#                     'reviews': [
#                         {'text': 'Мощный', 'rating': 5},
#                         {'text': 'Шумный', 'rating': 3}
#                     ]
#                 }
#             ]
#         }
#     }
# }
#
# # Запуск
# find_and_print_reviews(site)

#--------------------------------------------------------------------
# def summ_digit(data):
#     total_sum = 0
#     if isinstance(data, dict):
#         for key, value in data.items():
#             total_sum += summ_digit(value)
#     elif isinstance(data, list):
#         for item in data:
#             total_sum += summ_digit(item)
#     elif isinstance(data, (int, float)):
#             total_sum += data
#     return total_sum
#
# data = {
#     "a": 1,
#     "b": {
#         "c": 2,
#         "d": {
#             "e": 3,
#             "f": 4
#         }
#     },
#     "g": [5, 6, {"h": 7, "i": 8}],
# }
# digit = summ_digit(data)
# print(digit)

#--------------------------------------------------------------------
# def print_info_report(data):
#     if isinstance(data, dict):
#         # Если это словарь, проверим наличие имени и комментариев
#         if 'name' in data and 'comments' in data:
#             name = data['name']
#             for comment in data['comments']:
#                 comment_text = comment['comment']
#                 date = comment['date']
#                 print(f"{name}: {comment_text} - {date}")
#         # Если это вложенные словари, вызываем рекурсивно
#         else:
#             for key, value in data.items():
#                 print_info_report(value)
#     elif isinstance(data, list):
#         # Если это список, рекурсивно обрабатываем каждый элемент
#         for item in data:
#             print_info_report(item)
#
# data = {
#     "user1": {
#         "name": "Alice",
#         "comments": [
#             {"comment": "Great job!", "date": "2025-04-01"},
#             {"comment": "Very helpful, thanks!", "date": "2025-04-02"}
#         ]
#     },
#     "user2": {
#         "name": "Bob",
#         "comments": [
#             {"comment": "Nice work!", "date": "2025-04-03"},
#             {"comment": "Could use some improvements.", "date": "2025-04-04"}
#         ]
#     }
# }
#
# print_info_report(data)

#--------------------------------------------------------------------

# def print_num(data):
#     if isinstance(data, dict):
#         for key, value in data.items():
#             value = print_num(value)
#     elif isinstance(data, list):
#         for item in data:
#             item = print_num(item)
#     elif isinstance(data, (int, float)):
#             print(data, end= ': ')
#
# data = {
#     "a": 1,
#     "b": {
#         "c": 2,
#         "d": {
#             "e": 3,
#             "f": 4
#         }
#     },
#     "g": [5, 6, {"h": 7, "i": 8}],
# }
# print_num(data)
#--------------------------------------------------------------------
# def cheaper_find(data):
#     min_value = float('inf')
#     min_name = ""
#
#     if isinstance(data, dict):
#         # Если это товар с ценой
#         if "price" in data and "name" in data:
#             return data["name"], data["price"]
#         for key, value in data.items():
#             name, price = cheaper_find(value)
#             if price < min_value:
#                 min_value = price
#                 min_name = name
#     elif isinstance(data, list):
#         for item in data:
#             name, price = cheaper_find(item)
#             if price < min_value:
#                 min_value = price
#                 min_name = name
#
#     return min_name, min_value
#
# catalog = {
#     "Electronics": {
#         "Laptops": [
#             {"name": "Laptop A", "price": 1000},
#             {"name": "Laptop B", "price": 1500},
#         ],
#         "Phones": [
#             {"name": "Phone A", "price": 800},
#             {"name": "Phone B", "price": 1200},
#         ]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [
#             {"name": "Vacuum A", "price": 200},
#             {"name": "Vacuum B", "price": 250},
#         ],
#         "Microwaves": [
#             {"name": "Microwave A", "price": 100},
#             {"name": "Microwave B", "price": 150},
#         ]
#     }
# }
#
# # ВАЖНО: вызываем функцию и сохраняем результат
# name, price = cheaper_find(catalog)
#
# # Печатаем результат
# print(f"The cheapest item is {name} with price {price}")
#--------------------------------------------------------------------
# def count_products(data):
#     count = 0
#     if isinstance(data, dict):
#         if 'price' in data:
#             count += 1
#         else:
#             for value in data.values():
#                 count += count_products(value)
#     elif isinstance(data, list):
#         for item in data:
#             count += count_products(item)
#     return count
#
#
# catalog = {
#     "Electronics": {
#         "Laptops": [
#             {"name": "Laptop A", "price": 1000},
#             {"name": "Laptop B", "price": 1500},
#         ],
#         "Phones": [
#             {"name": "Phone A", "price": 800},
#             {"name": "Phone B", "price": 1200},
#         ]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [
#             {"name": "Vacuum A", "price": 200},
#             {"name": "Vacuum B", "price": 250},
#         ],
#         "Microwaves": [
#             {"name": "Microwave A", "price": 100},
#             {"name": "Microwave B", "price": 150},
#         ]
#     }
# }
#
# price = count_products(catalog)
# print(price)
#--------------------------------------------------------------------
# def count_products(data):
#     total_price = 0
#     count = 0
#     if isinstance(data, dict):
#         if 'price' in data:
#             total_price += data['price']
#             count += 1
#         else:
#             for value in data.values():
#                 sub_price, sub_count = count_products(value)
#                 total_price += sub_price
#                 count += sub_count
#     elif isinstance(data, list):
#         for item in data:
#             sub_price, sub_count = count_products(item)
#             count += sub_count
#             total_price += sub_price
#     return total_price, count
#
# catalog = {
#     "Electronics": {
#         "Laptops": [
#             {"name": "Laptop A", "price": 1000},
#             {"name": "Laptop B", "price": 1500},
#         ],
#         "Phones": [
#             {"name": "Phone A", "price": 800},
#             {"name": "Phone B", "price": 1200},
#         ]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [
#             {"name": "Vacuum A", "price": 200},
#             {"name": "Vacuum B", "price": 250},
#         ],
#         "Microwaves": [
#             {"name": "Microwave A", "price": 100},
#             {"name": "Microwave B", "price": 150},
#         ]
#     }
# }
# price = count_products(catalog)
# print(price)
#--------------------------------------------------------------------
def find_expensive(catalog, price_limit):
    expensive_good = []
    if isinstance(catalog, dict):
        if 'price' in catalog:
            if price_limit  < catalog['price']:
                result = (catalog['name'], catalog['price'])
                expensive_good.append(result)
        else:
            for value in catalog.values():
                expensive_good.extend(find_expensive(value, price_limit))
    elif isinstance(catalog, list):
        for item in catalog:
            expensive_good.extend(find_expensive(item, price_limit))
    return expensive_good

catalog = {
    "Electronics": {
        "Laptops": [
            {"name": "Laptop A", "price": 1000},
            {"name": "Laptop B", "price": 1500},
        ],
        "Phones": [
            {"name": "Phone A", "price": 800},
            {"name": "Phone B", "price": 1200},
        ]
    },
    "Home Appliances": {
        "Vacuum Cleaners": [
            {"name": "Vacuum A", "price": 200},
            {"name": "Vacuum B", "price": 250},
        ],
        "Microwaves": [
            {"name": "Microwave A", "price": 100},
            {"name": "Microwave B", "price": 150},
        ]
    }
}
prices = find_expensive(catalog, 1000)
for name, price in prices:
    print(f'{name} - {price}')