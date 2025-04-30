class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Точка с координатами ({}, {})'.format(self.x, self.y)

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

    def set_x(self, new_x):
        if isinstance(new_x, (int, float)):
            self.x = new_x
        else:
            raise ValueError("Недопустимое значение!!!")

    def set_y(self, new_y):
        if isinstance(new_y, (int, float)):
            self.y = new_y
        else:
            raise ValueError("Недопустимое значение!!!")

coord = Point(34, 56)
print(coord)