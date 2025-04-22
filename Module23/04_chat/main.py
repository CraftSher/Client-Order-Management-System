def view_chat():
    try:
        with open('chat_log.txt', 'r', encoding='utf-8') as chat_list:
            chat_view = chat_list.read()
            if chat_view:
                print(chat_view)
            else:
                print("Чат пустой или сообщений еще нет.")
    except FileNotFoundError:
        print("Чат пустой или его еще нет.")

def send_message(username):
    user_message = input('Введите сообщение: ')
    with open('chat_log.txt', 'a', encoding='utf-8') as chat_list:
        chat_list.write(f'{username}: {user_message}\n')
        chat_list.close()
        print('Сообщение отправлено.')

def main():
    username = input("Введите ваше имя: ")
    print(f"Добро пожаловать в чат, {username}!")

    while True:
        print("\nВыберите действие:")
        print("1. Посмотреть текущий текст чата")
        print("2. Отправить сообщение")
        print("3. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            view_chat()
        elif choice == '2':
            send_message(username)
        elif choice == '3':
            print('До свидание!')
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()