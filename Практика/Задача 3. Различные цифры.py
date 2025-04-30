text = input('Введите текст: ')
digit =set()
for sym in text:
    if '0' <= sym <= '9':
        digit.add(sym)
print(''.join(digit))




