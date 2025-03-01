num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
operation = input('Выберите операцию: + - / *')

if operation == '+':
    summ = num1 + num2
    print('Сумма чисел: ', summ)
elif operation == '-':
    subtraction = abs(num1 - num2)
    print('Вычетание чисел: ', subtraction)
elif operation == '/':
    division = num1 / num2
    print('Деление чисел: ', division)
elif operation == '*':
    multiplication = num1 * num2
    print('Умножение чисел: ', multiplication)