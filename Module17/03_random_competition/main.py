import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
print('Первая команда:', first_team)
print('Вторая команда:', second_team)

# result = [(x if x > y else y) for x, y in zip(first_team, second_team)]
result = [(first_team[i] if first_team[i] > second_team[i] else second_team[i]) for i in range(20)]
print('Победители тура:', result)