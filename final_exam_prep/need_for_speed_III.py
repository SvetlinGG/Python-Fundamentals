
number_of_cars = int(input())

car_info = {}

class Car:
    def __init__(self, name):
        self.name = name
        self.mileage = 0
        self.fuel = 0
    def add_mileage(self, mileage):
        self.mileage += mileage
    def add_fuel(self, fuel):
        self.fuel += fuel
