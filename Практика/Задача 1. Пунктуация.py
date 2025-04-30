punctuation_marks = {'.', ',', ';', ':', '!', '?'}
text = set(input('Введите текст: '))
# punctuation_count = 0
#
# for sym in text:
#     if sym in punctuation_marks:
#         punctuation_count += 1
# print('Количество знаков пунктуации:', punctuation_count)
print("Количество знаков пунктуации:", len(text.intersection(punctuation_marks)))
