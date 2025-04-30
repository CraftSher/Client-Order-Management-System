# import datetime
#
# def end_membership(clients):
#     name = input('Введите имя клиента: ').title()
#     for client in clients:
#         if name == client["name"]:
#             print('Клиент с таким именем уже есть в списке. Укажите другое имя: ')
#             return end_membership(clients)
#     membership = input('Введите срок абонемента: ')
#     visits = int(input('Введите количество посещений: '))
#     balance = int(input('Укажите баланс личного счета клиента: '))
#     clients.append({'name': name, 'membership': membership, 'visits': visits, 'balance': balance})
#     print(f'Обновленный список: {clients}')
#     from datetime import date
#     from dateutil.relativedelta import relativedelta
#     start_date = date.today()
#     membership_type = input('Введите тип абонемента (1- Годовой, 2 - Месяц, 3 - несколько дней): ')
#     if membership_type == '3':
#         membership_type1 = int(input('Введите количество дней: '))
#         member_end = today + relativedelta(days=membership_type1)
#     elif membership_type == '1':
#         member_end = today + relativedelta(years=1)
#     elif membership_type == '2':
#         member_end = today + relativedelta(month=1)
#     else:
#         print('Введите корректное данные: ')
#         return end_membership(clients)
#
#
#
# clients = [
#     {"name": "Alice", "membership": "месячный", "visits": 12, "balance": -5},
#     {"name": "Bob", "membership": "годовой", "visits": 40, "balance": 20}
# ]
#
# result = end_membership(clients)

def debt(clients):
    min_value = 0
    for client in clients:
        if client["balance"] < min_value:
            most_debt_client = client['name']
            debt = client['balance']
    print(f'Клиент с долгом {most_debt_client}. Долг составляет {debt}')
    return most_debt_client


clients = [
    {"name": "Alice", "membership": "месячный", "visits": 12, "balance": -5},
    {"name": "Bob", "membership": "годовой", "visits": 40, "balance": 20}
]

result = debt(clients)