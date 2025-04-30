import math
def cylinder(r, h):
    lateral_area = 2 * math.pi * r * h
    area_cylinder = 2 * math.pi * r * (h+r)
    return lateral_area, area_cylinder




radius = float(input('Введите радиус цилиндра: '))
height = float(input('Введите высоту цилиндра: '))

lateral, total_area = cylinder(radius, height)
print(f'Площадь боковой поверхности {round(lateral, 2)}, Полная площадь {round(total_area, 2)}')
