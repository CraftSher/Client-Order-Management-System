msg = input('Введите строку: ')
letters = list(msg)
index_letter = int(input('Номер символа: ')) - 1

count_letters =0

for _ in letters:
    count_letters += 1

neighbour_count = 0
if index_letter > 0:
    print('Символ слева:', letters[index_letter - 1])
    if letters[index_letter - 1] == letters[index_letter]:
        neighbour_count += 1

if index_letter < count_letters - 1:
    print('Символ справа:', letters[index_letter + 1])
    if letters[index_letter + 1] == letters[index_letter]:
        neighbour_count += 1

if neighbour_count == 0:
    print("Таких же символов нет.")
elif neighbour_count == 1:
    print('Есть ровно один такой же символ.')
elif neighbour_count == 2:
    print('Таких символов два.')

