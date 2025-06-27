

class Car:

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def drive(self):
        print(f'The{self.color} {self.brand} is driving')

    def refuel(self):
        print(f'The {self.color} {self.brand} is refueling with petrol')

car_1 = Car('black', 'Mercedes')
car_1.drive()