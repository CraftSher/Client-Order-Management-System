
k = int(input('Сдвиг: '))
num = [1, 4, -3, 0, 10]
k = k % len(num)

p1 = num[-k:]
p2 = num[:-k]

print('Изначальный список:', num)
print('Сдвинутый список:', p1 + p2)