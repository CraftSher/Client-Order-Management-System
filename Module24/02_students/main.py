class Student:
    def __init__(self, name, number, grades):
        self.student_name = name
        self.group_number = number
        self.student_grades = grades
    def get_average(self):
        return sum(self.student_grades) / len(self.student_grades)


students = []
for i in range(10):
    name = input(f'Введите имя {i + 1} студента: ')
    st_gr = input(f'Введите группу студента: ')
    grades = list(map(int, input('Введите 5 оценок через запятую: ').split(',')))
    student = Student(name, st_gr, grades)
    students.append(student)


sorted_students = sorted(students, key= lambda student: student.get_average(), reverse=True)
for student in sorted_students:
    print(student.student_name, student.group_number, student.get_average())
