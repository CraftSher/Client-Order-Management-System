people_quantity = int(input('Кол-во человек: '))
counting_rhyme = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {counting_rhyme}-й человек')
print()

current_circle = list(range(1, people_quantity + 1))
index = 0

while len(current_circle) > 1:
    print('Текущий круг людей:', current_circle)
    print('Начало счёта с номера', current_circle[index])
    index = (index + counting_rhyme - 1) % len(current_circle)
    print('Выбывает человек под номером', current_circle[index])
    print()

    current_circle.pop(index)

    if index >= len(current_circle):
        index = 0

print('Остался человек под номером', current_circle[0])