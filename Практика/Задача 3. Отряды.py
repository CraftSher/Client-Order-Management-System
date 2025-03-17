import random

squad1 = [random.randint(50, 80) for _ in range(10)]
squad2 = [random.randint(30, 60) for _ in range(10)]

state_squad3 = [('Погиб' if squad1[i_damage] + squad2[i_damage] > 100 else 'Выжил') for i_damage in range(10) ]

print('Урон первого отряда:', squad1)
print('Урон второго отряда:', squad2)
print('Состояние третьего отряда:', state_squad3)