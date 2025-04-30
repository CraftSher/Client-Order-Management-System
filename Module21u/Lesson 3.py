def try_to_change_values(some_list, num):
    for i_index, i_val in enumerate(some_list):
        some_list[i_index] += 10
    num += 10


my_list = [1, 2, 3]
number = 100

try_to_change_values(my_list, number)
print(my_list, number)