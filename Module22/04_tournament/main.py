with open('first_tour.txt', 'r') as first_tour:
    k = ''
    k = int(first_tour.readline())
    second_list = []
    text = first_tour.readlines()
for item in text:
    elem = item.split()
    if int(elem[2]) > k:
        winner = (elem[0], elem[1], int(elem[2]))
        second_list.append(winner)
second_list.sort(key = lambda x: x[2], reverse=True)
count = len(second_list)
for surname, name, value in second_list:
    print(f'{name[0]}. {surname} {value}')

with open('second_tour.txt', 'w', encoding= 'utf-8') as second_tour:
    second_tour.write(f'{count}\n')
    for i, (surname, name, value) in enumerate(second_list, 1):
        second_tour.write(f'{i}) {name[0]}. {surname} {value}\n')







