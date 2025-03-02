number = int(input('Введите число: '))
max_number = 0

while number != 0:
    digit = number % 10
    if digit >= max_number:
        max_number = digit
    number //= 10
print(max_number)



