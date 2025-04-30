class CanFly:
    def __init__(self):
        self.height = 0
        self.speed = 0
    def take_off(self):
        pass
    def fly(self):
        pass
    def land(self):
        self.height = 0
        self.speed = 0
    def display_status(self):
        print('Текущая высота: {}\nТекущая скорость: {}'.format(self.height, self.speed))

class Butterfly(CanFly):
    def __init__(self, height, speed):
        super().__init__(height, speed)

    def take_off(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5

class Rocket(CanFly):
    def __init__(self, height, speed):
        super().__init__(height, speed)

    def take_off(self):
        self.height = 500
        self.speed = 1000
    def land(self):
        self.height = 0
        print('Взрыв')
    def explode(self):
        print("БУМ!")

# Создание экземпляров
butterfly = Butterfly(0, 0)
rocket = Rocket(0, 0)

# Демонстрация работы с бабочкой
print("--- Бабочка ---")
butterfly.display_status()
butterfly.take_off()
butterfly.display_status()
butterfly.fly()
butterfly.display_status()
butterfly.land()
butterfly.display_status()

# Демонстрация работы с ракетой
print("\n--- Ракета ---")
rocket.display_status()
rocket.take_off()
rocket.display_status()
rocket.land()
rocket.display_status()
rocket.explode()