import random


class Property:
    def __init__(self, worth):
        self.__worth = worth

    def tax_calculation(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.worth = worth

    def tax_calculation(self):
        return self.worth // 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.worth = worth

    def tax_calculation(self):
        return self.worth // 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.worth = worth

    def tax_calculation(self):
        return self.worth // 500


try:
    print('За что будем платить налог?\n'
          '1 - Квартира;\n2 - Машина;\n3 - Дача.')
    answer = int(input('\nВыберите пункт(1, 2, 3): '))
    if answer == 1:
        price = random.randint(1000000, 2000000)
        apartment = Apartment(price)
        print('Стоимость квартиры составляет: {}\nНалог: {} руб.'.format(
            price, apartment.tax_calculation()
        ))
        cash = int(input('Сколько денег? '))
        if cash < apartment.tax_calculation():
            print('Не хватает для оплаты налога: ',
                  apartment.tax_calculation() - cash, 'руб.')
        else:
            print('Налог оплачен! Остаток: ',
                  cash - apartment.tax_calculation(), 'руб.')
    elif answer == 2:
        price = random.randint(500000, 1000000)
        car = Car(price)
        print('Стоимость машины составляет: {}\nНалог: {} руб.'.format(
            price, car.tax_calculation()
        ))
        cash = int(input('Сколько денег? '))
        if cash < car.tax_calculation():
            print('Не хватает для оплаты налога: ',
                  car.tax_calculation()- cash, 'руб.')
        else:
            print('Налог оплачен! Остаток: ',
                  cash - car.tax_calculation(), 'руб.')
    elif answer == 3:
        price = random.randint(2000000, 3000000)
        country_house = CountryHouse(price)
        print('Стоимость дачи составляет: {}\nНалог: {} руб.'.format(
            price, country_house.tax_calculation()
        ))
        cash = int(input('Сколько денег? '))
        if cash < country_house.tax_calculation():
            print('Не хватает для оплаты налога: ',
                  country_house.tax_calculation() - cash, 'руб.')
        else:
            print('Налог оплачен! Остаток: ',
                  cash - country_house.tax_calculation(), 'руб.')
    else:
        raise ValueError

except ValueError:
    print('Неверная команда!')
