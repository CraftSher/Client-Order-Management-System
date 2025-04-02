# import re
#
# def is_palindrome(text):
#     """Проверяет, является ли строка палиндромом."""
#     cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я]', '', text.lower())
#     reverse_text = cleaned_text[::-1]
#     return cleaned_text == reverse_text

# text = input('Введите текст: ')
# if is_palindrome(text):
#     cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я]', '', text.lower())
#     print(f'"{cleaned_text}" - Это палиндром!')
# else:
#     print('Это не палиндром.')
#
#
#num = int(input('Введите число: '))
#sum_primes = 0

#for i in range(2, num):
 #   is_prime = True
  #  for j in range(2, i):
   #     if i % j == 0:
    #        is_prime = False
    #if is_prime:
     #   sum_primes += i
#print(sum_primes)

import math

def is_prime(n):
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(limit):
    """Возвращает сумму простых чисел до limit."""
    total = 0
    for i in range(2, limit):
        if is_prime(i):
            total += i
    return total

num = int(input('Введите число: '))
result = sum_primes(num)
print(result)



