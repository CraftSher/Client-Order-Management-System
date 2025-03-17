text = input('Введите строку: ')
start = text.index('h')
end = text.rindex('h')
new_text = text[start+1: end]
print('Развёрнутая последовательность между первым и последним h:', new_text[::-1])
