class Parent:
    def __init__(self, name, age, child_list):
        self.parent_name = name
        self.parent_age = age
        self.child_list = child_list

    def print_info(self):
        print(f'Имя родителя: {self.parent_name}, возраст: {self.parent_age}')
        print('Дети:')
        for child in self.child_list:
            child.print_info()

    def calm_child(self, child_name):
        for child in self.child_list:
            if child.child_name == child_name:
                child.state_calm = True
                print(f'{child_name} успокоен.')

    def feed_child(self, child_name):
        for child in self.child_list:
            if child.child_name == child_name:
                child.state_hunger = False
                print(f'{child_name} накормлен.')


class Child:
    def __init__(self, name, age, state_calm, state_hunger):
        self.child_name = name
        self.child_age = age
        self.state_calm = state_calm
        self.state_hunger = state_hunger

    def print_info(self):
        print(
            f'{self.child_name}, возраст: {self.child_age}, спокойствие: {self.state_calm}, голод: {self.state_hunger}')

parent_name = input('Введите имя родителя: ')
parent_age = int(input('Введите возраст родителя: '))
child_name = input('Введите имя ребёнка: ')
child_age = int(input('Введите возраст ребёнка: '))

child_list = []
while True:
    if parent_age - child_age < 16:
        print('Введите правильный возраст ребёнка')
        child_age = int(input('Введите возраст ребёнка: '))
    else:
        child = Child(child_name, child_age, False, True)
        child_list.append(child)
        break

parent = Parent(parent_name, parent_age, child_list)
parent.print_info()

parent.calm_child(child_name)
parent.feed_child(child_name)

parent.print_info()



