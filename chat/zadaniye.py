# products = {
#     "apple": 1.2,
#     "banana": 0.5,
#     "orange": 0.9,
#     "grape": 2.5
# }
# for key, value in products.items():
#     print(key, ':', value)
# for key, value in products.items():
#     new_value = round(value * 1.1, 2)
#     products[key] = new_value
# print(products)
# for key, value in products.items():
#     if value > 1.5:
#         print(key, ':', value)

# numbers = [3, 7, 2, 8, 5, 10, 6]
# print(numbers)
# print('Максимальное значение:', max(numbers), 'Минимальное значение:', min(numbers))
# average_value  = sum(numbers)/len(numbers)
# print('Среднее значение:', round(average_value, 2))
# even_num = [item for item in numbers if item % 2 == 0]
# print('Все четные числа:', even_num)
# increase_num = [item * 2 for item in numbers]
# print('Увеличенные числа:', increase_num)

# people = {
#     "Alice": 25,
#     "Bob": 30,
#     "Charlie": 22
# }
# i = 0
# keys = list(people.keys())
# while i < len(keys):
#     key = keys[i]
#     i += 1
#     print(key, ':', people[key])
#
# people['sher'] = 44
# print(people)
# people['Bob'] = 35
# del people['Charlie']
# print(people)

# numbers = [15, 22, 9, 31, 45, 5, 13, 8]
# num_20 = [nums for nums in numbers if nums < 20]
# print(numbers)
# print(num_20)
# num10_30 = [nums for nums in numbers if 10 < nums < 30]
# print(num10_30)
# num_3 = [nums * 3 for nums in numbers]
# print(num_3)
# print(f'Максимальное число: {max(numbers)}, Минимальное число: {min(numbers)}')

# books = {
#     "War and Peace": 1000,
#     "The Great Gatsby": 180,
#     "Moby Dick": 600,
#     "1984": 328
# }
# for key, value in books.items():
#     print(key, ':', value)
#     new_value = value + 50
#     books[key] = new_value
# print(books)
# min_value = min(books.values())
# keys_remove = [key for key, value in books.items() if value == min_value]
# for key in keys_remove:
#     books.pop(key)
# print('Обновленный список:', books)

import random
def summa(num):
    return sum(num)

quantity = int(input('Сколько будет чисел? '))
numbers = [random.randint(1, 20) for _ in range(quantity)]
result = summa(numbers)
print(result)

def count_vowels(text):
    vowels = "аеёиоуыэюяaeiou"
    count = 0
    for letter in text.lower():
        if letter in vowels:
            count += 1
    return count

text = input('Введите текст: ')
result = count_vowels(text)
print(f"Количество гласных: {result}")

import random
numbers = [random.randint(1, 50) for _ in range(16)]
num_5 = [num for num in numbers if num % 5 == 0]
print(numbers)
print(num_5)

