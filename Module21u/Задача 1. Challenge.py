def factorial(num):
    if num == 1:
        return 1
    fact_n_minus_1 = factorial(num - 1)
    return num * fact_n_minus_1

num = int(input('Введите число для факториала: '))
num_fact = factorial(num)
print(num_fact)