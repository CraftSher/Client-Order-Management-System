text = input('Введите сообщение строчными буквами: ')
shift = int(input('Введите сдвиг: '))
encrypted_message = []
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for i in text:
    if i in alphabet:
        index = alphabet.index(i)
        new_index = (index + shift) % len(alphabet)
        encrypted_message.append(alphabet[new_index])
    elif i == ' ' or i == '.':
        encrypted_message.append(i)

print('Зашифрованное сообщение:', ''.join(encrypted_message))

