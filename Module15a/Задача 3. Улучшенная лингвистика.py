words_list = []
counts = [0, 0, 0]

for i in range(3):
    word = input(f'Введите {i + 1} слово:')
    words_list.append(word)

text = input('Слово из текста: ')
while text != 'end':
    for index in range(3):
        if words_list[index] == text:
            counts[index] += 1
    text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте:')
for i in range(3):
    print(words_list[i], ':', counts[i])