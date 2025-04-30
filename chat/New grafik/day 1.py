import random
# nums1 = [100, 200]
# nums = [random.randint(1, 10) for _ in range(5)]
# print(f'Исходные числа: {nums} и {nums1}')
# nums.pop(3)
# print(f'Список после удаления: {nums}')
# print(f'В списке цифры 2 встречается: {nums.count(2)}')
# nums.reverse()
# print(f'Перевернутый список: {nums}')
# nums.extend(nums1)
# print(f'Обновленный список: {nums}')


# nums = [random.randint(1, 20) for _ in range(7)]
# print(f'Исходные числа: {nums}')

# i = 0
# while i < len(nums):
#     print(nums[i], end= '; ')
#     i += 1
#
# count_even_numbers = 0
# suma_even_numbers = 0
# i = 0
# while i < len(nums):
#     if nums[i] % 2 == 0:
#         count_even_numbers += 1
#         suma_even_numbers += nums[i]
#     i += 1
#
# print(f'Четных чисел: {count_even_numbers}, их сумма: {suma_even_numbers}')

# assessments = [random.randint(2, 5) for _ in range(10)]
# i = 0
# while i < len(assessments):
#     i += 1
# print(f'Оценки студентов: {assessments}', end= '; ')
#
#
# asses5 = 0
# asses4 = 0
# asses3 = 0
# asses2 = 0
# i = 0
# while i < len(assessments):
#     if assessments[i] == 5:
#         asses5 += 1
#     elif assessments[i] == 4:
#         asses4 += 1
#     elif assessments[i] == 3:
#         asses3 += 1
#     elif assessments[i] == 2:
#         asses2 += 1
#     i += 1
#
# print(f'\nКоличество пятёрок: {asses5} \nКоличество четвёрок: {asses4} \nКоличество троек: {asses3} \nКоличество двоек: {asses2}')
#
# total = 0
# i = 0
# while i < len(assessments):
#     total += assessments[i]
#     i += 1
#
# average = total / len(assessments)
# print(f'Средняя оценка студентов: {average}')
# prices = [random.randint(10, 100) for _ in range(7)]
# print('Цены на товары:')
# for price in prices:
#     print(price, end= '; ')
#
# min_price = min(prices)
# max_price = max(prices)
# total = 0
# for price in prices:
#     total += price
# print()
# print(f'Минимальная цена товара: {min_price}')
# print(f'Максимальная цена товара: {max_price}')
#
# average = round(total / len(prices), 2)
# print(f'Средняя цена товаров: {average}')

# nums = [x ** 2 for x in range(1, 11)]
# print(f'Квадрат чисел от 1 до 10: {nums}')
# nums1 = [x for x in range(1, 21) if x % 2 == 0]
# print(f'Четные числа в диапазоне от 1 до 20: {nums1} ')
# nums2 = [x for x in nums1 if x > 5]
# print(nums2)
# nums = [x ** 2 for x in range(1, 21) if x % 2 != 0]
# print(f'Квадрат нечетных чисел от 1 до 20: {nums}')
# nums1 = [x for x in range(1, 31) if x % 3 == 0 and x % 5 == 0]
# print(f'Все числа от 1 до 30 делящиеся на 3 и 5 одновременно: {nums1}')

text = "Фриланс — это свобода и ответственность"
sym_count = 0
print(text)
for letter in text:
    sym_count += 1
print(f'Количество символов в тексте: {sym_count}')
print(text.upper())

word = 'свобода'
if word.lower() in text.lower():
    print(f'Слова {word} найден в тексте!!!')
else:
    print(f'Слова {word} нет в тексте!!!')

word1 = 'ответственность'
word2 = 'дисциплина'
if word1.lower() in text.lower():
    text = text.lower().replace(word1.lower(), word2)
print(f'Отредактированный текст: {text}')


