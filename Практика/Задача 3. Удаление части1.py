import random
n = int(input("Введите количество чисел N: "))
numbers = [random.randint(-10, 10) for _ in range(n)]
a = random.randint(0, len(numbers) - 2)
b = random.randint(a + 1, len(numbers) - 1)

print(numbers, a, b)
print(numbers[:a])

print(numbers[b + 1:])
numbers = numbers[:a] + numbers[b + 1:]
print(numbers)




