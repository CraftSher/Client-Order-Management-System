number_skates = int(input('Кол-во коньков: '))
skates = []
use = 0

for i in range(number_skates):
    size_skates = int(input(f'Размер {i + 1}-й пары: '))
    skates.append(size_skates)

number_people = int(input('Кол-во людей: '))

for j in range(number_people):
    foot_size = int(input(f'Размер ноги {j + 1}-го человека: '))
    for size in skates:
        if foot_size == size:
            skates.remove(size)
            use += 1
print('Наибольшее кол-во людей, которые могут взять ролики:', use)