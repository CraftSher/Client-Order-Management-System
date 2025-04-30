class Men:
    __count = 0

    def __init__(self, name, age):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError("Имя должно быть строкой и состоять только из букв")
        if not isinstance(age, int) or not 0 <= age <= 100:
            raise ValueError("Возраст должен быть целым числом в диапазоне от 0 до 100")
        self.__name = name
        self.__age = age
        Men.__count += 1

    def __str__(self):
        return "Имя: {}\tВозраст: {}".format(self.__name, self.__age)

    def get_count(self):
        return self.__count
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

    def set_name(self, name):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError("Имя должно быть строкой и состоять только из букв")
        self.__name = name

    def set_age(self, age):
        if not isinstance(age, int) or not 0 <= age <= 100:
            raise ValueError("Возраст должен быть целым числом в диапазоне от 0 до 100")
        self.__age = age

# Тестирование
man1 = Men("Алишер", 30)
print(man1)
print("Количество созданных объектов:", man1.get_count())

# Изменение возраста с помощью сеттера
man1.set_age(35)
print(f"Возраст после использования сеттера: {man1.get_age()}")

# Изменение возраста "крайне не рекомендуемым" способом
man1._Men__age = 40
print(f"Возраст после 'не рекомендуемого' способа: {man1.get_age()}")