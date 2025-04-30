# import requests
#
# def get_max_currency(data):
#     max_rate = float('-inf')
#     max_currency = ''
#
#     for elem in data:
#         if isinstance(elem, dict):
#             rate = float(elem.get('Rate', 0))
#             name = elem.get('CcyNm_RU', 'Неизвестно')
#             if rate > max_rate:
#                 max_rate = rate
#                 max_currency = name
#
#     return max_currency, max_rate
#
#
# url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
# response = requests.get(url)
# data = response.json()
#
# name, rate = get_max_currency(data)
# print(f'Самая дорогая валюта: {name} — {rate}')
#=========================================================
# import requests
#
# def get_max_currency(data):
#     currency = []
#     for elem in data:
#         if isinstance(elem, dict):
#             rate = float(elem.get('Rate', 0))
#             name = elem.get('CcyNm_RU', 'Неизвестно')
#             money = name, rate
#             currency.append(money)
#
#     return currency
#
#
# url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
# response = requests.get(url)
# data = response.json()
#
# result = get_max_currency(data)
# sorted_money = sorted(result, key=lambda x: x[1], reverse=True)
# print('Лидеры по курсам валют:')
# for i, (name, rate) in enumerate(sorted_money[:3]):
#     print(f'{i + 1}. {name}: {rate}')
#=========================================================
# import requests
#
# def get_max_min_diff_currency(data):
#     max_diff = float('-inf')
#     max_currency = ''
#     min_diff = float('inf')
#     min_currency = ''
#     for elem in data:
#         if isinstance(elem, dict):
#             diff = float(elem.get('Diff', 0))
#             name = elem.get('CcyNm_RU', 'Неизвестно')
#             if diff > max_diff:
#                 max_diff = diff
#                 max_currency = name
#             elif diff < min_diff:
#                 min_diff = diff
#                 min_currency = name
#
#     return max_currency, max_diff, min_currency, min_diff
#
#
# url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
# response = requests.get(url)
# data = response.json()
#
# max_currency, max_diff, min_currency, min_diff = get_max_min_diff_currency(data)
# print(f'Максимальный рост: {max_currency} - {max_diff} Максимальное падение: {min_currency} - {min_diff}')
#=========================================================
# import requests
#
# def get_max_min_list_currency(data):
#     max_diff = 10
#     min_diff = -10
#     max_list = []
#     min_list = []
#     for elem in data:
#         if isinstance(elem, dict):
#             diff = float(elem.get('Diff', 0))
#             name = elem.get('CcyNm_RU', 'Неизвестно')
#             if diff > max_diff:
#                 money_pls = name, diff
#                 max_list.append(money_pls)
#             elif diff < min_diff:
#                 money_min = name, diff
#                 min_list.append(money_min)
#
#     return max_list, min_list
#
# url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
# response = requests.get(url)
# data = response.json()
#
# max_list, min_list = get_max_min_list_currency(data)
# print('Резкий рост:')
# for i, (name, rate) in enumerate(max_list):
#     print(f'{i + 1}. {name}: +{rate}')
# print('Резкое падение:')
# for i, (name, rate) in enumerate(min_list):
#     print(f'{i + 1}. {name}: {rate}')
#=========================================================
import requests
import math
def get_stab_list_currency(data):
    stab_list = []
    for elem in data:
        if isinstance(elem, dict):
            diff = float(elem.get('Diff', 0))
            name = elem.get('CcyNm_RU', 'Неизвестно')
            money = name, diff
            stab_list.append(money)
    return stab_list

url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
response = requests.get(url)
data = response.json()

result = get_stab_list_currency(data)
stab_result = sorted(result, key=lambda n: abs(n[1]))
print('Тройка самых стабильных валют:')
for i, (name, rate) in enumerate(stab_result[:3]):
    print(f'{i + 1}. {name}: {rate}')