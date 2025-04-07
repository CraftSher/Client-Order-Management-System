# TODO здесь писать код
phone_book = {}

def add_new_contact():
    name = input('Введите имя: ').title()
    sur_name = input('Введите фамилию: ').title()
    number = input('Введите номер телефона: ')
    if number.isdigit():
        if (name, sur_name) in phone_book:
            print('Такой человек уже есть в контактах.')
        else:
            phone_book[name, sur_name] = number
        print(phone_book)
    else:
        print('Номер должен быть цифрой:')

def search_contact():
    sur_name = input('Введите фамилию: ').title()
    found = False
    for (name, surname), numbers in phone_book.items():
        if sur_name == surname:
            print(f'{name} {surname}: {numbers}')
            found = True
    if not found:
        print('Контакт не найден.')

while True:
    action = input(f'Выберите действие: (1 — добавить контакт, \n2 — найти контакт, \n0 - Выйти) ')
    if action == '1':
        result1 = add_new_contact()
    elif action == '2':
        result2 = search_contact()
    elif action == '0':
        break
    else:
        print('Не правильно выбранное действие!!!')


