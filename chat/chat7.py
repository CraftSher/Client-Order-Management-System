number = int(input('Введите число: '))
print('Четные числа:')
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, end= ' ')
