import random
num = [random.randint(1, 20) for _ in range(1)]
print('Исходное число:', num)
for i in range(1, 19+1):
    print(i)
#     if num % i == 0:
#         dividers.append(i)
#         count += 1
#
# print(f'Число {num} делится на {dividers} (всего {count} делителей')