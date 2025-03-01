# quantity = int(input('Кол-во сотрудников в офисе: '))
# ID = []
# for i in range(quantity):
#     ID_worker = int(input('ID сотрудника: '))
#     ID.append(ID_worker)
# question = int(input('Какой ID ищем? '))
#
# if question not in ID:
#     print('Сотрудник не работает')
# else:
#     print('Сотрудник на месте')


n = int(input('Кол-во сотрудников в офисе: '))
worker_id = []

for i in range(1, n + 1):
    employer_id = int(input(f'ID {i}-го сотрудника: '))
    worker_id.append(employer_id)
search_id = int(input('Какой ID ищем? '))
search = False
for id in worker_id:
    if id == search_id:
        search =True
if search:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает!')
