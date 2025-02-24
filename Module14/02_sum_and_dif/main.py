# TODO здесь писать код
import math
def summ(n):
    summ = 0
    while n != 0:
        digit = n % 10
        summ += digit
        n //= 10
    return summ


def digit_summ(n):
    total_digit = 0
    while n != 0:
        total_digit += 1
        n //= 10
    return total_digit


def main():
    n = int(input('Введите число: '))
    return n


n = main()
a = summ(n)
b = digit_summ(n)
print('Сумма чисел:', a)
print('Количество цифр в числе:', b)
print('Разность суммы и количества цифр:', abs(a - b))




