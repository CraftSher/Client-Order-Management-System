def get_low_stock(products):
    threshold = int(input('Введите количество: '))
    for name, value in products.items():
        if products[name] <= threshold:
            print(f'Товары с количеством меньше чем указанный порог {name}: {products[name]}')

def remove_product(products):
    name = input('Введите названия фрукта: ')
    amount = int(input('Введите количество: '))
    if name in products:
        if products[name] >= amount:
            products[name] -= amount
            print(f'Обновленный список фруктов {products}')
            return products
        else:
            print('Не достаточное количество фрукта на складе!!!')
            return products
    else:
        print('Такого фрукта нет на складе. ')
        return products

def add_product(products):
    fruit = input('Введите названия фрукта: ')
    quantity = int(input('Введите количество: '))
    if fruit in products:
        products[fruit] += quantity
        print(f'Обновленный список фруктов {products}')
        return products
    else:
        print('Такого фрукта нет на складе. ')
        return products

def show_products():
    for fruit, value in products.items():
        print(fruit, ':', value)
products = {
    "apple": 20,
    "banana": 35,
    "orange": 50,
    "grape": 40,
    "watermelon": 15
}
for name, quantity in products.items():
    print(name, ':', quantity)
while True:
    question = input('Выберите действие: \n1 - Показать продукты,\n2 - Добавить товар, \n3 - Удалить товар, \n4 - Показать товар с низким остатком, \n0 - Выйти \n')
    if question == '1':
        result = show_products()
    elif question == '2':
        result1 = add_product(products)
    elif question == '3':
        result2 = remove_product(products)
    elif question == '4':
        result3 = get_low_stock(products)
    elif question == '0':
        print('Счастливого дня!!!')
        break
    else:
        print('Не правильно выбранное действие!!!')




