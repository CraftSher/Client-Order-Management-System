def add(a, b):
    return a + b
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
result = add(a, b)
print(result)

def odd(number):
    if number % 2 == 0:
        print('число четное.')
    else:
        print('число не четное.')

num = int(input('Введите число: '))
odd(num)

import random

def random_number():
    num = random.randint(1, 100)
    print(num)

random_number()