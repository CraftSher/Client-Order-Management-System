text = input('Введите текст: ')
upper_count = len([letter for letter in text if letter.isupper()])
lower_count = len([letter for letter in text if letter.islower()])

if upper_count > lower_count:
    print('Результат: ', text.upper())
else:
    print('Результат: ', text.lower())