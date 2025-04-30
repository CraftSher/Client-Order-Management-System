# def sum_nested(numbers):
#     total = 0
#     for elem in numbers:
#         if isinstance(elem, int):
#             total += elem
#         else:
#             if isinstance(elem, list):
#                 total += sum_nested(elem)
#     return  total
#
# numbers = [1, [2, 3], [4, [5, 6], 7], 8]
#
# result = sum_nested(numbers)
# print(result)

#++++++=====================================

# def sum_all_numbers(data):
#     total = 0
#     for elem in data:
#         if isinstance(elem, int):
#             total += elem
#         elif isinstance(elem, list):
#             total += sum_all_numbers(elem)
#         elif isinstance(elem, dict):
#             for sub_value in elem.values():
#                 if isinstance(sub_value, int):
#                     total += sub_value
#                 else:
#                     total += sum_all_numbers(sub_value)
#
#     return total
#
# data = [
#         5,
#         {"a": 10, "b": [2, 3, {"c": 4}]},
#         [6, {"d": 1, "e": [7, {"f": 8}]}],
#         9
#     ]
#
# result = sum_all_numbers(data)
# print(result)
#++++++=====================================

def age_sorting(data):
    sorted_list = sorted(data, key=lambda item: item["age"])  # Исправленная строка
    return sorted_list

def report_men(data):
    report = []
    for person in data:
        report.append(f"Name: {person['name']}, Age: {person['age']}")
    return "\n".join(report)

def recursive_printer(obj, indent=0):
    if isinstance(obj, dict):
        for key, value in obj.items():
            print(' ' * indent + str(key))
            if isinstance(value, (dict, list)):
                recursive_printer(value, indent+1)
            elif isinstance(value, (int, str)):
                print(' ' * (indent + 1) + str(value))
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, (dict, list)):
                recursive_printer(item, indent+1)
            if isinstance(item, (int, str)):
                print(' ' * (indent + 1) + str(item))
    else:
        print(obj)

data = [
    {"name": "Ali", "age": 25, "address": {"city": "Tashkent", "zip": 1000}},
    {"name": "Zarina", "age": 30, "address": {"city": "Bukhara", "zip": 2000}},
    {"name": "Bekzod", "age": 22, "address": {"city": "Samarkand", "zip": 3000}},
    {"name": "Dilshod", "age": 28, "address": {"city": "Andijan", "zip": 4000}}
]

result = age_sorting(data)
result1 = report_men(data)
print(result)
print(result1)
recursive_printer(data, indent=0)
