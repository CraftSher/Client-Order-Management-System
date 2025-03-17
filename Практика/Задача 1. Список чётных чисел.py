start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

even_numbers = [x for x in range(start, end + 1) if x % 2 == 0]
print('Список из чётных чисел:', even_numbers)