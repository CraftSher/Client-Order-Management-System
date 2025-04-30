# def print_factorial_num(n):
#     if n == 0:
#         return 1
#     return n * print_factorial_num(n - 1)
#
# n = int(input('Введите число: '))
# result = print_factorial_num(n)
# print(result)

# def total_sum_num(n):
#     if n == 0:
#         return 0
#     total = n + total_sum_num(n - 1)
#     return total
#
# n = int(input('Введите число: '))
# result = total_sum_num(n)
# print(result)

def find_max(my_list):
    max_value = float('-inf')
    for item in my_list:
        if isinstance(item, list):
            item_max = find_max(item) #Рекурсивный вызов
            max_value = max(max_value, item_max) #Сравнение результатов рекурсии
        else:
            max_value = max(max_value, item) #Сравнение с не списочными элементами
    return max_value

my_list = [1, 3, [4, 5, [6, 7]], 2]
result = find_max(my_list)
print(result)


