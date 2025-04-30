# nums = [10, 20, 30, 40, 50, 30]
# nums.remove(30)
#
# print(nums)

# words = ['apple', 'banana', 'cherry', 'date']
# words.reverse()
# print(words)

# words = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']
# print('Количество слов',  words.count('blue'))

# first = ["a", "b", "c"]
# second = ["d", "e", "f"]
# first.extend(second)
# print(first)

# names = ['Alice', 'Bob', 'Charlie']
# for i in names:
#     print(i, end= ' ')

# numbers = [10, 25, 30, 45, 50, 65, 70]
# even_num = [i for i in numbers if i % 2 == 0]
# print(even_num)

# numbers = [10, 25, 30, 45, 50, 65, 70]
# odd_num = []
# for i in numbers:
#     if i % 2 != 0:
#         odd_num.append(i)
# print(odd_num)

# nums = [2, 4, 6, 8, 10]
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

# numbers = [5, 12, 7, 20, 3, 25]
# id = 0
# num = []
#
# while id < len(numbers):
#     if numbers[id] > 10:
#         num.append(numbers[id])
#     id += 1
# print(num)

# numbers = [2, 5, 8, 11, 14]
# double_numbers = [x * 2 for x in numbers]
# print((double_numbers))

# numbers = [3, 10, 15, 20, 25, 30]
# division = [i for i in numbers if i % 5 == 0]
# print(division)

# numbers = [4, 9, 16, 25, 36, 49, 64, 81, 100]
# roots = []
# for i in numbers:
#     roots.append(i ** 0.5)
# print(roots)

numbers = [4, 9, 16, 25, 36, 49, 64, 81, 100]
roots = [i ** 0.5 for i in numbers]
print(roots)