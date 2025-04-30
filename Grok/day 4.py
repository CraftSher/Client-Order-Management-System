# items = ['хлеб', 'молоко', 'яйца', 'мясо', 'макароны']
# for i in range(len(items)):
#     print(f'{i+1}. {items[i]}')

# shopping_dict = {'хлеб': 2, 'молоко': 1, 'яйца': 10}
# for key, value in shopping_dict.items():
#     print(f'Продукт: {key}, {value}')

items = ['хлеб', 'молоко', 'яйца', 'мясо', 'макароны']
items1 = ['чай', 'сахар', 'капуста']
items.extend(items1)
print(items)
shopping_dict = {'хлеб': 2, 'молоко': 1, 'яйца': 10}
for product in items:
    if product not in shopping_dict:
        shopping_dict[product] = 5

for key, value in shopping_dict.items():
    print(f'Продукт: {key}, количество: {value}')

new_product = []
for product in items:
    if len(product) > 4:
        new_product.append(product)
print(new_product)
summa = sum(shopping_dict.values())
print(summa)