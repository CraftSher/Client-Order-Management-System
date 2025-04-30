# def analyze_grade(grades):
#     report = {}
#     for grade in grades:
#         report[grade] = grades.count(grade)
#     report['avarege'] = (sum(grades) / len(grades))
#
#     return report
#
# grades = [5, 4, 3, 5, 2, 5, 4, 4]
# result = analyze_grade(grades)
# print(result)
# # {'5': 3, '4': 3, '3': 1, '2': 1, 'average': 4.0}

# def create_product_info(name, price, in_stock=True):
#     product = {
#   'name': name,
#   'price': price,
#   'in_stock': in_stock}
#     return product
#
# user = create_product_info('Рис', 250)
# print(user)

# def print_students_info(students):
#     for name, info in students.items():
#         print(f'Имя студентов: {name}')
#         average = sum(info['оценки']) / len(info['оценки'])
#         print(f'Средняя оценка: {round(average, 2)}')
#         print(f'Город: {info['город']}')
#         print('--------------')
#
#
# students = {
#     'Алиса': {'оценки': [5, 4, 5], 'город': 'Москва'},
#     'Боб': {'оценки': [3, 4, 2], 'город': 'СПб'},
#     'Sher': {'оценки': [5, 5, 5], 'город': 'Tashkent'},
# 'Madina': {'оценки': [5, 5, 5], 'город': 'Tashkent'}
#
# }
# print_students_info(students)
def print_employers_info(employers):
    for name, info in employers.items():
        print(f'Имя сотрудник: {name} \nДолжность: {info["должность"]} \nЗарплата: {info["зарплата"]}')

employers = {
    'Иван': {'должность': 'Менеджер', 'зарплата': 50000},
    'Мария': {'должность': 'Программист', 'зарплата': 80000},
    'Дмитрий': {'должность': 'Дизайнер', 'зарплата': 60000},
}
print_employers_info(employers)