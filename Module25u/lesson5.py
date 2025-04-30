class Person:
    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return "Имя: {}\tВозраст: {}".format(self.__name, self.__age)

    def get_count(self): #гетто
        return self.__count
    def get_age(self): #гетто
        return self.__age

    def get_name(self):
        return self.__name

    def set_age(self, age): #сетто
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception("Недопустимый возраст!!!")

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info, 'Студент учится в университете {}'.format(self.university)
            )
        )
        return info
        #return ('Студент {} учится в университете {}'.format(self.get_name(), self.university))

class Employer(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.company = company
        self.salary = salary

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info, 'Компания: {}\tЗарплата: {}'.format(self.company, self.salary)
            )
        )
        return info


misha = Person('Misha', 20)
tom = Person('Tom', 25)
print(misha.get_count())
new_age = 45
misha.set_age(new_age)
print(misha.get_age())
my_student = Student(name='Abdu', age=24, university="TASI")
print(my_student)
my_emp = Employer(name='Козим', age =34, salary = 4500000, company="AKFA")
print(my_emp)