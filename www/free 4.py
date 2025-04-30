# new_age = int(input('Age: '))
# student = {'name': 'John',
#            'age': 20,
#            'grade': 'A',
#            'city': 'London'
# }
# student['age'] = new_age
# student['hobby'] = 'football'
# del student['city']
# print(student)

# person = {
#     'name': 'Alice',
#     'age': 30,
#     'city': 'New York',
#     'job': 'Developer'
# }
# for key, values in person.items():
#     print(key, ':', values)

# students = {
#     'student1': {'name': 'John', 'age': 20, 'grade': 'A'},
#     'student2': {'name': 'Alice', 'age': 22, 'grade': 'B'}
# }
#
# for item in students:
#     print(students[item]['name'], students[item]['grade'])

students = {
    'student1': {'name': 'John', 'age': 20, 'grade': 'A'},
    'student2': {'name': 'Alice', 'age': 22, 'grade': 'B'}
}

while True:
    question = input('Хотите добавить студена? Да -1 Нет -2: ')
    if question == '1':
        student_name = input('Введите имя студента: ')
        student_age = input('Сколько лет студенту: ')
        student_grade = input('Введите оценку студента: ')

        if not student_age.isdigit():
            print('Ошибка: возраст необходимо указать числом!')
            continue
        students[f'student{len(students) + 1}'] = {'name': student_name, 'age': int(student_age), 'grade': student_grade}

    elif question == '2':
        break
    else:
        print('Введите правильное значение: ')

print('\nСписок студентов:')
for item in students:
    print(students[item]['name'], students[item]['grade'])

