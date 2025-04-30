# numbers = [10, 20, 30, 40, 50]  # список чисел
# fruits = ["яблоко", "банан", "вишня"]  # список строк
# mixed = [1, "hello", 3.14, True]  # смешанный список
# empty = []  # пустой список
# countres = ["Tashkent", "Samarkand", "Bukhara", "Xiva", "Fergana"]
# countres.append('Stanbul')
# countres.insert(1, 'Ankara')
# print(countres)
# countres.pop(1)
# countres.remove('Fergana')
# print(countres)
# countres[0] = 'New York'
# countres[-1] = 'Tokyo'
# print(countres)

# import random
# numbers = [random.randint(1, 50) for _ in range(6)]
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# numbers.sort()
# print(numbers)

# countres = ["Tashkent", "Samarkand", "Bukhara", "Xiva", "Fergana"]
#
# for counter in countres:
#     print(counter)

# import random
# numbers = [random.randint(1, 50) for _ in range(6)]
# count = 0
# while count < len(numbers):
#     print(numbers[count])
#     count += 1

import random
numbers = [random.randint(1, 50) for _ in range(5)]
print(numbers)
for i in reversed(numbers):
    print(i, end= ' ')
print()
i = 0
while i < len(numbers):
    if numbers[i] > 25:
        print(numbers[i])
    i += 1