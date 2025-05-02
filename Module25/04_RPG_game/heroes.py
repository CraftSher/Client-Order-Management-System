class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.magic_power = self.get_power() * 3

    def attack(self, target):
        damage = self.get_power() / 2
        target.take_damage(damage)

    def take_damage(self, damage):
        real_damage = damage * 1.2
        super().take_damage(real_damage)

    def heal(self, target):
        healing = self.magic_power
        new_hp = min(target.get_hp() + healing, target.max_hp)
        target.set_hp(new_hp)
        print(f"{self.name} лечит {target.name} на {healing} HP. Новое здоровье: {new_hp}")

    def make_a_move(self, friends, enemies):
        target = min(friends, key=lambda f: f.get_hp())
        if target.get_hp() < 100:
            self.heal(target)
        else:
            target = min(enemies, key=lambda enemy: enemy.get_hp())
            self.attack(target)

    def __str__(self):
        return f"{self.name}: Здоровье: {self.get_hp()}, Сила: {self.get_power()}, Магическа сила: {self.magic_power}"



class Tank(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.defense = 1
        self.shield_up = False

    def attack(self, target):
        damage = self.get_power() / 2
        target.take_damage(damage)

    def take_damage(self, damage):
        real_damage = damage / self.defense
        super().take_damage(real_damage)

    def raise_shield(self):
        if not self.shield_up:
            self.defense *= 2
            self.set_power(self.get_power() / 2)
            self.shield_up = True
            print(f"{self.name} поднимает щит. Броня: {self.defense}, Сила: {self.get_power()}")

    def lower_shield(self):
        if self.shield_up:
            self.defense /= 2
            self.set_power(self.get_power() * 2)
            self.shield_up = False
            print(f"{self.name} опускает щит. Броня: {self.defense}, Сила: {self.get_power()}")

    def make_a_move(self, friends, enemies):
        if self.get_hp() < 50 and not self.shield_up:
            self.raise_shield()
        elif self.get_hp() > 100 and self.shield_up:
            self.lower_shield()
        else:
            target = min(enemies, key=lambda enemy: enemy.get_hp())
            self.attack(target)

    def __str__(self):
        return f"{self.name}: Броня: {self.defense}, Сила: {self.get_power()}"


class Attacker(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1

    def attack(self, target):
        damage = self.get_power() * self.power_multiply
        target.take_damage(damage)
        if hasattr(target, 'power_down'):
            target.power_down()
        print(f"{self.name} атакует {target.name} на {damage} урона.")

    def take_damage(self, damage):
        real_damage = damage * (self.power_multiply / 2)
        super().take_damage(real_damage)

    def power_up(self):
        self.power_multiply *= 2
        print(f"{self.name} усиливает силу до {self.power_multiply}")

    def power_down(self):
        self.power_multiply = max(1, self.power_multiply / 2)
        print(f"{self.name} ослабляется до {self.power_multiply}")

    def make_a_move(self, friends, enemies):
        if self.power_multiply < 2:
            self.power_up()
        else:
            target = min(enemies, key=lambda enemy: enemy.get_hp())
            self.attack(target)

    def __str__(self):
        return f"{self.name}: Здоровье: {self.get_hp()}, Сила: {self.get_power()}, Множитель: {self.power_multiply}"

# Принят
