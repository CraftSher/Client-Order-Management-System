# def print_items(products):
#    for i in range(len(products)):
#       print(f'{i + 1}. {products[i]}')
#
# items = ['хлеб', 'молоко', 'яйца', 'мясо', 'чай', 'сахар', 'капуста']
# print_items(items)
from tkinter.font import names


def print_shopping_dict(products):
    for name, product in products.items():
        print(f'Продукт: {name}, Количество: {product}')

shopping_dict = {'хлеб': 2, 'молоко': 1, 'яйца': 10}
print_shopping_dict(shopping_dict)