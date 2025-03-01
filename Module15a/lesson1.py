
numbers_list = [1, 5, 2, -7, 6]
for _ in range(5):
    new_num = int(input('Введите число: '))
    numbers_list.append(new_num)
for number in numbers_list:
    print(number, '** 2 =', number ** 2)