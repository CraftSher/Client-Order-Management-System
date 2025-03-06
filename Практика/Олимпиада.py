n = int(input('Кол-во участников:'))
k = int(input('Кол-во участников в команде:'))
num = 1
members = []

for _ in range(n // k):
    if n % k != 0:
        print(n, 'участников невозможно поделить на команды по', k, 'человек!')

    else:
        members.append(list(range(num, num + k)))
print(members)
