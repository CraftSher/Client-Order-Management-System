# nums_sum = 0
# nums_count = 0
# try:
#     numbers_file = open('numbers.txt', 'r')
#     for i_line in numbers_file:
#         nums_sum += int(i_line)
#         nums_count += 1
#     numbers_file.close()
#     print('Среднее арим:', nums_sum / nums_count)
# except FileNotFoundError:
#     print("Такого файла не существует")
# except ValueError:
#     print('Нельзя преобразовать данные в целое число:')

def divide(number):
    return 10 / number

def sum_of_divided(left, right):
    div_sum = 0
    for i_num in range(left, right + 1):
        try:
            div_sum += divide(i_num)
            print(div_sum)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
    return div_sum

total = 0

try:
    numbers_file = open('numbers.txt', 'r')
    for i_line in numbers_file:
        nums_list = i_line.split()
        first_num = int(nums_list[0])
        second_num = int(nums_list[1])

        total += sum_of_divided(first_num, second_num)
    print('Общая сумма:', total)

except ZeroDivisionError:
    print('На ноль делить нельзя!')
