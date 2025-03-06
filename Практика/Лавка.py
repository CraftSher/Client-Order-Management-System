goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

print('Текущий ассортимент: ', goods)
print()
fruit = input('Новый фрукт: ')
price = int(input('Цена: '))

goods.append([fruit, price])

print('Новый ассортимент: ', goods)
tax = int(input('Налог увеличился на %: '))
k = 1 + tax / 100
for good in goods:
    good[1] = round(good[1] * k, 2)
print('Новый ассортимент с увел. ценой:', goods)