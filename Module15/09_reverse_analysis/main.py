# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
n = len(numbers_list)
even_number = []

print('Список чисел:', numbers_list)
print()
print('Чётные числа в обратном порядке:', end= ' ')

for num in range(n - 1, - 1, - 1):
    if numbers_list[num] % 2 == 0:
        even_number.append(numbers_list[num])

for i in even_number:
    print(i, end= ', ')