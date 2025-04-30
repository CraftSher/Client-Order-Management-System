# nums = [2, 4, 6, 8, 10]
# i = 0
# for i in nums:
#     print(i)
#-------------------------------
# while i < len(nums):
#     print(nums[i])
#     i += 1
#--------------------------------------
# squared_nums = [i ** 2 for i in nums]
# print(squared_nums)
#----------------------------------------
# numbers = [1, 2, 3, 4, 5, 2]
# print(numbers)
# numbers.remove(2)
# print(numbers)
# numbers.reverse()
# print(numbers)
# quantity = numbers.count(4)
# print(quantity)
# numbers1 = [6, 7, 8]
# numbers.extend(numbers1)
# print(numbers)

# import random
# nums = [random.randint(1, 100) for _ in range(10)]
# even_num = [i for i in nums if i % 2 == 0]
# print('Исходный список:', nums)
# print('Четные числа:', even_num)

# import random
# nums = [random.randint(1, 30) for _ in range(5)]
# print('Исходный список:', nums)
# new_num = int(input('Введите любое число: '))
# count = nums.count(new_num)
# print(f'Число {new_num} встречается {count} раз(а) в списке')

# import random
# nums = [random.randint(1, 20) for _ in range(7)]
# new_num = int(input('Введите любое число: '))
# print('Исходный список:', nums)
# if new_num in nums:
#     nums.remove(new_num)
# else:
#     nums.append(new_num)
# print('Откорректированный список:', nums)

# import random
# nums = [random.randint(1, 50) for _ in range(15)]
# count = 0
# print('Исходный список:', nums)
# while count < len(nums):
#     if nums[count] % 2 != 0:
#         nums.pop(count)
#     else:
#         count += 1
# print('Список после удаления не четных чисел:', nums)


import random

nums = [random.randint(1, 100) for _ in range(10)]
print('Исходный список:', nums)

new_num = int(input('Введите любое число: '))

if new_num in nums:
    while new_num in nums:
        nums.remove(new_num)
else:
    nums.append(new_num)
    nums.sort()

print('Откорректированный список:', nums)