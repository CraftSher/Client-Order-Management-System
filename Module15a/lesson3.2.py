words_list = [['', 0], ['', 0], ['', 0]]

for i in range(3):
    print('Введите', i + 1, 'слово:', end= ' ')
    word = input()
    words_list[i][0] = word

text = input('Слово из текста: ')
while text != 'end':
    for index in range(3):
        if words_list[index][0] == text:
            words_list[index][1] += 1
    text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте:')
for i in range(3):
    print(words_list[i][0], ':', words_list[i][1])