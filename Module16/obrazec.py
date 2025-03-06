numbers = int(input('Кол-во чисел: '))
subsequence = []
mirror_subsequence = []
lsuf = []
count = 0

for i in range(numbers):
    num = int(input(f'Введите {i + 1} число: '))
    subsequence.append(num)

# print(subsequence)
# print(subsequence[-2:])
# p = subsequence[-2:]
# print(p[::-1])

if subsequence == subsequence[::-1]:
    print('Это число симметричное!!!')
    exit()

for i in range(len(subsequence)):
    suf = subsequence[i:]
    if suf == suf[::-1]:
        lsuf = subsequence[:i]
        count = len(lsuf)
        break

print(lsuf)
print(count)

# print(subsequence)
# print(subsequence[-2:])
# p = subsequence[-2:]
# print(p[::-1])


# print('Нужно приписать чисел:', count)
# print('Сами числа:', mirror_subsequence)






# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
#
# list3 = sorted(list1 + list2)
# list4 = []
#
# for num in list3:
#     if num not in list4:
#         list4.append(num)
# print(list4)