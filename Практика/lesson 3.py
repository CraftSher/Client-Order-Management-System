text = input('Содержимое файла: ')
word_list = text.split()

print(word_list)
new_text = '---'.join(word_list)
print(new_text)
# for word in word_list:
#     new_text += '---' + word
#
# print(new_text[3:])