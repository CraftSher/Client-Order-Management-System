array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Задание № 1
common_elements = []
for elem in array_1:
    if elem in array_2 and elem in array_3:
        common_elements.append(elem)
print('Решение без множеств:', common_elements)

array_1_set = set(array_1)
array_2_set = set(array_2)
array_3_set = set(array_3)

print('Решение с множествами:', list(array_1_set & array_2_set & array_3_set))

# Задание № 2

unique_elements =[]

for elem in array_1:
    if not elem in array_2 and not elem in array_3:
        unique_elements.append(elem)
print('Решение без множеств:', unique_elements)

array_1_set = set(array_1)
array_2_set = set(array_2)
array_3_set = set(array_3)

print('Решение с множествами:', list(array_1_set - (array_2_set | array_3_set)))