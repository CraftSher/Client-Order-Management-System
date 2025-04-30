students = {
    "Alice": [5, 4, 3, 5],
    "Bob": [3, 3, 4, 4],
    "Charlie": [5, 5, 4, 3]
}
print(f'Исходный список студентов: {students}')
average_scores = {name: sum(points) / len(points) for name, points in students.items()}
print(f'Средняя оценка студентов: {average_scores}')
max_value = max(average_scores, key=average_scores.get)
min_value = min(average_scores, key=average_scores.get)
max_students = [name for name, avg in average_scores.items() if avg == average_scores[max_value]]
min_students = [name for name, avg in average_scores.items() if avg == average_scores[min_value]]
print(f'Студенты с самым высоким средним балом: {max_students}, {average_scores[max_value]}')
print(f'Студенты с самым низким средним балом: {min_students}, {average_scores[min_value]}')
for student in min_students:
    students.pop(student)
print(f'Обнавленный список: {students}')
students['Jimm'] = [4, 5, 5, 3]
print(f'Обнавленный список: {students}')