line = input('Введите слово: ')
palindrome = ''

for letter in line:
    palindrome = letter + palindrome

if line == palindrome:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

