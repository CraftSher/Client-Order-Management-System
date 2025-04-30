text = (input('Введите текст: ')).lower()
frequency = {}
for symbol in text:
    if symbol in frequency:
        frequency[symbol] += 1
    else:
        frequency[symbol] = 1

for letter, freq in sorted(frequency.items()):
    print(letter, ':', freq)

print('Максимальная частота:', max(frequency.values()))