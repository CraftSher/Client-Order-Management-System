num = int(input('Введите длину списка: '))
result = [(1 if i % 2 == 0 else i % 5) for i in range(num)]
print(result)
