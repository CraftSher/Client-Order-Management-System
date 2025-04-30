def get_person_name(seria, num):
    if (seria, num) in data:
        return data[(seria, num)]
    else:
        return "Данные не найдены"

data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}
seria = int(input('Введите серию паспорта: '))
num = int(input('Введите номер паспорта: '))
result = get_person_name(seria, num)
print(result)