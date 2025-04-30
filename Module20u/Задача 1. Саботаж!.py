text = input('Строка: ')
print('Ответ: ',end= ' ')
for index, sym in enumerate(text):
    if sym == '~':
        print(index, end= ' ')
