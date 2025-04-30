# import random
# nums = [random.randint(1, 100) for _ in range(10)]
# print('Исходный список:', nums)
# nums = [i for i in nums if i % 3 != 0]
# print('Обновленный список', nums)
# nums.reverse()
# print('Перевернутый список', nums)
# count = len(nums)
# print('Оставшиеся элементы:', count)

# import random
# nums = [random.randint(1, 50) for _ in range(15)]
# print(nums)
# freq = {}
# for num in nums:
#     freq[num] = freq.get(num, 0) + 1
# max_count = max(freq.values())
# most_common = [num for num, count in freq.items() if count == max_count]
# print(f'Числа {most_common} встречается по {max_count} раз')

# import random
# nums = [random.randint(1, 100) for _ in range(20)]
# print('Исходный список:', nums)
# nums1 = [i for i in nums if i % 2 == 0]
# print('Четные числа:', nums1)
# nums2 = [i for i in nums if i % 2 != 0]
# print('Нечетные числа:', nums2)

# import random
# nums = [random.randint(1, 50) for _ in range(30)]
# unique_nums = []
# seen = set()
#
# for num in nums:
#     if num not in seen:
#         unique_nums.append(num)
#         seen.add(num)
#
# print("Исходный список:", nums)
# print("Уникальные элементы:", unique_nums)

# import random
#
# # Создаем список из 30 случайных чисел от 1 до 50
# nums = [random.randint(1, 50) for _ in range(30)]
#
# # Удаляем дубликаты и сортируем
# unique_nums = sorted(set(nums))
#
# # Выводим результаты
# print("Исходный список:", nums)
# print("Уникальные элементы:", unique_nums)

# students = {'Ali': 85, 'Dina': 90, 'Said': 55, 'Mira': 40, 'Omar': 75}
# students = {key: point for key, point in students.items() if point >= 60}
# print(students)

# def square(num):
#     return num ** 2
# num = int(input('Введите число: '))
# print(square(num))

# def is_even(num):
#    return num % 2 == 0
#
# num = int(input('Введите число: '))
# print(is_even(num))

# import random
# def count_even(nums):
#     return sum(1 for i in nums if i % 2 == 0)
#
# nums = [random.randint(1, 20) for _ in range(6)]
# print(nums)
# print('Четные числа:', count_even(nums))

# import random
# def count_odd(nums):
#     return sum(1 for i in nums if i % 2 != 0)
#
# nums = [random.randint(1, 20) for _ in range(6)]
# print(nums)
# print('Нечетные числа:', count_odd(nums))

# import random
# def count_numbers(nums):
#     return sum(1 for i in nums if i % 2 != 0)
#
# nums = [random.randint(1, 20) for _ in range(6)]
# print(nums)
# print('Нечетные числа:', count_numbers(nums))
# print('Четные числа:', len(nums) - count_numbers(nums))

# import random
#
# def count_numbers(nums):
#     odd_count = sum(1 for i in nums if i % 2 != 0)  # Количество нечётных
#     even_count = len(nums) - odd_count  # Количество чётных
#     return even_count, odd_count  # Возвращаем два значения
#
# nums = [random.randint(1, 20) for _ in range(6)]
# print('Исходный список:', nums)
#
# even, odd = count_numbers(nums)  # Распаковываем два значения
# print('Чётные числа:', even)
# print('Нечётные числа:', odd)

# import random
#
# def analyze_numbers(nums):
#     even_count = sum(1 for i in nums if i % 2 == 0)  # Количество чётных
#     odd_count = len(nums) - even_count  # Количество нечётных
#     summa = sum(nums)  # Сумма всех чисел
#     arithmetic_mean = summa / len(nums)  # Среднее арифметическое
#     return even_count, odd_count, summa, arithmetic_mean
#
# nums = [random.randint(1, 20) for _ in range(6)]
# print('Исходный список:', nums)
#
# even, odd, summa, arithmetic_mean = analyze_numbers(nums)
# print(f'Чётные: {even}, Нечётные: {odd}, Сумма: {summa}, Среднее: {round(arithmetic_mean, 1)}')

# import random
# def find_min_max(nums):
#     max_value = max(nums)
#     min_value = min(nums)
#     difference = max_value - min_value
#     return max_value, min_value, difference
#
# nums = [random.randint(1, 20) for _ in range(6)]
# print('Исходный список:', nums)
# max_num, min_num, difference = find_min_max(nums)
# print(f'Минимум: {min_num}, Максимум: {max_num}, Разница: {difference}')

import random
def count_divisors(num):
    dividers = [i for i in range(1, num + 1) if num % i == 0]
    return dividers, len(dividers)
num = random.randint(1, 20)
print('Исходное число:', num)
dividers, count = count_divisors(num)
print(f'Число {num} делится на {dividers} (всего {count} делителей)')