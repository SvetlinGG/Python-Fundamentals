
#
# class Person:
#
#     def __init__(self, height, color, age):
#         self.height = height
#         self.color = color
#         self.age = age
#     def human(self):
#         print(f'I am a {person.height} meter height, with {person.color} eyes, and {person.age} years old')
#
# person = Person(1.75,'green', 54)
# person.human()

class Car:

    def __init__(self, color, brand, fuel):
        self.color = color
        self.brand = brand
        self.fuel = fuel
    def car(self):
        print(f'{self.color} {self.brand} using  {self.fuel} is driving')
car_one = Car('black', "Mercedes",'petrol')
print(car_one.car())

class ElectricCar(Car):
    def __int__(self, color, brand, battery_range):
        super().__init__(color, brand)
        self.battery_range = battery_range

    def refuel(self):
        print(f'The {self.color} {self.brand} is charging. Range {self.battery_range}')

petrol_car = Car('Red', 'Opel',)
petrol_car.car()
petrol_car.refuel()

electric_car = ElectricCar('Blue', 'Tesla', 500)
electric_car.car()
