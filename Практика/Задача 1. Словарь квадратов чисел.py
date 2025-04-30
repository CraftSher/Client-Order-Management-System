num = int(input('Введите число: '))
numbers = {}
for i in range(1, num + 1):
    numbers[i] = i ** 2
print('Результат:', numbers)