numbers_file = open('numbers.txt', 'r')
sum = 0
for number in numbers_file:
    number = number.strip()
    if number:
        sum += int(number)
print(f'Сумма чисел равно: {sum}')
numbers_file.close()

answer_file = open('answer.txt', 'w', encoding= 'utf-8')
answer_file.write(f'Сумма чисел равно: {sum}')