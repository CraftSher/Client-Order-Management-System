class Unit:
    def __init__(self, health):
        self._health = health

    def get_damage(self, damage):
        print('Юнит не получил урона!')

    def get_health(self):
        return self._health

class Soldier(Unit):
    def __init__(self, health):
        super().__init__(health)
    def get_damage(self, damage):
        self._health -= damage
        self._health = max(0, self._health)
        if self._health == 0:
            print('Солдат погиб!')

class Citizen(Unit):
    def __init__(self, health):
        super().__init__(health)
    def get_damage(self, damage):
        self._health -= 2 * damage
        self._health = max(0, self._health)
        if self._health == 0:
            print('Гражданский погиб!')

soldier1 = Soldier(100)
citizen1 = Citizen(50)

print(f"Здоровье солдата: {soldier1.get_health()}")
print(f"Здоровье гражданина: {citizen1.get_health()}")

soldier1.get_damage(30)
citizen1.get_damage(20)

print(f"Здоровье солдата после урона: {soldier1.get_health()}")
print(f"Здоровье гражданина после урона: {citizen1.get_health()}")

soldier1.get_damage(80)
citizen1.get_damage(10)
citizen1.get_damage(10) # Еще урон, чтобы погиб

print(f"Здоровье солдата после второго урона: {soldier1.get_health()}")
print(f"Здоровье гражданина после второго урона: {citizen1.get_health()}")


