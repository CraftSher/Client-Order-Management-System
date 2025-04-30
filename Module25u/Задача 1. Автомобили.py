class Auto:
    def __init__(self, model):
        self.model = model
    def __str__(self):
        return "Модель автомобиля: {model}".format(
            model=self.model
        )

    def report_model(self):
        print(f"Модель автомобиля: {self.model}")

    def drive(self):
        print("\nАвтомобиль куда-то поехал!!!")

class Trunk(Auto):
    def __init__(self, model):
        super().__init__(model)
        self.trunk_capacity = 0

    def load_trunk(self):
        print('\nЗагружаем грузовик')
        self.trunk_capacity += 1
        print('Текущая загруженность:', self.trunk_capacity)

    def unload_trunk(self):
        print('\nРазгружаем грузовик')
        if self.trunk_capacity > 0:
            self.trunk_capacity -= 1
        else:
            print('Грузовик уже разгружен!')
        print('Текущая загруженность:', self.trunk_capacity)

class Car(Auto):
    def __init__(self, model, navigation):
        super().__init__(model)
        self.navigation = navigation
        self.is_navigation_on = False

    def navigation_on_off(self):
        self.is_navigation_on = not self.is_navigation_on
        if self.is_navigation_on:
            print('Навигация включена!')
        else:
            print('Навигация отключена!')

# Создаем несколько экземпляров автомобилей
грузовик = Trunk("КамАЗ-5490")
легковушка = Car("Toyota Camry", "Яндекс.Навигатор")

# Проверяем методы базового класса
print(грузовик)
грузовик.report_model()
грузовик.drive()

print(легковушка)
легковушка.report_model()
легковушка.drive()

# Проверяем специфические методы грузовика
грузовик.load_trunk()
грузовик.load_trunk()
грузовик.unload_trunk()
грузовик.unload_trunk()
грузовик.unload_trunk()

# Проверяем специфические методы легковушки
легковушка.navigation_on_off()
легковушка.navigation_on_off()
легковушка.navigation_on_off()





