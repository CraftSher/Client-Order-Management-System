# my_dict = {'Англия': 'Лондон', 'Узбекистан': 'Ташкент', 'Франция': 'Париж'}
# country = input('Введите название страны: ')
# if country in my_dict:
#     print('Столица', country,':', my_dict[country])
# else:
#     print('Такой страны нет в базе.')

# my_dict = {'Шерзод': 44, 'Мадина': 38, 'Зумрадхон': 15, 'Зайниддин': 11}
# name = input('Введите имя: ')
# if name in my_dict:
#     print(f'{name}: {my_dict[name]} лет')
# else:
#     age = int(input('Сколько лет: '))
#     my_dict[name] = age
#     print(my_dict)

# my_dict = {'Мастер и Маргарита': 'Михаил Булгаков', 'Война и мир': 'Лев Толстой', 'Преступление и наказание': 'Фёдор Достоевский', '1984': 'Джордж Оруэлл', 'Убить пересмешника': 'Харпер Ли'}
# book = input('Введите название книги: ')
# if book in my_dict:
#     my_dict.pop(book)
#     print('Книга удалена')
# else:
#     print('Такой книги нет в базе')
# print(my_dict)

# population_millions = {
#     "Китай": 1444,
#     "Индия": 1393,
#     "США": 331,
#     "Индонезия": 274,
#     "Пакистан": 221
# }
# country = input('Введите название страны: ')
# if country in population_millions:
#     new_population = int(input('Введите новое значение популяции в миллионах: '))
#     population_millions[country] = new_population
#     print('Обновленный список стран:', population_millions)
# else:
#     print('Такой страны нет в базе')

students = {}
quantity = int(input('Сколько будет студентов? '))

for _ in range(quantity):
    name = input('Введите имя студента: ')
    point = int(input('Введите средний балл студента: '))
    students[name] = point
print(students)
new_name = input('Введите имя студента: ')
if new_name in students:
    print(f'Средний бал {new_name}: {students[new_name]} баллов')
else:
    print('Такого студента нету в списке.')