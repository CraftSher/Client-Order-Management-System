text1 = input('Введите первое сообщение: ')
text2 = input('Введите второе сообщение: ')

count_text1 = text1.count('!') + text1.count('?')
count_text2 = text2.count('!') + text2.count('?')

if count_text1 > count_text2:
    print(text1 + text2)
elif count_text2 > count_text1:
    print(text2 + text1)
else:
    print('Ой!!!')
