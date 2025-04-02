number = int(input('Введите число: '))
max_number = 0
min_number = 9

while number > 0:
    digit = number % 10
    if digit > max_number:
        max_number = digit
    if digit < min_number:
        min_number = digit
    number //= 10

print('Максимальное число:', max_number, 'Минимальное число:', min_number)