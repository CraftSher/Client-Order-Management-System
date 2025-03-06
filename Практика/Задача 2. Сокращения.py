employers = int(input('Введите количество сотрудников: '))
salarys = []



for i in range(employers):
    salary = int(input(f'Зарплата {i + 1} сотрудника: '))
    if salary > 0:
        salarys.append(salary)


print()
print('Осталось сотрудников:', len(salarys))
print('Зарплаты:', salarys)
print()
print('Максимальная зп:', max(salarys))
print('Минимальная зп:', min(salarys))

