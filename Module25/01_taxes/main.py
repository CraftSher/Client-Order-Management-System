class Property:
    TAX_VALUE = 0  # Константа, переопределяется в наследниках

    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def set_worth(self, worth):
        self.__worth = worth

    def calculate_tax(self):
        """
        Метод для расчета налогов
        """
        return self.__worth / self.TAX_VALUE


class Apartment(Property):
    TAX_VALUE = 1000


class Car(Property):
    TAX_VALUE = 200


class CountryHouse(Property):
    TAX_VALUE = 500


def main():
    name = input('Введите имя: ')
    sur_name = input('Введите фамилию: ')
    money_count = float(input('Введите количество денег на счету: '))
    property_type = input('Каким имуществом Вы владеете (квартира, машина, дача): ').lower()
    price_worth = float(input(f'Введите стоимость {property_type}: '))

    if property_type == 'квартира':
        my_property = Apartment(price_worth)
    elif property_type in ('машина', 'автомобиль'):
        my_property = Car(price_worth)
    elif property_type in ('дача', 'загородный дом'):
        my_property = CountryHouse(price_worth)
    else:
        print('Такой тип имущества не поддерживается.')
        return

    tax_amount = my_property.calculate_tax()

    print(f'\nЗдравствуйте, {name} {sur_name}!')
    print(f'Рассчитанный налог на {property_type}: {tax_amount}')

    if tax_amount <= money_count:
        print('Сумма на вашем счету хватает на налог.')
    else:
        surcharge = tax_amount - money_count
        print('Денег на Вашем счету не достаточно!!!')
        print(f'Необходимо доплатить: {surcharge}')


if __name__ == '__main__':
    main()