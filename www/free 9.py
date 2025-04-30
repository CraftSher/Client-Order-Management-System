# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# n = int(input('Введите число: '))
# print(f'Факториал {n} =', factorial(n))
from sys import set_int_max_str_digits

# students = {}
# quantity = int(input('Сколько будет студентов? '))
#
# # Заполняем словарь данными
# for _ in range(quantity):
#     name = input('Введите имя студента: ')
#     age = int(input('Введите возраст студента: '))
#     students[name] = age

# print('Исходный словарь:', students)
#
# # Получаем возраст Bob, если он есть
# print('Возраст Bob:', students.get("Bob", "Не найден"))
#
# # Безопасное удаление Charlie
# students.pop('Charlie', None)
# print('После удаления Charlie:', students)
#
# # Добавляем нового студента
# students.update({'Zay': 11})
# print('После добавления Zay:', students)

# students = {}
# quantity = int(input('Сколько будет студентов? '))
# for _ in range(quantity):
#     name = input('Введите имя студента: ')
#     point = int(input('Введите бал студента: '))
#     students[name] = point
#
# print('Исходный список:', students)
#
# max_point = max(students.values())
# min_point = min(students.values())
#
# max_students = [name for name, point in students.items() if point == max_point]
# min_students = [name for name, point in students.items() if point == min_point]
#
# print(f'Студенты с максимальным баллом {max_point}: {max_students}')
# print(f'Студенты с минимальным баллом {min_point}: {min_students}')
#
# # Удаление всех студентов с минимальным баллом
# for student in min_students:
#     students.pop(student)
#
# print('Список после удаления студентов с мин. баллом:', students)
#
# students.update({'Zay': 100})
# print('После добавления нового студента:', students)
# print('Список после удаления студента с мин. балом:', students)
# students.update({'Zay': 100})
# print('После добавления нового студента:', students)

students = {}
quantity = int(input('Сколько будет студентов? '))
for _ in range(quantity):
    name = input(f'Введите имя {_ + 1} студента: ')
    point_str = input(f'Введите балы студента:{name} через пробел ')
    points = list(map(int,point_str.split()))
    students[name] = points
average_scores = {name: sum(points) / len(points) for name, points in students.items()}

print('Исходный список:', students)
best_student = max(average_scores, key=average_scores.get)
seak_student = min(average_scores, key=average_scores.get)
print(f'Студент с максимальным средним баллом: {best_student} ({average_scores[best_student]: .2f})')
print(f'Студент с минимальным средним баллом: {seak_student} ({average_scores[seak_student]: .2f})')
