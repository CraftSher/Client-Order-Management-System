# def sum_nested_list(data):
#     sum = 0
#     if isinstance(data, list):
#         for item in data:
#             sum += sum_nested_list(item)
#     else:
#         sum += data
#     return sum
# nums = [1, 2, [3, 4, [5, 6]], 7]
#
# result = sum_nested_list(nums)
# print(result)
#===============================================
# def sum_even_numbers(data):
#     sum = 0
#     if isinstance(data, list):
#         for item in data:
#             sum += sum_even_numbers(item)
#     else:
#         if data % 2 == 0:
#             sum += data
#     return sum
# nums = [1, 2, [3, 4, [5, 6, 8]], 7]
#
# result = sum_even_numbers(nums)
# print(result)
#===============================================
# def max_length_name(data):
#     max_name = ''
#     max_len = 0
#
#     if isinstance(data, dict):
#         for value in data.values():
#             name, length = max_length_name(value)
#             if length > max_len:
#                 max_len = length
#                 max_name = name
#
#     elif isinstance(data, list):
#         for item in data:
#             if isinstance(item, dict) and 'name' in item:
#                 if len(item['name']) > max_len:
#                     max_len = len(item['name'])
#                     max_name = item['name']
#             else:
#                 name, length = max_length_name(item)
#                 if length > max_len:
#                     max_len = length
#                     max_name = name
#
#     return max_name, max_len
#
# catalog = {
#     "Electronics": {
#         "Laptops": [{"name": "Laptop A"}, {"name": "Super Mega Laptop B"}],
#         "Phones": [{"name": "Phone A"}, {"name": "Smartphone X Pro Ultra"}]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [{"name": "Vacuum A"}, {"name": "Vacuum Cleaner Model Z"}],
#         "Microwaves": [{"name": "Microwave A"}, {"name": "Compact Microwave B"}]
#     }
# }
#
# name, length = max_length_name(catalog)
# print(f'Самое длинное имя товара: {name} ({length} символов)')
#===============================================
# def count_products(data):
#     count = 0
#     if isinstance(data, dict):
#         for value in data.values():
#             count += count_products(value)
#     elif isinstance(data, list):
#         for item in data:
#             if isinstance(item, dict) and 'name' in item:
#                 count += 1
#             else:
#                 count += count_products(item)
#     return count
#
#
# catalog = {
#     "Electronics": {
#         "Laptops": [{"name": "Laptop A"}, {"name": "Super Mega Laptop B"}],
#         "Phones": [{"name": "Phone A"}, {"name": "Smartphone X Pro Ultra"}]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [{"name": "Vacuum A"}, {"name": "Vacuum Cleaner Model Z"}],
#         "Microwaves": [{"name": "Microwave A"}, {"name": "Compact Microwave B"}]
#     }
# }
#
# result = count_products(catalog)
# print(result)
#===============================================
# def lenght_name_products(data, lenght):
#     new_list = []
#     if isinstance(data, dict):
#         for value in data.values():
#             new_list += lenght_name_products(value, lenght)
#     elif isinstance(data, list):
#         for item in data:
#             if isinstance(item, dict) and 'name' in item:
#                 if len(item["name"]) > lenght:
#                     new_list.append(item["name"])
#             else:
#                 new_list += lenght_name_products(item, lenght)
#     return new_list
#
#
# catalog = {
#     "Electronics": {
#         "Laptops": [{"name": "Laptop A"}, {"name": "Super Mega Laptop B"}],
#         "Phones": [{"name": "Phone A"}, {"name": "Smartphone X Pro Ultra"}]
#     },
#     "Home Appliances": {
#         "Vacuum Cleaners": [{"name": "Vacuum A"}, {"name": "Vacuum Cleaner Model Z"}],
#         "Microwaves": [{"name": "Microwave A"}, {"name": "Compact Microwave B"}]
#     }
# }
#
# result = lenght_name_products(catalog, 12)
# print(result)
#===============================================

nums = [5, 3, 8, 1]

sort_num = []
while nums:
    min_num = nums[0]
    min_index = 0
    for i, num in enumerate(nums):
        if num < min_num:
            min_num = num
            min_index = i
    sort_num.append(min_num)
    del nums[min_index]

print(sort_num)

