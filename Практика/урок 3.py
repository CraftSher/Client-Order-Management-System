text = input('Содержимое файла: ')
words_list = text.split()
print(words_list)

new_text = '---'.join(words_list)
print(new_text)

