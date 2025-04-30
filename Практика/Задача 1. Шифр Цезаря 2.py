alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input("Введите текст: ").lower()
delta = int(input("Введите сдвиг: "))

result = []
for symbol in text:
    if symbol in alphabet:
        cipher = (alphabet.find(symbol) + delta)  % len(alphabet)
        new_symbol = alphabet[cipher]
    else:
        new_symbol = symbol
    result.append(new_symbol)
# Через list comprehension
# result = [
#     alphabet[(alphabet.find(symbol) + delta) % len(alphabet)] if symbol in alphabet
#     else symbol
#     for symbol in text
# ]

print(''.join(result))