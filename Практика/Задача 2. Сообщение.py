text = input('Введите строку: ')
symbol = input('Введите дополнительный символ:')
duble = [x * 2 for x in text]
clue = [x + symbol for x in duble]
print('Список удвоенных символов', duble)
print('Склейка с дополнительным символом:', clue)
