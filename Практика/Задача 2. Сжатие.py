# def text_coding(text):
#     if not text: #Проверка на пустую строку.
#         return ""
#     count, result = 1, "" #count = 1
#     for index, symbol in enumerate(text):
#         if index == len(text) - 1 or symbol != text[index + 1]:
#             result += f'{symbol}{count}'
#             if index < len(text) -1: #что бы не обнулять счетчик после последнего элемента.
#                 count = 1
#             else:
#                 count = 0
#         else:
#             count += 1
#     return result
#
# user_text = input('Введите строку: ')
# print('Закодированная строка:', text_coding(user_text))

def text_coding(text):
    if not text:
        return ''
    count, result = 1, ""
    for index, symbol in enumerate(text):
        if index == len(text) - 1 or symbol != text[index + 1]:
            result += f'{symbol}{count}'
            if index < len(text) - 1:
                count = 1
            else:
                count = 0
        else:
            count += 1
    return result

user_text = input('Введите строку: ')
print('Закодированная строка:', text_coding(user_text))




user_text = input('Введите строку: ')