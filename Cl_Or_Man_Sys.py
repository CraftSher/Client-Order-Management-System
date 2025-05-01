def new_clients(orders):
    """Функция добавления нового заказа."""
    name = input('Введите имя клиента: ').title()
    product_name = input('Введите наименование продукта: ').title()
    try:
        product_quantity = int(input('Введите количество товара: '))
    except ValueError:
        print('Ошибка: количество товара должно быть числом.')
        return

    new_order = {
        'client': name,
        'product': productcd_name,
        'quantity': product_quantity
    }

    orders.append(new_order)
    print(f'Новый заказ добавлен: {new_order}')
    print(f'Обновлённый список заказов:')
    display_orders(orders)


def max_client(orders):
    """Функция для поиска клиента с наибольшими заказами."""
    client_totals = {}
    for order in orders:
        client = order['client']
        quantity = order['quantity']
        if client in client_totals:
            client_totals[client] += quantity
        else:
            client_totals[client] = quantity

    max_quantity = max(client_totals.values())
    max_client = [client for client, total in client_totals.items() if total == max_quantity]
    print(f'Клиенты с наибольшими заказами: {max_client} с общим количеством {max_quantity}')


def product_counts(orders):
    """Функция для подсчета всех заказанных товаров."""
    product_counts = {}
    for order in orders:
        product = order['product']
        quantity = order['quantity']
        if product in product_counts:
            product_counts[product] += quantity
        else:
            product_counts[product] = quantity

    print('Все заказанные товары:')
    for product, count in product_counts.items():
        print(f'{product}: {count}')


def client_order(orders):
    """Функция для подсчета количества заказов определенного клиента."""
    name = input('Введите имя клиента: ').title()
    name_order = 0
    for order in orders:
        if name in order['client']:
            name_order += 1
    print(f'Количество товаров, заказанных {name}: {name_order}')


def total_order(orders):
    """Функция для подсчета общего количества заказов."""
    count = 0
    for order in orders:
        if order['quantity'] > 0:
            count += order['quantity']
    print(f'Общее количество заказов: {count}')


def display_orders(orders):
    """Функция для вывода всех заказов."""
    print(f"{'Клиент':<15}{'Продукт':<15}{'Количество'}")
    print('-' * 40)
    for order in orders:
        print(f"{order['client']:<15}{order['product']:<15}{order['quantity']}")
    print('-' * 40)


def menu():
    """Главное меню программы."""
    orders = [
        {"client": "Alice", "product": "Laptop", "quantity": 1},
        {"client": "Bob", "product": "Phone", "quantity": 2},
        {"client": "Alice", "product": "Phone", "quantity": 1},
        {"client": "Diana", "product": "Tablet", "quantity": 3},
        {"client": "Charlie", "product": "Laptop", "quantity": 2},
        {"client": "Bob", "product": "Tablet", "quantity": 1}
    ]

    while True:
        print('\nВыберите действие:')
        print('1 - Показать все заказы')
        print('2 - Показать сколько заказов у клиента')
        print('3 - Сколько товаров заказали')
        print('4 - Показать самые большие заказы')
        print('5 - Добавить новый заказ')
        print('0 - Выйти')

        question = input('Введите номер действия: ')

        if question == '1':
            display_orders(orders)  # Вызов функции для отображения всех заказов
        elif question == '2':
            client_order(orders)
        elif question == '3':
            product_counts(orders)
        elif question == '4':
            max_client(orders)
        elif question == '5':
            new_clients(orders)
        elif question == '0':
            print('Счастливого дня!!!')
            break
        else:
            print('Ошибка: выбрано неправильное действие!')


# Запуск программы
menu()
