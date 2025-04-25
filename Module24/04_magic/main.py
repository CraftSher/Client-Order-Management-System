class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return None

class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None

class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None

class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None

class Energy:
    def __add__(self, other):
        if isinstance(other, Water):
            return Super_steam()
        else:
            return None
#============================================
class Storm:
    def __init__(self):
        self.name = "Шторм"

    def __str__(self):
        return self.name


class Steam:
    def __init__(self):
        self.name = "Пар"

    def __str__(self):
        return self.name


class Mud:
    def __init__(self):
        self.name = "Грязь"

    def __str__(self):
        return self.name


class Lightning:
    def __init__(self):
        self.name = "Молния"

    def __str__(self):
        return self.name


class Dust:
    def __init__(self):
        self.name = "Пыль"

    def __str__(self):
        return self.name


class Lava:
    def __init__(self):
        self.name = "Лава"

    def __str__(self):
        return self.name


class Super_steam:
    def __init__(self):
        self.name = "Супер пар"

    def __str__(self):
        return self.name

water = Water()
air = Air()
fire = Fire()
earth = Earth()
energy = Energy()

result = water + air
result1 = water + fire
result2 = water + earth
result_self = energy + water
print(result)
print(result1)
print(result2)
print(result_self)

