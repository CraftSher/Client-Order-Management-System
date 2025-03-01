dogs_quantity = int(input('Введите количество собак: '))
point_ID = []


for _ in range(dogs_quantity):
    dogs_point = int(input('Введите очки каждой собаки: '))
    point_ID.append(dogs_point)

if point_ID:
    max_value = point_ID[0]
    min_value = point_ID[0]
    index_max = 0
    index_min = 0
    for index, i in enumerate(point_ID):

        if max_value < i:
            max_value = i
            index_max = index

        if min_value > i:
            min_value = i
            index_min = index

    print('Максимальное число в списке:', max_value)
    print('Минимальное число в списке:', min_value)

    print(point_ID)
    point_ID[index_min], point_ID[index_max] = point_ID[index_max], point_ID[index_min]
    print(point_ID)
else:
    print('В списке нету чисел')




