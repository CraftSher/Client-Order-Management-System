num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
arithmetic_operation = input('Выберите арифметическую операцию (+, -, *, /): ')

if arithmetic_operation == '+':
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
elif arithmetic_operation == '-':
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
elif arithmetic_operation == '*':
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
elif arithmetic_operation == '/':
    if num2 == 0:
        print('Ошибка: деление на ноль!')
    else:
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
else:
    print('Ошибка: некорректная операция!')
