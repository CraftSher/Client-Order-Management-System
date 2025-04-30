# text = input('Введите сообщение строчными буквами: ')
# shift = int(input('Введите сдвиг: '))
# encrypted_message = []
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# for i in text:
#     if i in alphabet:
#         index = alphabet.index(i)
#         new_index = (index + shift) % len(alphabet)
#         encrypted_message.append(alphabet[new_index])
#     elif i == ' ' or i == '.':
#         encrypted_message.append(i)
#
# print('Зашифрованное сообщение:', ''.join(encrypted_message))

def caeser_cipher(txt, user_shift):
    char_list = [(alphabet[(alphabet.index(i) + user_shift) % len(alphabet)] if i != ' ' else ' ') for i in txt]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение строчными буквами: ')
shift = int(input('Введите сдвиг: '))
encrypted_message = caeser_cipher(text, shift)

print('Зашифрованное сообщение:', encrypted_message)
