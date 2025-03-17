start = int(input('Левая граница: '))
end = int(input('Правая граница:'))

squares = [x ** 2 for x in range(start, end + 1)]
cube = [x ** 3 for x in range(start, end + 1)]
print(f'Список кубов чисел в диапазоне от {start} до {end}:', cube)
print(f'Список квадратов чисел в диапазоне от {start} до {end}]:', squares)