# me = {'name': 'Sherzod', 'age': 25, 'city': 'Tashkent'}
# print(me)
# me['job'] = 'developer'
# me['age'] = 44
# me.pop('city')
# print(me)

students = {
    "sher": [90, 100, 85],
    "madina": [98, 100, 88],
    "ziyovuddin": [85, 95, 90]
}
for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    print(f"{student}: {round(avg_grade, 2)}")

max_grade = max([max(grades) for grades in students.values()])
print(f"Максимальная оценка: {max_grade}")