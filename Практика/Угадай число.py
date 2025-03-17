import random

hidden_number = random.randint(1, 100)
number = None
attempts = 0

print('Добро пожаловать в игру "Угадай число"!')
print('Я загадал число от 1 до 100. Попробуйте угадать.')

while number != hidden_number:
    try:
        number = int(input('Ваше предположение: '))
        attempts += 1

        if number > hidden_number:
            print(f'Загаданное число меньше {number}')
        elif number < hidden_number:
            print(f'Загаданное число больше {number}')
        else:
            print(f'Поздравляем! Вы угадали число {hidden_number} за {attempts} попыток.')
    except ValueError:
        print('Ошибка: введите целое число!')

