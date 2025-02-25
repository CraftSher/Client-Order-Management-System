import math
def summ(number):
    summ = 0
    while number != 0:
        digit = number % 10
        summ += digit
        number //= 10
    return summ


def digit_summ(number):
    total_digit = 0
    while number != 0:
        total_digit += 1
        number //= 10
    return total_digit


number = int(input('Введите число: '))

number_summ = summ(number)
number_digit = digit_summ(number)
difference = number_summ - number_digit
print('Сумма чисел:', number_summ)
print('Количество цифр в числе:', number_digit)
print('Разность суммы и количества цифр:', difference)
