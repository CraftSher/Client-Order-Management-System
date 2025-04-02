line = input('Введите строку: ')
palindrome = ''

for letter in line:
    palindrome = letter + palindrome

if line == palindrome:
    print('Это палиндром.')
else:
    print('Это не палиндром')

