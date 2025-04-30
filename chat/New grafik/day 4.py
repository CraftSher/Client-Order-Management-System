# import copy
#
# template_site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам [product] недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на [product]',
#             'div': 'Купить',
#             'p': 'Продать'
#         }
#     }
# }
# site_list = []
# count = int(input("Сколько сайтов нужно создать? "))
#
# for i in range(count):
#     product = input(f"Введите название продукта для сайта {i + 1}:")
#     new_site =copy.deepcopy(template_site)
#     new_site['html']['head']['title'] = f'Куплю/продам {product} недорого'
#     new_site['html']['body']['h2'] = f'У нас самая низкая цена на {product}'
#     site_list.append({product: new_site})
#     print("\nТекущие сайты:")
#     for site in site_list:
#         print(site)
#------------------------------------------------------------------------------
# import copy
# template_review_site = {
#     'html': {
#         'head': {
#             'title': 'Отзывы о [product]'
#         },
#         'body': {
#             'h2': 'Что думают о [product] наши клиенты',
#             'ul': ['Отзыв 1', 'Отзыв 2', 'Отзыв 3']
#         }
#     }
# }
#
# site_list = []
# count = int(input("Сколько сайтов нужно создать? "))
# for i in range(count):
#     product = input(f'Введите названия для {i + 1} продукта: ')
#     new_site = copy.deepcopy(template_review_site)
#     new_site['html']['head']['title'] = f'Отзывы о {product}'
#     new_site['html']['body']['h2'] = f'Что думают о {product} наши клиенты'
#     site_list.append({product: new_site})
#     print("\nТекущие сайты:")
#     for site in site_list:
#         print(site)
#------------------------------------------------------------------------------
import copy
# template_review_site = {
#     'html': {
#         'head': {
#             'title': 'Отзывы о [product]'
#         },
#         'body': {
#             'h2': 'Что думают о [product] наши клиенты',
#             'ul': ['Отзыв 1', 'Отзыв 2', 'Отзыв 3']
#         }
#     }
# }
#
# site_list = []
# count = int(input("Сколько сайтов нужно создать? "))
# for i in range(count):
#     product = input(f'Введите названия для {i + 1} продукта: ')
#     reviews = []
#     for j in range(3):
#         review = input(f'Введите отзыв {j + 1} для продукта {product}: ')
#         reviews.append(review)
#     new_site = copy.deepcopy(template_review_site)
#     new_site['html']['head']['title'] = f'Отзывы о {product}'
#     new_site['html']['body']['h2'] = f'Что думают о {product} наши клиенты'
#     new_site['html']['body']['ul'] = reviews
#     site_list.append({product: new_site})
#     print("\nТекущие сайты:")
#     for site in site_list:
#         print(site)
#------------------------------------------------------------------------------
# template_review_site = {
#     'html': {
#         'head': {
#             'title': 'Отзывы о [product]'
#         },
#         'body': {
#             'h2': 'Что думают о [product] наши клиенты',
#             'reviews': [  # список словарей с отзывом и рейтингом
#                 {'text': 'Отзыв 1', 'rating': 5},
#                 {'text': 'Отзыв 2', 'rating': 4},
#                 {'text': 'Отзыв 3', 'rating': 3}
#             ]
#         }
#     }
# }
#
# site_list = []
# count = int(input("Сколько сайтов нужно создать? "))
# for i in range(count):
#     product = input(f'Введите названия для {i + 1} продукта: ')
#     reviews = []
#     for j in range(3):
#         review = input(f'Введите отзыв {j + 1} для продукта {product}: ')
#         rangs = int(input(f'Введите рейтинг {j + 1} для продукта {product}: '))
#         rev_rang = {'text': review, 'rating': rangs}
#         reviews.append(rev_rang)
#     new_site = copy.deepcopy(template_review_site)
#     new_site['html']['head']['title'] = f'Отзывы о {product}'
#     new_site['html']['body']['h2'] = f'Что думают о {product} наши клиенты'
#     new_site['html']['body']['reviews'] = reviews
#     site_list.append({product: new_site})
#     print("\nТекущие сайты:")
#     for site in site_list:
#         print(site)
#------------------------------------------------------------------------------
# import copy
# template_catalog_site = {
#     'html': {
#         'head': {
#             'title': 'Каталог [category]'
#         },
#         'body': {
#             'h2': 'Товары в категории [category]',
#             'products': [  # список товаров
#                 {'name': 'Товар 1', 'price': 10000, 'available': True}
#             ]
#         }
#     }
# }
#
# site_list = []
# count = int(input("Сколько сайтов нужно создать? "))
#
# for i in range(count):
#     categorys = input(f'Введите категорию для {i + 1} продукта: ')
#     products = []
#     for j in range(3):
#         name = input(f'Введите названия для {categorys}: ')
#         price = int(input(f'Введите цену {name}: '))
#         available_input = input(f'Есть {categorys} {name} на складе ДА / НЕТ: ').strip().lower()
#         available = True if available_input == 'да' else False
#         products.append({'name': name, 'price': price, 'available': available})
#     new_site = copy.deepcopy(template_catalog_site)
#     new_site['html']['head']['title'] = f'Каталог {categorys}'
#     new_site['html']['body']['h2'] = f'Товары в категории {categorys}'
#     new_site['html']['body']['products'] = products
#     site_list.append({categorys: new_site})
#     print("\nТекущие сайты:")
#     for site in site_list:
#         print(site)
#------------------------------------------------------------------------------
import copy
# template_catalog_site = {
#   'html': {
#     'head': {'title': 'Каталог Электроника'},
#     'body': {
#       'h2': 'Товары в категории Электроника',
#       'products': [
#         {
#           'name': 'Телевизор',
#           'price': 15000,
#           'available': True,
#           'reviews': [
#             {'text': 'Хорошее качество', 'rating': 5},
#             {'text': 'Быстрая доставка', 'rating': 4}
#           ]
#         },
#         ...
#       ]
#     }
#   }
# }
#
# site_list = []
# count = int(input("Сколько сайтов нужно создать? "))
#
# for i in range(count):
#     categorys = input(f'Введите категорию для {i + 1} продукта: ')
#     products = []
#     for j in range(3):
#         name = input(f'Введите названия для {categorys}: ')
#         price = int(input(f'Введите цену {name}: '))
#         reviews = []
#         for k in range(2):
#             review = input(f'Введите отзыв {k + 1} для продукта {name}: ')
#             raitng = int(input(f'Введите рейтинг {k + 1} для продукта {name}: '))
#             reviews.append({'text': review, 'rating': raitng})
#         available_input = input(f'Есть {categorys} {name} на складе ДА / НЕТ: ').strip().lower()
#         available = True if available_input == 'да' else False
#         products.append({'name': name, 'price': price, 'available': available, 'reviews': reviews})
#     new_site = copy.deepcopy(template_catalog_site)
#     new_site['html']['head']['title'] = f'Каталог {categorys}'
#     new_site['html']['body']['h2'] = f'Товары в категории {categorys}'
#     new_site['html']['body']['products'] = products
#     site_list.append({categorys: new_site})
#     print("\nТекущие сайты:")
#     for site in site_list:
#         print(site)
#------------------------------------------------------------------------------
# template_restaurant_site = {
#     'html': {
#         'head': {'title': 'Ресторан [restaurant_name]'},
#         'body': {
#             'h2': 'Меню ресторана [restaurant_name]',
#             'menu': []  # список блюд
#         }
#     }
# }
#
# site_list = []
# count = int(input("Сколько сайтов нужно создать? "))
#
# for i in range(count):
#     restourant_name = input(f'Введите название для {i + 1} ресторана: ')
#     menu = []
#     for j in range(3):
#         dish_name = input(f'Введите название для {j + 1} блюда: ')
#         dish_price = int(input(f'Введите цену для {j + 1} блюда: '))
#         dish_type = input(f'Блюда вегетарианское (ДА / НЕТ): ').strip().lower()
#         vegan = True if dish_type == 'да' else False
#         menu.append({'name': dish_name, 'price': dish_price, 'vegetarian': vegan})
#     new_site = copy.deepcopy(template_restaurant_site)
#     new_site['html']['head']['title'] = f'Ресторан {restourant_name}'
#     new_site['html']['body']['h2'] = f'Меню ресторана {restourant_name}'
#     new_site['html']['body']['menu'] = menu
#     site_list.append({restourant_name: new_site})
#     print("\nТекущие сайты:")
#     for site in site_list:
#         print(site)
#------------------------------------------------------------------------------
# def print_site_structure(data, indent=0):
#     for key, value in data.items():
#         if isinstance(value, dict):
#             print('  ' * indent + key)
#             print_site_structure(value, indent + 1)  # рекурсивный вызов
#         else:
#             print('  ' * indent + f"{key}: {value}")
#
# site = {
#     'html': {
#         'head': {'title': 'Мой сайт'},
#         'body': {
#             'h1': 'Добро пожаловать',
#             'p': 'Контент'
#         }
#     }
# }
#
# print_site_structure(site)
#------------------------------------------------------------------------------
def print_site_structure(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print('  ' * indent + str(key) + ':')
            print_site_structure(value, indent + 1)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            print('  ' * indent + f"- Элемент {index + 1}:")
            print_site_structure(item, indent + 1)
    else:
        print('  ' * indent + str(data))

site = {
    'html': {
        'head': {
            'title': 'Отзывы о телефоне'
        },
        'body': {
            'h2': 'Мнения покупателей',
            'reviews': [
                {'text': 'Отличный товар', 'rating': 5},
                {'text': 'Нормально, но дорого', 'rating': 3}
            ]
        }
    }
}

print_site_structure(site)