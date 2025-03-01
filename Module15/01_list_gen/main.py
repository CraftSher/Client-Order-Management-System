# TODO здесь писать код
number = int(input('Введите число: '))
odd_numbers = []
count = 0

for i in range(1, number + 1):
    if i % 2 == 1:
        count += 1
        odd_numbers.append(i)
print('Список из нечётных чисел от одного до', number, ':', odd_numbers)
