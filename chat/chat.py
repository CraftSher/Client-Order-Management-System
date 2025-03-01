number = int(input('Введите число: '))

if number < 2:
    print(number, ' - это не простое число.')
else:
    for i in range(2, number):
        if number % i == 0:
            print(number, ' - это не простое число.')
            break
    else:
        print(number, ' - это простое число.')