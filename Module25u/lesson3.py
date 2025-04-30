# class Pet:
#     legs = 4
#     has_tail = True
#
#     def __str__(self):
#         tail = 'Да' if self.has_tail else 'нет'
#         return 'Всего ног: {legs}\nХвост присутствует - {has_tail}'.format(
#             legs=self.legs,
#             has_tail=tail
#         )
#
# class Cat(Pet):
#     def sound(self):
#         print('Мяу!')
#
# class Dog(Pet):
#     def sound(self):
#         print('Гав!')
#
# class Frog(Pet):
#     has_tail = False
#     def sound(self):
#         print('Ква!')
#
# cat = Cat()
# dog = Dog()
# frog = Frog()
# print(cat)
# print(dog)
# print(frog)
# cat.sound()
# dog.sound()
# frog.sound()

class Ship:
    def __init__(self, model):
        self.model = model
    def __str__(self):
        return "\nМодель корабля: {model}".format(
            model=self.model
        )
    def sail(self):
        print("\nКорабль куда-то поплыл!!!")

class Warship(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print('\nКорабль атакует с помощью оружия:', self.gun)

class Cargoship(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self):
        print('\nЗагружаем корабль')
        self.tonnage_load += 1
        print('Текущая загруженность:', self.tonnage_load)

    def unload(self):
        print('\nРазгружаем корабль')
        if self.tonnage_load > 0:
            self.tonnage_load -= 1
        else:
            print('Корабль уже разгружен!')
        print('Текущая загруженность:', self.tonnage_load)

warship = Warship('QORQMAS', 'Пушки')
warship.attack()
cargoship = Cargoship('POLVON')
cargoship.load()
