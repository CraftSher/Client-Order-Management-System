class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Гав!")

my_dog = Dog("Рекс", "Немецкая овчарка")
your_dog = Dog("Белка", "Дворняга")

print(your_dog.name)   # Вывод: Рекс
your_dog.bark()       # Вывод: Гав!

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Какой-то звук")

class Cat(Animal):
    def speak(self):
        print("Мяу!")

my_cat = Cat("Муся")
print(my_cat.name)   # Вывод: Муся
my_cat.speak()      # Вывод: Мяу!