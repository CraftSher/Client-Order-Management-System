with open('numbers.txt', 'r') as numbers:
    text = numbers.read()
    nums = text.split()
sum = 0
for num in nums:
    sum += int(num)
print(f'Сумма чисел равно: {sum}')

with open('answer.txt', 'w', encoding= 'utf-8') as answer_file:
    answer_file.write(str(sum))