
user_name = input('Введите имя: ')

while True:
    print('Что бы увидеть текущий текст чата введите -1, что бы отправить сообщение введите - 2.')
    response = input('Введите 1 или 2.')
    if response == '1':
        try:
            with open('chat.txt', 'r', encoding= 'utf-8') as file:
                message = file.readlines()
                print(''.join(message))
        except FileNotFoundError:
            print('Служебное сообщение: Пока ничего нет\n')

    elif response == '2':
        new_message = input('Введите сообщение:')
        with open('chat.txt', 'a', encoding= 'utf-8') as file:
            file.write('{name}: {message}\n'.format(name = user_name, message = new_message))

    else:
        print('Неизвестная команда:\n')