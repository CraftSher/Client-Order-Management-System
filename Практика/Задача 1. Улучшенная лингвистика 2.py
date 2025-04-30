words = [input('Введите слово: ') for _ in range(3)]
text = input('Введите текст: ')
word_count = [text.count(word) for word in words]

print(word_count)