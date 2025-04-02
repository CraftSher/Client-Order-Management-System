text = input('Введите строку: ')
freq = {}
for letter in text:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1
odd_count = 0
for letter, count in freq.items():
    if count % 2 == 1:
        odd_count += 1
if odd_count > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')