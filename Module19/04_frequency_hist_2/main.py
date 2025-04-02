text = (input('Введите текст: ')).lower()
frequency = {}
inverted_frequencies = {}
for symbol in text:
    if symbol in frequency:
        frequency[symbol] += 1
    else:
        frequency[symbol] = 1

for letter, freq in sorted(frequency.items()):
    if not freq in inverted_frequencies:
        inverted_frequencies[freq] = [letter]
    else:
        inverted_frequencies[freq].append(letter)

print('Оригинальный словарь частот:')
for key, value in sorted(frequency.items()):
    print(key, ':', value)

print(f'Инвертированный словарь частот:')
for key, value in sorted(inverted_frequencies.items()):
    print(key, ':', value)


