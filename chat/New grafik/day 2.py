# def print_hello():
#     print('Привет, мир!!!')
#
# print_hello()
#=====================================
# def square_number(num):
#     return num ** 2
#
# num = int(input('Введите число: '))
# result = square_number(num)
# print(result)
#======================================
# def add_numbers(a, b):
#     return a + b
#
# num1 = int(input('Введите 1 число: '))
# num2 = int(input('Введите 2 число: '))
# result = add_numbers(num1, num2)
# print(result)
#=======================================
# def is_even(number):
#     return number % 2
#
# num = int(input('Введите число: '))
# result = is_even(num)
# print(result)
#=======================================
# def max_of_three(a, b, c):
#     return max(a, b, c)
#
# num1 = int(input('Введите 1 число: '))
# num2 = int(input('Введите 2 число: '))
# num3 = int(input('Введите 3 число: '))
# result = max_of_three(num1, num2, num3)
# print(result)
#=======================================
# def clculate_area(width, height):
#     return width * height
#
#
# num1 = int(input('Введите ширину: '))
# num2 = int(input('Введите высоту: '))
#
# result = clculate_area(num1, num2)
# print(result)
#=======================================
# def greet(name="пользователь"):
#     print(f"Привет, {name}!")
#
#
# greet()
# greet("Иван")
#=======================================
# def get_min_max(numbers):
#     minimum = min(numbers)
#     maximum = max(numbers)
#     return minimum, maximum
#
# numbers = [10, 20, 5, 40, 30]
# min_value, max_value = get_min_max(numbers)
# print(f"Минимум: {min_value}, Максимум: {max_value}")
#=======================================
# def divide_numbers(a, b):
#     return (a // b), (a % b)
#
# num1 = int(input('Введите 1 число: '))
# num2 = int(input('Введите 2 число: '))
# result = divide_numbers(num1, num2)
# print(result)
#=======================================
# def is_palindrome(text):
#     return text == text[::-1]
#
# text = input('Введите слово: ')
# result = is_palindrome(text)
#
# print(result)
#=======================================
# import random
# def find_max_min(nums):
#     max_num = max(nums)
#     min_num = min(nums)
#     return max_num, min_num
#
# numbers = [random.randint(1, 5) for _ in range(10)]
# print(numbers)
# result = find_max_min(numbers)
# print(result)
# =======================================
# import random
# def sum_of_square(nums):
#     return sum(x ** 2 for x in nums)
#
# numbers = [random.randint(1, 5) for _ in range(10)]
# print(numbers)
# result = sum_of_square(numbers)
# print(result)
#=======================================
# def greet(name, age = '18'):
#     print(f'Привет {name}!!! Тебе {age} лет.')
#
# name = input('Введите имя: ')
# age = input('Сколько вам лет: ')
# greet(name)
#========================================
# import random
# def sum_numbers(*args):
#     return sum(args)
#
# nums = [random.randint(1, 5) for _ in range(10)]
# print(nums)
# result = sum_numbers(*nums)
# print(result)
#========================================
# def name_profess(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
# new_dict = {}
# quantity = int(input('Сколько людей добавить? '))
# for i in range(quantity):
#     name = input('Введите имя: ').title()
#     profes = input('Введите должность: ').title()
#     new_dict[name] = profes
# result = name_profess(**new_dict)
#========================================
from soupsieve.util import lower


def aggregate_numbers(*args):
    average = (sum(args) / len(args))
    max_value = max(args)
    min_value = min(args)
    return average, max_value, min_value
nums = (10, 20, 30, 40)
result = aggregate_numbers(*nums)
print(result)  # Например, (25.0, 40, 10)
#========================================
def build_profile(name, **kwargs):
    kwargs['name'] = name
    return kwargs

profile = build_profile("Алиса", age=25, city="Москва", profession="Инженер")
print(profile)
# Ожидаемый вывод:
# {'name': 'Алиса', 'age': 25, 'city': 'Москва', 'profession': 'Инженер'}
#========================================
def process_text(text, case = 'lower'):
    if case == "lower":
        processed_text = text.lower()
    elif case == "upper":
        processed_text = text.upper()
    else:
        processed_text = text
    length = len(processed_text)
    return processed_text, length

result_text, length = process_text("Привет, Мир!", case="upper")
print(result_text)  # "ПРИВЕТ, МИР!"
print(length)       # Количество символов в строке
