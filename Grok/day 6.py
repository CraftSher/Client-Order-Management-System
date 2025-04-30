def check_product(name, amount):
    if name not in shopping_dict:
        print('Продукта нет в запасах!')
    else:
        check_stock(amount)

def check_stock(amount):
    if amount > 5:
        print('Запас большой.')
    elif 2 < amount <= 5:
        print('Запас нормальный.')
    else:
        print('Пора докупить!!!')

shopping_dict = {'хлеб': 2, 'молоко': 1, 'яйца': 10}
name = input('Введите наименование продукта: ')
amount = int(input('Введите количество запасов: '))
check_product(name, amount)

