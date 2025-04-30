import random
def change(nums):
    nums_list = list(nums)
    index = random.randint(0, 5) % len(my_nums)
    value = random.randint(100, 1000)
    nums_list[index]= value
    new_nums = tuple(nums_list)
    return nums, value

my_nums = 1, 2, 3, 4, 5
new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums2, rand_val2 = change(new_nums)  # Получаем новый кортеж и случайное число
rand_val += rand_val2  # Складываем только случайные числа
print(new_nums2, rand_val)  # Выводим новый кортеж и сумму случайных чисел