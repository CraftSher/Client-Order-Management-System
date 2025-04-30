words_list = []

for i in range(3):
    print('Введите', i + 1, 'слово:', end= ' ')
    word = input().lower()
    words_list.append(word)

text = input('Введите текс: ').lower().split()


print('\nПодсчёт слов в тексте:')
for i in range(3):
    print(words_list[i], ':', text.count(words_list[i]))