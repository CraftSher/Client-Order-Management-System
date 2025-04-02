n = int(input('Введите число: '))
print('Простые числа: ')

for i in range(2, n + 1):
    # Проверка на простоту числа
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):  # Оптимизация: проверяем до корня из числа
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=' ')