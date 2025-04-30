# def number_sum(data):
#     total_sum = 0
#     if isinstance(data, dict):
#         for value in data.values():
#             total_sum += number_sum(value)
#     elif isinstance(data, list):
#         for item in data:
#             total_sum += number_sum(item)
#     elif isinstance(data, (int, float)):
#         total_sum += data
#     return total_sum
#
# data = {
#     'a': 5,
#     'b': {
#         'c': 10,
#         'd': [1, 2, {'e': 3}]
#     },
#     'f': [4, {'g': 6}]
# }
#
# print(number_sum(data))
#=================================================
# from tabulate import tabulate
#
# def analyze_data(data, counts=None, depth=0, seen_strings=None):
#     if counts is None:
#         counts = {'num': 0, 'str': 0, 'lst': 0, 'dct': 0, 'max_depth': 0, 'sum': 0, 'unique_str': 0, 'null': 0, 'bool': 0}
#     if seen_strings is None:
#         seen_strings = set()
#
#     counts['max_depth'] = max(counts['max_depth'], depth)
#
#     if isinstance(data, dict):
#         counts['dct'] += 1
#         for value in data.values():
#             analyze_data(value, counts, depth + 1, seen_strings)
#     elif isinstance(data, list):
#         counts['lst'] += 1
#         for item in data:
#             analyze_data(item, counts, depth + 1, seen_strings)
#     elif isinstance(data, str):
#         counts['str'] += 1
#         if data not in seen_strings:
#             counts['unique_str'] += 1
#             seen_strings.add(data)
#     elif isinstance(data, (int, float)):
#         counts['num'] += 1
#         counts['sum'] += data
#     elif data is None:
#         counts['null'] += 1
#     elif isinstance(data, bool):
#         counts['bool'] += 1
#
#     return counts
#
# my_data = {
#     'a': 5,
#     'b': {
#         'c': "text",
#         'd': [1, 2, {'e': "hello"}]
#     },
#     'f': [4, {'g': 6}, "end", "text"]
# }
#
# result = analyze_data(my_data)
# print(tabulate(result.items(), headers=['ТИП','КОЛИЧЕСТВО']))
#=================================================
# def number_sum(data):
#     total_sum = 0
#     if isinstance(data, dict):
#         if data.get("ignore") == True:
#             return 0
#         else:
#             for value in data.values():
#                 total_sum += number_sum(value)
#     elif isinstance(data, list):
#         for item in data:
#             total_sum += number_sum(item)
#     elif isinstance(data, (int, float)):
#         total_sum += data
#     return total_sum
#
# data = {
#     "a": 1,
#     "b": {
#         "ignore": True,
#         "c": 100,
#         "d": [1, 2]
#     },
#     "e": [3, {"f": 5, "ignore": True, "g": 10}, 4]
# }
#
# print(number_sum(data))
#=================================================
def clear_data(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            if "удалить" in key:
                return None  # Исключаем весь словарь, возвращая None
            cleaned_value = clear_data(value)
            if cleaned_value is not None and cleaned_value is not False:
                new_dict[key] = cleaned_value
        return new_dict if new_dict else None  # Возвращаем словарь или None, если он пуст после очистки
    elif isinstance(data, list):
        new_list = []
        for item in data:
            cleaned_item = clear_data(item)
            if cleaned_item is not None and cleaned_item is not False:
                new_list.append(cleaned_item)
        return new_list if new_list else None  # Возвращаем список или None, если он пуст
    elif data is None or data is False:
        return None  # Удаляем None и False
    else:
        return data  # Возвращаем остальные типы данных без изменений

data = {
    "a": 1,
    "удалить_это": 100,
    "b": {
        "c": None,
        "удалить": "удалить меня",
        "d": [1, {"удалить": 2, "x": False}]
    },
    "e": [None, {"z": 10}]
}

cleaned_data = clear_data(data)
print(cleaned_data)