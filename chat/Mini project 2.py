def new_clients(orders):
    name = input('Введите имя клиента: ').title()
    product_name = input('Введите наименование продукта: ').title()
    product_quantity = int(input('Введите количество товара: '))

    orders.append(dict[name])
    orders.append([product_name])
    orders.append(product_quantity)
    print(f'Обновленный список: {orders}')

def max_client(orders):
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
    print(max_client, max_quantity)

def product_counts(orders):
    product_counts = {}
    for order in orders:
        product = order['product']
        quantity = order['quantity']
        if product in product_counts:
            product_counts[product] += quantity
        else:
            product_counts[product] = quantity
    print('Все заказанные товары:', product_counts)

def client_order(orders):
    name = input('Введите имя клиента: ').title()
    name_order = 0
    for dict in orders:
        if name in dict['client']:
            name_order += 1
    print(f' Количество товаров заказанных {name} = {name_order}')

def total_order(orders):
    count = 0
    for dict in orders:
        if dict['quantity'] > 0:
            count += dict['quantity']
    print('Общее количество заказов:', count)


orders = [
    {"client": "Alice", "product": "Laptop", "quantity": 1},
    {"client": "Bob", "product": "Phone", "quantity": 2},
    {"client": "Alice", "product": "Phone", "quantity": 1},
    {"client": "Diana", "product": "Tablet", "quantity": 3},
    {"client": "Charlie", "product": "Laptop", "quantity": 2},
    {"client": "Bob", "product": "Tablet", "quantity": 1}
]
for item in orders:
    for key, value in item.items():
        print(key, ':', value, end=' ')
while True:
    question = input('Выберите действие: \n1 - Показать все заказы,\n2 - Показать сколько заказов у клиента, \n3 - Сколько товаров заказали, \n4 - Показать самые большие заказы, \n5 - Добавить новый заказ, \n0 - Выйти \n')
    if question == '1':
        result = total_order(orders)
    elif question == '2':
        result1 = client_order(orders)
    elif question == '3':
        result2 = product_counts(orders)
    elif question == '4':
        result3 = max_client(orders)
    elif question == '5':
        result4 = new_clients(orders)
    elif question == '0':
        print('Счастливого дня!!!')
        break
    else:
        print('Не правильно выбранное действие!!!')






