
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

    def drive(self, distance, fuel):
        if self.fuel > fuel:
            self.fuel -= fuel
            self.mileage += distance
            print(f'{self.name} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            if self.mileage >= 100000:
                del car_info[self.name]
                print(f'Time to sell the {self.name}!')
        else:
            print(f"Not enough fuel to make that ride")

    def refuel(self, fuel):
        if self.fuel + fuel > 75:
            fuel = 75 - self.fuel
        self.fuel += fuel
        print(f'{self.name} refueled with {fuel} liters')

    def revert(self, kilometers):
        self.mileage -= kilometers
        if self.mileage < 10000:
            self.mileage = 10000
            return
        print(f'"{self.name} mileage decreased by {kilometers} kilometers')
    def __repr__(self):
        return f"{self.name} -> Mileage: {self.mileage} kms, Fuel in the tank: {self.fuel} lt."

