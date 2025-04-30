class Property:
    def __init__(self, worth):
        self.__worth = worth
    def get_worth(self):
        return self.__worth
    def set_worth(self, worth):
        self.__worth = worth

    def calculate_tax(self):
        """
        Метод для расчета налогов

        :return: NotImplementedError
        """
        return NotImplementedError

class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def calculate_tax(self):
        """
        Метод для расчета налога на квартиру как 1/1000 от ее стоимости.

        :return: Налог на квартиру
        """
        tax_apart = self.get_worth() / 1000
        return tax_apart

class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def calculate_tax(self):
        """
        Метод для расчета налога на автомобиль как 1/200 от ее стоимости.

        :return: Налог на автомобиль
        """
        tax_car = self.get_worth() / 200
        return tax_car

class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def calculate_tax(self):
        """
        Метод для расчета налога на загородный дом как 1/500 от ее стоимости.

        :return: Налог на загородный дом
        """
        tax_coun_house = self.get_worth() / 500
        return tax_coun_house

def main():
    name = input('Введите имя: ')
    sur_name = input('Введите фамилию: ')
    money_count = float(input('Введите количество денег на счету: '))
    property_type = input('Каким имуществом Вы владеете: ')
    price_worth = float(input(f'Введите стоимость {property_type}: '))
    if property_type == 'квартира':
        my_property = Apartment(price_worth)
        tax_amount = my_property.calculate_tax()
    elif property_type == 'машина' or property_type == 'автомобиль':
        my_property = Car(price_worth)
        tax_amount = my_property.calculate_tax()
    elif property_type == 'дача' or property_type == 'загородный дом':
        my_property = CountryHouse(price_worth)
        tax_amount = my_property.calculate_tax()
    if tax_amount <= money_count:
        print('Сумма на вашем счету хватает на налог.')
        print(f'Рассчитанный налог на имущество: {tax_amount}')
    else:
        surcharge = tax_amount - money_count
        print('Денег на Вашем счету не достаточно!!!')
        print(f'Не обходимо доплатить: {surcharge}')

main()