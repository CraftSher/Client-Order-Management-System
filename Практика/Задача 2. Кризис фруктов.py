incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
print('Исходный список:', incomes)
print(f'Общий доход за год составил {sum(incomes.values())} рублей')

def get_value(x):
    return x[1]
min_name, min_value = min(incomes.items(), key=get_value)

print(f'Самый маленький доход у {min_name}. Он составляет {min(incomes.values())} рублей')
incomes.pop(min_name)
print(f'Итоговый словарь: {incomes}')