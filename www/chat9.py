import random

hidden_number = random.randint(1, 100)

while True:
    user_number = int(input('Введите число: '))
    if user_number == hidden_number:
        print('Ура!!! Вы угодали.')
        break
    elif user_number > hidden_number:
        print('Загаданное число меньше.')
    else:
        print('Загаданное число больше.')