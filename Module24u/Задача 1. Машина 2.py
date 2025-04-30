import random

class Toyota:
    color = 'red'
    price = 1e6
    max_speed = 200
    current_speed = 0

    def check_info(self):
        print(self.color, self.price, self.max_speed, self.current_speed)

    def change_speed(self, new_speed):
        self.current_speed = new_speed

car = Toyota()
car.check_info()
car.change_speed(random.randint(0, 200))
car.check_info()
print(Toyota.current_speed)  # обратите внимание, что скорость внутри Класса осталась той же, её изменения не коснулись
