number = int(input('Введите число: '))

summa = 0

while number > 0:
    digital = number % 10
    summa += digital
    number //= 10

print('Сумма цифр:', summa)