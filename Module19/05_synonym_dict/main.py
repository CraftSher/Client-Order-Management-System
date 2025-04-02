quantity = int(input('Введите количество пар слов: '))

dictionary_synonyms = {}

for i in range(quantity):
    pair = input(f'{i + 1} пара: ')
    words = pair.split('—')
    word1 = words[0]
    word2 = words[1]
    dictionary_synonyms[word1.lower().strip()] = word2.lower().strip()
    dictionary_synonyms[word2.lower().strip()] = word1.lower().strip()
while True:
    syn_word = (input('Введите слово: ')).lower()
    if syn_word in dictionary_synonyms:
        print('Синоним:', dictionary_synonyms[syn_word])
        break
    else:
        print('Такого слова в словаре нет.')

