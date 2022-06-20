class Car:
    '''проектирование машины'''

    def __init__(self, make, model, year):  # атрибуты
        ''''''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100

    def get_descriptive_name(self):  # метод
        '''вернуть соотвецтвущее щтформанированое имя'''
        long_name = f'{self.make} {self.model} {self.year}'
        return long_name.title()

    def read_odometer(self):  # метод
        '''вивод пробега машины '''
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):  # метод
        '''
        Задать занчение одометра
        Откинуть переменную в случае отмотки одометнра
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):  # метод
        '''Добавить занчение к показателю одометра'''
        self.odometer_reading += miles


class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        '''Вывести уведомление про ростояние
        какое может преодолет машина взависимосте
        от размера батарей'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        self.battery_size = 100



class ElectricCar(Car):

    def __init__(self, mark, model, year):
        super().__init__(mark, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")

