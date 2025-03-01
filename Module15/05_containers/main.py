
number_containers = int(input('Количество контейнеров: '))
containers = []


for _ in range(1, number_containers + 1):
    weight_container = int(input('Введите вес контейнера: '))
    if 1 <= weight_container <= 200:
        containers.append(weight_container)

print()
new_con_weight = int(input('Введите вес нового контейнера:'))
for index, weight in enumerate(containers):
    if new_con_weight >= weight:
        containers.insert(index,new_con_weight)
        print()
        print('Номер, который получит новый контейнер:', index + 1)
        break
else:
    containers.append(new_con_weight)
    print('Номер, который получит новый контейнер:', len(containers))


