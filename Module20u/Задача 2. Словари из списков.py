import random
import string

list1 = [random.choice(string.ascii_lowercase) for i in range(10)]
list2 = [random.choice(string.ascii_lowercase) for i in range(10)]
print('Первый список:',list1)
print('Второй список:',list2)
list1_dict = {}
list2_dict = {}
for index, letter in enumerate(list1):
    list1_dict[index] = letter
print('Первый словарь:',list1_dict)
for index, letter in enumerate(list2):
    list2_dict[index] = letter
print('Второй словарь:',list2_dict)