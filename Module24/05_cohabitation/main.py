import random


class House:
    food = 50
    money = 0


class Human:
    def __init__(self, name, house):
        self.human_name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        self.satiety += 10
        self.house.food -= 10

    def work(self):
        self.satiety -= 10
        self.house.money += 10

    def go_shopping(self):
        self.house.food += 10
        self.house.money -= 10

    def play(self):
        num = random.randint(1, 6)
        if num != 1 and num != 2:
            print("Идёт игра!!!")

    def live_a_day(self):
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_shopping()
        elif self.house.money < 50:
            self.work()
        else:
            num = random.randint(1, 6)
            if num == 1:
                self.work()
            elif num == 2:
                self.eat()
            else:
                self.play()
                self.satiety -= 10
        print(f'{self.human_name}: сытость={self.satiety}, еда={self.house.food}, деньги={self.house.money}')


# Запрос имен и создание людей
persons = []
common_house = House()
for i in range(2):
    name = input(f'Введите имя {i + 1} человека: ')
    person = Human(name, common_house)
    persons.append(person)

# Симуляция 365 дней
for i in range(1, 366):
    print(f'\n{i} -й день.')
    for person in persons[:]:  # копия списка, чтобы безопасно удалять
        person.live_a_day()
        if person.satiety <= 0:
            print(f'{person.human_name} погиб....')
            persons.remove(person)

    if not persons:
        print("Все погибли. Эксперимент завершён.")
        break

