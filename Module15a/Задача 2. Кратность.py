N = int(input('Введите кол-во чисел: '))
number_list = []
index_sum = 0

for i in range(N):
    num = int(input(f'Введите {i + 1} число: '))
    number_list.append(num)
print()
divider = int(input('Введите делитель: '))

for index, number in enumerate(number_list):
    if number % divider == 0:
        print(f'Индекс числа {number}: {index}')
        index_sum += index

print()
print('Сумма индексов:', index_sum)
