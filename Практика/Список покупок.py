shopping_list = []

def add_item(item):
    """Добавляет элемент в список покупок."""
    shopping_list.append(item)
    print(f'"{item}" добавлен в список.')

def remove_item(item):
    """Удаляет элемент из списка покупок."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'"{item}" удален из списка.')
    else:
        print(f'"{item}" не найден в списке.')

def view_list():
    """Выводит текущий список покупок."""
    if shopping_list:
        print('Список покупок:')
        for i, item in enumerate(shopping_list):
            print(f'{i + 1}. {item}')
    else:
        print('Список покупок пуст.')

while True:
    print('\nВыберите действие:')
    print('1. Добавить элемент')
    print('2. Удалить элемент')
    print('3. Просмотреть список')
    print('4. Выйти')

    choice = input('Ваш выбор: ')

    if choice == '1':
        item = input('Введите название элемента: ')
        add_item(item)
    elif choice == '2':
        item = input('Введите название элемента для удаления: ')
        remove_item(item)
    elif choice == '3':
        view_list()
    elif choice == '4':
        print('До свидания!')
        break
    else:
        print('Некорректный выбор. Попробуйте снова.')