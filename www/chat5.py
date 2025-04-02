number = int(input('Введите число: '))
reverse_number = ''

while number > 0:
    digit = number % 10
    reverse_number += str(digit)
    number //= 10
print('Перевернутое число:', reverse_number)