
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f'The {self.make} {self.model} engine is tarting')

    def stop_engine(self):
        print(f'The {self.make} {self.model} engine is stopping')

car_one = Car('Ford', 'Mustang', 2020)
car_two = Car('Mercedes', 'S500 AMG', 2025)

car_one.start_engine()
car_two.stop_engine()