phone_book = {}
while True:
    print('Текущие контакты на телефоне:')
    if phone_book:
        for name in phone_book:
            print(name, phone_book[name])
    else:
        print('<Пусто>')
    new_contact = input('Введите имя (для остановки введите пустую строку): ')
    if new_contact == '':
        break
    new_telephone = int(input('Введите номер телефона: '))
    if new_contact in phone_book:
        print('Ошибка: такое имя уже существует.')
    else:
        phone_book[new_contact] = new_telephone
