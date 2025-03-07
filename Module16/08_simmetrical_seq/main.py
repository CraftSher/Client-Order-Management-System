# TODO переписать программу OK

numbers = int(input('Кол-во чисел: '))
subsequence = []
mirror_subsequence = []
lsuf = []
count = 0

for i in range(numbers):
    num = int(input(f'Введите {i + 1} число: '))
    subsequence.append(num)
print('Последовательность:', subsequence)

if subsequence == subsequence[::-1]:
    print('Это число симметричное!!!')
    exit()

for i in range(len(subsequence)):
    suf = subsequence[i:]
    if suf == suf[::-1]:
        lsuf = subsequence[:i]
        count = len(lsuf)
        break

print('Нужно приписать чисел:', count)
print('Сами числа:', lsuf[::-1])