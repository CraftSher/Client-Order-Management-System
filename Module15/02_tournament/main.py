# TODO здесь писать код
tournament_participants = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар", "Игорь", "Константин", "Максим", "Никита", "Павел", "Роман"]
first_group = []
second_group = []

for index, name  in enumerate(tournament_participants):
    if index % 2 == 0:
        first_group.append(name)
    else:
        second_group.append(name)

print('Первая группа:', ' '.join(first_group))
print('Вторая группа:', ' '.join(second_group))

# print('Первая группа:', end= ' ')
# for i in first_group:
#     print(i, end= ' ')
# print()
# print('Вторая группа:', end= ' ')
# for j in second_group:
#     print(j, end= ' ')


