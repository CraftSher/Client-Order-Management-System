word = input('Введите слово: ')
replace_num = int(input('Номер символа для замены: '))
replace_sym = input('Чем заменяем? ')

new_world = ''

count = 0
for sym in word:
    count += 1
    if replace_num != count:
        new_world += sym
    else:
        new_world += replace_sym

print(new_world)