import random

class Toyota:
    color = 'red'
    price = 1e6
    max_speed = 200
    current_speed = 0

first_car = Toyota()
first_car.current_speed = random.randint(0, 200)
second_car = Toyota()
second_car.current_speed = random.randint(0, 200)
third_car = Toyota()
third_car.current_speed = random.randint(0, 200)
print(first_car.current_speed, second_car.current_speed, third_car.current_speed)