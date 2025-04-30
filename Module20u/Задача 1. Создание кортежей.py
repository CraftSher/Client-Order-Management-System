import random
first_tuple = tuple(random.randint(0, 5) for i in range(10))
second_tuple = tuple(random.randint(-5, 0) for i in range(10))
print(first_tuple, second_tuple)
third_tuple = first_tuple + second_tuple
zero = third_tuple.count(0)
print(f'в третьем кортеже {third_tuple}, количество нулей {zero}')
