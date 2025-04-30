# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         # Флаг, чтобы узнать, были ли изменения
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:  # Если элементы идут в неправильном порядке
#                 arr[j], arr[j+1] = arr[j+1], arr[j]  # Меняем местами
#                 swapped = True
#         # Если за проход не было изменений, список уже отсортирован
#         if not swapped:
#             break
#     return arr
#
# # Пример
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("Отсортированный массив:", bubble_sort(arr))
#=========================================================
# def sum_numbers(numbers):
#     if not numbers:
#         return 0
#     else:
#         return numbers[0] + sum_numbers(numbers[1:])
# numbers = [1, 2, 3, 4]
# result = sum_numbers(numbers)
# print(result)
#=========================================================
# def max_numbers(numbers):
#     if len(numbers) == 1:
#         return numbers[0]
#     else:
#         max_rest = max_numbers(numbers[1:])
#         return max(numbers[0], max_rest)
# numbers = [5, 8, 2, 10, 3]
# result = max_numbers(numbers)
# print(result)
#=========================================================
# def sum_nested(numbers):
#     total = 0
#     for element in numbers:
#         if isinstance(element, list):
#             # если элемент — список, вызываем рекурсивно
#             total += sum_nested(element)
#         else:
#             if isinstance(element, int):
#                 total += element
#     return total
#
# nested = [1, [2, 3], [4, [5, 6]], 7]
# print(sum_nested(nested))  # должно вывести 28
#=========================================================
# def max_nested(numbers):
#     max_value = float('-inf')
#     for element in numbers:
#         if isinstance(element, list):
#             max_value = max(max_value, max_nested(element))
#         else:
#             max_value = max(max_value, element)
#     return max_value
#
# nested = [1, [12, 3], [4, [5, 26]], 7]
# print(max_nested(nested))
#=========================================================
# def max_nested(numbers):
#     max_value = float('-inf')
#     for elem in numbers:
#         if isinstance(elem, list):
#             max_value = max(max_value, max_nested(elem))
#         else:
#             max_value = max(max_value, elem)
#     return max_value
#
# nested_list = [1, [2, [3, [4]]], 5]
# print(max_nested(nested_list))
#=========================================================
# def sum_nested(numbers):
#     total_sum = 0
#     for elem in numbers:
#         if isinstance(elem, list):
#             total_sum += sum_nested(elem)
#         else:
#             total_sum += elem
#     return total_sum
#
#
# nested = [1, [2, [3, [4]]], 5]
# print(sum_nested(nested))  ## Должно вывести: 15
#=========================================================
# def average_nested(lst):
#     def helper(sublist):
#         total = 0
#         count = 0
#         for elem in sublist:
#             if isinstance(elem, list):
#                 sub_total, sub_count = helper(elem)
#                 total += sub_total
#                 count += sub_count
#             else:
#                 total += elem
#                 count += 1
#         return total, count
#
#     total_sum, total_count = helper(lst)
#     return total_sum / total_count
#
# nested = [1, [2, [3, [4]]], 5]
# print(average_nested(nested))

#=========================================================
# def find_max(data):
#     max_value = float('-inf')
#
#     if isinstance(data, dict):
#         for value in data.values():
#             max_value = max(max_value, find_max(value))
#     elif isinstance(data, list):
#         for item in data:
#             max_value = max(max_value, find_max(item))
#     elif isinstance(data, (int, float)):
#         max_value = data
#
#     return max_value
#
#
# data = {
#     "a": [1, 2, {"b": 10, "c": [3, 4]}],
#     "d": {"e": [5, {"f": 20}], "g": 6},
#     "h": 0
# }
#
# print(find_max(data))  # Должно вывести: 20
#=========================================================
# def find_min(data):
#     min_value = float('inf')
#
#     if isinstance(data, dict):
#         for value in data.values():
#             min_value = min(min_value, find_min(value))
#     elif isinstance(data, list):
#         for item in data:
#             min_value = min(min_value, find_min(item))
#     elif isinstance(data, (int, float)):
#         return data
#
#     return min_value
#
#
# data = {
#     "x": [9, {"y": [3, 8]}, 15],
#     "z": {"w": 2, "v": [7, {"u": -5}]},
#     "k": 12
# }
#
# print(find_min(data))
#=========================================================
# def count_numbers(data):
#     count = 0
#     if isinstance(data, dict):
#         for value in data.values():
#             count += count_numbers(value)
#     elif isinstance(data, list):
#         for item in data:
#             count += count_numbers(item)
#     elif isinstance(data, (int, float)):
#         count += 1
#     return count
#
# data = {
#     "a": [1, 2, {"b": 10, "c": [3, 4]}],
#     "d": {"e": [5, {"f": 20}], "g": 6},
#     "h": 0
# }
#
# print(count_numbers(data))
#=========================================================
# def calculate_total(data):
#     total_price = 0
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if key == 'price' and isinstance(value, (int, float)):
#                 total_price += value
#             else:
#                 total_price += calculate_total(value)
#     elif isinstance(data, list):
#         for item in data:
#             total_price += calculate_total(item)
#
#     return total_price
#
#
# orders = {
#     "orders": [
#         {"id": 1, "price": 100},
#         {"id": 2, "items": [{"price": 200}, {"price": 150}]},
#         {"id": 3, "details": {"info": {"price": 50}}},
#         [{"price": 300}, {"id": 4, "extra": {"price": 75}}],
#         {"misc": [10, 20, {"something": {"price": 25}}]}
#     ]
# }
# print(calculate_total(orders))
#=========================================================
# def total_price_productions(data):
#     total = 0
#     if isinstance(data, dict):
#         if 'price' in data:
#             price = data['price']
#             quantity = data.get('quantity', 1)  # если нет quantity, считать как 1
#             total += price * quantity
#         for value in data.values():
#             total += total_price_productions(value)
#     elif isinstance(data, list):
#         for item in data:
#             total += total_price_productions(item)
#     return total
#
#
# orders = {
#     "orders": [
#         {"id": 1, "price": 100, "quantity": 2},                         # 200
#         {"id": 2, "items": [{"price": 200, "quantity": 1}, {"price": 150}]},  # 200 + 150
#         {"id": 3, "details": {"info": {"price": 50, "quantity": 3}}},   # 150
#         [{"price": 300, "quantity": 2}, {"id": 4, "extra": {"price": 75}}],  # 600 + 75
#         {"misc": [10, 20, {"something": {"price": 25, "quantity": 4}}]} # 100
#     ]
# }
#
# print(total_price_productions(orders))
#=========================================================
def total_order_price(data):
    orders = {}
    for item in data:
        if isinstance(item, dict):
            item_id = item.get('id')  # Получаем уникальный id товара
            if item_id:  # Проверяем, есть ли id
                total_price = item['price'] * item['quantity']  # Вычисляем общую стоимость товара
                if item_id in orders:
                    orders[item_id] += total_price  # Добавляем к существующему значению
                else:
                    orders[item_id] = total_price  # Добавляем новый товар
    return orders

orders = {
    "orders": [
        {"id": 1, "price": 100, "quantity": 2},
        {"id": 2, "price": 200, "quantity": 3},
        {"id": 1, "price": 100, "quantity": 1},
        {"id": 3, "price": 150, "quantity": 4},
        {"id": 2, "price": 200, "quantity": 2}
    ]
}

# Вызываем функцию с передачей списка товаров
order_totals = total_order_price(orders["orders"])

# Выводим результат
for key, value in order_totals.items():
    print(f"Item ID: {key}, Total Price: {value}")