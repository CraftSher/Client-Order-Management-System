text = input('Введите текст: ')
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
list_vowels = [i for i in text if i in vowels]
print('Список гласных букв: ', list_vowels)
print('Длина списка:', len(list_vowels))

