class Robot:
    def __init__(self, model_number):
        self.model_number = model_number
        print('Модель робота:', self.model_number)
    def operate(self):
        print('Робот начал работу!')

class VacuumCleanerRobot(Robot):
    def __init__(self, model_number):
        super().__init__(model_number)
        self.dustbag_capacity = 0
    def operate(self):
        print('Начал пылесосить пол!!!')
        self.dustbag_capacity += 1
        print('Текущая загруженность мешка:', self.dustbag_capacity)

class SecurityRobot(Robot):
    def __init__(self, model_number):
        super().__init__(model_number)
        self.has_alarm = True
    def operate(self):
        print('Начал охрану дома с сигнализацией!!!')

class PoolRobot(SecurityRobot):
    def __init__(self, model_number, depth):
        super().__init__(model_number)
        self.depth = depth

    def operate(self):
        super().operate()
        print('Охрана ведется под водой на глубине', self.depth)

# Создаем экземпляры роботов
пылесос = VacuumCleanerRobot("VC01")
охранник = SecurityRobot("SR02")
робот_для_бассейна = PoolRobot("PR03", 2)

# Запускаем их работу
print("--- Робот-пылесос ---")
пылесос.operate()
пылесос.operate()

print("\n--- Робот-охранник ---")
охранник.operate()

print("\n--- Робот для бассейна ---")
робот_для_бассейна.operate()
