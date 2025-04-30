def debt(clients):
    min_value = 0
    most_debt_client = None
    for client in clients:
        if client["balance"] < min_value:
            most_debt_client = client['name']
            debt = client['balance']
    print(f'Клиент с долгом {most_debt_client}. Долг составляет {debt}')
    return most_debt_client

def most_active(clients):
    if not clients:
        return None
    most_active_client = clients[0]
    for client in clients[1:]:
        if client["visits"] > most_active_client["visits"]:
            most_active_client = client
    print(f'Самый активный клиент {most_active_client}')
    return most_active_client

def remove_client(clients):
    while True:
        name = input('Введите имя клиента: ').title()
        found = False
        for client in clients:
            if client["name"] == name:
                found = True
                print(f'Количество посещений {client['name']} = {client['visits']}')
                if (client['membership'] == "месячный" and client['visits'] >= 30) or (client['membership'] == "годовой" and client['visits'] >= 303):
                    print(f'Абонемент клиента {client['name']} окончен')
                    action = input('Удалить его из базы данных: 1 - ДА, 2- НЕТ')
                    if action == '1':
                        clients.remove(client)
                        print(f'Клиент {name} удалён.')
                        break
                    elif action == '2':
                        break
                    else:
                        print('Введите корректный запрос!!!')
                else:
                    print(f'Абонемент клиента {name} ещё не окончен.')
                    break
        if not found:
            print(f'Клиента с таким именем в базе нету:')
        choice = input('Попробовать еще раз? (да/нет): ').lower()
        if choice != 'да':
            return clients

def show_all_clients(clients):
    for item in clients:
        for client, value in item.items():
            print(client, ':', value)
        print()

def add_visits(clients):
    while True:
        name = input('Введите имя клиента: ').title()
        for client in clients:
            if client["name"] == name:
                print(f'Количество посещений {client['name']} = {client['visits']}')
                quantity = int(input('Введите количество посещений: '))
                client["visits"] += quantity
                print(f'Обновленный список: {clients}')
                return clients
        print(f'Клиента с таким именем в базе нету:')
        choice = input('Попробовать еще раз? (да/нет): ').lower()
        if choice != 'да':
            return clients

def add_new_clients(clients):
    name = input('Введите имя клиента: ').title()
    for client in clients:
        if name == client["name"]:
            print('Клиент с таким именем уже есть в списке. Укажите другое имя: ')
            return add_new_clients(clients)
    membership = input('Введите срок абонемента: ')
    visits = int(input('Введите количество посещений: '))
    balance = int(input('Укажите баланс личного счета клиента: '))
    clients.append({'name': name, 'membership': membership, 'visits': visits, 'balance': balance})
    print(f'Обновленный список: {clients}')

clients = [
    {"name": "Alice", "membership": "месячный", "visits": 12, "balance": -5},
    {"name": "Bob", "membership": "годовой", "visits": 40, "balance": 20}
]
while True:
    question = input('Выберите действие: \n1 - Показать всех клиентов,\n2 - Добавить нового клиента, \n3 - Увеличить количество посещений, \n4 - Удалить клиента, \n5 - Показать самого активного клиента, \n6 - Показать клиента с долгом \n0 - Выйти')
    if question == '1':
        result = show_all_clients(clients)
    elif question == '2':
        result1 = add_new_clients(clients)
    elif question == '3':
        result2 = add_visits(clients)
    elif question == '4':
        result3 = remove_client(clients)
    elif question == '5':
        result4 = most_active(clients)
    elif question == '6':
        result5 = debt(clients)
    elif question == '0':
        print('Счастливого дня!!!')
        break
    else:
        print('Не правильно выбранное действие!!!')




