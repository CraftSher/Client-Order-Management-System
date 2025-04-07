# TODO здесь писать код
import random
numbers = [random.randint(0, 10) for _ in range(10)]
print(f'Оригинальный список: {numbers}')
new_numbers = [tuple(numbers[i:i + 2]) for i in range(0, len(numbers), 2)]
print(f'Новый список: {new_numbers}')

numbers = [random.randint(0, 10) for _ in range(10)]
print(f'Оригинальный список: {numbers}')
new_numbers = list(zip(numbers[::2], numbers[1::2]))
print(f'Новый список: {new_numbers}')