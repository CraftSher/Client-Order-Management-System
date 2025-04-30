phone_book = {}

while True:
    name = input('Введите имя (или "стоп" для выхода): ')
    if name.lower() == 'стоп':
        break
    sur_name = input('Введите фамилию: ')
    number = int(input('Введите номер телефона: '))
    if (name, sur_name) in phone_book:
        print('Контакт уже существует')
    else:
        phone_book[(name, sur_name)] = number
    print(phone_book)
