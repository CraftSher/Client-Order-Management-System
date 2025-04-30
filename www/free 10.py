#import random
#number_list = [random.randint(1, 10) for _ in range(5)]
#print('Исходный список:', number_list)
#print(f'Первый элемент: {number_list[0]}, последний элемент: {number_list[-1]}')
#number_list.append(100)
#print('Список после добавления:', number_list)
#number_list.pop(1)
#print('Список после удаления 2го элемента:', number_list)
from tkinter.font import names

# student = {"Name": "Zayniddin", "Age": 10, "Grade": 100}
# print(student["Name"])
# student["Age"] = 21
# student["City"] = "Tashkent"
# print(student)

# students = {}
# quantity = int(input('Сколько будет студентов? '))
# for i in range(quantity):
#     name = input(f'Введите имя {i+1} студента: ')
#     age = int(input(f'Введите возраст {name} '))
#     students[name] = age
# print('Список студентов:', students)
# print('Возраст Bob:', students.get("Bob", "Не найден"))
# min_age = min(students.values())
# min_students = [name for name, age in students.items() if age == min_age]
# print('Самый молодой студент:',min_students)
# for student in min_students:
#     students.pop(student)
#
# print('Обновленный список:', students)
# students['sher'] = 44
# print('Обновленный список после добавления:', students)

# students = {}
# quantity = int(input('Сколько будет студентов? '))
# for i in range(quantity):
#     name = input(f'Введите имя {i+1} студента: ')
#     grade = input(f'Введите баллы студента {name} через пробел: ')
#     grades = list(map(int, grade.split()))
#     students[name] = grades
#
# # Вычисляем средние баллы
# average_scores = {name: sum(points) / len(points) for name, points in students.items()}
#
# print('Исходный список:', students)
#
# # Определяем лучших и слабых студентов
# best_student = max(average_scores, key=average_scores.get)
# seak_student = min(average_scores, key=average_scores.get)
# min_students = [name for name, avg in average_scores.items() if avg == average_scores[seak_student]]
#
# print(f'Студент с максимальным средним баллом: {best_student} ({average_scores[best_student]:.2f})')
# print(f'Студенты с минимальным средним баллом: {min_students} ({average_scores[seak_student]:.2f})')
#
# # Удаляем всех студентов с минимальным баллом
# for student in min_students:
#     students.pop(student)
#
# print('Обновленный список после удаления:', students)
#
# # Добавляем нового студента
# students['Bob'] = [45, 50, 60]
# print('Обновленный список после добавления:', students)

# students = {}
# quantity = int(input('Сколько будет студентов? '))
# for i in range(quantity):
#     name = input(f'Введите имя {i+1} студента: ')
#     grade = input(f'Введите баллы студента {name} через пробел: ')
#     grades = list(map(int, grade.split()))
#     students[name] = grades
#
# # Вычисляем средние баллы
# average_scores = {name: sum(points) / len(points) for name, points in students.items()}
#
# # Находим максимальный и минимальный балл среди всех студентов
# max_point = max(map(max, students.values()))
# min_point = min(map(min, students.values()))
#
# # Ищем студентов, у которых максимальный или минимальный балл
# max_students = [name for name, points in students.items() if max(points) == max_point]
# min_students = [name for name, points in students.items() if min(points) == min_point]
#
# print('Исходный список:', students)
#
# # Определяем лучших и слабых студентов по среднему баллу
# best_student = max(average_scores, key=average_scores.get)
# weak_students = [name for name, avg in average_scores.items() if avg == min(average_scores.values())]
#
# print(f'Студенты с максимальным баллом {max_point}: {max_students}')
# print(f'Студенты с минимальным баллом {min_point}: {min_students}')
# print(f'Студент с максимальным средним баллом: {best_student} ({average_scores[best_student]:.2f})')
# print(f'Студенты с минимальным средним баллом: {weak_students} ({average_scores[weak_students[0]]:.2f})')
#
# # Удаляем всех студентов с минимальным средним баллом
# for student in weak_students:
#     students.pop(student)
#
# print('Обновленный список после удаления:', students)
#
# # Добавляем нового студента
# students['Bob'] = [45, 50, 60]
# print('Обновленный список после добавления:', students)

students = {
    "Alice": [5, 4, 3, 5],
    "Bob": [3, 3, 4, 4],
    "Charlie": [5, 5, 4, 3]
}

grades_count = {}  # Словарь для подсчета оценок

for points in students.values():  # Перебираем списки оценок
    for grade in points:  # Перебираем каждую оценку
        if grade in grades_count:
            grades_count[grade] += 1  # Увеличиваем счетчик
        else:
            grades_count[grade] = 1  # Добавляем новую оценку

print("Количество каждой оценки:", grades_count)

