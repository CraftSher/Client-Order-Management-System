with open('zen.txt', 'r') as zen:
    text = zen.readlines()
    reverse_text = text[::-1]
for line in reverse_text:
    print(line, end= '')

